# Retail playbook: Surface Hybrid Intelligence x Retail

**Event:** Retail leaders, theme *Local and hybrid AI for stores, merchandising and IT*.
The session is not prepared for any named company: nothing in the app or this guide
describes a real retailer's fleet, systems, stores, people, products or results. Contoso
Apparel is a fictional apparel retailer, and the reference architecture is illustrative
rather than a description of any company's actual design. This playbook is the
presenting team's guide: the app serves it at `/seller-guide`, so keep it off the
shared screen.

**Audience (roles only):** retail leaders in store operations, merchandising and
product, inventory and allocation, customer care, store technology and the IT service
desk, with CIOs, CISOs and the information security, privacy and change-management
reviewers who work with them. This guide names no customer or Microsoft staff; keep it
that way in notes and follow-ups.

**Presenting team (roles only):**
- The account technology strategist opens at 00:00 and leads the close at 00:55.
- The local and hybrid AI specialist drives the app in every live segment, from 00:05
  to 00:35.
- The Surface specialist owns Surface Laptop Ultra specs, Arm requirements, pricing and
  purchase options at 00:45.

**Positioning:** Local and hybrid AI for stores, merchandising and IT. Store and
operations calls, customer and associate personal data, store performance figures,
device and ticket details and unreleased product information stay inside the company;
only de-identified, minimized queries for complex questions would go to Azure OpenAI;
store operations, merchandising, customer care, store technology, the service desk and
the other owners review and approve every draft. This is a locally
demonstrated workflow, not a claim that every workload belongs on a PC. The device
earns its place through a measured pilot.

**Ground rules for the session:**
- Every company, customer, store, associate, device, app and record is fictional and
  synthetic: Contoso Apparel (an apparel retailer with a headquarters, stores such as
  Store 0412, distribution centers such as DC-2, an online store, a customer care team
  and a product development team), Relecloud Scheduler (a store scheduling app), the
  VanArsdel TP-40 receipt printer, Lucerne VPN, the Trey Research endpoint agent and
  the Southridge inventory app. Scenario staff are named only as Ana (store operations
  manager), Marcus (desktop engineer), Priya (service desk manager), Kenji (incident
  manager) and Jamie Lin (customer care agent); demo fixtures use fictional full names.
- Drafts only; nothing is deployed, changed or sent. Store operations, merchandising,
  allocation, customer care, store technology, the service desk and the incident
  manager review every draft.
- No draft approves or deploys a change or update, closes or reassigns a ticket,
  changes a device policy, determines a root cause, issues a refund or credit, places
  an order, transfer or allocation, or makes an HR, vendor, purchasing, pricing or
  supplier decision. Nothing is sent to customers, associates, stores, vendors or
  stakeholders. Not legal or HR advice.
- No performance, cost or productivity claims, on screen or in conversation. Timings are
  one run on this laptop, not a benchmark or a comparison.
- Never name real people, the audience's systems or tools, or third-party vendors. Say
  "point-of-sale", "order management", "endpoint management", "service desk (ITSM)
  export" and "an in-house monitoring agent".
- No regulatory or compliance determination. De-identification removes structured
  identifiers only and is not certified. The app does not connect to point-of-sale,
  order management, endpoint management, service desk (ITSM), HR or any system of
  record, and never calls a cloud service.

## Two questions retail leaders ask

Retail leaders often ask two questions, paraphrased here. Confirm which of these matter
to the audience early in the session, and never present them as the audience's own
words.

1. **The NPU question.** What does the NPU in the Copilot+ PCs we already have actually
   run, and why do the NPU and local LLMs see so little use? Answer it at 00:05 on
   **Device classes**.
2. **The use-case question.** Setting the specs aside, which of our use cases would
   Surface Laptop Ultra help, and how do others use local LLMs? Answer it with the
   **Device classes** matrix and the Builder PCs card at 00:05, then live from 00:15 to
   00:35.

| They ask about | Where the session answers it |
|---|---|
| The NPU in the Copilot+ PCs they already have | **Device classes** (00:05): *The Copilot+ PCs you already have*, *Try this on a Copilot+ PC you already have* and the NPU objection |
| Which of their use cases Surface Laptop Ultra would help | The *Everyday workloads by device class* matrix and the Builder PCs card (00:05), **Retail scenarios** (00:15), **Live demos** and **Hybrid router** (00:25), **Build on Surface** and **T-shirt sizing** (00:35) |
| How others use local LLMs | *Patterns from other industries*: fictional patterns, not customer references; ask the account team for named customer references |
| Their own always-on monitoring agent, if they mention one | *If the team already runs its own monitoring agent* (00:15) |
| Specs, Arm requirements, pricing and purchase options | The Surface specialist (00:45) |

## 60-minute run of show

Roles only: the account technology strategist opens and closes, the local and hybrid AI
specialist drives the app in every live segment, and the Surface specialist takes
00:45. Keep to the times so the specialist's ten minutes are not squeezed. The native
**Retail playbook** page and the companion web presentation's **Retail playbook**
button show the same run of show.

**Before you start (about 30 minutes ahead):**
1. Plug in, and close other apps that use the GPU, such as local model servers.
2. Run `.\Start-NativeShowcase.ps1` and wait until the status pill turns green and reads
   *... ready on GPU*.
3. Open **Live demos** and press **Pre-flight: run every demo live** (see below), then
   check the **Ready to present?** panel.
4. Run the operations call capture and the store visit follow-up once and read the
   output; generation quality can vary.
5. Confirm the audience-facing device name, availability and approved specifications.
6. Agree the hand-off with the Surface specialist, and re-check the Microsoft sources
   linked on **Device classes**: rollout plans can change.

