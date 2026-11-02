using Microsoft.UI.Text;
using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;
using Microsoft.UI.Xaml.Media;
using static HybridIntelligenceRetail.Ui;

namespace HybridIntelligenceRetail;

internal sealed partial class MainWindow
{
    private readonly TextBlock _deviceClassBudget = Id(Text(DeviceClasses.BudgetLine(null), 16, Ink, FontWeights.SemiBold), "DeviceClassBudget");
    private readonly Dictionary<string, (Border Cell, TextBlock Fit)> _deviceClassHere = [];
    private readonly List<(HyperlinkButton Link, string Url)> _deviceClassLinks = [];

    /// <summary>What the AI PCs a customer already has can run, where a Builder PC fits, and patterns from other showcases.</summary>
    private FrameworkElement BuildDeviceClasses()
    {
        var device = _status?.Device;
        var header = Stack(10, Eyebrow(DeviceClasses.PageEyebrow), H1(DeviceClasses.PageTitle), Body(DeviceClasses.PageIntro));
        var disclaimer = CardBorder(Lead(12, Glyph("\uE946", 18), Id(Body(DeviceClasses.Disclaimer, Ink), "DeviceClassesDisclaimer")), 16, SlateTint);
        var classes = new AdaptiveGrid(380, 2, 18).With(BuildDeviceClassBuilderCard(), BuildDeviceClassAlwaysOnCard());
        return Page(Stack(22, header, disclaimer, BuildDeviceClassCopilotPlusCard(), classes,
            BuildDeviceClassMatrix(device), BuildDeviceClassPatterns(device)));
    }

    private Border BuildDeviceClassCopilotPlusCard()
    {
        var facts = new AdaptiveGrid(340, 2, 18);
        for (int i = 0; i < DeviceClasses.CopilotPlusFacts.Length; i++)
            facts.With(DeviceClassFact(DeviceClasses.CopilotPlusFacts[i], $"DeviceClassSource_copilot_{i}"));

        var tryThis = Stack(10, H3(DeviceClasses.TryTitle));
        for (int i = 0; i < DeviceClasses.TryThis.Length; i++)
            tryThis.Children.Add(Lead(8, Text($"{i + 1}.", 14, AccentDeep, FontWeights.SemiBold),
                DeviceClassFact(DeviceClasses.TryThis[i], $"DeviceClassSource_try_{i}")));

        return Id(CardBorder(Stack(16,
            DeviceClassBand(Accent),
            Stack(6, H2(DeviceClasses.CopilotPlusTitle), Body(DeviceClasses.CopilotPlusIntro)),
            facts,
            Id(CardBorder(tryThis, 18, Sand), "DeviceClassTryThis")), 24), "DeviceClassCopilotPlus");
    }

    private Border BuildDeviceClassBuilderCard()
    {
        var body = Stack(14, DeviceClassBand(GreenInk), H2(DeviceClasses.BuilderTitle));
        for (int i = 0; i < DeviceClasses.BuilderFacts.Length; i++)
            body.Children.Add(DeviceClassFact(DeviceClasses.BuilderFacts[i], $"DeviceClassSource_builder_{i}"));

        var quotes = Stack(8);
        foreach (var quote in DeviceClasses.BuilderQuotes)
            quotes.Children.Add(Set(Text(quote.Text, 15, Ink), t => { t.FontStyle = Windows.UI.Text.FontStyle.Italic; t.LineHeight = 22; }));
        quotes.Children.Add(DeviceClassLink(DeviceClasses.BuilderQuotes[0].Source!, "DeviceClassSource_quote_0"));
        body.Children.Add(Id(CardBorder(quotes, 16, Paper), "DeviceClassQuotes"));

        body.Children.Add(CardBorder(Stack(4, _deviceClassBudget, Small(DeviceClasses.BudgetNote)), 16, GreenTint));
        body.Children.Add(DeviceClassFact(DeviceClasses.BuilderSpecs, "DeviceClassSource_specs_0"));
        return Id(CardBorder(body, 24), "DeviceClassBuilder");
    }

