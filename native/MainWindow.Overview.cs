using Microsoft.UI.Text;
using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;
using static HybridIntelligenceRetail.Ui;

namespace HybridIntelligenceRetail;

internal sealed partial class MainWindow
{
    private TextBlock _ovInstalled = null!, _ovGpuCores = null!, _ovCpuCores = null!, _ovDevice = null!;

    private static Border StatCard(out TextBlock value, string initial, string label, string detail, string id, out TextBlock detailText)
    {
        value = Id(Set(Text(initial, 30, Ink, FontWeights.SemiBold), t => t.FontFamily = Display), id);
        detailText = Small(detail);
        return CardBorder(Stack(4, value, Text(label, 14, Ink, FontWeights.SemiBold), detailText), 20);
    }

    private FrameworkElement BuildOverview()
    {
        _ovDevice = Id(Body("Reading device inventory..."), "OverviewDeviceName");
        var startLive = Id(Primary("Start the live GPU demo"), "OverviewStartLive");
        startLive.Click += (_, _) => Navigate("live");
        var size = Id(Secondary("Size a workload"), "OverviewOpenSizing");
        size.Click += (_, _) => Navigate("sizing");
        var evidence = Id(Secondary("Device evidence"), "OverviewDeviceEvidence");
        evidence.Click += async (_, _) => await ShowDeviceEvidenceAsync();

        var hero = Stack(14,
            Eyebrow("Company overview  |  " + Event.Session),
            H1("Hybrid AI for retail, with customer, associate and store data kept inside the company."),
            Set(Body("For store operations, merchandising, inventory, customer care, store technology and IT leaders: capture a store operations call, transcribe it and draft notes, store visit follow-ups, case summaries and incident updates on this laptop's RTX GPU with Microsoft-provided and open-source models, escalate only de-identified complex questions to the cloud, and keep every decision and approval with your people. Synthetic data, evidence first, no hype."),
                t => { t.FontSize = 16; t.LineHeight = 24; t.MaxWidth = 820; t.HorizontalAlignment = HorizontalAlignment.Left; }),
            _ovDevice,
            Set(Row(10, startLive, size, evidence), r => r.Margin = new Thickness(0, 6, 0, 0)));

        var stats = new AdaptiveGrid(230, 4).With(
            StatCard(out _ovInstalled, "...", "LPDDR5x unified memory", "Installed in this laptop, shared by the CPU and RTX GPU", "OverviewInstalledMemory", out _),
            StatCard(out _ovGpuCores, "...", "NVIDIA Blackwell RTX GPU", "NVIDIA RTX Spark N1X", "OverviewGpuCores", out _),
            StatCard(out _ovCpuCores, "...", "CPU", "NVIDIA RTX Spark N1X", "OverviewCpuCores", out _),
            StatCard(out _, "15-inch", "PixelSense Ultra display", "3270 × 2180, up to 120Hz, 2,000-nit HDR peak", "OverviewDisplay", out _));
        var specNote = Id(Small("Memory and core counts as reported by this laptop. Display and processor family from Microsoft's Surface Laptop Ultra tech specs."), "OverviewSpecSource");

        var story = new AdaptiveGrid(260, 3).With(
            StoryCard("1", "Prove it live", "Run the retail leadership briefing or a store technology code draft on the RTX GPU. Real timing, real model, private reasoning withheld.", "live"),
            StoryCard("2", "Keep customer and store data local", "Route store emails and complex questions: what stays in the company, what is de-identified first and what would go to Azure OpenAI, with every reason shown.", "hybrid"),
            StoryCard("3", "Make it real for retail", "Run six retail workflows, from store visit follow-ups and customer care case summaries to in-stock reviews and line review follow-ups, then size the device and frame a pilot with your own numbers.", "industries"));

        var hybridWays = new AdaptiveGrid(260, 3).With(
            WayCard("\uE8AB", "See the split", "Route a store's service desk email or a complex question and watch what stays on this PC, what is de-identified here first and what would go to the cloud, with every reason shown.", "Open the Hybrid router", "hybrid"),
            WayCard("\uEC4A", "Show it off", "Measure the loaded model live, rank models over the session and follow a five-minute run of show that ends with a deck.", "Open Show it off", "showoff"),
            WayCard("\uE943", "Build on it", "Give developers, data analysts and architects a loopback, OpenAI-compatible endpoint, working code and starter projects that run against this GPU.", "Open Build on Surface", "build"));

        var deviceClasses = WayCard("\uE772", "What runs where", "See what the AI PCs you already have can run on the device, what needs more memory and where Surface Laptop Ultra fits, with Microsoft sources.", "Open Device classes", "deviceclasses");

        var guardrails = CardBorder(Stack(8,
            H3("What this showcase will not claim"),
            Body("- No cash savings, ROI forecast or subscription replacement; capacity value is illustrative."),
            Body("- No battery or speed comparisons with other devices; metrics describe one local run."),
            Body("- No claim that Snapdragon or Intel workflows ran on this laptop; they are recommended pilots verified per SKU."),
            Body("- Drafts only: no change or update is approved, scheduled or deployed, no ticket is closed or reassigned, no device policy is changed, no root cause is determined, no refund or credit is issued, no order, transfer or allocation is placed, and nothing is sent to customers, associates, stores, vendors or stakeholders."),
            Body("- Not legal or HR advice. No HR, vendor, purchasing, pricing or supplier decision and no regulatory or compliance determination; store operations, merchandising, allocation, customer care, store technology, the service desk and the incident manager review everything."),
            Body("- Synthetic data only: no real customers, associates, stores, devices, orders, tickets or personal data, and team leads review every draft."),
            Body("- De-identification removes structured identifiers only; it is not certified. No point-of-sale, order management, endpoint management, service desk (ITSM) or HR system connection is made."),
            Body("- Generated code is shown as text and never executed. Sources are synthetic.")), 22);

        return Page(Stack(26, hero, Stack(10, stats, specNote), deviceClasses, BuildArchitecture(), Stack(14, H2("The five-minute retail story"), story),
            Stack(14, H2("Hybrid Intelligence: see it, show it, build on it"),
                Body("The PC does what it does best - private, fast, always available - and the cloud does what only it can. These pages make that split visible, measurable and buildable."),
                hybridWays),
            guardrails));
    }

