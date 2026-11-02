"""Live demo registry: synthetic fixtures, pipelines, authored rehearsal output and ground-truth checks.

Every fixture is fictional. Speech and document images are rendered on this laptop at runtime from the text
below, so the text is also the ground truth the live checks compare against. Checks only ever run on live output.
"""
import itertools
import re

import media
from content import SCENARIOS

# ---------------------------------------------------------------- speech fixtures (rendered by Windows TTS)
MEETING_SEGMENTS = (
    ("female", "Thanks for joining, Marcus. This is Ana, the store operations manager, and Priya, our service desk manager, is on the line too. With your consent, I am recording this call for our notes."),
    ("male", "That is fine. The back-office laptop refresh pilot covers 12 stores, and it must finish before the holiday change freeze."),
    ("female", "Priya will send you the store list and the training guide by Friday. We have not booked a change advisory board slot yet."),
    ("male", "My desktop engineering team will prepare the device images for the pilot. We did not agree a date for that."),
    ("female", "We also agreed that someone should brief the store managers, but nobody owns that yet."),
    ("male", "One more thing. We might add the distribution centers next year, but that is only an idea for now."),
    ("female", "Understood. That question stays open. I will send these notes to everyone this afternoon. Thank you."),
)
MEMO_SEGMENTS = (
    ("male", "End of shift note for the Contoso Apparel service desk from the shift supervisor at distribution "
             "center two. Location is dock three. Handheld scanners in bay H seventeen failed to sync from 05:30 "
             "to 06:15 this morning."),
    ("male", "They show error code forty, and the shift lead restarted them twice. Please open a priority two "
             "ticket and request the access point log from the network team. I am on shift until three this "
             "afternoon."),
)

def script_text(segments):
    return " ".join(text for _, text in segments)


# ---------------------------------------------------------------- document images (rendered by System.Drawing)
SERVICE_FORM = {
    "form_id": "SF-0738", "store": "STORE-0412", "device": "VanArsdel TP-40 receipt printer",
    "asset_tag": "ASSET-52914", "reported_at": "14:00", "fault": "Register 3 prints blank receipts",
    "reported_by": "Sam Okafor", "technician": "J. Alvarez",
    "notes": "Paper roll was loaded upside down. Reloaded it and printed a test receipt.",
    "status": "Resolved",
}
SERVICE_FORM_CHECK = {"form_id": "SF-0738", "store": "0412", "device": "TP-40", "asset_tag": "52914",
                      "reported_at": "14:00", "fault": "blank", "reported_by": "Okafor",
                      "technician": "Alvarez", "notes": "test receipt", "status": "Resolved"}
RECEIPT_ITEMS = (("Thermal paper rolls (10)", "42.00"), ("Barcode labels (2 packs)", "26.00"),
                 ("Print head cleaning kit", "18.40"))
RECEIPT = {"merchant": "VanArsdel Store Supply", "date": "14 Oct 2026", "order_number": "2291",
           "subtotal": "86.40", "tax": "7.13", "total": "93.53", "card_last4": "4417"}
RECEIPT_CHECK = {"merchant": "VanArsdel", "date": "14 Oct 2026", "order_number": "2291", "subtotal": "86.40",
                 "tax": "7.13", "total": "93.53", "card_last4": "4417"}

MEDIA_SPEC = {
    "files": [
        {"name": "meeting.wav", "kind": "speech", "rate": 16000,
         "segments": [{"voice": v, "text": t, "pause_ms": 550} for v, t in MEETING_SEGMENTS]},
        {"name": "voice-memo.wav", "kind": "speech", "rate": 16000,
         "segments": [{"voice": v, "text": t, "pause_ms": 300} for v, t in MEMO_SEGMENTS]},
        {"name": "work-order.png", "kind": "form", "width": 1100, "height": 900, "rotate": -1.2,
         "title": "STORE DEVICE SERVICE FORM",
         "subtitle": "Contoso Apparel  |  Store IT  |  Fictional form",
         "rows": [
             {"label": "Form ID", "value": SERVICE_FORM["form_id"]},
             {"label": "Store", "value": SERVICE_FORM["store"]},
             {"label": "Device", "value": SERVICE_FORM["device"]},
             {"label": "Asset tag", "value": SERVICE_FORM["asset_tag"]},
             {"label": "Reported at", "value": SERVICE_FORM["reported_at"], "hand": True},
             {"label": "Fault", "value": SERVICE_FORM["fault"], "hand": True},
             {"label": "Reported by", "value": SERVICE_FORM["reported_by"], "hand": True},
             {"label": "Technician", "value": SERVICE_FORM["technician"], "hand": True},
             {"label": "Notes", "value": SERVICE_FORM["notes"], "hand": True, "wide": True},
             {"label": "Status", "value": SERVICE_FORM["status"]},
         ],
         "footer": "FICTIONAL FORM  |  Synthetic data for a local AI demonstration  |  No real company"},
        {"name": "receipt.png", "kind": "receipt", "width": 620, "height": 640, "rotate": 1.5,
         "merchant": "VANARSDEL STORE SUPPLY",
         "header": ["77 Market Street, Port Ellis", "Tel 555-0163", "14 Oct 2026   12:47", "Order #2291"],
         "lines": [{"left": d, "right": a} for d, a in RECEIPT_ITEMS] + [
             {"left": "---"}, {"left": "Subtotal", "right": "86.40"}, {"left": "Tax 8.25%", "right": "7.13"},
             {"left": "TOTAL", "right": "93.53", "bold": True}, {"left": "---"},
             {"left": "Paid: Corporate card", "right": "**** 4417"}],
         "footer": ["Thank you!", "FICTIONAL RECEIPT FOR DEMONSTRATION"]},
    ]
}
MEDIA_NAMES = tuple(item["name"] for item in MEDIA_SPEC["files"])