    private Border BuildDeviceClassAlwaysOnCard()
    {
        var body = Stack(14, DeviceClassBand(Slate), H2(DeviceClasses.AlwaysOnTitle));
        var facts = Stack(6);
        foreach (var fact in DeviceClasses.AlwaysOnFacts) facts.Children.Add(Body(fact.Text, Ink));
        var sources = DeviceClasses.AlwaysOnFacts.Select(f => f.Source!).Distinct().ToArray();
        for (int i = 0; i < sources.Length; i++) facts.Children.Add(DeviceClassLink(sources[i], $"DeviceClassSource_alwayson_{i}"));
        body.Children.Add(facts);
        body.Children.Add(Id(CardBorder(Stack(4,
            Text(DeviceClasses.IllustrativeLabel, 11, AmberInk, FontWeights.SemiBold),
            Body(DeviceClasses.AlwaysOnExample, Ink)), 16, AmberTint), "DeviceClassAlwaysOnExample"));
        body.Children.Add(Small(DeviceClasses.AlwaysOnNote));
        return Id(CardBorder(body, 24), "DeviceClassAlwaysOn");
    }

    private FrameworkElement BuildDeviceClassMatrix(DeviceFacts? device)
    {
        var rows = new AdaptiveGrid(480, 2, 16);
        foreach (var row in DeviceClasses.Matrix(device)) rows.With(DeviceClassRowCard(row));
        var openSizing = Id(Secondary(DeviceClasses.OpenSizingLabel), "DeviceClassOpenSizing");
        openSizing.Click += (_, _) => { Navigate("sizing"); ShowSizingTab(technical: false); };
        return Id(Stack(14,
            Stack(6, H2(DeviceClasses.MatrixTitle), Body(DeviceClasses.MatrixIntro)),
            rows,
            Id(Small(DeviceClasses.MatrixFootnote, Ink), "DeviceClassMatrixFootnote"),
            openSizing), "DeviceClassMatrix");
    }

    private Border DeviceClassRowCard(DeviceClassRow row)
    {
        var w = row.Workload;
        var title = Lead(10, Pill(w.Size.ToString(), AccentTint, AccentDeep), Stack(2, Text(w.Name, 15, Ink, FontWeights.SemiBold), Small(w.Plain)));
        var hereCell = DeviceClassFitCell(DeviceClasses.ColumnHere, row.ThisLaptop.Fit, $"DeviceClassFitHere_{w.Id}", out var hereText);
        _deviceClassHere[w.Id] = (hereCell, hereText);
        var cells = new AdaptiveGrid(110, 4, 8).With(
            DeviceClassFitCell(DeviceClasses.Column16, row.Laptop16.Fit, $"DeviceClassFit16_{w.Id}", out _),
            DeviceClassFitCell(DeviceClasses.Column32, row.Laptop32.Fit, $"DeviceClassFit32_{w.Id}", out _),
            hereCell,
            DeviceClassCell(DeviceClasses.ColumnClass, row.SuggestedClass, SlateTint, Ink, $"DeviceClassSuggested_{w.Id}", out _));

        var route = Stack(2,
            Text(DeviceClasses.RouteLabel.ToUpperInvariant(), 11, Muted, FontWeights.SemiBold),
            Id(Small(row.Route.Route, Ink), $"DeviceClassRoute_{w.Id}"));
        for (int i = 0; i < row.Route.Sources.Length; i++)
            route.Children.Add(DeviceClassLink(row.Route.Sources[i], $"DeviceClassRouteSource_{w.Id}_{i}"));

        UIElement action;
        if (row.CanRunLive && w.DemoId is string demoId)
        {
            var run = Id(Primary(DeviceClasses.RunLabel), $"DeviceClassRun_{w.Id}");
            run.Padding = new Thickness(14, 6, 14, 7);
            ToolTipService.SetToolTip(run, DeviceClasses.RunTooltip);
            run.Click += async (_, _) => await OpenDeviceClassDemoAsync(demoId);
            action = run;
        }
        else action = Id(Small(DeviceClasses.NotLiveHere), $"DeviceClassNotLive_{w.Id}");

        return Id(CardBorder(Stack(12, title, cells, route, action), 18), $"DeviceClassRow_{w.Id}");
    }