    private FrameworkElement WayCard(string glyph, string title, string body, string action, string target)
    {
        var go = Id(Secondary(action + "  \u2192"), "OverviewWay_" + target);
        go.HorizontalAlignment = HorizontalAlignment.Left;
        go.Click += (_, _) => Navigate(target);
        return CardBorder(Stack(10, Glyph(glyph, 24, Accent), H3(title), Body(body), go), 22);
    }

    private FrameworkElement StoryCard(string number, string title, string body, string target)
    {
        var badge = new Border
        {
            Width = 34, Height = 34, CornerRadius = new CornerRadius(17), Background = Accent,
            HorizontalAlignment = HorizontalAlignment.Left,
            Child = Set(Text(number, 15, White, FontWeights.Bold), t => { t.HorizontalAlignment = HorizontalAlignment.Center; t.VerticalAlignment = VerticalAlignment.Center; })
        };
        var go = Id(new HyperlinkButton { Content = "Open", Padding = new Thickness(0), Foreground = Accent }, "OverviewStory_" + target);
        go.Click += (_, _) => Navigate(target);
        return CardBorder(Stack(10, badge, H3(title), Body(body), go), 22);
    }

    private void ApplyOverviewStatus(StatusSnapshot status)
    {
        var d = status.Device;
        _ovDevice.Text = d.Error is null
            ? $"{d.DisplayName}  |  {d.Cpu}"
            : "Device inventory unavailable: " + d.Error;
        _ovInstalled.Text = Gb(d.InstalledGiB);
        _ovGpuCores.Text = CoreCount(d.Cpu, "GPU") ?? d.Accelerators.Select(a => CoreCount(a, "")).FirstOrDefault(c => c is not null) ?? "Unavailable";
        _ovCpuCores.Text = CoreCount(d.Cpu, "CPU") ?? (d.Cores is int cores ? $"{cores}-core" : "Unavailable");
    }

    private static string? CoreCount(string? text, string unit)
    {
        var match = text is null ? null : System.Text.RegularExpressions.Regex.Match(text, $@"(\d+)-core\s*(?:\w+\s+)*?{unit}");
        return match is { Success: true } && int.TryParse(match.Groups[1].Value, out int n)
            ? n.ToString("N0", System.Globalization.CultureInfo.InvariantCulture) + "-core"
            : null;
    }