# ---------------------------------------------------------------- text fixtures
NOTICE = (
    "FICTIONAL NOTICE | Contoso Apparel\n"
    "Planned maintenance on the back-office systems in your store will take place on Tuesday 20 October 2026, "
    "from 14:00 to 16:00. During this window, stockroom PCs cannot print shipping labels, but registers and card "
    "payments are not affected. If you have an urgent issue, contact the service desk and quote store reference "
    "STORE-0412. We apologise for the inconvenience and thank you for your patience."
)
PROTECTED_TERMS = ("Contoso Apparel", "STORE-0412", "14:00", "16:00")
LANGUAGES = (("es", "Spanish"), ("fr", "French"), ("de", "German"), ("pt-BR", "Brazilian Portuguese"),
             ("ja", "Japanese"))

POLICIES = (
    ("POL-01", "Device refresh cycle", "Headquarters PCs and store back-office PCs are refreshed every four years, "
     "and store handheld scanners every five years. Desktop engineering plans each refresh by store and region, "
     "and pilots come first."),
    ("POL-02", "Standard builds", "Every PC uses one of three standard builds: store, headquarters or distribution "
     "center. Exceptions need written approval from the desktop engineering lead and are reviewed every year."),
    ("POL-03", "Lost or stolen devices", "Report a lost or stolen laptop, tablet or phone used for company work "
     "to the IT Security Operations desk within one hour of noticing, on extension 4400 or "
     "security@contoso.example. Do not delay the report to keep searching. IT will remotely lock and wipe the "
     "device."),
    ("POL-04", "Change approval", "Submit a change request at least five business days before any change to store "
     "systems or devices. The change advisory board (CAB) meets weekly to approve changes. Emergency changes need "
     "the incident manager's approval and a CAB review on the next business day."),
    ("POL-05", "Holiday change freeze", "No changes to registers, receipt printers, store networks or back-office "
     "PCs are made from 16 November 2026 to 4 January 2027. During the freeze, only emergency changes approved by "
     "the incident manager go ahead. Pilots must finish before the freeze starts."),
    ("POL-06", "Software requests", "Request new software through the IT service portal. Information security, "
     "privacy and change-management review takes up to ten business days. AI tools must be approved before use "
     "with associate personal data or unreleased product information."),
    ("POL-07", "Remote access", "Use the Lucerne VPN for all internal systems when away from a company site. "
     "Back-office PCs connect only to the store network, never to guest Wi-Fi."),
    ("POL-08", "Data retention", "Service desk tickets are kept for three years after they are closed. Call "
     "recordings and transcripts are deleted after 90 days unless the Legal department places them on legal hold."),
    ("POL-09", "Store equipment", "Registers, receipt printers and handheld scanners belong to the store. Report a "
     "fault through the service desk with the asset tag and register number. Do not move equipment between stores "
     "without approval from store operations."),
    ("POL-10", "Purchasing", "Peripheral purchases up to 2,500 dollars need one budget manager approval. Larger "
     "purchases need quotes from two suppliers and procurement approval."),
    ("POL-11", "Training", "Each employee has 24 hours of paid professional development per year. "
     "Information security and privacy training is mandatory every 12 months for anyone with access to "
     "associate personal data."),
    ("POL-12", "Service desk priorities", "An incident that stops store sales is priority one, with a call back "
     "within 15 minutes. Equipment requests go through the IT service portal and are answered within one business "
     "day."),
)
DOCS_QUESTION = "I think I left my work laptop on the commuter train. What should I do, and how fast?"
DOCS_EXPECTED = "POL-03"
QUERY_INSTRUCTION = "Instruct: Given a staff question, retrieve the company policy that answers it\nQuery: "