| Time | Segment | Who | Click | Say |
|---|---|---|---|---|
| 00:00 | Introductions and goals - the account technology strategist (5 min). | Account technology strategist | Nothing yet; the app is open on **Company overview** | Introduce the team by role and confirm which of the *Two questions retail leaders ask* matter to the room: "Today is about what the AI PCs you already have can run, and where this laptop fits for your use cases, not another spec sheet. Everything you will see is synthetic and runs on this laptop." |
| 00:05 | Your question first: why the NPU on the Copilot+ PCs you have sits idle, and what runs where - open Device classes (10 min). | Local and hybrid AI specialist | **Device classes** (or the **Company overview** card *What runs where*, then **Open Device classes**). Read the disclaimer aloud, then walk *The Copilot+ PCs you already have*, *Try this on a Copilot+ PC you already have*, the *Everyday workloads by device class* matrix and the Builder PCs card | "The NPU only helps when software is built to use it. Built-in Windows experiences such as improved Windows search and Live Captions use it, and your own apps reach it through the Windows AI APIs, Windows ML or Foundry Local." Then: "Each fit in this matrix comes from the same memory arithmetic as T-shirt sizing. Everything live here runs on this laptop's RTX GPU." |
| 00:15 | Live: Company overview, then Retail scenarios - run the store visit follow-up on the GPU (10 min). | Local and hybrid AI specialist | **Company overview** reference architecture and device facts; then **Retail scenarios**: the *Store operations* card (*Store visit notes to a district follow-up list.*), **Run live workflow** (the overview's **Draft a store visit follow-up** button runs the same scenario) | "Capture, in-company drafting, and the cloud only for de-identified complex questions. It is illustrative, not any company's actual design." Then: "Fictional notes from a Saturday visit to Store 0412 become a cited draft: what was observed, the device and IT issues, and what needs the district manager. The prompt forbids deciding layout, staffing or schedules, and the draft must end by saying the district manager must review it and no store change has been made." If they mention their own monitoring agent, use *If the team already runs its own monitoring agent*. |
| 00:25 | Live demos: store operations call to notes and actions; de-identify before any cloud step; Hybrid router (10 min). | Local and hybrid AI specialist | **Run operations call capture**, then **Run live on GPU**; **Preview the cloud payload**, then **Run live on GPU**; **Route a complex question** (optionally **Run it on this PC**) | "Ana, Marcus and Priya plan a back-office laptop refresh pilot at 12 stores before the holiday change freeze. The call is transcribed and drafted into notes and actions on this GPU, and the store manager briefing nobody owns is marked 'Not assigned' instead of getting an invented owner." Then: "Personal details are swapped for placeholders on the laptop before anything is shared." Then: "Two desktop engineers read a vendor support statement differently, so the router escalates after masking the associate, asset, store and incident identifiers it detects. The payload is marked NOT SENT, and the desktop engineering lead still decides." |
| 00:35 | Model choice: Build on Surface (one OpenAI-compatible API for Foundry Local and llama.cpp; Microsoft-provided and open-source models) and T-shirt sizing (10 min). | Local and hybrid AI specialist | **Build on Surface**: start the **Local endpoint**, **Send a test call**; **Show it off**: **Run speed test**; **T-shirt sizing**: **Leader view** | Use *Model choice*: "One API on this laptop, whether the model comes from Microsoft's Foundry Local catalog or is an open-weight model on llama.cpp. Your code changes a base URL and a model name." |
| 00:45 | The Surface specialist: Surface Laptop Ultra specs, Arm requirements, pricing and purchase options (10 min). | Surface specialist | **T-shirt sizing**: leave the **Surface Laptop Ultra configurations** cards on screen | Hand over; see *Hand-off to the Surface specialist*. The presenter quotes no prices. |
| 00:55 | Discovery questions and next steps: agree a scoped pilot (5 min). | Account technology strategist, with both specialists | **Retail playbook** | Ask the nine questions below, record the answers, and agree a scoped pilot (see *Proposed pilot acceptance sheet*), with the information security, privacy and change-management owners setting the gates. |

Pick one more scenario for the room after the store visit follow-up:

- **Customer care: case summary for the team lead** for customer care leaders. The
  draft never decides or promises a refund, credit or reshipment, and nothing is sent
  to the customer.
- **Inventory and allocation: weekly in-stock review** for inventory and allocation
  teams. No order, transfer or allocation decision is made.
- **Merchandising: line review follow-ups** for merchandising and product teams (the
  collection is fictional and unreleased).
- **Store technology: weekly device health summary** for store technology leaders, and
  any team that runs its own monitoring agent.
- **Service desk: major incident update draft** for the service desk and incident
  managers.

Five-minute version: reference architecture -> **Run operations call capture** ->
**Draft a store visit follow-up** -> **Route a complex question** -> pilot close.

### If the GPU is busy or a run fails

- Say so and move on. Never present rehearsal as an inference or timing measurement.
- One GPU job runs at a time. If the app says another run is in progress, wait for it
  or press **Stop**.
- **Live demos**: press **Play rehearsal** instead of **Run live on GPU**. The output is
  bannered *REHEARSAL - authored sample, not model output. No checks, no metrics.* The
  face-off, the five-model demo and non-default translation languages have no
  rehearsal.
- **Retail scenarios**: if **Run live workflow** reports *Workflow cannot
  start*, another run or model switch may still be in progress: wait, then try again.
  If the engine is unavailable, the scenario is already selected in the **Live GPU
  workspace**; press **Play authored rehearsal** there.
- **Hybrid router**: **Explain the route** and the Company overview's **Route a complex
  question** apply the policy only, with no model, so the escalation step still works.
  Skip **Run it on this PC**.
- If the GPU or models are unavailable for the whole session, close the app (its own
  service stops with it) and use rehearsal-only mode, which loads no model:

  ```powershell
  .\Start-Showcase.ps1 -RehearsalOnly -NoBrowser   # terminal 1; keep it open
  .\Start-NativeShowcase.ps1                        # terminal 2; reuses that service
  ```

  The app's engine status then reads **Rehearsal only**. In the companion web
  presentation, choose **Authored rehearsal** explicitly. To return to live, close the
  app, press Ctrl+C in terminal 1, then run `.\Start-NativeShowcase.ps1` again.

## Device classes: what runs where

Use this page at 00:05, and whenever the room asks about the AI PCs they already have.
It answers the first question and the device half of the second. Open it from the
native navigation (**Device classes**, right after **Platform fit**), from the **Company
overview** card *What runs where* with **Open Device classes**, or directly with
`.\Start-NativeShowcase.ps1 -Section deviceclasses`. It is headed *What runs where: the
AI PCs you have, and where Surface Laptop Ultra fits.* In the companion web
presentation, the **Device classes** header button opens the same story as a dialog
under the same heading; its fits are memory only, and its sources are listed as plain
URLs at the end.

Read the disclaimer aloud first. It is on the page and in the dialog:

> NPU routes on this page are documented by Microsoft; this app does not run anything on an NPU. Everything live here runs on this laptop's RTX GPU through CUDA.

Use only the facts below and name the source when you use one. Quote no speed multiples
or competitor comparisons, add no facts beyond this section, and make no performance,
cost or productivity claim.

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

Ask which on-device AI features or local models they use today and what has blocked
wider use (question 3).

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

Close with the practical point: value from the AI PCs they already have starts with one
or two repeated retail tasks, run locally on synthetic data first and reviewed by their
own teams; the discovery questions pick the first.

### Everyday workloads by device class

The matrix has one row per T-shirt sizing workload. Each fit comes from the same engine
as **T-shirt sizing** (4-bit weights, 8K context): the 16 GB and 32 GB columns are
illustrative memory sizes, and the *This laptop (GPU budget)* column uses this laptop's
live GPU memory budget, so read it from the page rather than from this guide. Every
documented NPU route links to its Microsoft source. The outcomes for the illustrative
laptops:

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

- **Run live** appears only on rows that have a live demo on this laptop (its tooltip:
  *Opens this workload's live demo. Start it from the demo runner.*). It opens the demo
  without starting it; press **Run live on GPU** there. The other rows read *Memory
  estimate only; this row has no live demo on this page.*
- **Open T-shirt sizing**, under the matrix, opens **T-shirt sizing** on the **Leader
  view**.
- Present the suggested class as a memory fit, not a device recommendation, and ask
  which of these workloads they run today (question 1).

### Builder PCs: Surface Laptop Ultra (this laptop)

Position this laptop as a Builder PC and sell NVIDIA RTX Spark and local AI, using only
these sourced lines:

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
  open models), plus the larger llama.cpp models in *Going bigger*.
- **Local agents**: keep sensitive work on the device and reserve the cloud for larger
  workloads, the pattern the **Hybrid router** shows.
- **Proprietary code**: a local coding assistant for e-commerce and store systems code
  and internal tools, with the code kept on the device (the *Local coding assistant*
  demo and **Build on Surface**).

Ask where it would fit for them (question 9) rather than assuming every seat.

The page's live line, *GPU memory budget on this laptop now: X GB* (*Not known yet*
until the driver reports it), comes from the graphics driver. The GPU can address less
than the installed memory, so the estimates for this laptop use that budget, not the
installed total. On this laptop Foundry Local offers the CUDA, NvTensorRTRTX and WebGPU
execution providers and no NPU provider; everything live in the app runs through CUDA.

