using System.Globalization;

namespace HybridIntelligenceRetail;

/// <summary>A Microsoft page that backs a statement on the Device classes page.</summary>
internal sealed record DeviceClassSource(string Key, string Label, string Url);

/// <summary>Why a line on the Device classes page may say what it says.</summary>
internal enum DeviceClassTextKind { Sourced, Route, Disclaimer, Guidance }

internal sealed record DeviceClassText(string Text, DeviceClassTextKind Kind, DeviceClassSource? Source = null);

/// <summary>The Microsoft-documented on-device route for a workload, or <see cref="DeviceClasses.NoRoute"/>.</summary>
internal sealed record DeviceClassRoute(string WorkloadId, string Route, DeviceClassSource[] Sources);

/// <summary>A fictional pattern from another industry showcase, mapped to a live demo and the demo's sizing workload.</summary>
internal sealed record DeviceClassPattern(string Industry, string Pattern, string InRetail, string DemoId, string WorkloadId);

/// <summary>One matrix row. Every fit comes from <see cref="SalesSizing.Evaluate"/>; nothing is hardcoded.</summary>
internal sealed record DeviceClassRow(SalesWorkload Workload, SalesDeviceFit Laptop16, SalesDeviceFit Laptop32, SalesDeviceFit ThisLaptop,
    DeviceClassRoute Route, string SuggestedClass)
{
    internal bool CanRunLive => DeviceClasses.CanRunLive(Workload);
}

/// <summary>
/// Data and logic for the Device classes page: what Microsoft documents about the AI PCs a customer already has, where a
/// Builder PC fits, and which everyday workloads fit which memory size. This app itself runs nothing on an NPU.
/// </summary>
internal static class DeviceClasses
{
    // Sources first: the arrays below read them during static initialization, which runs in textual order.
    internal static readonly DeviceClassSource NpuDevices = new("npu-devices", "NPU devices (Microsoft Learn)", ApprovedLinks.NpuDevices);
    internal static readonly DeviceClassSource Apis = new("apis", "Windows AI APIs (Microsoft Learn)", ApprovedLinks.WindowsAiApis);
    internal static readonly DeviceClassSource PhiSilica = new("phi-silica", "Phi Silica (Microsoft Learn)", ApprovedLinks.PhiSilica);
    internal static readonly DeviceClassSource ExecutionProviders = new("eps", "Windows ML execution providers (Microsoft Learn)", ApprovedLinks.WindowsMlExecutionProviders);
    internal static readonly DeviceClassSource FoundryBlog = new("foundry-blog", "Foundry Local meets more silicon (Microsoft Foundry blog)", ApprovedLinks.FoundryLocalMoreSilicon);
    internal static readonly DeviceClassSource FoundryStart = new("foundry-start", "Get started with Foundry Local (Microsoft Learn)", ApprovedLinks.FoundryLocalGetStarted);
    internal static readonly DeviceClassSource CopilotPlus = new("copilot-plus", "Copilot+ PCs for business (Microsoft)", ApprovedLinks.CopilotPlusPcs);
    internal static readonly DeviceClassSource SurfaceLaptop = new("surface-laptop", "Surface Laptop (Microsoft)", ApprovedLinks.SurfaceLaptop);
    internal static readonly DeviceClassSource Ultra = new("ultra", "Surface Laptop Ultra (Microsoft)", ApprovedLinks.SurfaceLaptopUltra);
    internal static readonly DeviceClassSource UltraSpecs = new("ultra-specs", "Surface Laptop Ultra tech specs (Microsoft Learn)", ApprovedLinks.SurfaceLaptopUltraSpecs);
    internal static readonly DeviceClassSource Blog = new("blog", "Building Windows for hybrid intelligence (Windows Experience Blog)", ApprovedLinks.HybridIntelligenceBlog);

    internal static readonly DeviceClassSource[] Sources =
        [NpuDevices, Apis, PhiSilica, ExecutionProviders, FoundryBlog, FoundryStart, CopilotPlus, SurfaceLaptop, Ultra, UltraSpecs, Blog];

    internal const string PageEyebrow = "Device classes";
    internal const string PageTitle = "What runs where: the AI PCs you have, and where Surface Laptop Ultra fits.";
    internal const string PageIntro =
        "See which local AI work suits the AI PCs you already have, which work needs more memory, and where a Builder PC fits. " +
        "Each fact links to its Microsoft source, and each fit is a memory estimate from the same arithmetic as T-shirt sizing.";