EMAIL_OFFICE = "Contoso Apparel service desk team"
EMAIL = (
    "FICTIONAL EMAIL\n"
    "From: Dana Whitfield <dana.whitfield@example.com>\n"
    f"To: {EMAIL_OFFICE}\n"
    "Subject: Laptop and phone for my first day\n\n"
    "Hello, I start at Contoso Apparel as a field technician next month. Please ship my new laptop and phone to my "
    "home address, 1847 Lakeview Terrace, Port Ellis, PE4 7QT. My employee ID is EMP-318274 and my date of birth is "
    "3 March 1984 if you need to verify me. You can reach me on 555-0187 after six. My hiring manager Marcus Lee "
    "(marcus.lee@example.com) is copied on this request.\n"
    "Thanks, Dana"
)
IDENTIFIERS = (
    ("Name: Dana Whitfield", (r"\bDana\b", r"\bWhitfield\b")),
    ("Email: dana.whitfield@example.com", (r"dana\.whitfield",)),
    ("Street address", (r"\b1847\b", r"\bLakeview\b")),
    ("Postcode", (r"\bPE4\b", r"\b7QT\b")),
    ("Employee ID", (r"\b318274\b",)),
    ("Date of birth", (r"\b1984\b",)),
    ("Phone number", (r"\b0187\b",)),
    ("Name: Marcus Lee", (r"\bMarcus\b",)),
    ("Email: marcus.lee@example.com", (r"marcus\.lee",)),
)

INBOX = (
    ("E1", "Store Wi-Fi down", "The stockroom at Store 0412 has had no Wi-Fi since 07:10, and the store opens at "
     "09:00. Please help urgently.", "incident"),
    ("E2", "New store manager laptop", "Can we order a laptop and headset for a new store manager starting on "
     "2 November?", "request"),
    ("E3", "Invoice INV-7302 query", "Our October invoice shows 140 Relecloud Scheduler licences but we only use "
     "120. Please check.", "billing"),
    ("E4", "Thank you", "The technician who fixed the register display before yesterday's store opening was "
     "excellent. Just wanted to say thanks.", "feedback"),
    ("E5", "You have won a gift card", "Click this link within 24 hours to claim your prize.", "spam"),
    ("E6", "VPN keeps dropping", "Three merchandisers at headquarters cannot stay connected to the Lucerne VPN "
     "today; they can work offline for now.", "incident"),
)
CATEGORIES = ("incident", "request", "billing", "feedback", "spam")

STORES = ("Atlas", "Birch", "Cedar", "Delta", "Harbor")
PUZZLE = (
    "Plan a five-week back-office laptop refresh pilot, one store per week, for the stores Atlas, Birch, Cedar, "
    "Delta and Harbor. Constraints: (1) Delta needs a network upgrade that finishes at the end of week 2, so Delta "
    "cannot be before week 3. (2) Harbor must be in the week immediately after Cedar. (3) Atlas cannot be in week 1 "
    "or week 5. (4) Birch must come before Atlas. (5) Delta cannot be in week 5 because the holiday change freeze "
    "for flagship stores starts that week, and Delta is the only flagship store. (6) Cedar cannot be in week 1. "
    "Find the only schedule that satisfies every constraint. Explain the key deductions in at most five short "
    "bullets, then finish with one line exactly in this format: ORDER: store, store, store, store, store"
)
PUZZLE_SYSTEM = ("You solve scheduling puzzles carefully and concisely. Use only the stated constraints. "
                 "Keep the explanation under 120 words and always end with the ORDER line.")
# GPT-OSS samples at temperature 1.0 and its hidden reasoning shares this cap; 3,072 occasionally ran out before
# the visible answer. Typical runs finish far below this, so the cap only bounds the worst case.
REASONING_BUDGET = 6144


def schedule_violations(order):
    """Which of the six puzzle constraints a proposed week-by-week order breaks (empty list = valid)."""
    if sorted(order) != sorted(STORES):
        return ["Not a schedule of the five stores, each exactly once"]
    week = {store: index + 1 for index, store in enumerate(order)}
    rules = (
        ("(1) Delta not before week 3", week["Delta"] >= 3),
        ("(2) Harbor immediately after Cedar", week["Harbor"] == week["Cedar"] + 1),
        ("(3) Atlas not in week 1 or 5", week["Atlas"] not in (1, 5)),
        ("(4) Birch before Atlas", week["Birch"] < week["Atlas"]),
        ("(5) Delta not in week 5", week["Delta"] != 5),
        ("(6) Cedar not in week 1", week["Cedar"] != 1),
    )
    return [name for name, ok in rules if not ok]


def valid_schedules():
    return [order for order in itertools.permutations(STORES) if not schedule_violations(order)]


def parse_order(text):
    lines = [line for line in text.splitlines() if re.match(r"\s*\**\s*ORDER\s*:", line, re.IGNORECASE)]
    if not lines:
        return None
    names = re.findall(r"[A-Za-z]+", lines[-1].split(":", 1)[1])
    found = [name.capitalize() for name in names if name.capitalize() in STORES]
    return found or None


# ---------------------------------------------------------------- registry
def _step(title, role):
    return {"title": title, "role": role}