    private FrameworkElement BuildDeviceClassPatterns(DeviceFacts? device)
    {
        var cards = new AdaptiveGrid(300, 3, 16);
        foreach (var p in DeviceClasses.Patterns)
        {
            var row = DeviceClasses.PatternRow(p, device);
            string demoId = p.DemoId;
            var run = Id(Secondary(DeviceClasses.PatternRunLabel), $"DeviceClassPattern_{demoId}");
            run.Click += async (_, _) => await OpenDeviceClassDemoAsync(demoId);
            cards.With(Id(CardBorder(Stack(8,
                Text(p.Industry.ToUpperInvariant(), 11, Muted, FontWeights.SemiBold),
                H3(p.Pattern),
                Body(DeviceClasses.PatternPrefix + p.InRetail, Ink),
                Id(Small(DeviceClasses.PatternClassPrefix + (row?.SuggestedClass ?? DeviceClasses.BudgetUnknown), Ink), $"DeviceClassPatternClass_{demoId}"),
                Small(DeviceClasses.PatternWorkloadPrefix + (row is null ? DeviceClasses.BudgetUnknown : $"{row.Workload.Name} ({row.Workload.Size})")),
                run), 20), $"DeviceClassPatternCard_{demoId}"));
        }
        return Id(Stack(14, Stack(6, H2(DeviceClasses.PatternsTitle), Body(DeviceClasses.PatternsSubtitle)), cards), "DeviceClassPatterns");
    }

    private FrameworkElement DeviceClassFact(DeviceClassText fact, string linkId)
    {
        var body = Stack(2, Body(fact.Text, Ink));
        if (fact.Source is { } source) body.Children.Add(DeviceClassLink(source, linkId));
        return body;
    }

    /// <summary>Opens only allow-listed Microsoft URLs; the URL is also the link's tooltip and help text.</summary>
    private HyperlinkButton DeviceClassLink(DeviceClassSource source, string id)
    {
        var link = Id(new HyperlinkButton { Content = source.Label + "  \u2197", Padding = new Thickness(0, 2, 0, 2), Foreground = Accent }, id);
        Microsoft.UI.Xaml.Automation.AutomationProperties.SetHelpText(link, source.Url);
        ToolTipService.SetToolTip(link, source.Url);
        link.Click += async (_, _) =>
        {
            if (ApprovedLinks.IsApproved(source.Url)) await Windows.System.Launcher.LaunchUriAsync(new Uri(source.Url));
        };
        _deviceClassLinks.Add((link, source.Url));
        return link;
    }

    private static Border DeviceClassBand(Brush brush) => new() { Height = 6, CornerRadius = new CornerRadius(3), Background = brush };

    private static Border DeviceClassFitCell(string label, SalesFit fit, string id, out TextBlock value)
    {
        var (background, foreground) = DeviceClassFitColors(fit);
        return DeviceClassCell(label, SalesSizing.FitLabel(fit), background, foreground, id, out value);
    }

    private static Border DeviceClassCell(string label, string text, Brush background, Brush foreground, string id, out TextBlock value)
    {
        value = Id(Text(text, 14, foreground, FontWeights.SemiBold), id);
        return CardBorder(Stack(2, Text(label, 11, Muted, FontWeights.SemiBold), value), 10, background);
    }

    private static (Brush Background, Brush Foreground) DeviceClassFitColors(SalesFit fit) => fit switch
    {
        SalesFit.Comfortable => (GreenTint, GreenInk),
        SalesFit.Tight => (AmberTint, AmberInk),
        SalesFit.WontFit => (AccentTint, AccentDeep),
        _ => (Sand, Muted),
    };

    /// <summary>Opens the demo runner only; the presenter starts the run there.</summary>
    private async Task OpenDeviceClassDemoAsync(string demoId)
    {
        if (_demoCatalog.Find(demoId) is null) await RefreshDemoCatalogAsync();
        if (!OpenDemo(demoId))
            ShowServiceError("Live demo unavailable", _demoCatalogError ?? "The local service has not provided this demo. Check the service and try again.");
    }

    /// <summary>The "This laptop" column and the budget line follow the live GPU memory budget from the driver.</summary>
    private void ApplyDeviceClassesStatus(StatusSnapshot status)
    {
        string budget = DeviceClasses.BudgetLine(status.Device);
        if (_deviceClassBudget.Text != budget) _deviceClassBudget.Text = budget;
        foreach (var workload in SalesSizing.Workloads)
        {
            if (!_deviceClassHere.TryGetValue(workload.Id, out var here)) continue;
            var fit = DeviceClasses.Row(workload, status.Device).ThisLaptop.Fit;
            string label = SalesSizing.FitLabel(fit);
            if (here.Fit.Text == label) continue;
            var (background, foreground) = DeviceClassFitColors(fit);
            here.Fit.Text = label;
            here.Fit.Foreground = foreground;
            here.Cell.Background = background;
        }
    }
}