    /// <summary>Exact wording shared with the web edition and the docs wherever NPU routes are shown.</summary>
    internal const string Disclaimer =
        "NPU routes on this page are documented by Microsoft; this app does not run anything on an NPU. " +
        "Everything live here runs on this laptop's RTX GPU through CUDA.";

    internal const string CopilotPlusTitle = "The Copilot+ PCs you already have";
    internal const string CopilotPlusIntro = "What Microsoft documents about these PCs. Each line links to its source.";

    internal static readonly DeviceClassText[] CopilotPlusFacts =
    [
        new("Copilot+ PCs have an NPU that can perform more than 40 trillion operations per second, but software must be programmed to use it. " +
            "Task Manager shows NPU usage, and Microsoft recommends Windows ML for running your own models on the NPU.", DeviceClassTextKind.Sourced, NpuDevices),
        new("Built-in Copilot+ PC experiences include improved Windows search, Recall (preview) and Live Captions with real-time translation from 40+ languages into English. " +
            "Availability depends on the device, Windows version, region and organization settings.", DeviceClassTextKind.Sourced, CopilotPlus),
        new("On Surface Laptop, Copilot+ PC experiences are available on configurations with 16 GB of memory or more.", DeviceClassTextKind.Sourced, SurfaceLaptop),
        new("Windows AI APIs such as Phi Silica, text recognition (OCR), Image Description, Image Super Resolution and Image Segmentation run on the NPU on Copilot+ PCs. " +
            "The Speech Recognition API is experimental and the Semantic Search API is in private preview; AI Dev Gallery in the Microsoft Store has samples.", DeviceClassTextKind.Sourced, Apis),
        new("Phi Silica is Windows' on-device language model, preinstalled on Copilot+ PCs and offered as a Limited Access Feature. " +
            "Its successor, Aion Instruct, arrives in Windows Insider builds from November 2026 and in retail Windows from January 2027, with no Limited Access Feature token.", DeviceClassTextKind.Sourced, PhiSilica),
        new("Windows ML picks an execution provider such as QNN (Snapdragon) or OpenVINO (Intel) and can fall back to the GPU or CPU.", DeviceClassTextKind.Sourced, ExecutionProviders),
        new("Foundry Local detects the NPU, GPU and CPU and downloads matching execution providers. " +
            "Which models have an NPU variant depends on the device, so verify on the target PC.", DeviceClassTextKind.Sourced, FoundryBlog),
    ];

    internal const string TryTitle = "Try this on a Copilot+ PC you already have";

    internal static readonly DeviceClassText[] TryThis =
    [
        new("Open Task Manager to see NPU activity.", DeviceClassTextKind.Sourced, NpuDevices),
        new("Install AI Dev Gallery from the Microsoft Store and run the Windows AI API samples.", DeviceClassTextKind.Sourced, Apis),
        new("Ask a developer to try Foundry Local: its SDK discovers the PC's execution providers and lists the model variants available for it.", DeviceClassTextKind.Sourced, FoundryStart),
        new("Pick one workload below that fits a 16 GB Copilot+ PC and pilot it on synthetic data first.", DeviceClassTextKind.Guidance),
    ];

    internal const string BuilderTitle = "Builder PCs: Surface Laptop Ultra (this laptop)";

    internal static readonly DeviceClassText[] BuilderFacts =
    [
        new("Microsoft describes Builder PCs as a device class for hybrid intelligence, and Surface Laptop Ultra is one.", DeviceClassTextKind.Sourced, Blog),
        new("Surface Laptop Ultra has the NVIDIA RTX Spark Superchip, built for local AI and 3D graphics, and up to 128 GB of unified memory.", DeviceClassTextKind.Sourced, Ultra),
    ];

    /// <summary>Verbatim from Microsoft's Surface Laptop Ultra page.</summary>
    internal static readonly DeviceClassText[] BuilderQuotes =
    [
        new("\u201CRun local agents, automate routine tasks, keep sensitive work closer to you, and reserve the cloud for larger AI workloads.\u201D", DeviceClassTextKind.Sourced, Ultra),
        new("\u201Cbuilt for organizations working with proprietary code, AI models, customer data, and intellectual property\u201D", DeviceClassTextKind.Sourced, Ultra),
    ];

    internal static readonly DeviceClassText BuilderSpecs =
        new("For memory configurations and full specifications, see the tech specs.", DeviceClassTextKind.Sourced, UltraSpecs);

    internal const string BudgetPrefix = "GPU memory budget on this laptop now: ";
    internal const string BudgetUnknown = "Not known yet";
    internal const string BudgetNote =
        "Reported live by the graphics driver. The GPU can address less than the installed memory, " +
        "so the estimates for this laptop below use this budget, not the installed total.";