    private FrameworkElement BuildPlaybook()
    {
        var runOfShow = Id(CardBorder(Stack(8,
            H3("Run of show (60 minutes)"),
            RunItem("00:00", "Introductions and goals - the account technology strategist (5 min)."),
            RunItem("00:05", "Your question first: why the NPU on the Copilot+ PCs you have sits idle, and what runs where - open Device classes (10 min)."),
            RunItem("00:15", "Live: Company overview, then Retail scenarios - run the store visit follow-up on the GPU (10 min)."),
            RunItem("00:25", "Live demos: store operations call to notes and actions; de-identify before any cloud step; Hybrid router (10 min)."),
            RunItem("00:35", "Model choice: Build on Surface (one OpenAI-compatible API for Foundry Local and llama.cpp; Microsoft-provided and open-source models) and T-shirt sizing (10 min)."),
            RunItem("00:45", "The Surface specialist: Surface Laptop Ultra specs, Arm requirements, pricing and purchase options (10 min)."),
            RunItem("00:55", "Discovery questions and next steps: agree a scoped pilot (5 min).")), 22), "PlaybookRunOfShow");

        var beats = new AdaptiveGrid(280, 3).With(
            Beat("Open (30 s)", "\"Customer and associate personal data, store performance figures and unreleased product information never need to leave your company. This laptop transcribes and drafts on its RTX GPU; only de-identified complex questions would go to the cloud, and your team leads review every draft.\""),
            Beat("Prove (2 min)", "Walk the architecture: run operations call capture (Tier 1), draft a store visit follow-up (Tier 2), then route the complex question and show the NOT SENT de-identified payload (Tier 3). Rehearsal is labelled and has no metrics."),
            Beat("Land (2 min)", "Size the workload with T-shirt sizes, map headquarters, store, distribution center and customer care devices with Platform fit, then agree a four-week pilot on synthetic store visit, customer care and service desk records with measured baselines."));

        var questions = CardBorder(Stack(8,
            H3("Discovery questions"),
            Body("1. Which repeated retail tasks (store visit follow-ups, customer care case summaries, in-stock reviews, line review follow-ups, store device health summaries, incident updates) take meaningful time today?"),
            Body("2. Which AI PCs and processor families are deployed, by persona (headquarters, stores, distribution centers, customer care)?"),
            Body("3. Which on-device AI features or local models are in use today, and what has blocked wider use? (Device classes shows what the NPU runs today.)"),
            Body("4. Arm64 readiness: which VPN, security agent, printer and peripheral, and line-of-business app dependencies remain?"),
            Body("5. Management: how are Intune and Windows Autopilot set up for AI PCs, and who approves new local models and runtimes?"),
            Body("6. Data: which customer, associate, store and product data may a local model read, and where must outputs stay?"),
            Body("7. Model choice: which Microsoft-provided and open-source models, runtimes and licences are approved, and what does the AI acceptable-use policy allow?"),
            Body("8. Measures: which measures (visit report time, case handling time, handoff quality, service desk volumes) would a pilot compare against?"),
            Body("9. Where would a Surface Laptop Ultra fit (data and AI builders, design and product teams, developers), and what memory configuration do those workloads need?")), 22);

        var objections = Stack(8, H3("Objection handling"),
            Objection("We bought Copilot+ PCs for their NPU. Why aren't we using it?", "The NPU only helps when software is built to use it. Built-in Windows experiences such as improved Windows search and Live Captions use it, and your own apps reach it through the Windows AI APIs, Windows ML or Foundry Local; Task Manager shows NPU activity. Open Device classes to see what runs where. Everything live in this app runs on this laptop's RTX GPU."),
            Objection("How is AI accelerated on this device?", "On the RTX GPU through the CUDA execution provider in Foundry Local. The run evidence names the model variant and provider; there is no silent CPU fallback."),
            Objection("Can we run Microsoft-provided and open-source models?", "Yes. Foundry Local and llama.cpp both serve the same OpenAI-compatible API on loopback, so the same code can call a Microsoft-provided or an open-source model by changing a base URL and model name. Check each model's licence and your AI acceptable-use policy, and verify the exact model variant on each device."),
            Objection("Is it really 128 GB?", "128 GB is installed physical memory. Windows reports about 64 GB visible, and the GPU driver reports a 64,000 MiB budget. These are separate views and are never added."),
            Objection("Will it save us money?", "This app shows illustrative capacity value only, not cash savings or ROI. Time savings and adoption must be measured in a pilot; cloud subscriptions are unchanged."),
            Objection("Can we use real customer, associate or store data?", "Not in this showcase. Every record here is synthetic, including Contoso Apparel, Relecloud Scheduler and the VanArsdel TP-40 receipt printer. A pilot with real customer or associate personal data, store figures, orders or ticket details needs your company's information security, privacy and change-management reviews first; this app makes no legal, regulatory or compliance determination."),
            Objection("Will it change orders, devices or tickets?", "No. It drafts notes, follow-up lists, case summaries, incident updates and review lists for team leads to review and approve. Refunds and credits, orders, transfers and allocations, approving or deploying changes and updates, closing or reassigning tickets, changing device policies, determining a root cause and HR, vendor, purchasing, pricing or supplier decisions stay with authorized people, and nothing is sent to customers, associates, stores, vendors or stakeholders; nothing here is legal or HR advice."),
            Objection("What goes to Azure OpenAI?", "In the architecture, only de-identified, minimized queries for complex questions. In this showcase nothing is sent: the Hybrid router shows the payload marked NOT SENT. Structured identifiers are removed; free-text customer, associate or device detail still needs human review."),
            Objection("Does this run on our Snapdragon or Intel fleet?", "Those are recommended pilots. Verify the exact model, runtime and accelerator support per SKU; nothing here ran on those devices."),
            Objection("What about model reasoning text?", "Private reasoning is counted but never displayed, exported or saved. Only the final answer is shown."),
            Objection("Does local AI replace the cloud?", "No. Hybrid Intelligence keeps private, fast and offline work on the PC and uses the cloud for current information, organisation-wide data and frontier scale. The Hybrid router shows the split and its reasons; the studio itself never calls a cloud service."),
            Objection("Can our developers build on this?", "Yes. Build on Surface starts an OpenAI-compatible endpoint on loopback (off by default, this PC only) and creates small starter projects in Python and C#. Your code reviews and runs them; the studio never executes generated code."));

        var doDont = new AdaptiveGrid(300, 2).With(
            CardBorder(Stack(6, Set(H3("Do"), t => t.Foreground = GreenInk),
                Body("Use live runs whenever the model is ready."),
                Body("Name the exact model and provider shown."),
                Body("Position every estimate as illustrative."),
                Body("Keep every example synthetic and every decision human."),
                Body("Say \"Synthetic data only. Drafts only; nothing is deployed, changed or sent.\" before the first run.")), 22),
            CardBorder(Stack(6, Set(H3("Don't"), t => t.Foreground = AccentDeep),
                Body("Present rehearsal as live output."),
                Body("Compare speed or battery with other devices."),
                Body("Add memory views together or call the GPU budget VRAM."),
                Body("Promise savings, customer outcomes, compliance or decision accuracy."),
                Body("Describe any real company's fleet, stores, systems, vendors or people."),
                Body("Turn the hour into a device-spec briefing; the Surface specialist covers specs, Arm requirements, pricing and purchase options.")), 22));

        var rampUp = Id(CardBorder(Lead(14, Glyph("\uE7BE", 22, Accent), Stack(8,
            H3("Optional: ramp up technically"),
            Body("'Coding as a second language' is eight short AI-literacy lessons for store operations, merchandising, customer care and IT teams that teach you to read code like a new language, with a quick check per lesson and a local coding tutor on the RTX GPU. Progress is saved on this laptop only."),
            _learnToggle)), 22), "PlaybookLearnCard");

        return Page(Stack(24,
            Stack(10, Eyebrow("Retail playbook  |  " + Event.Name), H1("One hour. Three beats. One scoped pilot."),
                Body("A concise talk track for store operations, merchandising, customer care, store technology and IT leaders: a 60-minute run of show, a five-minute story in three beats and the guardrails that keep it credible. Synthetic data only. Drafts only; nothing is deployed, changed or sent.")),
            runOfShow, Stack(10, H3("The five-minute story"), beats), questions, objections, doDont, rampUp));
    }

    private static FrameworkElement RunItem(string time, string text) =>
        Lead(12, Set(Text(time, 14, Accent, FontWeights.SemiBold), t => t.LineHeight = 21), Body(text, Ink));

    private static FrameworkElement Beat(string title, string body) =>
        CardBorder(Stack(8, Set(Text(title.ToUpperInvariant(), 12, Accent, FontWeights.SemiBold), t => t.CharacterSpacing = 80), Set(Body(body, Ink), t => t.FontSize = 15)), 22);

    private static FrameworkElement Objection(string question, string answer) => new Expander
    {
        Header = Text(question, 14, Ink, FontWeights.SemiBold),
        Content = Body(answer, Ink),
        HorizontalAlignment = HorizontalAlignment.Stretch,
        HorizontalContentAlignment = HorizontalAlignment.Left,
    };
}
