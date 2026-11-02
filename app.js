"use strict";
const $ = id => document.getElementById(id);
const fields = ["users", "tasks", "minutes", "days", "adoption", "hourly", "premium"];
const copy = {
  brief: {eyebrow: "01 / EXECUTIVE BRIEFING", description: "Turn a fictional account's discovery notes into a source-aware meeting agenda, using a model running on this laptop.", cue: '"What if the first draft didn\'t depend on a round trip to a cloud model?"', boundary: "A drafting demonstration, not a security certification. Human review remains essential."},
  code: {eyebrow: "02 / DEVELOPER ACCELERATION", description: "Turn a small service-desk requirement into a code draft. Watch a dedicated coding model generate Python on the RTX GPU.", cue: '"Which repetitive development tasks could your team prototype directly on their laptops?"', boundary: "Generated code is displayed, never executed. Assert examples are model output, not proof they pass."}
};
let status, scenarios, story = "brief", busy = false, switching = false, lastRun = null, lastCase = null, timer = null, caseRevision = 0;
const num = new Intl.NumberFormat("en-US", {maximumFractionDigits: 1});
const usd = new Intl.NumberFormat("en-US", {style: "currency", currency: "USD", maximumFractionDigits: 0});

async function getJson(url) {
  const response = await fetch(url, {cache: "no-store"});
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`);
  return data;
}
async function switchModel() {
  if (busy || switching) return;
  const selected = $("model").value;
  switching = true;
  clearOutput();
  controls();
  $("model-status").textContent = "Requesting model change…";
  try {
    const response = await post("/api/model", {model: selected});
    const data = await response.json();
    if (!response.ok) throw new Error(data.error);
    await refreshStatus();
  } catch (error) {
    errorText(`Model change failed: ${error.message}`);
    if (status?.engine.selected_model) $("model").value = status.engine.selected_model;
  } finally {
    switching = false;
    controls();
  }
}
async function post(url, body) {
  return fetch(url, {method: "POST", headers: {"Content-Type": "application/json", "X-Showcase-Token": status.token}, body: JSON.stringify(body)});
}
function errorText(message) { $("error").textContent = message; $("error").hidden = false; }
function clearOutput() {
  lastRun = null;
  $("output").textContent = "";
  $("output").hidden = true;
  $("empty-state").hidden = false;
  $("error").hidden = true;
  $("review-note").hidden = true;
  $("run-state").textContent = "Ready when you are";
  for (const id of ["ttft", "elapsed", "received"]) $(id).textContent = "—";
  $("route").textContent = "Not run";
  $("export-run").disabled = true;
}
function controls() {
  const rehearsal = $("mode").value === "rehearsal";
  $("run-button").disabled = busy || switching || (!rehearsal && status?.engine.state !== "ready");
  $("run-button").textContent = busy ? "Generating locally…" : rehearsal ? "Show authored example ↗" : status?.engine.state === "ready" ? "Run on this device ↗" : "Local AI not ready";
  $("mode").disabled = busy;
  $("model").disabled = busy || switching || rehearsal || !["ready", "error"].includes(status?.engine.state) || !status?.engine.models?.length;
  $("prompt").readOnly = rehearsal || busy;
  document.querySelectorAll("[data-story]").forEach(button => { button.disabled = busy; });
  $("output-label").textContent = rehearsal ? "AUTHORED REHEARSAL · NO INFERENCE" : "THE RESULT";
}
function selectStory(next) {
  if (busy) return;
  story = next;
  document.querySelectorAll("[data-story]").forEach(button => {
    const active = button.dataset.story === story;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", String(active));
  });
  $("ai-workspace").hidden = story === "value";
  $("value-workspace").hidden = story !== "value";
  if (story === "value") return;
  const entry = scenarios[story];
  $("story-title").textContent = entry.title;
  $("story-eyebrow").textContent = copy[story].eyebrow;
  $("story-description").textContent = copy[story].description;
  $("say-this").textContent = copy[story].cue;
  $("story-boundary").textContent = copy[story].boundary;
  $("prompt").value = entry.prompt;
  $("output").classList.toggle("code-output", story === "code");
  clearOutput();
  controls();
}
function renderStatus() {
  const engine = status.engine, device = status.device;
  $("engine-badge").className = "badge " + (engine.state === "ready" ? "ready" : engine.state === "error" ? "failed" : "");
  $("engine-badge").replaceChildren();
  $("engine-badge").append(document.createElement("i"), document.createTextNode(engine.state === "ready" ? "Local AI ready · RTX GPU" : engine.state === "error" ? "Local AI unavailable" : engine.detail));
  $("ram-proof").textContent = device.installed_ram_gb ? `${num.format(device.installed_ram_gb)} GB` : "Not verified";
  $("ram-detail").textContent = device.os_visible_ram_gb ? `Installed · ${num.format(device.os_visible_ram_gb)} GB Windows-visible` : "Installed physical memory · OS visibility not verified";
  $("cpu-proof").textContent = device.cores ? `${device.cores} cores` : "Not verified";
  const gpu = (device.accelerators || []).find(name => /GPU|RTX/i.test(name));
  $("gpu-proof").textContent = gpu ? /Blackwell/i.test(gpu) ? "Blackwell RTX GPU" : gpu : "GPU not verified";
  $("model-line").textContent = engine.model ? `${engine.model.name} · ${engine.model.provider} · RTX GPU inference` : engine.error || engine.detail;
  if (engine.error) $("model-line").textContent = engine.error;
  const choices = engine.models || [];
  const signature = JSON.stringify(choices);
  if (choices.length && $("model").dataset.choices !== signature) {
    $("model").replaceChildren(...choices.map(choice => new Option(`${choice.label}${choice.reasoning ? " · reasoning" : " · coding"}${choice.cached ? "" : " · not cached"}`, choice.alias)));
    $("model").dataset.choices = signature;
  }
  if (choices.length) $("model").value = engine.selected_model;
  $("model-status").textContent = engine.state === "ready" ? `${engine.model?.reasoning ? "Reasoning model · first visible text may take longer" : "Coding model"} · One model resident at a time` : engine.error || engine.detail;
  if (device.error) $("model-line").textContent += ` · ${device.error}`;
  controls();
}
async function refreshStatus() {
  try {
    status = await getJson("/api/status");
    renderStatus();
  } catch (error) {
    if (status) status.engine = {state: "error", detail: "Local server disconnected"};
    $("engine-badge").textContent = "Server disconnected";
    $("engine-badge").className = "badge failed";
    $("model-line").textContent = error.message;
    controls();
  }
}
async function run() {
  if (busy) return;
  clearOutput();
  const mode = $("mode").value, prompt = $("prompt").value.trim();
  if (!prompt) { errorText("Enter a request first."); return; }
  busy = true;
  controls();
  document.querySelector(".run-panel").classList.add("running");
  document.querySelector(".output-area").setAttribute("aria-busy", "true");
  $("empty-state").hidden = true;
  $("output").hidden = false;
  $("run-state").textContent = mode === "live" ? "Sending request to the local model…" : "Displaying authored sample";
  $("route").textContent = mode === "live" ? "Local · RTX GPU" : "No inference";
  const started = performance.now();
  if (mode === "live") timer = setInterval(() => {
    $("elapsed").textContent = `${((performance.now() - started) / 1000).toFixed(1)} s`;
    if (!$("output").textContent && !reasoningCharacters) $("run-state").textContent = "Waiting for first visible model text…";
  }, 100);
  let completion = null, chunks = 0, reasoningCharacters = 0;
  try {
    const response = await post("/api/run", {scenario: story, mode, prompt});
    if (!response.ok) throw new Error((await response.json()).error);
    const reader = response.body.getReader(), decoder = new TextDecoder();
    let buffer = "";
    function event(line) {
      if (!line.trim()) return;
      const item = JSON.parse(line);
      if (item.type === "error") throw new Error(item.error);
      if (item.type === "activity") {
        reasoningCharacters = item.reasoning_characters;
        $("run-state").textContent = `Reasoning activity received · ${num.format(reasoningCharacters)} chars · text hidden`;
      }
      if (item.type === "token") {
        $("output").textContent += item.text;
        chunks++;
        $("received").textContent = `${num.format($("output").textContent.length)} chars`;
        $("run-state").textContent = mode === "live" ? `Receiving output · ${num.format(chunks)} text chunks` : "Authored example · no model run";
        $("output").scrollTop = $("output").scrollHeight;
      }
      if (item.type === "done") completion = item;
    }
    while (true) {
      const {value, done} = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, {stream: true});
      const lines = buffer.split("\n");
      buffer = lines.pop();
      lines.forEach(event);
    }
    buffer += decoder.decode();
    if (buffer.trim()) event(buffer);
    if (!completion) throw new Error("The stream ended before a completion record. Output is incomplete.");
    if (!$("output").textContent.trim()) throw new Error("No visible answer was received.");
    $("output").scrollTop = 0;
    $("ttft").textContent = completion.ttft_ms === null ? "Not measured" : `${num.format(completion.ttft_ms)} ms`;
    $("elapsed").textContent = completion.total_ms === null ? "Not measured" : `${(completion.total_ms / 1000).toFixed(1)} s`;
    const truncated = /length|max.*token/i.test(completion.finish_reason);
    $("run-state").textContent = mode === "rehearsal" ? "Authored rehearsal · no inference" : truncated ? "Token limit reached · incomplete draft" : "Generated on this device · review required";
    $("review-note").hidden = false;
    $("review-note").textContent = mode === "rehearsal" ? "Authored sample, not a model response. No timing or performance measurement." : truncated ? "Output token limit reached. This draft may be incomplete; inspect before use." : "AI-generated draft · Review facts and code before use. Code is displayed, not executed.";
    lastRun = {scenario: story, prompt, source: scenarios[story].source, output: $("output").textContent,
      ...completion, observed_at: new Date().toISOString(), device: status.device,
      measurement_notes: "TTFT: request start to first visible answer text, excluding private reasoning. Total: SDK generation wall time; excludes model load but includes reasoning. Output volume counts visible answer characters; reasoning activity is separately counted without exposing its text. SDK output tokens can include reasoning; token rate is tokens divided by full generation seconds, not decode-only speed. No code execution or accuracy certification."};
    $("export-run").disabled = false;
  } catch (error) {
    errorText(`${error.message} No authored answer has been substituted. You may explicitly choose Authored rehearsal.`);
    $("run-state").textContent = "Run failed · do not present as a completed result";
    $("route").textContent = "Run failed";
  } finally {
    clearInterval(timer);
    busy = false;
    document.querySelector(".run-panel").classList.remove("running");
    document.querySelector(".output-area").setAttribute("aria-busy", "false");
    controls();
  }
}
function download(name, content) {
  const url = URL.createObjectURL(new Blob([JSON.stringify(content, null, 2)], {type: "application/json"}));
  const anchor = document.createElement("a");
  anchor.href = url; anchor.download = name; anchor.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
async function updateCase() {
  const revision = ++caseRevision;
  $("export-case").disabled = true;
  lastCase = null;
  try {
    const values = {};
    for (const name of fields) {
      const input = $(name);
      if (!input.value.trim() || !input.checkValidity()) throw new Error(`Check the assumption: ${input.parentElement.firstChild.textContent.trim()}.`);
      values[name] = Number(input.value);
    }
    const response = await post("/api/calculate", values), data = await response.json();
    if (!response.ok) throw new Error(data.error);
    if (revision !== caseRevision) return;
    lastCase = data;
    $("calc-error").hidden = true;
    $("hours-result").textContent = num.format(data.hours);
    $("capacity-result").textContent = usd.format(data.capacity);
    $("investment-result").textContent = usd.format(data.investment);
    $("formula").textContent = `${num.format(values.users)} people × ${values.tasks} tasks × ${values.minutes} min ÷ 60 × ${values.days} days × ${values.adoption}% adoption = ${num.format(data.hours)} hours/year`;
    $("export-case").disabled = false;
  } catch (error) {
    if (revision !== caseRevision) return;
    $("calc-error").hidden = false; $("calc-error").textContent = error.message;
    ["hours-result", "capacity-result", "investment-result"].forEach(id => { $(id).textContent = "—"; });
    $("formula").textContent = "Correct the assumptions to calculate a case.";
  }
}
function dialog(title, text) {
  $("dialog-title").textContent = title;
  $("dialog-content").textContent = text;
  $("info-dialog").showModal();
}
const playbook = `RETAIL PLAYBOOK | RETAIL LEADERS
Local and hybrid AI for stores, merchandising and IT. Presenters are listed by role only. Every scenario is synthetic and labelled FICTIONAL.

THE 60-MINUTE RUN OF SHOW
00:00 Introductions and goals - the account technology strategist (5 min).
00:05 Your question first: why the NPU on the Copilot+ PCs you have sits idle, and what runs where - open Device classes (10 min).
00:15 Live: Company overview, then Retail scenarios - run the store visit follow-up on the GPU (10 min).
00:25 Live demos: store operations call to notes and actions; de-identify before any cloud step; Hybrid router (10 min).
00:35 Model choice: Build on Surface (one OpenAI-compatible API for Foundry Local and llama.cpp; Microsoft-provided and open-source models) and T-shirt sizing (10 min).
00:45 The Surface specialist: Surface Laptop Ultra specs, Arm requirements, pricing and purchase options (10 min).
00:55 Discovery questions and next steps: agree a scoped pilot (5 min).
The live segments use the native app; this browser studio offers the five-minute walkthrough below.

THE 5-MINUTE EXECUTIVE WALKTHROUGH

00:00 — OPEN WITH THE WORK, NOT THE SILICON
"The question isn't whether a laptop can run AI. It's which useful tasks we can put closer to the person doing the work."
Point to the observed device evidence. This unit has 128 GB installed, with about 64 GB visible to Windows. The GPU budget is a separate driver-reported view, not an additive memory pool. Memory partition settings are unchanged.

00:45 — WORK WHERE YOU ARE
Select Executive briefing and Run on this device. Qwen2.5-Coder 14B is the default; select GPT-OSS 20B to demonstrate a larger reasoning model. Wait for its ready status before running. Watch actual output activity; private reasoning text stays hidden. Inspect the synthetic source and compare the draft. Model size is not a quality guarantee.
"For selected workflows, the draft can be generated here rather than by a cloud model."
Do not say the whole application is air-gapped or security-approved. Validate disconnected operation separately after setup.

02:00 — BUILD AT THE EDGE
Select Developer acceleration. Run the small Python request. Explain that the code is not executed; examples are not passing test evidence.
"A developer can explore a bounded first draft on the device. Their review and testing still matter."

03:15 — MAKE THE CASE
Select Company-specific economics. Swap the illustrative assumptions for the company's numbers. Show how adoption changes capacity; set minutes gained to zero to show the result disappears.
"This is capacity value, not a reduction in payroll, and not a reason to subtract existing cloud subscriptions."

04:15 — CLOSE ON A PILOT
"Let's select one workflow, ten users and two weeks. We'll baseline task time, output quality, app compatibility and connectivity needs on the actual shipping SKU."
Confirm shipping availability, exact specifications, approved positioning, price, model license, procurement and partner service scope before an external proposal.

DISCOVERY QUESTIONS (ASK; NEVER ANSWER FOR THE CUSTOMER)
1. Which repeated retail tasks (store visit follow-ups, customer care case summaries, in-stock reviews, line review follow-ups, store device health summaries, incident updates) take meaningful time today?
2. Which AI PCs and processor families are deployed, by persona (headquarters, stores, distribution centers, customer care)?
3. Which on-device AI features or local models are in use today, and what has blocked wider use? (Device classes shows what the NPU runs today.)
4. Arm64 readiness: which VPN, security agent, printer and peripheral, and line-of-business app dependencies remain?
5. Management: how are Intune and Windows Autopilot set up for AI PCs, and who approves new local models and runtimes?
6. Data: which customer, associate, store and product data may a local model read, and where must outputs stay?
7. Model choice: which Microsoft-provided and open-source models, runtimes and licences are approved, and what does the AI acceptable-use policy allow?
8. Measures: which measures (visit report time, case handling time, handoff quality, service desk volumes) would a pilot compare against?
9. Where would a Surface Laptop Ultra fit (data and AI builders, design and product teams, developers), and what memory configuration do those workloads need?

GUARDRAILS
Drafts only; nothing is deployed, changed or sent. No draft approves or deploys a change, closes or reassigns tickets, changes device policies, determines a root cause, issues a refund or credit, places an order, transfer or allocation, or makes HR, vendor, purchasing, pricing or supplier decisions.
Store operations, merchandising, allocation, customer care, store technology, the service desk and the incident manager review everything. Nothing is sent to customers, associates, stores, vendors or stakeholders.
The audience is never the subject: every scenario uses the fictional Contoso Apparel. Never describe the audience's fleet, systems, stores, people or products, and never name real people.
Make no performance, cost or productivity claims. Platform-fit pilots are illustrative; verify the exact model variant on each device.

OBJECTION HANDLING
"We bought Copilot+ PCs for their NPU. Why aren't we using it?" — The NPU only helps when software is built to use it. Built-in Windows experiences such as improved Windows search and Live Captions use it, and your own apps reach it through the Windows AI APIs, Windows ML or Foundry Local; Task Manager shows NPU activity. Open Device classes to see what runs where. Everything live in this app runs on this laptop's RTX GPU.
"Why not just use cloud AI?" — Keep cloud for the workloads and services that belong there. This demonstrates an additional local option, not a cloud replacement.
"Can we choose our own models?" — Yes. Foundry Local and llama.cpp serve Microsoft-provided and open-source models through the same OpenAI-compatible API on this laptop. Licensing and the company's approval process still apply.
"How is AI accelerated?" — These models execute on the NVIDIA RTX GPU through CUDA. Inspect each run's model and execution-provider evidence.
"Is it faster or longer-lasting than another laptop?" — No comparison or battery test is included. Scope a controlled benchmark.
"Are these Microsoft 365 Copilot features?" — No. This is an independent custom Foundry Local application. No certification, bundled license or Microsoft 365 integration is implied.
"What if live inference fails?" — The error stays visible. Explicitly select Authored rehearsal; never describe it as measured or live.

HANDOFF
Export evidence after a real run. Export the business case with its assumptions. Print the executive handout. All scenarios are fictional; never paste real customer, associate, order, device or ticket records, unreleased product information or confidential company data into an unapproved prototype.`;
const deviceClasses = `See which local AI work suits the AI PCs you already have, which work needs more memory, and where a Builder PC fits. Each fact cites its Microsoft source, listed at the end, and each fit is a memory estimate from the same arithmetic as T-shirt sizing.

NPU routes on this page are documented by Microsoft; this app does not run anything on an NPU. Everything live here runs on this laptop's RTX GPU through CUDA.

THE COPILOT+ PCS YOU ALREADY HAVE
- Copilot+ PCs have an NPU that can perform more than 40 trillion operations per second, but software must be programmed to use it. Task Manager shows NPU usage, and Microsoft recommends Windows ML for running your own models on the NPU. [1]
- Built-in Copilot+ PC experiences include improved Windows search, Recall (preview) and Live Captions with real-time translation from 40+ languages into English. Availability depends on the device, Windows version, region and organization settings. [7]
- On Surface Laptop, Copilot+ PC experiences are available on configurations with 16 GB of memory or more. [8]
- Windows AI APIs such as Phi Silica, text recognition (OCR), Image Description, Image Super Resolution and Image Segmentation run on the NPU on Copilot+ PCs. The Speech Recognition API is experimental and the Semantic Search API is in private preview; AI Dev Gallery in the Microsoft Store has samples. [2]
- Phi Silica is Windows' on-device language model, preinstalled on Copilot+ PCs and offered as a Limited Access Feature. Its successor, Aion Instruct, arrives in Windows Insider builds from November 2026 and in retail Windows from January 2027, with no Limited Access Feature token. [3]
- Windows ML picks an execution provider such as QNN (Snapdragon) or OpenVINO (Intel) and can fall back to the GPU or CPU. [4]
- Foundry Local detects the NPU, GPU and CPU and downloads matching execution providers. Which models have an NPU variant depends on the device, so verify on the target PC. [5]

TRY THIS WEEK ON A COPILOT+ PC YOU ALREADY HAVE
1. Open Task Manager to see NPU activity. [1]
2. Install AI Dev Gallery from the Microsoft Store and run the Windows AI API samples. [2]
3. Ask a developer to try Foundry Local: its SDK discovers the PC's execution providers and lists the model variants available for it. [6]
4. Pick one workload below that fits a 16 GB Copilot+ PC and pilot it on synthetic data first.

BUILDER PCS: SURFACE LAPTOP ULTRA (THIS LAPTOP)
- Microsoft describes Builder PCs as a device class for hybrid intelligence, and Surface Laptop Ultra is one. [11]
- Surface Laptop Ultra has the NVIDIA RTX Spark Superchip, built for local AI and 3D graphics, and up to 128 GB of unified memory. [9]
- "Run local agents, automate routine tasks, keep sensitive work closer to you, and reserve the cloud for larger AI workloads." [9]
- "built for organizations working with proprietary code, AI models, customer data, and intellectual property" [9]
- For memory configurations and full specifications, see the tech specs. [10]
- The GPU can address less than the installed memory. Select Inspect the evidence to see the GPU memory budget the graphics driver reports for this laptop.

ALWAYS-ON AND SHARED
- Mini desktop PCs are a device class for always-on agents. [11]
- DGX Station for Windows, with NVIDIA GB300, is a device class for trillion-parameter models and 32 or more simultaneous agents. [11]
- Illustrative fit, not a recommendation: an always-on agent that drafts a daily fleet health summary for people to review.
This app does not size or run these classes; ask the account team about them.

EVERYDAY WORKLOADS BY DEVICE CLASS
Memory fit only; open the native app's Device classes page for the engine-computed view, including this laptop's GPU budget. Outcomes use 4-bit weights and an 8K context at illustrative 16 GB and 32 GB memory sizes.

Suggested class: Copilot+ PC (16 GB)
- Transcription & meeting notes, size S (3.8B): Comfortable at 16 GB and at 32 GB. Documented NPU route: Speech Recognition API (experimental) and Live Captions. [2] [7]
- Field & frontline notes, size S (3.8B): Comfortable at 16 GB and at 32 GB. Documented NPU route: Phi Silica text skills (Aion Instruct from 2027). [3]
- Translation, size M (8B): Comfortable at 16 GB and at 32 GB. Documented NPU route: Live Captions real-time speech translation. [7]
- Writing & summaries, size M (8B): Comfortable at 16 GB and at 32 GB. Documented NPU route: Phi Silica text skills (Aion Instruct from 2027). [3]
- Ask your documents, size M (8B): Comfortable at 16 GB and at 32 GB. Documented NPU route: Improved Windows search; Semantic Search API (private preview). [7] [2]
- Photos & scanned forms, size M (8B): Comfortable at 16 GB and at 32 GB. Documented NPU route: Text recognition (OCR) and Image Description APIs. [2]

Suggested class: 32 GB AI PC or Builder PC
- Local coding assistant, size L (14B): Won't fit at 16 GB; Comfortable at 32 GB. No documented NPU route on this page.
- Analysis & reasoning, size L (14B): Won't fit at 16 GB; Comfortable at 32 GB. No documented NPU route on this page.
- Bigger-model prototyping, size XL (32B): Won't fit at 16 GB; Comfortable at 32 GB. No documented NPU route on this page.

Suggested class: Builder PC (Surface Laptop Ultra)
- Largest open models (70B class), size XXL (70B): Won't fit at 16 GB or at 32 GB. No documented NPU route on this page.

Memory fit only, using the same arithmetic as T-shirt sizing; it does not confirm an NPU model variant or runtime support. Verify on the target PC.

PATTERNS FROM OTHER INDUSTRY SHOWCASES
Fictional patterns from Microsoft's industry showcases, not customer references. Ask the account team for named customer references.
- Financial services: Meeting capture. In retail: store operations calls. T-shirt sizing workload: Transcription & meeting notes, size S (3.8B). Suggested class: Copilot+ PC (16 GB).
- Telecom and media: Offline field notes. In retail: distribution center shift handoffs. T-shirt sizing workload: Field & frontline notes, size S (3.8B). Suggested class: Copilot+ PC (16 GB).
- Tax and accounting: Scanned forms. In retail: store device service forms. T-shirt sizing workload: Photos & scanned forms, size M (8B). Suggested class: Copilot+ PC (16 GB).
- Higher education: Policy questions with citations. In retail: device standards and change policy. T-shirt sizing workload: Ask your documents, size M (8B). Suggested class: Copilot+ PC (16 GB).
- Private markets: De-identify before the cloud. In retail: associate emails before any cloud step. T-shirt sizing workload: Writing & summaries, size M (8B). Suggested class: Copilot+ PC (16 GB).
- Engineering and software: Proprietary code assistant. In retail: e-commerce and store systems code. T-shirt sizing workload: Local coding assistant, size L (14B). Suggested class: 32 GB AI PC or Builder PC.
Open the native app's Device classes page to run the equivalent demos on this laptop.

SOURCES
[1] NPU devices (Microsoft Learn): https://learn.microsoft.com/en-us/windows/ai/npu-devices/
[2] Windows AI APIs (Microsoft Learn): https://learn.microsoft.com/en-us/windows/ai/apis/
[3] Phi Silica (Microsoft Learn): https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica
[4] Windows ML execution providers (Microsoft Learn): https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/supported-execution-providers
[5] Foundry Local meets more silicon (Microsoft Foundry blog): https://devblogs.microsoft.com/foundry/foundry-local-meets-more-silicon/
[6] Get started with Foundry Local (Microsoft Learn): https://learn.microsoft.com/en-us/azure/foundry-local/get-started
[7] Copilot+ PCs for business (Microsoft): https://www.microsoft.com/en-us/windows/business/devices/copilot-plus-pcs
[8] Surface Laptop (Microsoft): https://www.microsoft.com/en-us/surface/devices/surface-laptop
[9] Surface Laptop Ultra (Microsoft): https://www.microsoft.com/en-us/surface/devices/surface-laptop-ultra
[10] Surface Laptop Ultra tech specs (Microsoft Learn): https://learn.microsoft.com/en-us/surface/tech-specs/surface-laptop-ultra-1stedition
[11] Building Windows for hybrid intelligence (Windows Experience Blog): https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/`;

async function initialize() {
  try {
    [status, scenarios] = await Promise.all([getJson("/api/status"), getJson("/api/scenarios")]);
    renderStatus();
    selectStory("brief");
    for (const name of fields) $(name).value = status.assumptions[name];
    await updateCase();
    const focusExperience = () => document.querySelector(".experience").scrollIntoView({behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth", block: "start"});
    $("begin-button").addEventListener("click", focusExperience);
    document.querySelectorAll("[data-story]").forEach(button => button.addEventListener("click", () => { selectStory(button.dataset.story); focusExperience(); }));
    $("mode").addEventListener("change", () => { $("prompt").value = scenarios[story].prompt; clearOutput(); controls(); });
    $("run-button").addEventListener("click", run);
    $("model").addEventListener("change", switchModel);
    $("source-button").addEventListener("click", () => dialog("Inspect the source.", scenarios[story].source));
    $("device-button").addEventListener("click", () => dialog("Observed. Not assumed.", JSON.stringify(status.device, null, 2) + "\n\nInstalled memory is the sum of firmware DIMM capacities, not Windows-visible memory. GPU memory is the budget reported by nvidia-smi; these views must not be added or treated as separate dedicated memory pools. No memory partition settings were changed.\n\nGPU-focused inventory, not a published shipping specification.\n\nRuntime:\n" + JSON.stringify(status.engine, null, 2) + "\n\nInference runs on the RTX GPU through CUDA. No battery, accelerator-rating, dedicated-VRAM, all-network-isolation, competitive advantage or production-accuracy result is established."));
    $("device-classes-button").addEventListener("click", () => dialog("What runs where: the AI PCs you have, and where Surface Laptop Ultra fits.", deviceClasses));
    $("guide-button").addEventListener("click", () => dialog("Land the story. Then scope the pilot.", playbook));
    $("close-dialog").addEventListener("click", () => $("info-dialog").close());
    $("info-dialog").addEventListener("click", event => { if (event.target === $("info-dialog")) { const bounds = event.target.getBoundingClientRect(); if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) event.target.close(); } });
    $("fullscreen-button").addEventListener("click", async () => {
      try { if (document.fullscreenElement) await document.exitFullscreen(); else await document.documentElement.requestFullscreen(); }
      catch (error) { dialog("Full screen unavailable", error.message); }
    });
    $("export-run").addEventListener("click", () => { if (lastRun) download(`surface-${lastRun.scenario}-${lastRun.mode}-evidence.json`, lastRun); });
    $("export-case").addEventListener("click", () => { if (lastCase) download("surface-illustrative-business-case.json", {...lastCase, exported_at: new Date().toISOString()}); });
    fields.forEach(name => $(name).addEventListener("input", updateCase));
    $("reset-calc").addEventListener("click", () => { fields.forEach(name => { $(name).value = status.assumptions[name]; }); updateCase(); });
    $("print-button").addEventListener("click", () => window.print());
    document.addEventListener("keydown", event => { if (event.ctrlKey && event.key === "Enter" && story !== "value" && !$("run-button").disabled && !$("info-dialog").open) { event.preventDefault(); run(); } });
    setInterval(refreshStatus, 3000);
  } catch (error) { errorText(`Showcase initialization failed: ${error.message}`); $("engine-badge").textContent = "Initialization failed"; }
}
initialize();