DEMOS = {
    "meeting": {
        "title": "Store operations and IT call to notes and actions", "category": "Listen", "glyph": "\uE720", "workload": "transcription",
        "pitch": "Tier 1 and Tier 2 on one PC: a recorded store operations and IT call becomes meeting notes and an action list without leaving the laptop.",
        "proof": "Speech recognition and drafting both run on the RTX GPU; word accuracy is measured against the script.",
        "input": {"kind": "audio", "media": "meeting.wav",
                  "label": "Synthetic two-voice store operations and IT call recorded with Windows text-to-speech"},
        "source": script_text(MEETING_SEGMENTS),
        "prompt": ("Turn this store operations and IT call transcript into meeting notes with three sections: "
                   "Summary (two sentences), Actions (a table with columns Action, Owner, Due), and Open decisions. "
                   "Use only what was said. Write 'Not assigned' or 'Not agreed' when an owner or date is missing."),
        "system": ("You write concise, factual meeting notes from a machine transcript of a store operations and IT "
                   "call. Do not invent owners, dates, approvals, costs or commitments, and do not make technical or "
                   "change approval decisions. An idea is not an approved action. Keep it under 170 words. The store "
                   "operations manager must review the notes before they are sent or filed."),
        "max_tokens": 700,
        "steps": [_step("Transcribe the call (Tier 1)", "asr"), _step("Draft meeting notes and actions (Tier 2)", "chat")],
        "rehearsal": [script_text(MEETING_SEGMENTS), (
            "Summary\nThe back-office laptop refresh pilot covers 12 stores and must finish before the holiday change "
            "freeze; no change advisory board slot has been booked yet. Adding the distribution centers next year was "
            "mentioned as an idea only; nothing was decided.\n\n"
            "Actions\nAction | Owner | Due\n"
            "Send the store list and the training guide | Priya (service desk manager) | Friday\n"
            "Prepare the device images for the pilot | Marcus (desktop engineering team) | Not agreed\n"
            "Brief the store managers | Not assigned | Not agreed\n"
            "Send the meeting notes | Ana (store operations manager) | This afternoon\n\n"
            "Open decisions\nWhether to add the distribution centers next year.\n\n"
            "Store operations manager review required before the notes are sent.")],
    },
    "voice-memo": {
        "title": "Voice memo to a shift handoff note", "category": "Listen", "glyph": "\uE707", "workload": "field",
        "pitch": "A distribution center shift supervisor talks at the end of a shift; a structured handoff ticket comes back, ready for a person to check.",
        "proof": "Speech to text, then text to structured fields, on the GPU; fields are checked against the memo.",
        "input": {"kind": "audio", "media": "voice-memo.wav",
                  "label": "Synthetic shift supervisor voice memo recorded with Windows text-to-speech"},
        "source": script_text(MEMO_SEGMENTS),
        "prompt": ("Convert this voice memo transcript into a shift handoff ticket. Return only one JSON object "
                   "with the keys team, location, asset, issue, actions_taken, error_code, priority, "
                   "documents_requested and available_until. Use null when the memo does not say."),
        "system": ("You turn shift handoff voice memos into structured service desk tickets. Use only what the "
                   "transcript says. Do not invent ticket numbers, causes, costs or fixes. Return JSON only."),
        "max_tokens": 400,
        "steps": [_step("Transcribe the voice memo", "asr"), _step("Structure the handoff ticket", "chat")],
        "rehearsal": [script_text(MEMO_SEGMENTS), (
            '{\n  "team": "Contoso Apparel service desk",\n  "location": "Dock 3, distribution center 2",\n'
            '  "asset": "Handheld scanners in bay H-17",\n'
            '  "issue": "Failed to sync from 05:30 to 06:15 this morning",\n'
            '  "actions_taken": "Shift lead restarted them twice",\n  "error_code": "40",\n  "priority": "P2",\n'
            '  "documents_requested": "Access point log from the network team",\n'
            '  "available_until": "Three this afternoon"\n}')],
        "check_fields": {"team": "service desk", "location": "dock 3", "asset": "H17",
                         "actions_taken": "restarted", "error_code": "40", "priority": "2",
                         "documents_requested": "access point"},
    },
    "translate": {
        "title": "Translate on the device", "category": "Write", "glyph": "\uF2B7", "workload": "translation",
        "pitch": "Store IT notices translated locally, keeping names, references and times intact.",
        "proof": "Runs on the selected local model; protected terms are checked automatically, meaning needs a fluent reviewer.",
        "input": {"kind": "text", "label": "Synthetic store IT notice"},
        "source": NOTICE,
        "prompt": ("Translate the notice into {language}. Keep the company name Contoso Apparel in English, the "
                   "store reference STORE-0412 and the times 14:00 and 16:00 exactly as written. Return only the "
                   "translation."),
        "system": ("You are a professional translator running locally. Translate faithfully and naturally. "
                   "Do not add or remove information. Never translate brand names. Keep names, references, numbers "
                   "and 24-hour times unchanged."),
        "max_tokens": 600,
        "options": [{"id": code, "label": name} for code, name in LANGUAGES],
        "option_label": "Target language",
        "steps": [_step("Translate", "chat")],
        "rehearsal": [(
            "AVISO FICTICIO | Contoso Apparel\n"
            "El mantenimiento programado de los sistemas administrativos de su tienda se realizará el martes 20 de "
            "octubre de 2026, de 14:00 a 16:00. Durante este periodo, los PC del almacén no podrán imprimir etiquetas "
            "de envío, pero las cajas registradoras y los pagos con tarjeta no se verán afectados. Si tiene un "
            "problema urgente, póngase en contacto con la mesa de servicio de TI e indique la referencia de tienda "
            "STORE-0412. Disculpe las molestias y gracias por su paciencia.")],
    },
    "brief": {
        "title": "Executive brief from notes", "category": "Write", "glyph": "\uE70F", "workload": "writing",
        "pitch": "Discovery notes become a cited agenda for retail operations and IT leaders, on the laptop. The same pattern fits a CAB pre-read before the holiday change freeze.",
        "proof": "Every point must cite its source note; the required no-benefit-claimed sentence is checked.",
        "input": {"kind": "text", "label": "Synthetic company notes (three sources)"},
        "source": SCENARIOS["brief"]["source"], "prompt": SCENARIOS["brief"]["prompt"],
        "system": SCENARIOS["brief"]["system"], "max_tokens": 650,
        "steps": [_step("Draft the brief", "chat")],
        "rehearsal": [SCENARIOS["brief"]["rehearsal"]],
    },
    "redact": {
        "title": "De-identify before escalating (Tier 3)", "category": "Protect", "glyph": "\uE72E", "workload": "writing",
        "pitch": "Before a complex question escalates to the cloud, associate identifiers are stripped inside the company; only the de-identified text would leave.",
        "proof": "Counts how many of the nine known synthetic identifiers survive. This demo sends nothing anywhere.",
        "input": {"kind": "text", "label": "Synthetic new-hire device request with personal data"},
        "source": EMAIL,
        "prompt": ("Redact every personal identifier in this email so it can be shared with a cloud service. Swap "
                   "each one for a typed placeholder: [NAME], [EMAIL], [PHONE], [ADDRESS], [POSTCODE], [ID] or "
                   "[DATE_OF_BIRTH]. Keep all other wording unchanged. Return only the redacted email."),
        "system": ("You are a privacy filter running locally. Use placeholders in place of personal identifiers "
                   "(people's names, email addresses, phone numbers, street addresses, postcodes, employee IDs, dates "
                   "of birth). Company names and office wording stay. Never echo an identifier."),
        "max_tokens": 450,
        "steps": [_step("Redact personal data", "chat")],
        "rehearsal": [(
            "FICTIONAL EMAIL\nFrom: [NAME] <[EMAIL]>\nTo: Contoso Apparel service desk team\n"
            "Subject: Laptop and phone for my first day\n\n"
            "Hello, I start at Contoso Apparel as a field technician next month. Please ship my new laptop and phone "
            "to my home address, [ADDRESS], Port Ellis, [POSTCODE]. My employee ID is [ID] and my date of birth is "
            "[DATE_OF_BIRTH] if you need to verify me. You can reach me on [PHONE] after six. My hiring manager "
            "[NAME] ([EMAIL]) is copied on this request.\nThanks, [NAME]")],
    },
    "triage": {
        "title": "Inbox triage to structured data", "category": "Write", "glyph": "\uE715", "workload": "writing",
        "pitch": "A morning's service desk inbox sorted into incidents, requests and noise, as data a workflow can use.",
        "proof": "Output must be valid JSON; categories are compared with the fixture's labels.",
        "input": {"kind": "text", "label": "Six synthetic emails"},
        "source": "FICTIONAL INBOX\n" + "\n".join(f"[{i}] Subject: {s}. {b}" for i, s, b, _ in INBOX),
        "prompt": ("Triage these six emails. Return only a JSON array with one object per email, using the keys id, "
                   "category, urgency and next_step. category must be one of incident, request, billing, feedback or "
                   "spam. urgency must be high, medium or low. next_step is one short sentence."),
        "system": ("You triage an IT service desk inbox. Classify each email from its text only. Do not reply to anyone, "
                   "click links or invent details. Return JSON only."),
        "max_tokens": 600,
        "steps": [_step("Triage the inbox", "chat")],
        "rehearsal": ['[\n' + ",\n".join(
            f'  {{"id": "{i}", "category": "{c}", "urgency": "{u}", "next_step": "{n}"}}' for i, c, u, n in (
                ("E1", "incident", "high", "Dispatch network support to the Store 0412 stockroom before 09:00."),
                ("E2", "request", "medium", "Raise a hardware order for the new store manager."),
                ("E3", "billing", "medium", "Ask billing to reconcile the licence count on INV-7302."),
                ("E4", "feedback", "low", "Share the thanks with the technician's manager."),
                ("E5", "spam", "low", "Report as phishing and delete; do not click the link."),
                ("E6", "incident", "medium", "Open a network ticket for the Lucerne VPN drops."))) + "\n]"],
    },
    "ask-docs": {
        "title": "Ask your documents", "category": "Know", "glyph": "\uE8A5", "workload": "documents",
        "pitch": "Questions answered from a synthetic end user device standard and change policy, with citations, on the laptop.",
        "proof": "GPU embeddings find the right policy (checked), then the local model answers only from it.",
        "input": {"kind": "text", "label": "Twelve synthetic device and change policies"},
        "source": "\n".join(f"[{pid}] {title}: {text}" for pid, title, text in POLICIES),
        "prompt": DOCS_QUESTION, "prompt_label": "Question",
        "system": ("Answer the staff member's question only from the supplied policy excerpts. Cite the policy ID in "
                   "square brackets after each fact, for example [POL-03]. If the excerpts do not answer the "
                   "question, say so. Keep it under 90 words."),
        "max_tokens": 300,
        "steps": [_step("Search the documents", "embed"), _step("Answer with citations", "chat")],
        "rehearsal": [
            "1. POL-03 Lost or stolen devices\n2. POL-07 Remote access\n3. POL-09 Store equipment",
            ("Report the lost laptop to the IT Security Operations desk within one hour of noticing, on extension "
             "4400 or security@contoso.example [POL-03]. Do not delay the report to keep searching; IT will "
             "remotely lock and wipe the device [POL-03].")],
    },
    "vision": {
        "title": "Scanned form to structured data", "category": "See", "glyph": "\uE722", "workload": "vision",
        "pitch": "Photos of forms and receipts read on the laptop, including handwriting, into data a system can use.",
        "proof": "A vision-language model runs on the RTX GPU; every field is compared with the synthetic document.",
        "input": {"kind": "image", "label": "Synthetic scanned document rendered on this laptop"},
        "source": "", "prompt": "", "max_tokens": 450,
        "options": [{"id": "work-order", "label": "Store device service form (handwritten fields)"},
                    {"id": "receipt", "label": "Store supply receipt"}],
        "option_label": "Document",
        "documents": {
            "work-order": {"media": "work-order.png", "check": SERVICE_FORM_CHECK, "prompt": (
                "Extract the fields from this scanned store device service form as one JSON object with exactly "
                "these keys: form_id, store, device, asset_tag, reported_at, fault, reported_by, technician, notes, "
                "status. Copy each value exactly as printed or handwritten. Use null for a missing value. Return "
                "only JSON.")},
            "receipt": {"media": "receipt.png", "check": RECEIPT_CHECK, "prompt": (
                "Extract this receipt as one JSON object with exactly these keys: merchant, date, order_number, "
                "line_items (a list of objects with description and amount), subtotal, tax, total, card_last4. "
                "Copy values exactly as printed. Return only JSON.")},
        },
        "system": "You extract data from document images accurately. Never guess unreadable values; use null.",
        "steps": [_step("Read the document", "vision")],
        "rehearsal_options": {
            "work-order": ['{\n' + ",\n".join(f'  "{k}": "{v}"' for k, v in SERVICE_FORM.items()) + "\n}"],
            "receipt": ['{\n  "merchant": "VanArsdel Store Supply",\n  "date": "14 Oct 2026",\n'
                        '  "order_number": "2291",\n  "line_items": [\n'
                        + ",\n".join(f'    {{"description": "{d}", "amount": "{a}"}}' for d, a in RECEIPT_ITEMS)
                        + '\n  ],\n  "subtotal": "86.40",\n  "tax": "7.13",\n  "total": "93.53",\n'
                        '  "card_last4": "4417"\n}'],
        },
    },
    "code": {
        "title": "Local coding assistant", "category": "Build", "glyph": "\uE943", "workload": "coding",
        "pitch": "A 14-billion-parameter coding model drafts and explains code with no source leaving the laptop.",
        "proof": "Runs on the RTX GPU. The code is displayed for review and is never executed by this app.",
        "input": {"kind": "text", "label": "Synthetic service desk requirement"},
        "source": SCENARIOS["code"]["source"], "prompt": SCENARIOS["code"]["prompt"],
        "system": SCENARIOS["code"]["system"], "max_tokens": 1600,
        "steps": [_step("Draft the code", "chat")],
        "rehearsal": [SCENARIOS["code"]["rehearsal"]],
    },
    "reasoning": {
        "title": "Plan it out with a reasoning model", "category": "Think", "glyph": "\uE82F", "workload": "reasoning",
        "pitch": "A 20-billion-parameter reasoning model works through a multi-constraint plan, locally.",
        "proof": "The engine checks the proposed schedule against all six constraints; exactly one schedule is valid.",
        "input": {"kind": "text", "label": "Synthetic store pilot constraints"},
        "source": "", "prompt": PUZZLE, "system": PUZZLE_SYSTEM, "max_tokens": REASONING_BUDGET, "model": "gpt-oss-20b",
        "steps": [_step("Reason through the plan", "gpt-oss-20b")],
        "rehearsal": [(
            "- Delta must be week 3 or 4, and Atlas week 2, 3 or 4.\n"
            "- Week 1 cannot be Delta, Atlas, Cedar or Harbor (Harbor follows Cedar), so Birch is week 1.\n"
            "- Cedar and Harbor need consecutive weeks: 2-3 and 3-4 leave no valid place for Delta.\n"
            "- So Cedar is week 4 and Harbor week 5; Delta takes week 3 and Atlas week 2.\n"
            "ORDER: Birch, Atlas, Delta, Cedar, Harbor")],
    },
    "faceoff": {
        "title": "Model face-off: 14B versus 20B", "category": "Scale", "glyph": "\uE9D5", "workload": "prototyping",
        "pitch": "Two large models, both resident on one laptop, answer the same question side by side.",
        "proof": "Both run on the RTX GPU with measured speed. The engine grades each answer against the puzzle's "
                 "single valid schedule, so you see which model got it right.",
        "input": {"kind": "text", "label": "Same prompt for both models"},
        "source": "", "prompt": PUZZLE, "system": PUZZLE_SYSTEM, "max_tokens": REASONING_BUDGET,
        "steps": [_step("Qwen2.5-Coder 14B answers", "qwen2.5-coder-14b"), _step("GPT-OSS 20B answers", "gpt-oss-20b")],
        "rehearsal": None,
    },
    "team": {
        "title": "Five models, one laptop", "category": "Scale", "glyph": "\uE950", "workload": "prototyping",
        "pitch": "Chat, reasoning, speech, vision and search models all resident at once, each doing real work, from a shift handoff memo to a store supply receipt.",
        "proof": "Each model runs a task; residency and GPU memory are read from Foundry Local and Windows counters.",
        "input": {"kind": "text", "label": "Measurement: no associate or device data"},
        "source": "", "prompt": "",
        "steps": [_step("Chat model", "qwen2.5-coder-14b"), _step("Reasoning model", "gpt-oss-20b"),
                  _step("Speech model", "asr"), _step("Vision model", "vision"), _step("Embedding model", "embed"),
                  _step("Measure residency and memory", "measure")],
        "rehearsal": None,
    },
}
ORDER = ("meeting", "voice-memo", "vision", "ask-docs", "translate", "brief", "redact", "triage", "code",
         "reasoning", "faceoff", "team")