    internal const string AlwaysOnTitle = "Always-on and shared";

    internal static readonly DeviceClassText[] AlwaysOnFacts =
    [
        new("Mini desktop PCs are a device class for always-on agents.", DeviceClassTextKind.Sourced, Blog),
        new("DGX Station for Windows, with NVIDIA GB300, is a device class for trillion-parameter models and 32 or more simultaneous agents.", DeviceClassTextKind.Sourced, Blog),
    ];

    internal const string IllustrativeLabel = "ILLUSTRATIVE FIT, NOT A RECOMMENDATION";
    internal const string AlwaysOnExample = "An always-on agent that drafts a daily fleet health summary for people to review.";
    internal const string AlwaysOnNote = "This app does not size or run these classes; ask the account team about them.";

    internal const string MatrixTitle = "Everyday workloads by device class";
    internal const string MatrixIntro =
        "One row per T-shirt sizing workload. The 16 GB and 32 GB columns are illustrative memory sizes; " +
        "the third column uses this laptop's live GPU memory budget.";
    internal const string Column16 = "16 GB estimate";
    internal const string Column32 = "32 GB estimate";
    internal const string ColumnHere = "This laptop (GPU budget)";
    internal const string ColumnClass = "Suggested class";
    internal const string RouteLabel = "Documented NPU route";
    internal const string NoRoute = "No documented NPU route on this page";

    /// <summary>Exact wording shared with the web edition and the docs.</summary>
    internal const string MatrixFootnote =
        "Memory fit only, using the same arithmetic as T-shirt sizing; it does not confirm an NPU model variant or runtime support. Verify on the target PC.";

    internal const string RunLabel = "Run live";
    internal const string RunTooltip = "Opens this workload's live demo. Start it from the demo runner.";
    internal const string NotLiveHere = "Memory estimate only; this row has no live demo on this page.";
    internal const string OpenSizingLabel = "Open T-shirt sizing";

    internal const string ClassCopilotPlus = "Copilot+ PC (16 GB)";
    internal const string ClassMidrange = "32 GB AI PC or Builder PC";
    internal const string ClassBuilder = "Builder PC (Surface Laptop Ultra)";

    internal static readonly DeviceClassRoute[] Routes =
    [
        new("transcription", "Speech Recognition API (experimental) and Live Captions", [Apis, CopilotPlus]),
        new("field", "Phi Silica text skills (Aion Instruct from 2027)", [PhiSilica]),
        new("translation", "Live Captions real-time speech translation", [CopilotPlus]),
        new("writing", "Phi Silica text skills (Aion Instruct from 2027)", [PhiSilica]),
        new("documents", "Improved Windows search; Semantic Search API (private preview)", [CopilotPlus, Apis]),
        new("vision", "Text recognition (OCR) and Image Description APIs", [Apis]),
        new("coding", NoRoute, []),
        new("reasoning", NoRoute, []),
        new("prototyping", NoRoute, []),
        new("frontier", NoRoute, []),
    ];

    internal const string PatternsTitle = "Patterns from other industry showcases";
    internal const string PatternsSubtitle =
        "Fictional patterns from Microsoft's industry showcases, not customer references. Ask the account team for named customer references.";
    internal const string PatternPrefix = "In retail: ";
    internal const string PatternClassPrefix = "Suggested class: ";
    internal const string PatternWorkloadPrefix = "T-shirt sizing workload: ";
    internal const string PatternRunLabel = "Run the equivalent here";

    internal static readonly DeviceClassPattern[] Patterns =
    [
        new("Financial services", "Meeting capture", "store operations calls", "meeting", "transcription"),
        new("Telecom and media", "Offline field notes", "distribution center shift handoffs", "voice-memo", "field"),
        new("Tax and accounting", "Scanned forms", "store device service forms", "vision", "vision"),
        new("Higher education", "Policy questions with citations", "device standards and change policy", "ask-docs", "documents"),
        new("Private markets", "De-identify before the cloud", "associate emails before any cloud step", "redact", "writing"),
        new("Engineering and software", "Proprietary code assistant", "e-commerce and store systems code", "code", "coding"),
    ];

    internal static DeviceClassRoute RouteFor(string workloadId) =>
        Routes.FirstOrDefault(r => r.WorkloadId == workloadId) ?? new DeviceClassRoute(workloadId, NoRoute, []);

    internal static bool Fits(SalesFit fit) => fit is SalesFit.Comfortable or SalesFit.Tight;

