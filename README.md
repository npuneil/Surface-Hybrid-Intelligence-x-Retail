# Surface Hybrid Intelligence x Retail

A native **WinUI 3** local AI showcase for retail leaders, set at **Contoso Apparel**, a
fictional apparel retailer: local and hybrid AI for stores, merchandising and IT. Built
for leaders in store operations, merchandising and product, inventory and allocation,
customer care, store technology and the IT service desk, with CIOs, CISOs and the
information security, privacy and change-management reviewers who work with them, it
adds a **Device classes** page (what the AI PCs you already have can run on the device,
what needs more memory and where Surface Laptop Ultra fits, with Microsoft sources), a
three-tier **illustrative reference architecture for stores, merchandising and IT**
(smart capture on the store visit or operations call, in-company drafting, cloud
support only for de-identified complex questions), six fictional **retail scenarios**
(store visit follow-up, line review follow-ups, customer care case summary, weekly
in-stock review, store device health summary and major incident update draft), twelve
one-click **live demos** (including a synthetic store operations and IT call
transcribed and drafted into notes and actions on the RTX GPU),
a **Hybrid router** that shows what stays in the company and what de-identified query
would go to the cloud, a **GPU speedometer** and run of show, a **Build on Surface**
hub, T-shirt model sizing, platform-fit use cases and an assumption-driven capacity
calculator. Independent demonstration prototype, not a product announcement or
endorsement. The conceptual device illustration is original, not a product photograph.

## For retail leaders

The theme is *Local and hybrid AI for stores, merchandising and IT*. This edition is
written for retail leaders in store operations, merchandising and product, inventory
and allocation, customer care, store technology and the IT service desk; it is not
prepared for any named company. Nothing in the app describes a real retailer's fleet,
systems, stores, people, products or results, and the architecture is illustrative
rather than a description of any company's design.

### Two questions retail leaders ask

Retail leaders often ask two questions, paraphrased here; confirm which of them matter
to the audience early. The app answers each one:

1. **What does the NPU in the Copilot+ PCs we already have actually run, and why do
   the NPU and local LLMs see so little use?** The **Device classes** page (native
   navigation, right after **Platform fit**) and the companion web presentation's
   **Device classes** dialog show what Microsoft documents running on the NPU, why it
   sits idle unless software is built to use it, how your own apps reach it (Windows AI
   APIs, Windows ML, Foundry Local) and what to try this week, each with its Microsoft
   source. See *Device classes: what runs where*.
2. **Setting the specs aside, which of our use cases would Surface Laptop Ultra help,
   and how do others use local LLMs?** The **Device classes** matrix sizes
   everyday workloads for 16 GB and 32 GB laptops and for this laptop's GPU budget with
   the T-shirt sizing engine, with **Run live** proof on this laptop's RTX GPU. The
   **Retail scenarios**, **Live demos**, **Hybrid router**, **Build on Surface**
   (one OpenAI-compatible API for Foundry Local and llama.cpp) and **T-shirt sizing**
   pages show those use cases working. Fictional patterns from other industry showcases
   answer the second half; they are not customer references (see *Patterns from other
   industries*).

Every company, person, device and record in the app is fictional:

- **Contoso Apparel**: an apparel retailer with a headquarters, stores such as Store
  0412, distribution centers such as DC-2, an online store, a customer care team and a
  product development team, the subject of every scenario and demo.
- **Relecloud Scheduler** (a store scheduling app), the **VanArsdel TP-40** receipt
  printer, **Lucerne VPN** (a VPN client), the **Trey Research** endpoint agent and the
  **Southridge** inventory app: fictional products and vendors in the scenarios and
  demos.

Guardrails:

- Synthetic data only: no real customers, associates, stores, devices, orders or
  tickets, no personal data and no unreleased product information.
- Drafts only; nothing is deployed, changed or sent. Store operations, merchandising,
  allocation, customer care, store technology, the service desk and the incident
  manager review every draft.
- No draft approves or deploys a change or update, closes or reassigns a ticket,
  changes a device policy, determines a root cause, issues a refund or credit, places
  an order, transfer or allocation, or makes an HR, vendor, purchasing, pricing or
  supplier decision.
- Nothing is sent to customers, associates, stores, vendors or stakeholders. Not legal
  or HR advice.
- De-identification removes structured identifiers only and is not certified. No
  point-of-sale, order management, endpoint management, service desk (ITSM) or HR
  system connection is made.

Suggested five-minute flow: **Company overview** reference architecture ->
**Run operations call capture** (Tier 1) -> **Draft a store visit follow-up** (Tier 2) ->
**Route a complex question** in the Hybrid router (escalate, NOT SENT) ->
**Retail playbook** to agree a four-week pilot on synthetic store visit and service
desk records. For the full hour, open with **Device classes**: see the 60-minute run of
show in [SELLER-GUIDE.md](SELLER-GUIDE.md) (the Retail playbook; the file name
is kept for the `/seller-guide` route).

The service listens on `127.0.0.1:8814` by default so it can run beside other
demos.

## Illustrative reference architecture: local and hybrid AI for stores, merchandising and IT

The **Company overview** opens with a three-tier reference architecture headed
*Three tiers. Customer and store data stay in the company. The cloud only when
needed.* It is labelled "Illustrative reference architecture, not any company's actual
design." Each tier has a button that proves it with a live, local demo:

| Tier | Where it runs | What it does | Proved in the app by |
|---|---|---|---|
| **Tier 1: Smart capture** | A store manager's or field technician's Surface on the store visit or operations call | Capture the conversation with consent, transcribe locally, draft notes on the device, sync securely inside the company | **Run operations call capture**: the *Store operations and IT call to notes and actions* demo transcribes a synthetic call in which Ana (store operations manager), Marcus (desktop engineer) and Priya (service desk manager) plan a back-office laptop refresh pilot at 12 stores before the holiday change freeze, on the RTX GPU |
| **Tier 2: In-company drafting** | Local AI beside the company's store operations and service desk systems (illustrative) | Apply store and IT procedures, draft store visit follow-ups and incident updates, keep customer, associate and store data inside the company | **Draft a store visit follow-up**: the *Store visit notes to a district follow-up list* scenario (`store-visit`), live |
| **Escalate only when needed** | Inside the company | Remove customer, associate, asset and ticket identifiers (names, emails, employee ids, asset tags, ticket numbers), minimize context, algorithmic delegation (route by rule, with every reason shown) | **Route a complex question**: the Hybrid router's *Complex question: escalate to Tier 3* preset masks the structured identifiers it finds and shows the de-identified payload, marked NOT SENT |
| **Tier 3: Cloud support** | External cloud (Azure OpenAI) | Frontier reasoning for complex questions; de-identified queries in, model support out | **Preview the cloud payload**: the *De-identify before escalating (Tier 3)* demo shows what would leave, marked NOT SENT |

Output: **draft notes + store visit follow-ups**, then **review and approval by store
operations, merchandising, customer care, store technology and the service desk**.
Customer, associate and store data stay in the company: recordings, customer and
associate personal data, store performance figures, device and ticket details and
unreleased product information remain inside the company.