The Windows Experience Blog post says Surface Laptop Ultra "combines up to 128 GB of
unified memory with the ability to run AI models exceeding 120 billion parameters
locally". That is the blog's statement, not something this app runs or computes: the
largest size the app's engine sizes is XXL (70B class), and on this unit's memory
configuration the app refuses GPT-OSS 120B (see *Going bigger*). If you quote it,
attribute it to the blog.

If asked which device class this laptop belongs to, say it is a Builder PC, as the blog
describes it. Exact-SKU questions go to the Surface specialist at 00:45.

### Always-on and shared

- Mini desktop PCs are a device class for always-on agents
  ([blog](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/)).
- DGX Station for Windows, with NVIDIA GB300, is a device class for trillion-parameter
  models and 32 or more simultaneous agents (same blog post).

The page labels one example *Illustrative fit, not a recommendation*: an always-on
agent that drafts a daily fleet health summary for people to review. This app does not
size or run these classes; take questions about them back to the account team.

### If the team already runs its own monitoring agent

Ask; do not assume. If the team mentions an always-on monitoring agent of its own,
refer to it only generically: do not name it, guess its tools or vendors, or ask to see
its data in the session.

If the team already runs its own always-on monitoring agent (for example store device
and service desk data in a database, with an open-source local model), map it to the
always-on class, Foundry Local or llama.cpp on loopback, and a Builder PC for larger
models. Make two generic connections:

1. **The same shape: the store device health scenario.** `fleet-health` (*Store
   technology: weekly device health summary*) drafts from a fictional weekly endpoint
   management and service desk export (FH-2026-W43) under three headings: *What the
   data shows*, *Watch items* and *Needs an owner*. The prompt requires a source tag on
   every bullet, keeps the recorded numbers, forbids determining a root cause and ends
   the draft with: "Draft only; the store technology team must review, and no device or
   policy has been changed." Say: "This is the same shape as an always-on monitoring
   agent: data you already collect, a local model, a cited draft and a person who
   decides." Do not claim it matches their agent; ask how their agent presents its
   findings and who reviews them.
2. **The same API.** An agent that calls a local model through an OpenAI-compatible API
   can point at a different local endpoint by changing a base URL and a model name.
   Show it on **Build on Surface**: the **Local endpoint** is
   `http://127.0.0.1:<studio port + 1000>/v1`, larger llama.cpp models serve the same
   API on their own loopback port, and every starter kit reads `LOCAL_AI_BASE_URL` and
   `LOCAL_AI_MODEL`. The Hybrid router's *Same code, local or cloud* pattern makes the
   same point. The endpoints are loopback only and unauthenticated, so a test agent
   must run on the same PC.

Ask whether their agent uses an OpenAI-compatible API, and which model and runtime it
uses today on which devices. Compatibility with their agent has not been tested: make
it a pilot item, with their engineers running their own prompts against a
Microsoft-provided and an open-source model on synthetic or approved data and reviewing
every output.

## Patterns from other industries

When they ask how other customers use local LLMs, answer with patterns, not names. The
**Device classes** page ends with *Patterns from other industry showcases*: fictional
patterns from Microsoft's industry showcases, not customer references. For named
customer references, ask the account team; never name another organization, and never
say that anyone has deployed, measured or benefited from a pattern. Each card names the
pattern, says what it looks like in retail, shows the engine-computed suggested
class for its T-shirt sizing workload, and has a **Run the equivalent here** button
that opens the matching live demo on this laptop without starting it:

| Industry | Pattern | In retail | Suggested class | Run the equivalent here |
|---|---|---|---|---|
| Financial services | Meeting capture | Store operations calls | Copilot+ PC (16 GB) | *Store operations and IT call to notes and actions* |
| Telecom and media | Offline field notes | Distribution center shift handoffs | Copilot+ PC (16 GB) | *Voice memo to a shift handoff note* |
| Tax and accounting | Scanned forms | Store device service forms | Copilot+ PC (16 GB) | *Scanned form to structured data* |
| Higher education | Policy questions with citations | Device standards and change policy | Copilot+ PC (16 GB) | *Ask your documents* |
| Private markets | De-identify before the cloud | Associate emails before any cloud step | Copilot+ PC (16 GB) | *De-identify before escalating (Tier 3)* |
| Engineering and software | Proprietary code assistant | E-commerce and store systems code | 32 GB AI PC or Builder PC | *Local coding assistant* |

Ask which of these they have tried on their AI PCs and what blocked wider use
(question 3).

## The reference architecture (00:15)

The **Company overview** opens with *Three tiers. Customer and store data stay in the
company. The cloud only when needed.* It is labelled "Illustrative reference
architecture, not any company's actual design." Say that out loud.

| Tier | Button on the Company overview | Say |
|---|---|---|
| Tier 1: Smart capture (a store manager's or field technician's Surface on the store visit or operations call) | **Run operations call capture** | "The operations call is captured with consent and transcribed locally. Nothing has left the laptop." |
| Tier 2: In-company drafting (local AI beside the company's store operations and service desk systems, illustrative) | **Draft a store visit follow-up** | "Store and IT procedures are applied inside the company, and a cited store visit follow-up list comes back for the district manager. No store change has been made." |
| Escalate only when needed (algorithmic delegation, inside the company) | **Route a complex question** | "Only when a question needs frontier reasoning does the router remove the customer, associate, asset and ticket identifiers it detects and minimize the context, and it shows every reason." |
| Tier 3: Cloud support (Azure OpenAI) | **Preview the cloud payload** (opens *De-identify before escalating (Tier 3)*) | "This is the de-identified query that would go out, marked NOT SENT. Model support comes back; the decisions stay with your people." |

Reviewers in the architecture: store operations, merchandising, customer care, store
technology and the service desk.

## Five-minute executive flow

| Time | Show | Say |
|---|---|---|
| 0:00 | Company overview: reference architecture and Device evidence | "Customer, associate and store data stay in the company: recordings, customer and associate personal data, store performance figures, device and ticket details and unreleased product information remain inside. Let me prove each tier." |
| 0:45 | **Run operations call capture** (Store operations and IT call to notes and actions, live) | "A synthetic store operations call is transcribed and drafted into notes and actions on this GPU. It marks the store manager briefing 'Not assigned' instead of inventing an owner." |
| 2:00 | **Draft a store visit follow-up**, then **Route a complex question** | "The follow-up list waits for the district manager. For a complex question, only the de-identified query would reach the cloud." |
| 3:15 | T-shirt sizing **Leader view**, then Business case | "Which retail workflow matters most to you? Put your own baseline in place of these illustrative inputs." |
| 4:15 | Pilot close | "Let's scope a four-week pilot on synthetic store visit and service desk records, with store operations and service desk team leads approving every draft and clear quality gates." |

Swap the scenario to match the room: **Customer care** for customer care leaders,
**Inventory and allocation** for inventory and allocation teams, **Merchandising** for
merchandising and product teams, **Store technology** for store technology leaders and
field IT, and **Service desk** for the service desk and incident managers.

Before the meeting, launch the app, wait for **Local AI ready**, and run both
stories once. Then open **Live demos** and press **Pre-flight: run every demo
live** (see below). Inspect the actual output; generation quality can vary. Confirm
the audience-facing device name, availability and approved specifications.
For a non-live walkthrough, explicitly choose **Authored rehearsal**.
Never present rehearsal as an inference or timing measurement.

### Device facts and larger models

**Memory correction:** This unit has **128 GB installed**, measured from physical
DIMM capacity. Approximately **64 GB is visible to Windows**; NVIDIA separately
reports a **64,000 MiB GPU budget**. These are distinct memory views, not separate
additive pools or a dedicated-VRAM claim. No memory partition settings are changed.
The Company overview shows the hero specs (128 GB unified memory, 6,144-core
Blackwell RTX GPU, 20-core CPU, 15-inch PixelSense Ultra display); open
**Device evidence** for the three memory views.

**Larger-model walkthrough:** Start with **Qwen2.5-Coder 14B**, then use the
on-device model selector to load **GPT-OSS 20B**. Wait for ready status before
running. The workspace keeps one chat model resident at a time; the Live demos
face-off loads both. GPT-OSS can spend longer reasoning
before the answer appears; activity counts are real, while private reasoning text
is neither displayed nor saved. A larger parameter count is not an accuracy claim.

**Going bigger (30B and up):** When Local-AI-Bench weights are installed, the
selector also lists **Qwen3-Coder 30B-A3B**, **Llama 3.3 70B** and **GPT-OSS 120B**
on llama.cpp CUDA. Plugged in, the 30B ran the code and scenario stories here at
83–91 tok/s decode (48–75 on battery), with every layer on the GPU. The app checks free dedicated GPU memory *before*
unloading anything: if another app's model server holds the memory, the switch is
refused, the current model keeps running and the message names the server to close.
The 70B needs about 43.6 GiB free, so close other local model stacks first. Say plainly
that the 120B (about 61.5 GiB) does not fit in this device's dedicated GPU memory.
**MAI Code 1.1 Flash** appears disabled with Microsoft's published figures, labelled
*Not measured by this app*. It ships through GitHub Copilot's local model support, not
this app. Plug in before showing large models.

## Show it live: the Live demos tab (00:25)

**Before the session starts**, open **Live demos** and press **Pre-flight:
run every demo live**. On this unit a warm pre-flight takes about three
minutes; the first one of the day also loads every model. Green means the demo
ran and passed every engine check. Amber on the face-off usually means one
model answered wrong. That is a real, graded result and worth showing. Red
means a step did not run; read its message. The **Ready to present?** panel
lists anything still missing. If models or NVIDIA libraries are missing, run
`.\Start-Showcase.ps1 -Prepare` once on an approved network.

**In the session**, choose two or three demos that match what the room cares about:

| If they mention | Open | Say |
|---|---|---|
| Operations calls, store visits, shift handoffs | Store operations and IT call to notes and actions; Voice memo to a shift handoff note | "That recording was transcribed on this laptop. The app checks the transcript against the script we wrote." |
| Device service forms, receipts and store paperwork | Scanned form to structured data | "A vision model reads the image here and returns data a system can use. The app checks the result against the document we generated." |
| Device standards, change policy or IT questions | Ask your documents | "It answers only from the documents it found on this laptop and cites them, and the app checks those citations." |
| Multilingual store notices, global teams | Translate on the device | "Names, references and times come through exactly as written. The app checks that." |
| CAB pre-reads and leadership updates | Executive brief from notes | "The brief cites its notes, and the app checks for the sentence saying no benefit is claimed." |
| Associate personal data, device and ticket identifiers | De-identify before escalating (Tier 3) | "Personal details are swapped for placeholders on the laptop before anything is shared." |
| Service desk inbox volume | Inbox triage to structured data | "Six synthetic emails become structured data on this laptop, and the app checks each category against its label." |
| Scripting and internal IT tool developers | Local coding assistant | "The code is drafted here and shown for review. This app never runs it." |
| Change windows, scheduling, planning | Plan it out with a reasoning model | "A large reasoning model works through six constraints, and the app checks every one." |
| "How much can it run?" | Model face-off; Five models, one laptop | "These models are loaded together on one laptop, and each is doing real work right now." |

What the synthetic inputs contain, if the room asks:

- **Store operations and IT call**: Ana (store operations manager), Marcus (desktop
  engineer) and Priya (service desk manager) plan a back-office laptop refresh pilot at
  12 stores that must finish before the holiday change freeze. No change advisory board
  slot is booked yet, nobody owns briefing the store managers (the notes must mark it
  'Not assigned'), and adding the distribution centers next year is only an idea.
- **Voice memo**: a distribution center shift supervisor reports that handheld scanners
  in bay H-17 at dock 3 failed to sync from 05:30 to 06:15, with error code 40, and asks
  for a priority two ticket and the access point log.
- **Scanned form**: *Store device service form (handwritten fields)* is form SF-0738 for
  the VanArsdel TP-40 receipt printer (ASSET-52914) at STORE-0412, with the fault
  "Register 3 prints blank receipts", reported by Sam Okafor and handled by technician
  J. Alvarez. *Store supply receipt* is a VanArsdel Store Supply receipt whose line-item
  arithmetic is checked.
- **Ask your documents**: twelve fictional Contoso Apparel IT policies; the default
  question, about a work laptop left on a train, must retrieve and cite POL-03, *Lost or
  stolen devices*.
- **Translate**: a fictional store IT maintenance notice; Contoso Apparel, STORE-0412,
  14:00 and 16:00 must come through unchanged. Spanish is the default.
- **De-identify**: Dana Whitfield's request for a laptop and phone before her first day,
  copying her hiring manager Marcus Lee and quoting employee ID EMP-318274. The model
  swaps each identifier for a typed placeholder such as [NAME] or [ID], and the check
  counts how many of the nine synthetic identifiers survive.
- **Inbox triage**: six synthetic service desk emails, including a licence-count query
  on invoice INV-7302.
- **Plan it out**: a five-week back-office laptop refresh pilot for the fictional stores
  Atlas, Birch, Cedar, Delta and Harbor, under six constraints.

Rules for live demos:
- All inputs are synthetic and fictional. Do not type real customer, associate, store,
  device, order or ticket records, personal data or unreleased product information into
  the instruction box.
- **Play rehearsal** is labelled *Rehearsal: no model ran*. It is a fallback
  walkthrough, not a measurement.
- If a live run fails, say so and move on. The app never substitutes rehearsal
  output for a failed run.
- Timings are this run on this laptop. They are not a comparison with any other
  device or with cloud AI.
- **Export** saves the run's evidence as JSON (models, timings, checks), with
  no reasoning text.
- On the **T-shirt sizing** Leader view tab, click the red **Run live demo** button
  with the play icon to open and run the matching demo on the GPU. Use the
  separate checkboxes to select workloads for sizing. If the GPU is busy or
  not ready, the demo explains why it cannot start.
- On **Device classes**, **Run live** and **Run the equivalent here** open the matching
  demo without starting it; press **Run live on GPU** to run it.

## Retail scenarios and a leave-behind deck

The **Retail scenarios** page has six fictional workflows for the fictional
Contoso Apparel, each drafted live on the GPU, across store operations, merchandising,
customer care, inventory and allocation, store technology and the service desk. Every
prompt ends with a fixed review line, so the draft always hands the decision back to a
person:

| Scenario | Drafts | Fictional subject | Bring it out for | Fixed review line |
|---|---|---|---|---|
| Store operations: store visit follow-up | Store visit notes to a district follow-up list. | Store 0412 Saturday visit (SV-0412) | Store operations, district managers and field IT | "Draft only; the district manager must review, and no store change has been made." |
| Merchandising: line review follow-ups | Line review notes to a sample follow-up list. | Spring 2027 collection (unreleased), line review LR-2027S | Merchandising and product teams | "Draft only; the product team must review, and no style or supplier decision has been made." |
| Customer care: case summary for the team lead | Customer contact notes to a case summary. | Online order WEB-771204 delivered incomplete (case CC-58210) | Customer care leaders and team leads | "Draft only; a customer care team lead must review, and nothing has been sent to the customer." |
| Inventory and allocation: weekly in-stock review | Weekly in-stock notes to a replenishment review. | Weekly in-stock export for 310 stores (IS-2026-W43) | Inventory, allocation and replenishment teams | "Draft only; the allocation lead must review, and no order, transfer or allocation decision has been made." |
| Store technology: weekly device health summary | Weekly fleet and service desk data to a health summary. | Contoso Apparel endpoint management and service desk export (FH-2026-W43) | Store technology leaders, and any team that runs its own monitoring agent | "Draft only; the store technology team must review, and no device or policy has been changed." |
| Service desk: major incident update draft | Major incident notes to a stakeholder update draft. | Relecloud Scheduler sign-in incident (MI-3317) | Service desk and incident managers | "Draft only; the incident manager must review, and nothing has been sent to stores or stakeholders." |

What the two newest fixtures contain, if the room asks:

- **Customer care**: online order WEB-771204 shipped in two parcels; one was delivered
  on 21 October 2026, and carrier tracking for the second has not updated since 22
  October. The customer contacted care three times in six days and asked for a refund
  of the missing item, and Jamie Lin (customer care agent) asked the team lead whether
  to reship the item or refund it. No refund or reshipment has been issued; the draft
  never decides or promises a refund, credit, reshipment or compensation.
- **Weekly in-stock review**: the in-stock rate is 94.2% against 95.0% across 310
  stores, 18 products are below safety stock at 40 or more stores, and two core
  products (the Everyday Crew Tee in white and navy) are out of stock at 23 stores.
  DC-2 holds 4,800 units and the next supplier receipt is planned for 6 November 2026.
  The allocation analyst asked whether to transfer units from lower-selling stores
  before the weekend. No order, transfer or allocation decision has been made.

Pick the one closest to the room, then:

1. **Run live workflow** to run its prompt on the GPU in front of them.
2. **Prepare deck in Forge** to stage a matching brief in Offline PPTX Forge. In
   Forge, select *<Client> - sales (custom)*, review the facts, then **Build deck**.
   Forge builds the deck locally; nothing is generated until you choose Build deck.

Say these are illustrative workflows at a fictional company. Swap the fictional facts in
Forge for real ones only after the company agrees and its information security, privacy
and change-management reviews allow it; unreleased product information also needs the
product team's approval.

## Hybrid Intelligence: show it, then hand it to the builders

**Positioning:** Hybrid Intelligence means each request runs where it fits. Private,
fast and offline work stays on the PC; current information, organisation-wide data and
frontier scale go to the cloud. The PC does not replace the cloud.

The **Show it off** page has a five-step run of show, one button per step:

| Step | Button | Say |
|---|---|---|
| 1. Show the decision | Open the router (loads *Store manager question that needs the latest release notes*) | "This store manager's question has personal contact details and a store number *and* needs the latest Windows update release notes. The PC redacts the details first, so only the clean request would go to the cloud." |
| 2. Put a number on it | Run speed test | "That's how fast this model is generating on this laptop's GPU right now. One run here, not a benchmark." |
| 3. Prove it is an endpoint | Open Build on Surface | "Desktop engineers and internal tool developers call this like a cloud API, but it's on 127.0.0.1." Start the endpoint, then **Send a test call**. |
| 4. Make it theirs | Retail scenarios | Run the retail workflow closest to their role. |
| 5. Leave with a deck | Open PPTX Forge | Stage the matching brief and build the leave-behind locally. |

On the **Hybrid router**, press **Explain the route** for the decision and its reasons (no model
runs), then **Run it on this PC** to stream the local answer or redaction from the GPU.
Every cloud payload is shown and marked **NOT SENT**: the studio never calls a cloud
service. If the redaction check blocks a payload, show that too: the PC caught it before
anything could leave. Try the *Store visit note while offline* preset to show the cloud step
being queued rather than failing. The rules catch structured identifiers (emails,
phone numbers, structured ID numbers, credentials), not every name, free-text identifier or
context clue.

The seven presets:

- *Associate email to the service desk*: stays on this PC.
- *Store manager question that needs the latest release notes*: hybrid.
- *Public Windows on Arm news*: cloud.
- *Service desk export connector config with a credential*: stays on this PC (the
  credential blocks the cloud).
- *Store visit note while offline*: stays on this PC, offline.
- *Company-wide question*: cloud.
- *Complex question: escalate to Tier 3*: hybrid, beyond-device scale; the Company
  overview's **Route a complex question** button opens it.

**Speedometer and leaderboard:** run the speed test on each model you load to fill the
session leaderboard. Numbers are this run on this laptop; never compare them with other
devices or cloud services. **Export results (JSON)** saves timings, not text.

**For developers**, open **Build on Surface**:
- Start the **Local endpoint** (off by default, this PC only, no key). Copy a snippet
  (Python, JavaScript, C#, PowerShell or curl) and run it in their own terminal.
- **Create** a starter kit: streaming chat, ask private documents, redact-then-cloud,
  a tool-using agent (Python) or a C# chat app. The studio writes the files and opens
  the folder; it never runs them. The redact-then-cloud kit uses the router's own policy
  and stops before any real cloud call.
- Stop the endpoint when finished; closing the studio also stops it.

**Companion tools** on the same page open Offline PPTX Forge, Local AI Tokenomics,
Local AI Headroom, Local AI Bench and HydraFusion autorouting when they are installed
beside the studio. Each tool's own claims and guardrails apply.

## Model choice: one API, Microsoft-provided and open-source models (00:35)

Retail leaders ask which of their use cases Surface Laptop Ultra would help; part of the
answer is the freedom to run Microsoft-provided or open-source local models. At 00:35,
show it, then position the device.

- **Two runtimes, one API.** Foundry Local is Microsoft's local runtime, serving models
  from the Foundry Local catalog; llama.cpp is an open-source runtime, serving
  open-weight model files. In this studio both serve the same OpenAI-compatible API on
  loopback: the **Local endpoint** on **Build on Surface** serves the loaded Foundry
  Local model at `http://127.0.0.1:<studio port + 1000>/v1`, and larger models loaded
  through llama.cpp serve the same API on their own loopback port. The same code calls
  either one; only the base URL and model name change.
- **What runs here, all on the RTX GPU.** Foundry Local CUDA: Qwen2.5-Coder 14B (the
  default), GPT-OSS 20B, Whisper medium, Qwen3-VL 4B and Qwen3-Embedding 0.6B. llama.cpp
  CUDA: Qwen3-Coder 30B-A3B and Llama 3.3 70B, when their weights are installed. For any
  number, quote README.md *What is real* and *Larger models* exactly and add nothing.
  GPT-OSS 120B does not fit in this unit's dedicated GPU memory, and MAI Code 1.1 Flash
  is listed with Microsoft's published figures, labelled *Not measured by this app*.
- **Show it in this order.**
  1. **Build on Surface**: start the **Local endpoint** and press **Send a test call** (a
     real loopback request that shows its HTTP status and timing), then copy a snippet
     and show the starter kits.
  2. **Show it off**: **Run speed test** on the loaded model. One run on this PC, not a
     benchmark.
  3. **T-shirt sizing**: on the **Leader view**, tick the workloads they named and read
     *Say it like this*. The **Surface Laptop Ultra configurations** cards turn that into
     a memory recommendation; leave them on screen for the Surface specialist.
- **Position this laptop as a Builder PC.** Sell NVIDIA RTX Spark and local AI, using
  only the sourced lines in *Builder PCs: Surface Laptop Ultra (this laptop)*. Ask where
  it would fit for them (question 9) rather than assuming every seat.
- **Do not say** that one runtime, model or device is better or quicker than another, or
  that a larger model is more accurate. Which models, runtimes and licences are approved
  is the company's decision (question 7).

## Right-size the model, then qualify the platform

Use the native **T-shirt sizing** planner to start the conversation, not to
declare a winning device. With retail and business leaders, stay on the **Leader view** tab: tick the
workloads they mention (coding, transcription, translation and so on) and read
the "Say it like this" line. Switch to **Technical view** only when an architect
wants the arithmetic. S (1-4B), M (7-8B), L (14-20B), XL (24-32B) and
XXL (65-72B)
describe nominal model-size bands, not accuracy tiers. Show how precision,
context, runtime/KV allowances and operating headroom change the estimated
working set. A model whose weights fit may still fail to load or be unsuitable.
Never sum the unit's installed, OS-visible and driver-reported memory views.

### Which memory configuration should they order?

Scroll below the Leader view results to **Surface Laptop Ultra configurations**. It
uses the same ticked workloads and marks one of the 24, 32, 48, 64 or 128 GB
options **Recommended**.

1. Tick what data and AI builders, design and product teams, developers and the service
   desk will actually run. Ask whether those AI tools stay
   open together; if so, turn on **All open together**.
2. Turn on **Long documents** if they will work with long store policies, returns
   procedures, vendor support statements or transcripts.
3. Leave the GPU share on **Microsoft launch unit** for a leadership
   conversation. Switch to **This PC's measured split** to show what this
   demo unit reports (it is more conservative).
4. Read or copy **Say it like this**. It names the recommended configuration,
   any smaller one that only just holds the workload, and what stepping up
   would add.

Examples on the default settings: a coding assistant points to 48 GB; coding
plus reasoning open together points to 64 GB; a 70B-class model points to
128 GB. A "Little room" card is a warning, not a recommendation: real model
files are larger than the estimate. The planner is memory-only. Do not quote
it for price, response time or battery life, and confirm the configuration
and processor pairing in the configurator before an order.

| Platform | Pilot use case | What must be qualified |
|---|---|---|
| Snapdragon | Store visit or distribution center walk-through notes into a reviewed summary | Windows ARM64 app and exact model/runtime bundle for the shipping SKU |
| Snapdragon | Transcription followed by a short summary | Speech pipeline, microphone/consent workflow, model license and target-specific runtime |
| Snapdragon | Image-assisted inspection | Supported vision model, image handling, human review and task-specific accuracy |
| Intel | Meeting transcription and summary | Exact Intel CPU/GPU, supported OpenVINO pipeline and audio/data policy |
| Intel | Service-desk or policy knowledge draft | Approved retrieval sources, citations, compatibility and response-quality gate |
| Intel | Visual-document triage | Supported vision/OCR pipeline, document formats and human-review rule |
| This RTX unit | Live 14B code draft or 20B structured reasoning | Exact cached CUDA variant, actual run evidence and output review |

These are workload-fit hypotheses, not exclusive capabilities or measured
vendor comparisons. The app runs the current RTX workflows; Snapdragon and
Intel cards are planning guidance, not demonstrations on those processors.
Speech, image processing, retrieval and external point-of-sale, order management,
endpoint management, service desk (ITSM) or HR system integration are not implemented
merely because a use-case card describes them.

**Platform fit:** if the room asks about the Snapdragon and Intel AI PCs they already
have, present these rows as illustrative pilots. Confirm their actual processor mix
first (question 2); none of these pilots was run or measured here.

**Presenter line:** "Right-size the workflow first. Then prove the exact model,
runtime and device together." Use the platform page's official source links
to qualify a proposed configuration; memory arithmetic alone is insufficient.

## Hand-off to the Surface specialist (00:45)

- Surface Laptop Ultra specs, Arm requirements, pricing and purchase options belong to
  the Surface specialist. This guide states no prices; the presenter quotes none, and no
  availability or delivery dates either.
- Hand over on the **T-shirt sizing** **Leader view** with the **Surface Laptop Ultra
  configurations** cards on screen for the workloads the room ticked. The planner is a
  memory-only estimate: no pricing or response-time claim.
- Pass on what the room has said so far on questions 2 (AI PCs and processor families
  by persona), 4 (Arm64 dependencies), 5 (Intune and Windows Autopilot) and 9 (where
  Surface Laptop Ultra fits and which memory configuration). Note any still open for
  00:55.
- Arm64 readiness (question 4) is for the company's own engineers to test with the
  specialist and their vendors; this app shows no Arm64 readiness result.
- Exact-SKU questions go to the specialist.

## Questions that scope a pilot (00:55)

1. Which repeated retail tasks (store visit follow-ups, customer care case summaries, in-stock reviews, line review follow-ups, store device health summaries, incident updates) take meaningful time today?
2. Which AI PCs and processor families are deployed, by persona (headquarters, stores, distribution centers, customer care)?
3. Which on-device AI features or local models are in use today, and what has blocked wider use? (Device classes shows what the NPU runs today.)
4. Arm64 readiness: which VPN, security agent, printer and peripheral, and line-of-business app dependencies remain?
5. Management: how are Intune and Windows Autopilot set up for AI PCs, and who approves new local models and runtimes?
6. Data: which customer, associate, store and product data may a local model read, and where must outputs stay?
7. Model choice: which Microsoft-provided and open-source models, runtimes and licences are approved, and what does the AI acceptable-use policy allow?
8. Measures: which measures (visit report time, case handling time, handoff quality, service desk volumes) would a pilot compare against?
9. Where would a Surface Laptop Ultra fit (data and AI builders, design and product teams, developers), and what memory configuration do those workloads need?

These are questions only: record the audience's answers and do not suggest them. Then
agree a scoped pilot using the *Proposed pilot acceptance sheet* below.

**Guardrails for the close:**
- Drafts only; nothing is deployed, changed or sent, in the demo or in a pilot proposal.
- Synthetic data only in the session. A pilot uses synthetic or approved data, after the
  company's information security, privacy and change-management reviews.
- No performance, cost or productivity claims. Timings are one run on this laptop, the
  calculator's capacity value is an assumption, and any benefit is unproven until a
  pilot measures it.
- Neither the app nor this playbook makes a change approval, technical, refund,
  allocation, HR, vendor, purchasing, legal, privacy or compliance determination.

## Optional: ramp up with "Coding as a second language"

Service desk analysts, store operations and IT support staff who are new to code and
want to follow conversations with desktop engineers, developers and architects can take
the optional eight-lesson AI-literacy module. It teaches reading,
not writing, code, and ends with reviewing AI-written code. Its examples use the
fictional Contoso Apparel (for example `technicians = 240`). Use **Ask the
local coding tutor** to have the on-device coding model explain any lesson's code
in plain English. Treat its answer as a draft, like any generated output.
Hide the tab from the Retail playbook page if you do not need it.

## Handle the important objections

**"Why not cloud AI?"** Keep cloud AI for the workloads and managed services
that suit it. This demonstrates an additional local route, not a replacement.
No cloud price, performance comparison or subscription reduction is claimed.

**"Does local AI replace the cloud?"** No. Hybrid Intelligence keeps private, fast
and offline work on the PC and uses the cloud for current information,
organisation-wide data and frontier scale. The Hybrid router shows the split and
its reasons; the studio itself never calls a cloud service.

**"Can our developers build on this?"** Yes. Build on Surface starts an
OpenAI-compatible endpoint on loopback (off by default, this PC only) and creates
small starter projects in Python and C#. Their code reviews and runs them; the
studio never executes generated code. Production use still needs the company's
own model licensing, security review and deployment plan.

**"How is AI accelerated?"** These models run on the NVIDIA RTX GPU through
CUDA. Inspect each run's model identity and execution-provider evidence.

**"We bought Copilot+ PCs for their NPU. Why aren't we using it?"** The NPU only helps
when software is built to use it. Built-in Windows experiences such as improved Windows
search and Live Captions use it, and your own apps reach it through the Windows AI
APIs, Windows ML or Foundry Local; Task Manager shows NPU activity. Open Device classes
to see what runs where. Everything live in this app runs on this laptop's RTX GPU.

**"Can we run Microsoft-provided and open-source models?"** Yes. Foundry Local and
llama.cpp both serve the same OpenAI-compatible API on loopback, so the same code can
call a Microsoft-provided or an open-source model by changing a base URL and model
name. Check each model's licence and your AI acceptable-use policy, and verify the
exact model variant on each device.

**"Is this Microsoft 365 Copilot?"** No. This is a custom Foundry
Local prototype. Certification, licensing, integrations and availability are
separate questions.

**"Is the data completely isolated?"** The showcased model executes locally.
That is not a security or air-gap certification. Setup/catalog operations can
use the network, and minimal SDK process telemetry may remain.
Evaluate deployment controls with the company's information security, privacy and
change-management review teams.

**"How much money will it save?"** The calculator estimates possible capacity,
not cash savings. Its device cost is an assumption, not a quote. Add software,
deployment, support and change-management costs in a complete business case.
Retain existing cloud subscriptions in the analysis.

**"Does it work disconnected?"** Do not claim a result not measured. Prepare
models first, then validate the exact workflow with connectivity intentionally
disabled in an approved pilot. This showcase does not change network settings.

**"Can we use real customer, store, ticket or associate data?"** Not in this showcase.
Every record is synthetic. A pilot with customer or associate personal data, store
performance figures, device and ticket details, order details or unreleased product
information needs the company's information security, privacy and change-management
reviews first; this app makes no legal, regulatory or compliance determination.

**"Will it change devices, orders or tickets?"** No. Drafts only; nothing is
deployed, changed or sent. No draft approves or deploys a change or update, closes or
reassigns a ticket, changes a device policy, determines a root cause, issues a refund
or credit, or places an order, transfer or allocation. Store operations, allocation,
customer care, store technology, the service desk and the incident manager decide.

**"Does it connect to our store, order or service desk systems?"** No. The studio
connects to no point-of-sale, order management, endpoint management, service desk
(ITSM), HR or other system of record, and never calls a cloud service. The scenarios
draft from fictional notes and exports supplied as text. Any integration is design work
for the company's engineers in a reviewed pilot.

**"Will it make refund, allocation, HR, vendor or purchasing decisions?"** No. Drafts
support store operations, merchandising, allocation, customer care, store technology
and the service desk. Refund, credit, allocation, HR, vendor, purchasing, pricing,
supplier, style and cost decisions stay with authorized people, and every draft is
reviewed. Nothing is sent to customers, associates, stores, vendors or stakeholders.

**"Why these models?"** The 14B coder provides a larger dedicated coding option;
the 20B model adds a larger reasoning option. Both are cached CUDA variants
verified for local inference. Parameter count alone proves neither quality nor
speed. Their identities and actual selected providers are inspectable on screen.

## Proposed pilot acceptance sheet

Run the pilot on synthetic store visit, customer care and service desk records (or
approved data after review), with a team lead reviewing every draft. Start with one
workflow, for example the store visit follow-up, the customer care case summary or the
major incident update draft. Record current task time,
output accuracy and quality rubric, connectivity conditions, actual shipping
SKU, app/peripheral compatibility, model/runtime licenses, required data
controls, total deployment cost and support ownership.

Run ten users for two weeks as a **proposal**, not a validated study design.
Agree acceptance gates with the store operations, customer care and service desk team
leads and the information security, privacy and change-management owners before
starting. Keep team-lead review of every draft in scope. Export actual run evidence and
the current assumption-based case.
Use the results to determine whether to stop, adapt or scale.

**Partner opportunity:** Discovery, device selection, application compatibility
validation, deployment planning and lifecycle support, subject to the actual partner's
engagement scope. No unverified service entitlement or commercial offer is implied.