    /// <summary>Fits 16 GB, else fits 32 GB, else needs a Builder PC. Only the illustrative memory sizes decide the class.</summary>
    internal static string SuggestedClass(SalesDeviceFit at16, SalesDeviceFit at32) =>
        Fits(at16.Fit) ? ClassCopilotPlus : Fits(at32.Fit) ? ClassMidrange : ClassBuilder;

    internal static bool CanRunLive(SalesWorkload workload) => workload.LiveOnThisLaptop && workload.DemoId is not null;

    /// <summary>The live GPU memory budget reported by the driver, never the installed or Windows-visible memory.</summary>
    internal static double? GpuBudgetGiB(DeviceFacts? device) => Sizing.ResolveBudget(BudgetSource.GpuDriverBudget, device, double.NaN);

    internal static string BudgetText(DeviceFacts? device) =>
        GpuBudgetGiB(device) is double gib ? gib.ToString("0.#", CultureInfo.InvariantCulture) + " GB" : BudgetUnknown;

    internal static string BudgetLine(DeviceFacts? device) => BudgetPrefix + BudgetText(device);

    internal static DeviceClassRow Row(SalesWorkload workload, DeviceFacts? device)
    {
        var at16 = Compare("laptop16", workload.Size);
        var at32 = Compare("laptop32", workload.Size);
        var here = SalesSizing.Evaluate(SalesSizing.ThisLaptop, workload.Size, GpuBudgetGiB(device));
        return new DeviceClassRow(workload, at16, at32, here, RouteFor(workload.Id), SuggestedClass(at16, at32));
    }

    internal static DeviceClassRow[] Matrix(DeviceFacts? device) => SalesSizing.Workloads.Select(w => Row(w, device)).ToArray();

    /// <summary>The pattern's suggested class comes from the engine through the demo's sizing workload.</summary>
    internal static DeviceClassRow? PatternRow(DeviceClassPattern pattern, DeviceFacts? device) =>
        SalesSizing.Find(pattern.WorkloadId) is { } workload ? Row(workload, device) : null;

    private static SalesDeviceFit Compare(string comparisonId, TShirtSize size)
    {
        foreach (var (device, budget) in SalesSizing.Comparisons)
            if (device.Id == comparisonId) return SalesSizing.Evaluate(device, size, budget);
        return SalesSizing.Evaluate(new SalesDevice(comparisonId, comparisonId, ""), size, null);
    }

    /// <summary>Every link the page can open.</summary>
    internal static IEnumerable<string> Links =>
        Texts().Where(t => t.Source is not null).Select(t => t.Source!.Url)
            .Concat(Routes.SelectMany(r => r.Sources).Select(s => s.Url))
            .Distinct();

    /// <summary>Every string the page shows, tagged with why it may say what it says.</summary>
    internal static IEnumerable<DeviceClassText> Texts()
    {
        foreach (var source in Sources) yield return new(source.Label, DeviceClassTextKind.Sourced, source);
        string[] guidance =
        [
            PageEyebrow, PageTitle, PageIntro, CopilotPlusTitle, CopilotPlusIntro, TryTitle, BuilderTitle, BudgetPrefix, BudgetUnknown, BudgetNote,
            AlwaysOnTitle, IllustrativeLabel, AlwaysOnExample, AlwaysOnNote, MatrixTitle, MatrixIntro, Column16, Column32, ColumnHere, ColumnClass,
            RunLabel, RunTooltip, NotLiveHere, OpenSizingLabel, ClassCopilotPlus, ClassMidrange, ClassBuilder,
            PatternsTitle, PatternsSubtitle, PatternPrefix, PatternClassPrefix, PatternWorkloadPrefix, PatternRunLabel,
        ];
        foreach (string text in guidance) yield return new(text, DeviceClassTextKind.Guidance);
        yield return new(Disclaimer, DeviceClassTextKind.Disclaimer);
        yield return new(MatrixFootnote, DeviceClassTextKind.Disclaimer);
        yield return new(RouteLabel, DeviceClassTextKind.Route);
        foreach (var route in Routes) yield return new(route.Route, DeviceClassTextKind.Route, route.Sources.FirstOrDefault());
        foreach (var fact in CopilotPlusFacts.Concat(TryThis).Concat(BuilderFacts).Concat(BuilderQuotes).Append(BuilderSpecs).Concat(AlwaysOnFacts))
            yield return fact;
        foreach (var pattern in Patterns)
        {
            yield return new(pattern.Industry, DeviceClassTextKind.Guidance);
            yield return new(pattern.Pattern, DeviceClassTextKind.Guidance);
            yield return new(pattern.InRetail, DeviceClassTextKind.Guidance);
        }
    }

    internal static IEnumerable<string> AllText() => Texts().Select(t => t.Text);
}