In this showcase the Surface Laptop Ultra stands in for Tier 1 and Tier 2, using
synthetic data only. The studio never calls a cloud service and does not connect
to point-of-sale, order management, endpoint management, a service desk (ITSM) system,
an HR system or any system of record. De-identification removes structured identifiers
only (pattern rules do not catch every name or identifier in free text); it is not
certified and makes no privacy, regulatory or compliance determination.

## Device classes: what runs where

The **Device classes** page (native navigation, right after **Platform fit**) answers
the first question and the device half of the second. It is headed *What
runs where: the AI PCs you have, and where Surface Laptop Ultra fits.* The **Company
overview** card *What runs where* opens it with **Open Device classes**. In the
companion web presentation, the **Device classes** header button opens the same story
as a dialog under the same heading, with numbered sources listed as plain URLs at the
end. The dialog's first two parts cover the Copilot+ PCs you already have and what to
try on one this week. Its next parts are *Builder PCs: Surface Laptop Ultra (this
laptop)*, *Always-on and shared*, *Everyday workloads by device class* (memory fit only;
the native page shows the engine-computed view, including this laptop's GPU budget) and
*Patterns from other industry showcases*. Every NPU statement on the page and in the
dialog is a Microsoft-sourced fact shown with its source, under this disclaimer:

> NPU routes on this page are documented by Microsoft; this app does not run anything on an NPU. Everything live here runs on this laptop's RTX GPU through CUDA.

### The Copilot+ PCs you already have

What Microsoft documents about these PCs, with the source for each line:

- Copilot+ PCs have an NPU that can perform more than 40 trillion operations per
  second, but software must be programmed to use it. Task Manager shows NPU usage, and
  Microsoft recommends Windows ML for running your own models on the NPU
  ([NPU devices, Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/npu-devices/)).
- Built-in Copilot+ PC experiences include improved Windows search, Recall (preview)
  and Live Captions with real-time translation from 40+ languages into English.
  Availability depends on the device, Windows version, region and organization
  settings ([Copilot+ PCs for business](https://www.microsoft.com/en-us/windows/business/devices/copilot-plus-pcs)).
- On Surface Laptop, Copilot+ PC experiences are available on configurations with
  16 GB of memory or more ([Surface Laptop](https://www.microsoft.com/en-us/surface/devices/surface-laptop)).
- Windows AI APIs such as Phi Silica, text recognition (OCR), Image Description, Image
  Super Resolution and Image Segmentation run on the NPU on Copilot+ PCs. The Speech
  Recognition API is experimental and the Semantic Search API is in private preview;
  AI Dev Gallery in the Microsoft Store has samples
  ([Windows AI APIs, Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/apis/)).
- Phi Silica is Windows' on-device language model, preinstalled on Copilot+ PCs and
  offered as a Limited Access Feature. Its successor, Aion Instruct, arrives in Windows
  Insider builds from November 2026 and in retail Windows from January 2027, with no
  Limited Access Feature token
  ([Phi Silica, Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)).
- Windows ML picks an execution provider such as QNN (Snapdragon) or OpenVINO (Intel)
  and can fall back to the GPU or CPU
  ([Windows ML execution providers, Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/supported-execution-providers)).
- Foundry Local detects the NPU, GPU and CPU and downloads matching execution
  providers. Which models have an NPU variant depends on the device, so verify on the
  target PC
  ([Foundry Local meets more silicon, Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/foundry-local-meets-more-silicon/)).
- Foundry Local runs models on the device with no cloud dependency or Azure
  subscription. Its SDK discovers the device's execution providers, downloads and
  registers them, and provides a model catalog; the Windows package integrates with
  Windows ML
  ([Get started with Foundry Local, Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry-local/get-started)).

Why the NPU sits idle: it only helps when software is built to use it. Built-in Windows
experiences such as improved Windows search and Live Captions use it, and your own apps
reach it through the Windows AI APIs, Windows ML or Foundry Local.

#### Try this on a Copilot+ PC you already have

1. Open Task Manager to see NPU activity
   ([NPU devices](https://learn.microsoft.com/en-us/windows/ai/npu-devices/)).
2. Install AI Dev Gallery from the Microsoft Store and run the Windows AI API samples
   ([Windows AI APIs](https://learn.microsoft.com/en-us/windows/ai/apis/)).
3. Ask a developer to try Foundry Local: its SDK discovers the PC's execution providers
   and lists the model variants available for it
   ([Get started with Foundry Local](https://learn.microsoft.com/en-us/azure/foundry-local/get-started)).
4. Pick one workload below that fits a 16 GB Copilot+ PC and pilot it on synthetic data
   first.

#### Everyday workloads by device class

The page's matrix has one row per T-shirt sizing workload. Each fit comes from the same
engine as **T-shirt sizing** (4-bit weights, 8K context): the 16 GB and 32 GB columns
are illustrative memory sizes, and a third column, *This laptop (GPU budget)*, uses
this laptop's live GPU memory budget, so it is computed on the device and not repeated
here. Every documented NPU route carries a link to its Microsoft source. **Run live**
(shown only for the workloads that have a live demo on this laptop) opens the matching
demo without starting it; start the run from the demo runner, on the RTX GPU. The other
rows read *Memory estimate only; this row has no live demo on this page.* **Open
T-shirt sizing**, under the matrix, opens **T-shirt sizing** on the **Leader view**.
The outcomes for the illustrative laptops:

| Workload | Size | 16 GB estimate | 32 GB estimate | Suggested class | Documented NPU route |
|---|---|---|---|---|---|
| Transcription & meeting notes | S (3.8B) | Comfortable | Comfortable | Copilot+ PC (16 GB) | Speech Recognition API (experimental) and Live Captions |
| Field & frontline notes | S (3.8B) | Comfortable | Comfortable | Copilot+ PC (16 GB) | Phi Silica text skills (Aion Instruct from 2027) |
| Translation | M (8B) | Comfortable | Comfortable | Copilot+ PC (16 GB) | Live Captions real-time speech translation |
| Writing & summaries | M (8B) | Comfortable | Comfortable | Copilot+ PC (16 GB) | Phi Silica text skills (Aion Instruct from 2027) |
| Ask your documents | M (8B) | Comfortable | Comfortable | Copilot+ PC (16 GB) | Improved Windows search; Semantic Search API (private preview) |
| Photos & scanned forms | M (8B) | Comfortable | Comfortable | Copilot+ PC (16 GB) | Text recognition (OCR) and Image Description APIs |
| Local coding assistant | L (14B) | Won't fit | Comfortable | 32 GB AI PC or Builder PC | No documented NPU route on this page |
| Analysis & reasoning | L (14B) | Won't fit | Comfortable | 32 GB AI PC or Builder PC | No documented NPU route on this page |
| Bigger-model prototyping | XL (32B) | Won't fit | Comfortable | 32 GB AI PC or Builder PC | No documented NPU route on this page |
| Largest open models (70B class) | XXL (70B) | Won't fit | Won't fit | Builder PC (Surface Laptop Ultra) | No documented NPU route on this page |

Memory fit only, using the same arithmetic as T-shirt sizing; it does not confirm an
NPU model variant or runtime support. Verify on the target PC.

### Builder PCs: Surface Laptop Ultra (this laptop)

- Microsoft describes Builder PCs as a device class for hybrid intelligence, and Surface
  Laptop Ultra is one
  ([Building Windows for hybrid intelligence, Windows Experience Blog, 7 October 2026](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/)).
- Surface Laptop Ultra has the NVIDIA RTX Spark Superchip, built for local AI and 3D
  graphics, and up to 128 GB of unified memory
  ([Surface Laptop Ultra](https://www.microsoft.com/en-us/surface/devices/surface-laptop-ultra);
  memory configurations and full specifications in the
  [tech specs](https://learn.microsoft.com/en-us/surface/tech-specs/surface-laptop-ultra-1stedition)).
- From the same product page: "Run local agents, automate routine tasks, keep sensitive
  work closer to you, and reserve the cloud for larger AI workloads." It is "built for
  organizations working with proprietary code, AI models, customer data, and
  intellectual property".

Where it fits, for retail use cases:

- **Workloads that outgrow a 16 GB laptop**: the L, XL and XXL rows above (a local
  coding assistant, analysis and reasoning, bigger-model prototyping and the largest
  open models), plus the larger llama.cpp models in *Larger models*.
- **Local agents**: keep sensitive work on the device and reserve the cloud for larger
  workloads, the pattern the **Hybrid router** shows.
- **Proprietary code**: a local coding assistant for e-commerce and store systems code
  and internal tools, with the code kept on the device (the *Local coding assistant*
  demo and **Build on Surface**).

The page's live line, *GPU memory budget on this laptop now: X GB* (*Not known yet*
until the driver reports it), comes from the graphics driver. The GPU can address less
than the installed memory, so the estimates for this laptop use that budget, not the
installed total. On this laptop Foundry Local offers the CUDA, NvTensorRTRTX and WebGPU
execution providers and no NPU provider; everything live in the app runs through CUDA.

The Windows Experience Blog post says Surface Laptop Ultra "combines up to 128 GB of
unified memory with the ability to run AI models exceeding 120 billion parameters
locally". That is the blog's statement, not something this app runs or computes: the
largest size the app's engine sizes is XXL (70B class), and on this unit's memory
configuration the app refuses GPT-OSS 120B (see *Larger models*). The app does not
repeat the blog's claim.

### Always-on and shared

- Mini desktop PCs are a device class for always-on agents
  ([blog](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/)).
- DGX Station for Windows, with NVIDIA GB300, is a device class for trillion-parameter
  models and 32 or more simultaneous agents (same blog post).

The page labels one example *Illustrative fit, not a recommendation*: an always-on
agent that drafts a daily fleet health summary for people to review. This app does not
size or run these classes; ask the account team about them.

## Patterns from other industries

The **Device classes** page ends with *Patterns from other industry showcases*:
fictional patterns from Microsoft's industry showcases, not customer references. Ask
the account team for named customer references. Each card names the pattern, says
what it looks like in retail, shows the engine-computed suggested class for its
T-shirt sizing workload, and has a **Run the equivalent here** button that opens the
matching live demo on this laptop:

| Industry | Pattern | In retail | Suggested class | Run the equivalent here |
|---|---|---|---|---|
| Financial services | Meeting capture | Store operations calls | Copilot+ PC (16 GB) | *Store operations and IT call to notes and actions* |
| Telecom and media | Offline field notes | Distribution center shift handoffs | Copilot+ PC (16 GB) | *Voice memo to a shift handoff note* |
| Tax and accounting | Scanned forms | Store device service forms | Copilot+ PC (16 GB) | *Scanned form to structured data* |
| Higher education | Policy questions with citations | Device standards and change policy | Copilot+ PC (16 GB) | *Ask your documents* |
| Private markets | De-identify before the cloud | Associate emails before any cloud step | Copilot+ PC (16 GB) | *De-identify before escalating (Tier 3)* |
| Engineering and software | Proprietary code assistant | E-commerce and store systems code | 32 GB AI PC or Builder PC | *Local coding assistant* |

The companion web presentation's **Device classes** dialog lists the same six patterns
with each one's T-shirt sizing workload; run the equivalents from the native page.

## Download

No release has been published for this edition yet; run it from source (see
*Run on this device*). A release built with `tools\New-ReleasePackage.ps1` contains:

| File | What it is |
|---|---|
| `HybridIntelligenceRetail-<version>-win-arm64.zip` | The self-contained app (no .NET or Windows App SDK install needed), the local service, demo content and `Setup.cmd` |
| `HybridIntelligenceRetail-<version>-icon-pack.zip` | The app icon: PNG from 16 to 1024 px, a multi-size `.ico` and the `.svg` source, with a NOTICE |
| `SHA256SUMS.txt` | SHA-256 hashes of both zips |

Check the hash, unblock the zip (`Unblock-File`), extract it to a short path
such as `C:\Apps`, then double-click `Setup.cmd`. It finds an ARM64 Python 3.12
to 3.14 (3.13 tested), creates `.venv`, installs `requirements.txt` with the
tested dependency versions pinned in `constraints.txt`, adds the
desktop shortcut, then downloads every model the app uses and runs each live
demo once to check it. `.\Setup.ps1 -Prepare` does the same from a terminal
(Windows PowerShell 5.1 or PowerShell 7); `-NoShortcut`, `-Port` and
`-Python <path>` are optional. The pre-flight result is saved to
`.runtime\setup-prepare.json`. Requires Windows 11 on ARM64 with an NVIDIA GPU.
The app is not code-signed, so Windows may ask you to confirm the first launch.

## Run on this device

From the repository root:

```powershell
.\Start-NativeShowcase.ps1
```

The native application uses real WinUI controls, not an embedded browser.
Its C# interface talks to the existing loopback Python inference service so the
verified CUDA model selection, stream filtering, and calculation rules stay
consistent. **Qwen2.5-Coder 14B** and **GPT-OSS 20B** are the featured live models;
larger llama.cpp models are offered when their weights are installed (see *Larger models*).
Snapdragon and Intel recommendations are separate planning content, not
claims of having run those platforms on this machine. This build targets
Windows ARM64; platform guidance is not a cross-platform deployment package.

The app reuses an identified showcase service already running on
`127.0.0.1:8814` and leaves that external service running when it closes.
If none exists, it starts the local Python service itself and stops that
owned service on exit; a Windows job object also prevents an orphan if the
app crashes. Startup logs are in `.runtime\native\backend-*.log`.
`-Port`, `-Windowed`, `-Section <page>` (overview, live, demos, hybrid, industries,
showoff, build, sizing, platforms, deviceclasses, business, playbook, learn), and `-Rebuild` are supported by
`Start-NativeShowcase.ps1`; no browser or extra terminal must remain open.
The launcher builds the native executable if it is missing. A .NET 10 SDK
and Windows App SDK NuGet packages are required for a build, not for every launch.

The original red **laptop-and-spark icon** (Fluent-style, drawn for this project) appears in native window/taskbar
branding, the executable, and the companion browser tab. It is prototype
artwork, not official Microsoft brand artwork or an endorsement. The name, logo and
accent colours come from `edition.json` (see *Editions and scale-out harness*);
`.\tools\Sync-Edition.ps1` regenerates `native\Brand.cs` and the PNG/ICO/SVG
assets in `native\Assets`.
`.\tools\Install-NativeShortcut.ps1` installs or updates the
**Surface Hybrid Intelligence x Retail** desktop shortcut with the native target,
app icon and matching Windows taskbar identity.

The live workspace offers five synthetic text workflows: a retail leadership briefing,
store technology code drafting, **Snapdragon-fit distribution center shift handover**,
**Intel-fit store operations review actions**, and a plain-English **coding tutor** used
by the optional lessons. The handover and store operations review workflows demonstrate
portable workflow patterns on the current
RTX device, not execution on a Snapdragon or Intel accelerator. They consume
supplied text fixtures; they do not record, transcribe, inspect images or
connect to business systems. Speech, images and document search are on the
**Live demos** tab.

### Live demos

The **Live demos** tab has a launch button for each of twelve demos that run
real models on the RTX GPU (Foundry Local CUDA variants only; no CPU or cloud
fallback). Every input is synthetic and fictional. The meeting and voice-memo
audio is spoken by Windows text-to-speech, and the form and receipt images are
drawn by Windows. Both are rendered once on the laptop by
`Render-DemoMedia.ps1` into `.runtime\demo-media`. Because the script is known,
the engine can grade live output against it.

| Demo | Runs on the GPU | Graded by the engine |
|---|---|---|
| Store operations and IT call to notes and actions | Whisper medium, then Qwen2.5-Coder 14B | Word accuracy against the spoken script; unowned action marked |
| Voice memo to a shift handoff note | Whisper medium, then Qwen2.5-Coder 14B | Valid JSON; fields match the memo |
| Scanned form to structured data | Qwen3-VL 4B (store device service form or receipt) | Valid JSON; fields or line-item arithmetic |
| Ask your documents | Qwen3-Embedding 0.6B, then Qwen2.5-Coder 14B | Right policy retrieved; answer cites only retrieved policies |
| Translate on the device | Qwen2.5-Coder 14B | Names, references and times kept unchanged |
| Executive brief from notes | Qwen2.5-Coder 14B | Source citations; no-benefit-claimed sentence |
| De-identify before escalating (Tier 3) | Qwen2.5-Coder 14B | No synthetic identifier remains; business wording kept |
| Inbox triage to structured data | Qwen2.5-Coder 14B | Valid JSON for all six emails; categories match the labels |
| Local coding assistant | Qwen2.5-Coder 14B | A Python function was drafted (never executed) |
| Plan it out with a reasoning model | GPT-OSS 20B | Schedule satisfies all six constraints |
| Model face-off: 14B versus 20B | Both chat models, same prompt | Each answer graded separately |
| Five models, one laptop | Chat, reasoning, speech, vision, embedding | Each model's task; residency from Foundry Local, memory from Windows counters |

Each step shows its model, load time on first use, time to first token, speed
and total time. Answers under 20 tokens show *too short to measure* instead
of a speed. Reasoning is counted but its text is never shown, exported or saved. A wrong
answer is shown as a graded result, never hidden or replaced. **Play rehearsal**
replays authored sample output, labelled *Rehearsal: no model ran*. The
face-off, the five-model demo and non-default translation languages have no
rehearsal. Editing a live instruction skips checks that depend on the default
prompt. **Pre-flight: run every demo live** runs all twelve with their default
inputs and reports how many ran end to end and how many passed every check. On
this unit a warm pre-flight takes about three minutes. Export saves the
selected run's evidence as JSON. On the **Leader view** sizing tab, each red **Run live
demo** button with a play icon opens the matching demo and starts a live GPU
run. The separate checkboxes select workloads for sizing; the buttons do not
change that selection. If the GPU is busy or
not ready, the demo opens with the reason it cannot start; no rehearsal is substituted.

Demos load extra models beside the selected chat model and keep them resident,
so later runs skip loading. Selecting a model in the Live GPU workspace still
unloads the other chat models. Speech, vision and embedding models need two
items that `Start-Showcase.ps1 -Prepare` downloads once:
- the model weights;
- NVIDIA's cuDNN 9.26 and NVRTC 13.4 redistributables, about 210 MB of
  SHA-256-pinned wheels from PyPI. They go into the app-data folder, because the
  Foundry Local ARM64 CUDA bundle ships cuDNN without the sub-libraries that
  convolution and attention graphs need.

Nothing is installed into Python and no NVIDIA DLL is committed. The
**Ready to present?** panel shows what is still missing before you start.

### T-shirt sizing and platform fit

The **T-shirt sizing** page has two tabs. **Leader view** (the default) is a
100-level view: pick broad workloads such as transcription and meeting notes,
translation, writing, a local coding assistant, reasoning or the largest open
models (70B class). The app recommends
the largest size those workloads need, shows the fit on this unit's RTX GPU
budget versus illustrative 32 GB and 16 GB laptops, and gives a jargon-free
talk track whose percentages come from the same engine. **Technical view** is the
full planner described below; **See the technical math** hands the selected
size across with identical results.

#### Which Surface Laptop Ultra configuration?

Below the Leader view results, the **Surface Laptop Ultra configurations** planner
turns the picked workloads into a memory recommendation across the 24, 32, 48,
64 and 128 GB options in Microsoft's tech specs. Each card runs the same
estimate (4-bit weights, 8,192-token context, 6 GiB reserve, 2 GiB headroom)
against that configuration's dedicated GPU memory and shows **Recommended**,
**Plenty of room**, **Little room** or **Won't fit**, plus a copyable talk track.

- **Recommended** is the smallest configuration whose estimate uses at most 80%
  of the memory left for AI. Real 4-bit model files are larger than the
  estimate (the Llama 3.3 70B file the app loads is 39.6 GiB against 32.6 GiB
  estimated), so a "Little room" fit is flagged rather than recommended.
- **AI models in use**: *One at a time* sizes for the largest model;
  *All open together* adds the models up. Writing, translation and documents
  share one general model.
- **Document length**: *Long documents* raises the context to 32,768 tokens.
- **GPU share**: the default is Microsoft's launch Task Manager image of a
  128 GB unit (79.9 GB dedicated GPU memory, 62%), applied to every
  configuration. *This PC's measured split* uses this unit's driver report
  instead (62.5 GB of 128 GB here, 49%); *Custom share* accepts 10-90%.
  Microsoft has not published the split for the smaller configurations.
- Processor pairings (24 GB entry with the 18-core CPU, 128 GB with the
  20-core CPU) come from launch coverage; confirm them in the configurator.

It is a memory-only estimate: no pricing, response-time, battery or support
claims. Sources: [Surface Laptop Ultra tech specs](https://learn.microsoft.com/en-us/surface/tech-specs/surface-laptop-ultra-1stedition),
Microsoft's launch Task Manager image of a 128 GB unit, and this unit's driver
report on the Device evidence page.

Sizing is a transparent planning estimate, not a benchmark or procurement
guarantee. Start with a model band, then adjust precision, context, working-set
allowances, reserve and headroom against **one** appropriate memory budget.

| Size | Nominal parameter band | Example workload |
|---|---|---|
| S | 1-4B | Bounded note drafting, short summaries |
| M | 7-8B | Service-desk drafts, richer document assistance |
| L | 14-20B | Code drafting and structured reasoning pilots |
| XL | 24-32B | Larger-model evaluation on a qualified configuration |
| XXL | 65-72B | Largest open models (Llama 3.3 70B class) on a large-memory configuration |

Raw weight estimate in GiB = billions of parameters × 1,000,000,000 ×
weight bits ÷ 8 ÷ 1,073,741,824. Runtime, context/KV cache, reserve and
headroom are additional assumptions. Quantization metadata, architecture,
activation memory, execution-provider behavior and concurrency can change
the actual working set. A fit indicator is not proof of model compatibility,
quality, speed, or support. Do not add Windows-visible memory and the GPU's
reported budget, and do not use 128 GB installed as proof of 128 GB GPU capacity.

**Snapdragon pilots:** field-note drafting, transcription followed by a reviewed
summary, and image-assisted inspection. Qualify the exact Windows ARM64 app,
shipping SKU, model artifact, license and accelerator/runtime route first.
Qualcomm's official Windows tutorial demonstrates target-specific Qwen3-4B
deployment; its model card and runtime requirements still govern each target.

**Intel pilots:** meeting transcription and summaries, service-desk/knowledge
drafts, and visual-document triage. Qualify the Intel device, exported model
and supported OpenVINO pipeline. A supported CPU path does not establish GPU
support, and not every Core or Core Ultra SKU has the same capabilities.

**This RTX device:** the live 14B coding and 20B reasoning paths use their
exact cached CUDA variants. The other use cases are pilot recommendations,
not new speech/image integrations or measured cross-device comparisons.

Official references:
- [Qualcomm: LLMs on Windows Snapdragon with target-specific runtime/model assets](https://github.com/qualcomm/ai-hub-apps/tree/main/tutorials/llm_on_genie)
- [Qualcomm: Whisper-Base export and deployment](https://github.com/qualcomm/ai-hub-models/tree/main/src/qai_hub_models/models/whisper_base)
- [OpenVINO GenAI pipelines and platform support](https://github.com/openvinotoolkit/openvino.genai)
- [Microsoft Foundry Local SDK and execution providers](https://learn.microsoft.com/en-us/azure/foundry-local/reference/reference-sdk-current)

### Optional: Coding as a second language

An optional AI-literacy tab for service desk analysts, store operations and IT support
staff who are new to code and want to follow conversations with desktop engineers,
developers and architects. Eight
short lessons teach reading code the way you learn a language: vocabulary
(variables), grammar (decisions, loops), sentences (functions, data/JSON),
conversation (APIs, AI sizing words) and fluency (reading AI-written code).
The examples use the fictional Contoso Apparel (for example `technicians = 240`).
Each lesson has a plain-English analogy, line-by-line notes, a colleague-ready
sentence and a quick check; a correct answer completes the lesson. Numbers in
lessons are computed by the same engine as the sizing page (for example 14B at
4-bit = 6.52 GiB of weights). **Ask the local coding tutor** opens the Live GPU
workspace with the lesson's code in the prompt so the local coding model explains it
on the RTX GPU. Code is displayed, never executed. Progress is stored only in
`%LOCALAPPDATA%\HybridIntelligenceRetail\learning.json`. Hide or restore the tab from
the lesson page or the **Retail playbook** page.

### Companion web presentation

```powershell
.\Start-Showcase.ps1
```

Open **http://127.0.0.1:8814**. Keep the launch terminal open. Ctrl+C stops only
the process started by the launcher. Ctrl+Enter runs the selected AI story.
The full-screen button expands the presentation. The **Device classes** header button
opens the dialog *What runs where: the AI PCs you have, and where Surface Laptop Ultra
fits.* (see *Device classes: what runs where*). The **Retail playbook** contains
the talk track and objection handling; **Print executive handout** prints a
clean, audience-facing summary with the calculator's current assumptions.
`.\tools\Install-NativeShortcut.ps1` adds a **Surface Hybrid Intelligence x Retail** desktop shortcut.
`.\tools\Test-Edition.ps1 -Browser` writes `Executive-Handout.pdf`, a single-page
handout using illustrative default assumptions (this edition does not ship one);
print again from the app after changing those inputs.
Launching again opens the existing showcase rather than starting a second
model process. Stop the original launch terminal before changing startup mode.

### Retail scenarios and Offline PPTX Forge

The **Retail scenarios** page (section `industries`) adds six fictional
workflows for the fictional Contoso Apparel, across store operations, merchandising,
customer care, inventory and allocation, store technology and the service desk. Each is
a live drafting workflow on the local GPU model. Each drafts from cited source notes
([A], [B] or [C]) under three review headings, and every prompt ends with a fixed review
sentence that begins *Draft only;* and names who must review the draft:

| Key | Industry | Workflow | Fictional subject |
|---|---|---|---|
| `store-visit` | Store operations | Store visit notes to a district follow-up list | Store 0412 Saturday visit (SV-0412) |
| `line-review` | Merchandising | Line review notes to a sample follow-up list | Spring 2027 collection (unreleased), line review LR-2027S |
| `customer-care` | Customer care | Customer contact notes to a case summary | Online order WEB-771204 delivered incomplete (case CC-58210) |
| `replenishment` | Inventory and allocation | Weekly in-stock notes to a replenishment review | Weekly in-stock export for 310 stores (IS-2026-W43) |
| `fleet-health` | Store technology | Weekly fleet and service desk data to a health summary | Contoso Apparel endpoint management and service desk export (FH-2026-W43) |
| `major-incident` | Service desk | Major incident notes to a stakeholder update draft | Relecloud Scheduler sign-in incident (MI-3317) |

Names and data are invented for demonstration; no real company, customer, store,
associate, device, order, app, vendor or product appears. Drafts support store
operations, merchandising, allocation, customer care, store technology and the service
desk. They never approve or deploy a change, close or reassign a ticket, change a device
policy, determine a root cause, issue a refund or credit, place an order, transfer or
allocation, or make HR, vendor, purchasing, pricing or supplier decisions, and nothing
is sent to customers.

Each card offers:

- **Run live workflow**: opens the Live GPU workspace with the scenario's prompt.
- **Prepare deck in Forge**: writes a deck brief to Offline PPTX Forge's
  `briefs\custom\studio_<key>.json` (hyphens become underscores, for example
  `studio_store_visit.json`) and opens Forge. In Forge's Pre-staged mode select
  *<Client> - sales (custom)*, review the facts and template, then choose **Build deck**.
  Nothing is generated until you do. If Forge is already open, it is not launched again
  (Forge lists briefs at startup): use **Open another brief (.json)...** in that window.
- **Export deck brief (JSON)**: saves the same brief under the export folder's
  `forge-briefs` directory for use on another PC.

Forge is found beside this repository (`..\Offline-PPTX-Forge`) or at
`HYBRID_RETAIL_FORGE_ROOT`. Forge is started through Explorer, so closing the studio does
not close Forge. `.\Start-NativeShowcase.ps1 -Section industries` opens the page directly.

### Hybrid Intelligence: router, show-off tools and builder hub

Three pages turn "Hybrid Intelligence on Surface" from a slide into something people can
see, measure and build on. The Company overview links to all three.

**Hybrid router** (`-Section hybrid`) shows where a request should run and why. A published,
deterministic policy (`hybrid.py`, standard library only) scans the text for identifiers and
credentials and for needs only a cloud service meets (current information, organisation-wide
data, beyond-device scale). It then picks one lane:

- **On this PC**: private data and nothing that needs the cloud, or credentials (cloud blocked),
  or the *offline* what-if (the cloud step is queued, never sent).
- **Hybrid**: personal data *and* a cloud need. The on-device model redacts first, then
  the policy re-scans the result and checks that the request itself survived (a model that
  answers or rewrites the request instead of redacting it is blocked). Only a payload that passes both checks is shown.
- **Cloud**: nothing sensitive and a real cloud need.

Seven fictional presets cover every lane:

| Preset | Expected lane |
|---|---|
| *Associate email to the service desk* | On this PC |
| *Store manager question that needs the latest release notes* | Hybrid |
| *Public Windows on Arm news* | Cloud |
| *Service desk export connector config with a credential* | On this PC (the credential blocks the cloud) |
| *Store visit note while offline* | On this PC (offline what-if) |
| *Company-wide question* | Cloud |
| *Complex question: escalate to Tier 3* | Hybrid, beyond-device scale (opened by the Company overview's **Route a complex question**) |

**Explain the route** is policy only (no model runs); **Run it on
this PC** streams the local answer or the redaction from the RTX GPU. Cloud payloads are
displayed and marked **NOT SENT**: the studio never calls a cloud service. A gallery of seven
hybrid patterns (local-first, redact-then-cloud, private knowledge, field, high volume,
right-size, same API) links each pattern to a demo or page you can run now. The rules catch
structured identifiers, not every name, free-text identifier or context clue; they are not a data-loss-prevention product.

**Show it off** (`-Section showoff`) has:

- **GPU speedometer**: measures the loaded model's generation speed (output tokens after the
  first, over streaming time, or llama.cpp's own timings), first visible text, and reading speed
  (an estimate that includes request setup). One run on this PC, not a benchmark. **Export
  results (JSON)** saves timings and counts only, never generated text.
- **Session leaderboard**: one row per run, ranked by generation speed; cleared when the studio closes.
- **Five-minute run of show**: decision → number → endpoint → industry → deck, one button per step.
- **Companion tools**: finds and opens Offline PPTX Forge, Local AI Tokenomics, Local AI
  Headroom, Local AI Bench and HydraFusion autorouting when they are cloned beside the studio
  (or at `HYBRID_RETAIL_FORGE_ROOT`, `_TOKENOMICS_ROOT`, `_HEADROOM_ROOT`, `_BENCH_ROOT`,
  `_HYDRAFUSION_ROOT`); otherwise it links to their GitHub repositories. Tools start through
  Explorer, so they outlive the studio. Headroom and Bench open existing reports only.

**Build on Surface** (`-Section build`) is for developers:

- **Local endpoint**: an OpenAI-compatible API for the loaded model on
  `http://127.0.0.1:<studio port + 1000>/v1` (set `HYBRID_RETAIL_ENDPOINT_PORT` to change it).
  It is **off by default**, loopback only and unauthenticated (any app on this PC can call it
  while it runs), stops when you stop it or close the studio, and shares the GPU with the
  studio. Larger llama.cpp models already serve this API while loaded. **Send a test call**
  makes a real loopback request and shows the HTTP status and timing; private reasoning is never shown.
- **Code snippets**: copy-ready calls for the current endpoint and model (PowerShell, curl,
  Python, the OpenAI Python SDK, JavaScript, C# and the models list).
- **Starter kits**: five small projects written to
  `Documents\Surface Hybrid Intelligence x Retail\Exports\Starters\<kit>-<time>`:

  | Kit | Run | Shows |
  |---|---|---|
  | Streaming chat (Python) | `python chat.py "..."` | Streaming from the local model |
  | Ask private documents (Python) | `python ask_docs.py "..."` | Retrieval with cited answers over synthetic policies |
  | Redact, then cloud (Python) | `python redact_then_cloud.py sample.txt` | The router policy, on-device redaction, both checks; `send_to_cloud()` is a stub |
  | Tool-using agent (Python) | `python agent.py` | A JSON-action agent with an allow-listed calculator, policy lookup and date |
  | Streaming chat (C# / .NET 10) | `dotnet run -- "..."` | `HttpClient` and `System.Text.Json`, no NuGet packages |

  Python kits need Python 3.10+ and the standard library only. Every kit reads
  `LOCAL_AI_BASE_URL` and `LOCAL_AI_MODEL` when set, so the same code can target another
  loopback model or, after your own review, an approved cloud endpoint. The studio writes
  the files and never runs them; it refuses to overwrite a non-empty folder.

One GPU job runs at a time: while a speed test, hybrid run or endpoint change is active, the
Live, Demos and Industries runs wait, and the other way round.

### Larger models

The model selector has two tiers, all running on the RTX GPU:

| Model | Runtime | Notes |
|---|---|---|
| **Qwen2.5-Coder 14B** (default), **GPT-OSS 20B** (reasoning) | Foundry Local CUDA | Featured models; already cached |
| **Qwen3-Coder 30B-A3B** | llama.cpp CUDA | Speech, vision and second-model demos can still run beside it |
| **Llama 3.3 70B**, **GPT-OSS 120B** | llama.cpp CUDA | Need the GPU to themselves: Foundry Local closes while selected |
| **MAI Code 1.1 Flash** (137B MoE) | Not available | Listed, disabled; see below |

30B+ weights come from the checksum-verified Local-AI-Bench collection
(`%USERPROFILE%\Local-AI-Bench\models\installed.json`) and its pinned `tools\llama\llama-server.exe`.
Set `HYBRID_RETAIL_LLAMA_HOME` if Local-AI-Bench is not in your user folder. Rules:

- **Dedicated GPU memory only.** Before anything unloads, the app checks free dedicated
  GPU memory (nvidia-smi) and Windows commit against the weights file plus an estimated
  context overhead. Memory the app itself would release counts toward the fit. If the
  model cannot fit, the switch is refused and the current model stays loaded. The
  message names any other llama-server holding memory; the app never stops another
  app's server.
- **Every layer on the GPU or no load.** The server runs with `-ngl all -fit off`; the app
  reads `offloaded N/N layers to GPU` from its log and measures the process's dedicated
  and shared GPU memory with Windows performance counters. More than 2 GiB of shared GPU
  memory is refused.
- **Attach, don't duplicate.** If a llama-server is already serving the same weights with
  every layer on the GPU (for example a local coding-model stack on port 8090), the app uses
  it and leaves it running. Otherwise it starts its own server, which stops when another
  model is selected or the app closes. Logs: `.runtime\llama-<alias>.log`.
- **After sleep.** Windows can page a llama-server's GPU memory out while the PC sleeps:
  nvidia-smi then reports 3.6 GiB used while the 30B server still holds 30.7 GiB. The
  app counts that paged-out memory as in use. Before attaching, it sends the server a
  one-token request to move its weights back onto the GPU, then measures (4.4 s for the
  30B here).

**Why shared GPU memory is not used.** This GPU reports 63,986 MB dedicated plus
49,132 MB shared (Windows RAM it can borrow), so CUDA lists about 110 GB. Measured on this
Surface Laptop Ultra (Oct 18, 2026, on battery power, llama.cpp b11573): Llama 3.3 70B with
28.3 GiB dedicated and 14.3 GiB shared loaded all 81/81 layers but decoded at
2.6–3.2 tok/s, and the load took Windows commit from 44.8 GiB available to 1.3 GiB.

**Measured in this app** (Oct 18, 2026): Qwen3-Coder 30B-A3B, all layers on the GPU,
29.6 GiB dedicated and 0.4 GiB shared. On AC power: decode 83–91 tok/s across the code,
insurance and manufacturing scenarios, prompt processing about 2,010 tok/s, TTFT
178–183 ms where the prompt was not already cached. Earlier on battery power the same
code scenario decoded at 48–75 tok/s, slower at lower charge. Plug in before a demo.

**Llama 3.3 70B** needs about 43.6 GiB of free dedicated memory and **GPT-OSS 120B**
about 61.5 GiB. The Windows desktop held about 7 GiB of the 62.5 GiB in these tests, so
the 120B is refused on this memory configuration; it does not fit in dedicated memory.

**MAI Code 1.1 Flash** is not installed: Microsoft delivers its local build through
GitHub Copilot's Windows ML provider, with no standalone download for this app. The app
shows Microsoft's published figures (137B total and 6.8B active parameters, a 53 GB
quantized build, 75.5 GB peak memory at 256K context) labelled **Not measured by this app**, with the
[source](https://commandline.microsoft.com/local-models-sandboxed-tools-github-windows/).

Select a model, wait for its ready status, then run either AI story. In this
workspace, switching unloads the other chat models first. The Live demos tab can
load both Foundry models side by side for the face-off.
Neither parameter count nor larger memory is presented as proof of better quality.

```powershell
.\Start-Showcase.ps1 -Model gpt-oss-20b
```

On an existing instance, `-Model` requests the same in-app model change.
Model acquisition is permitted only when the server was started with `-Prepare`.
The two featured CUDA models are already cached on this device.
Reasoning can increase time before visible answer text. The app shows actual
reasoning character-count activity without revealing or saving reasoning text.

Both launchers and the native app choose Python in this order: the
`HYBRID_RETAIL_PYTHON` environment variable (must point to an existing
`python.exe`), a project `.venv`, then an installed Foundry SDK environment in
sibling folder `..\hydrafusion-autorouting-demo\.venv` if one exists. They do not
modify that project. When present, the existing SDK data/cache folder
`%LOCALAPPDATA%\ASUAgenticShowcase` is reused for provider registration and its
`models` subfolder for the larger model weights; no ASU application source is changed.
Otherwise the SDK uses `%USERPROFILE%\.surface-hybrid-intelligence-retail`. SDK logs
for this showcase go to `.runtime\foundry-logs`. Providers must be registered
in each process, even when already cached. That SDK operation can check the
network and repair its cache. No Python packages are automatically installed.
Use `-Prepare` explicitly to allow missing model/initial provider acquisition
before presenting. `-RehearsalOnly` does not import the SDK or load a model.
`-NoBrowser` and `-Port 8791` are also available.

For a standalone installation from source on compatible Windows ARM64 NVIDIA hardware:

```powershell
git clone https://github.com/npuneil/Surface-Hybrid-Intelligence-x-Retail.git
Set-Location Surface-Hybrid-Intelligence-x-Retail
.\Setup.ps1 -Prepare                      # .venv, requirements.txt, every model checked
.\Start-NativeShowcase.ps1                # builds the native app on first run
.\tools\Install-NativeShortcut.ps1
```

The native build needs the .NET 10 SDK: the launchers use
`HYBRID_RETAIL_DOTNET` if set, then `dotnet.exe` on PATH or the standard install
locations. NuGet restores the Windows App SDK packages pinned in
`native\packages.lock.json` from the public dotnet feed in `native\NuGet.Config`
into the standard NuGet cache (override with `NUGET_PACKAGES`).
`.\tools\Install-NativeShortcut.ps1` then adds the desktop shortcut.

The companion web UI and backend calculator use only the Python standard
library; no npm, CDN, remote fonts, JavaScript dependencies or cloud-model
endpoint is used. The native front end additionally uses .NET and the Windows
App SDK.

## What is real

- Windows CIM inventory is collected at each server start. This device currently
  reports Microsoft Surface Laptop Ultra, **128 GB installed physical RAM**, 20 CPU cores,
  and NVIDIA RTX Spark N1X Blackwell RTX GPU. These are observed
  device identifiers, **not confirmed shipping-SKU specifications**.
  Installed capacity is the sum of `Win32_PhysicalMemory.Capacity` records:
  137,438,953,472 bytes (128 GiB; displayed as the device's 128 GB configuration).
  Windows reports about **64 GB visible**, from
  `Win32_OperatingSystem.TotalVisibleMemorySize`. The earlier build incorrectly
  treated the OS-usable view as installed capacity; this is corrected.
  `nvidia-smi` separately reports a **64,000 MiB GPU memory budget**. These are
  distinct views, not independently additive pools or a dedicated-VRAM claim.
  No memory partition settings are changed.
- Live inference uses Foundry Local SDK 2.1.0 and pinned CUDA GPU variants:
  `qwen2.5-coder-14b-instruct-cuda-gpu:4` and `gpt-oss-20b-cuda-gpu:1`.
  Both require `CUDAExecutionProvider`. The app refuses silent CPU or cloud
  fallback. Its former 7B TensorRT model is no longer the default or a selectable
  fallback. The historical 7B coding benchmark does not establish these larger
  CUDA models' accuracy or speed; every displayed result is from the current run.
- The Live demos add the pinned CUDA variants `openai-whisper-medium-cuda-gpu:3`,
  `qwen3-vl-4b-instruct-cuda-gpu:2` and `qwen3-embedding-0.6b-cuda-gpu:1`.
  The five-model demo reads residency from Foundry Local's loaded-model list and
  GPU memory from the Windows WDDM counters at that moment: this process's use and
  the whole adapter's use, which includes other apps. It is a snapshot, not a
  capacity limit.
- Every live run measures first visible SDK text and total generation wall time.
  Model loading is excluded; reasoning time is included. Output volume shows
  visible answer characters, with private reasoning activity counted separately, not tokens
  or an invented progress percentage. Evidence exports include SDK token usage
  where available. SDK output token counts can include reasoning. Exported token
  rate includes prompt processing and reasoning, not decode-only speed.
  No comparative performance is implied.
- The capacity calculator runs deterministic server-side arithmetic:
  people × tasks/day × minutes gained/task ÷ 60 × days/year × effective adoption.
  Capacity value = hours × loaded labor value. Assumed incremental hardware
  cost = people × assumed per-device difference. Default result: 2,640 hours,
  $158,400 illustrative capacity value and $60,000 assumed incremental hardware.

## Boundaries

All scenarios and all company, customer, store, associate, device, order, ticket and
product data are synthetic. Do not enter customer or associate personal data, device and
asset identifiers, order or ticket details or unreleased product information into an
unapproved prototype. Drafts only; nothing is deployed, changed or sent. No change is
approved or deployed, no ticket is closed or reassigned, no device policy is changed, no
root cause is determined, no refund or credit is issued, no order, transfer or
allocation is placed, and no HR, vendor, purchasing, pricing or supplier decision is
made. Nothing is sent to customers, associates, stores, vendors or stakeholders.
The generated code is displayed, never
executed. Generated asserts are examples, not verified passing tests.
Drafts require human review. Token-limit completions are labeled incomplete.
No email, file-system automation, point-of-sale, order management, service-desk or
Microsoft 365 integration exists.

Rehearsal is explicitly selected, labeled **authored / no inference**, and tied
to the fixed sample prompt. Failures never substitute rehearsed text.
The presentation and device inventory focus on the RTX GPU and CUDA.
There is no fabricated cloud baseline, savings counter, battery test,
accelerator-rating claim, PC certification claim or subscription replacement claim.
RAM is not described as dedicated GPU memory.

Local inference means the model executes on this PC; it does **not** mean the
application is certified air-gapped. Setup and SDK catalog/provider operations
may access the network. Non-essential SDK telemetry is disabled; the SDK may
still send a minimal ProcessInfo event. Validate disconnected behavior in a
separate controlled pilot before making an offline-availability claim.

The server binds only to 127.0.0.1 and rejects non-loopback Host headers.
POSTs require a per-process token and same-origin requests. Model text is
rendered as text, never HTML. No inputs or outputs are persisted automatically;
evidence and business-case JSON are saved only through explicit exports.
The runtime may maintain its own model caches and logs. The optional builder
endpoint is a separate, unauthenticated loopback API that is off until started;
starter kits are written only when you create one and are never executed by the studio.

Capacity value is not cash savings or an ROI forecast. Software, implementation,
support, financing and change-management costs are excluded. Adoption and time
improvements are assumptions until a pilot measures them. Cloud subscriptions
are unchanged. Confirm availability, approved positioning, model licensing,
exact shipping SKU and pricing with the appropriate channels before selling.

## Editions and scale-out harness

This edition was generated from the Surface Hybrid Intelligence Studio with
`tools\New-Edition.ps1` and a retail manifest, then its content was retargeted to
retail workflows for stores, merchandising and IT at the fictional Contoso Apparel.

The studio is built to be re-badged for another partner, device or audience
without hand-editing a fork. `edition.json` is this tree's brand manifest:

| Field | Used for |
|---|---|
| `id`, `displayName`, `device` | Window title, title bar, exports folder, web title |
| `mark`, `markSubtitle`, `logo` | Navigation header and the generated icon/logo: `logo.style` is `monogram` (default; `logo.text` on a rounded square) or `device` (an original laptop-and-spark glyph from `tools\LogoGeometry.psd1`); optional `logo.backgroundEnd` adds a gradient |
| `accent`, `webAccent` | WinUI accent ramp and palette; web accent and focus colours |
| `codeName` | C# namespace, assembly/executable, project file, app-data folder |
| `appUserModelId`, `shortcutName` | Windows taskbar identity and desktop shortcut |
| `serviceAppId`, `schemaPrefix`, `envPrefix` | Service identity, export schema names, `<prefix>PYTHON`/`<prefix>DOTNET` |
| `repository`, `visibility` | Publishing target |

```powershell
.\tools\Sync-Edition.ps1             # regenerate Brand.cs, icon/logo, XAML/CSS accents
.\tools\Sync-Edition.ps1 -Check      # fail if generated files drifted from edition.json
.\tools\New-Edition.ps1 -Edition <id> -Destination ..\<folder>
.\tools\Test-Edition.ps1 -Path ..\<folder> -ForbiddenToken <word>
.\tools\New-ReleasePackage.ps1 -ForbiddenToken <word>   # release zips in .runtime\release
```

A target edition lives in `editions\<id>.json`: the same fields plus optional
`rules` (literal phrase rewrites for prose, each optionally limited by `files`
wildcards) and `forbiddenTokens`. `New-Edition.ps1` copies the tracked tree,
applies the rules, maps every source identity token to the target in a single
longest-match pass (a replacement is never re-replaced), renames paths such as
the project file, writes the target `edition.json` without its rules, then
regenerates `Brand.cs`, accents and assets. It fails if a forbidden token or any
source identity token remains in a file name or content, binaries included.
`-Force` refreshes an existing destination but keeps its `.git` folder, so an
edition repository can be regenerated from upstream and reviewed as a diff.
Editions have their own app identity and data folder, so several can be
installed side by side; give each its own service port, for example
`.\tools\Install-NativeShortcut.ps1 -Port 8792`.

`Test-Edition.ps1` is the conformance gate: manifest validation (including any
`editions\*.json` targets), sync check, leak scan, hygiene scan (user-profile
paths, user name, tokens, keys; binaries included), Python tests, native build,
self-test and UI smoke. `-Live` adds CUDA runs; `-Browser` runs the browser
check, refreshes `Executive-Handout.pdf` and scans it. Results are written to
`.runtime\edition-conformance.json`. The native self-test also fails if
`Brand.cs` disagrees with `edition.json`.

`New-ReleasePackage.ps1` builds the downloadable release for the current
edition: it stages the edition's files, exports the icon pack, builds the
self-contained native app for `win-arm64` without PDBs where the shortcut
expects it (`dotnet publish` would omit the app's `.pri` and `App.xbf`),
runs the hygiene scan on everything and the forbidden-token scan on text
files and the app's own binaries, then writes both zips, `SHA256SUMS.txt`
and `release-notes.md` (version from the project file). Publish with
`gh release create v<version> <both zips> SHA256SUMS.txt --notes-file release-notes.md`.

## Checks

Recorded results are committed in [validation/test-results.json](validation/test-results.json),
including GitHub API visibility verification and the tested commit. The November 2,
2026 run passed 115 Python tests, 443 native self-tests, 333 live UI checks and 35
browser checks. All 12 live demo pipelines completed; 11 passed every answer check.
In the model face-off, Qwen2.5-Coder 14B missed one scheduling constraint while
GPT-OSS 20B passed. This observed model-quality miss is retained, not counted as a
correct answer. Hybrid cloud payloads were previewed only (NOT SENT).

```powershell
.\tools\Test-Edition.ps1 -Browser -Live -NativePort 8814
.\tests\Native-Smoke.ps1
.\tests\Native-Smoke.ps1 -Live
python -m unittest discover -s tests -v
.\tests\Browser-Smoke.ps1
.\tests\Browser-Smoke.ps1 -IncludeLive
.\tools\Test-Edition.ps1
```

Native checks exercise deterministic sizing boundaries, Sales-to-Technical
parity, coding-lesson answers and progress storage, scenario parsing,
platform claims, exports, native navigation, calculator, authored rehearsal,
every Live demos launch, rehearsal and hand-off, every Hybrid router preset's
lane, the starter-kit writer's path guards, companion-tool discovery and the
interlock between GPU jobs.
The live option additionally runs every workflow, including the coding tutor,
on the actual CUDA model, then runs the full live-demo pre-flight, a speed test,
a real call to the builder endpoint and a live hybrid redaction. It requires
all demo models to be prepared and allows up to 40 minutes by default.
Native reports and render-target screenshots are in `.runtime\native`.
`tests\Inspect-NativeUI.ps1` provides external Windows UI Automation inspection
and JSON snapshots for an explicitly selected app process.

The browser check uses installed Microsoft Edge and native DevTools, with no
downloads or extensions. It saves reports/screenshots under `.runtime`.
The live option exercises both AI stories on both featured larger CUDA models,
exports measured evidence, and restores the default 14B model. It requires a
running showcase with both models cached and checks this device's 128 GB / 64 GB
memory views. Both browser modes validate the single-page PDF layout.
See `SELLER-GUIDE.md` (the Retail playbook) for the presentation.
