using Microsoft.UI.Text;
using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;
using System.Text.Json;
using static HybridIntelligenceRetail.Ui;

namespace HybridIntelligenceRetail;

// Three-tier illustrative reference architecture for retail teams, with each tier proved by an existing live demo.
internal sealed partial class MainWindow
{
    private FrameworkElement BuildArchitecture()
    {
        var tier1 = TierCard("Tier 1", "Smart capture", "Store manager's or field technician's Surface on the store visit or operations call",
            ["Capture the conversation with consent", "Transcribe locally", "Draft notes on the device", "Sync securely inside the company"],
            "Run operations call capture", "ArchTier1", () => { if (!OpenDemo("meeting")) ShowServiceError("Live demo unavailable", _demoCatalogError ?? "The local service has not provided this demo."); },
            Card, Accent);
        var tier2 = TierCard("Tier 2", "In-company drafting", "Local AI beside the company's store operations and service desk systems (illustrative)",
            ["Apply store and IT procedures", "Draft store visit follow-ups and incident updates", "Keep customer, associate and store data inside the company"],
            "Draft a store visit follow-up", "ArchTier2", () => _ = LaunchIndustryAsync("store-visit"),
            Card, Accent);
        var escalate = TierCard("Escalate only when needed", "Algorithmic delegation", "Runs inside the company",
            ["Remove customer, associate, asset and ticket identifiers (names, emails, employee ids, asset tags, ticket numbers)", "Minimize context", "Route by rule, with every reason shown"],
            "Route a complex question", "ArchEscalate", () => OpenArchitecturePreset("complex-case"),
            AmberTint, AmberInk);
        var tier3 = TierCard("Tier 3  |  External cloud", "Cloud support", "Azure OpenAI frontier reasoning for complex questions",
            ["Receives de-identified queries only", "Returns model support", "Never sees recordings, customer or associate personal data, or store, device and ticket details"],
            "Preview the cloud payload", "ArchTier3", () => { if (!OpenDemo("redact")) ShowServiceError("Live demo unavailable", _demoCatalogError ?? "The local service has not provided this demo."); },
            SlateTint, Slate);

        var flow = Id(CardBorder(Stack(8,
            Set(Text("FLOW", 12, Accent, FontWeights.SemiBold), t => t.CharacterSpacing = 80),
            Body("Store visit or operations call  \u2192  Tier 1 capture and local transcript  \u2192  Tier 2 drafting against store and IT procedures  \u2192  draft notes + store visit follow-ups  \u2192  store operations, store technology and service desk review and approval.", Ink),
            Body("Only when a question is complex: remove customer, associate, asset and ticket identifiers (names, emails, employee ids, asset tags, ticket numbers) and minimize context  \u2192  de-identified query to Tier 3  \u2192  model support returns to Tier 2. Every decision, approval and technical judgement stays with the company's people.", Ink)), 18), "ArchFlow");

        var review = Id(CardBorder(Lead(12, Glyph("\uE8FB", 22, GreenInk), Stack(6,
            Set(H3("Draft notes + follow-ups  \u2192  team lead review and approval"), t => t.Foreground = GreenInk),
            Body("AI drafts; people decide. Drafts never approve or deploy a change or update, close or reassign tickets, change device policies, determine a root cause, issue a refund or credit, place an order, transfer or allocation, or make HR, vendor, purchasing, pricing or supplier decisions, and nothing is sent to customers, associates, stores, vendors or stakeholders without review by store operations, merchandising, allocation, customer care, store technology, the service desk or the incident manager.", Ink))), 18, GreenTint), "ArchReview");

        var sensitive = Id(CardBorder(Lead(12, Glyph("\uE72E", 22, AccentDeep), Stack(6,
            H3("Customer, associate and store data stay in the company"),
            Body("Recordings, customer and associate personal data, store performance figures, device and ticket details and unreleased product information remain inside the company. Only de-identified queries go out; only model support comes back.", Ink))), 18, AccentTint), "ArchSensitive");

        var mapping = Id(Small("Illustrative reference architecture, not any company's actual design. In this showcase the Surface Laptop Ultra stands in for Tier 1 capture and Tier 2 local AI, using synthetic data only. "
            + "Tier 3 is shown as a NOT SENT payload preview: the studio never calls a cloud service, and it does not connect to point-of-sale, order management, endpoint management, a service desk (ITSM) system, an HR system or any system of record. "
            + "De-identification removes structured identifiers only; it is not certified and makes no privacy, regulatory or compliance determination. Drafts only; nothing is deployed, changed or sent."), "ArchMapping");

        return Id(Stack(14,
            Eyebrow("Reference architecture  |  Hybrid AI for retail"),
            H2("Three tiers. Customer and store data stay in the company. The cloud only when needed."),
            new AdaptiveGrid(250, 4).With(tier1, tier2, escalate, tier3),
            flow,
            new AdaptiveGrid(320, 2).With(review, sensitive),
            mapping), "OverviewArchitecture");
    }

    private Border TierCard(string tier, string title, string where, string[] points, string action, string id, Action onClick,
        Microsoft.UI.Xaml.Media.SolidColorBrush background, Microsoft.UI.Xaml.Media.SolidColorBrush ink)
    {
        var go = Id(Secondary(action + "  \u2192"), id + "Run");
        go.HorizontalAlignment = HorizontalAlignment.Left;
        go.Click += (_, _) => onClick();
        var list = Stack(4);
        foreach (string point in points) list.Children.Add(Body("- " + point, Ink));
        return Id(CardBorder(Stack(8,
            Set(Text(tier.ToUpperInvariant(), 12, ink, FontWeights.SemiBold), t => t.CharacterSpacing = 80),
            H3(title), Small(where), list, go), 20, background), id);
    }

    private void OpenArchitecturePreset(string presetId)
    {
        Navigate("hybrid");
        if (_hybridCatalog is { } catalog && Items(catalog, "presets").FirstOrDefault(p => Str(p, "id") == presetId) is { ValueKind: JsonValueKind.Object } preset)
            _ = ApplyHybridPresetAsync(preset);
    }
}