assert set(ORDER) == set(DEMOS)


def option_ids(demo):
    return [option["id"] for option in demo.get("options", [])]


def default_option(demo):
    ids = option_ids(demo)
    return ids[0] if ids else None


def prompt_for(demo_id, option=None):
    demo = DEMOS[demo_id]
    if demo_id == "vision":
        return demo["documents"][option or default_option(demo)]["prompt"]
    if demo_id == "translate":
        language = dict(LANGUAGES)[option or default_option(demo)]
        return demo["prompt"].replace("{language}", language)
    return demo["prompt"]


def rehearsal_for(demo_id, option=None):
    demo = DEMOS[demo_id]
    if "rehearsal_options" in demo:
        return demo["rehearsal_options"][option or default_option(demo)]
    if demo_id == "translate" and (option or default_option(demo)) != default_option(demo):
        return None
    return demo.get("rehearsal")


def is_editable(demo_id):
    return demo_id != "team"


def has_rehearsal(demo_id, option=None):
    return rehearsal_for(demo_id, option) is not None


def media_for(demo_id, option=None):
    demo = DEMOS[demo_id]
    if demo_id == "vision":
        return demo["documents"][option or default_option(demo)]["media"]
    return demo["input"].get("media")


def public():
    """Registry as served to the apps; every option carries its own default prompt, media and rehearsal flag."""
    rows = []
    for demo_id in ORDER:
        demo = DEMOS[demo_id]
        row = {key: demo.get(key) for key in ("title", "category", "glyph", "workload", "pitch", "proof",
                                              "source", "option_label")}
        options = [{**option, "prompt": prompt_for(demo_id, option["id"]),
                    "media": media_for(demo_id, option["id"]), "rehearsal": has_rehearsal(demo_id, option["id"])}
                   for option in demo.get("options", [])]
        row.update(id=demo_id, input=dict(demo["input"], media=media_for(demo_id)), options=options,
                   prompt=prompt_for(demo_id), prompt_label=demo.get("prompt_label", "Instruction"),
                   editable=is_editable(demo_id), rehearsal=has_rehearsal(demo_id),
                   steps=[{"title": step["title"], "role": step["role"]} for step in demo["steps"]],
                   default_option=default_option(demo))
        rows.append(row)
    return rows


# ---------------------------------------------------------------- checks (live output only)
def check(label, value, passed, detail=""):
    return {"type": "check", "label": label, "value": value, "pass": passed, "detail": detail}


def transcript_check(segments, transcript):
    score = media.word_errors(script_text(segments), transcript)
    return check("Word accuracy vs the synthetic script", f"{score['accuracy'] * 100:.1f}%",
                 score["accuracy"] >= 0.9,
                 f"{score['errors']} word errors in {score['reference_words']} reference words "
                 "(substitutions, insertions and deletions).")


def fields_check(label, expected, text):
    try:
        data = media.extract_json(text)
    except ValueError:
        return [check("Valid JSON", "No", False, "The output did not contain a JSON object.")]
    if isinstance(data, list):
        data = data[0] if data and isinstance(data[0], dict) else {}
    matched = [key for key, want in expected.items() if media.field_matches(want, data.get(key))]
    missed = [key for key in expected if key not in matched]
    return [check("Valid JSON", "Yes", True),
            check(label, f"{len(matched)} of {len(expected)}", len(matched) == len(expected),
                  "Mismatched: " + ", ".join(missed) if missed else "Every checked field matches.")]


def receipt_sum_check(text):
    try:
        data = media.extract_json(text)
        items = data.get("line_items") if isinstance(data, dict) else None
        amounts = [media._number(item.get("amount")) for item in items or [] if isinstance(item, dict)]
        subtotal = media._number(data.get("subtotal"))
    except (ValueError, AttributeError):
        return check("Line items add up to the subtotal", "Not checked", False, "No readable line items.")
    if not amounts or None in amounts or subtotal is None:
        return check("Line items add up to the subtotal", "Not checked", False, "Amounts were missing or not numbers.")
    total = round(sum(amounts), 2)
    return check("Line items add up to the subtotal", f"{total:.2f} vs {subtotal:.2f}", abs(total - subtotal) < 0.005,
                 f"{len(amounts)} line items summed by the engine.")


def schedule_check(text):
    order = parse_order(text)
    if not order:
        return check("Schedule satisfies all six constraints", "No ORDER line", False,
                     "The answer did not end with an ORDER line the engine could read.")
    broken = schedule_violations(order)
    return check("Schedule satisfies all six constraints", "Yes" if not broken else f"{len(broken)} broken",
                 not broken, ", ".join(order) + ("" if not broken else " | Broken: " + "; ".join(broken)))


def leak_check(text):
    leaked = [label for label, patterns in IDENTIFIERS
              if any(re.search(p, text, re.IGNORECASE) for p in patterns)]
    return check("Synthetic identifiers remaining", f"{len(leaked)} of {len(IDENTIFIERS)}", not leaked,
                 "Leaked: " + ", ".join(leaked) if leaked else "None of the nine known identifiers appear.")


def protected_terms_check(text):
    kept = [term for term in PROTECTED_TERMS if term in text]
    return check("Protected terms kept unchanged", f"{len(kept)} of {len(PROTECTED_TERMS)}",
                 len(kept) == len(PROTECTED_TERMS),
                 "Missing: " + ", ".join(t for t in PROTECTED_TERMS if t not in kept) if len(kept) < len(PROTECTED_TERMS)
                 else "Company name, reference and both times are intact. Meaning still needs a fluent reviewer.")


def triage_checks(text):
    try:
        data = media.extract_json(text)
    except ValueError:
        return [check("Valid JSON", "No", False, "The output did not contain a JSON array.")]
    rows = {str(row.get("id")).strip().upper(): row for row in data if isinstance(row, dict)} \
        if isinstance(data, list) else {}
    expected = {i: c for i, _, _, c in INBOX}
    valid = all(str(row.get("category", "")).lower() in CATEGORIES for row in rows.values())
    agree = [i for i, c in expected.items() if str(rows.get(i, {}).get("category", "")).lower() == c]
    return [check("Valid JSON with all six emails", "Yes" if set(expected) <= set(rows) else "No",
                  set(expected) <= set(rows) and valid,
                  "Every category is from the allowed list." if valid else "A category is outside the allowed list."),
            check("Categories agree with fixture labels", f"{len(agree)} of {len(expected)}",
                  len(agree) == len(expected),
                  "Disagree: " + ", ".join(i for i in expected if i not in agree) if len(agree) < len(expected)
                  else "All six match the labels written into the fixture.")]


def brief_checks(text):
    cites = len(re.findall(r"SOURCE\s+[ABC]\b", text))
    return [check("Source citations", str(cites), cites >= 4, "Each of the four points should cite SOURCE A, B or C."),
            check("No-benefit-claimed sentence present", "Yes" if "Benefits are unproven" in text else "No",
                  "Benefits are unproven" in text, "The brief must end by saying no gain has been measured.")]


def code_checks(text):
    has_block = "```python" in text and "def prioritize_tickets" in text
    return [check("Python function drafted", "Yes" if has_block else "No", has_block,
                  "Displayed for review only. This app never runs generated code.")]
