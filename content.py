"""Synthetic retail scenarios and deterministic business-case arithmetic."""
import math

SCENARIOS = {
    'brief': {
        'title': 'Your next leadership briefing. Already prepared.',
        'label': 'Retail leadership briefing',
        'prompt': 'Prepare an executive meeting agenda with four discovery questions. After each question include one short factual note from SOURCE A, B or C. Cover the current visit report, case summary and shift handoff writing baseline, where customer and associate personal data, store performance figures and unreleased product information must stay, pending approvals and the proposed pilot. Ask questions; do not answer them or predict any improvement. Return only four numbered question/note pairs, then the final sentence. Do not add a title, meeting date, time, location or attendees. End with: Benefits are unproven; no time, accuracy or savings gain has been measured.',
        'source': "FICTIONAL COMPANY: Contoso Apparel\nSOURCE A | Store operations, customer care and IT discovery notes | 14 October 2026\n180 district managers, customer care leads and IT analysts each write about 20 visit reports, case summaries and shift handoffs per week. Writing one currently takes 8 minutes. They often write them on the store floor and in distribution centers, where connectivity is unreliable. No AI productivity study has been conducted.\n\nSOURCE B | Information security, privacy and change-management working session | 15 October 2026\nCustomer and associate personal data, store performance figures and unreleased product information must remain within the company. Only de-identified queries could go to a cloud model for complex questions. The information security, privacy and change-management review and model licensing are not yet complete. Existing cloud productivity tools remain in use; this is not a replacement proposal.\n\nSOURCE C | Pilot proposal | 16 October 2026\nPropose a 15-person, four-week evaluation using synthetic records only, with every draft reviewed by a team lead. Compare preparation time, accuracy, connectivity dependency and staff experience against today's workflow. No device price, battery result, comparative GPU benchmark, customer outcome or committed savings is available.",
        'system': 'You prepare concise executive discovery agendas for retail operations and IT leaders from synthetic source notes. Write four questions, each with a source citation and a factual note. Use only supplied facts. Do not invent outcomes, delays, errors, inefficiencies, future task durations, customer or financial outcomes or improvement estimates. Ask what the company should evaluate, rather than predicting benefits. Keep it under 180 words. Do not add a meeting date, time, location, attendees or title. End with the requested benefits-unproven statement.',
        'rehearsal': '1. What baseline should the pilot compare against?\nSOURCE A: 180 district managers, customer care leads and IT analysts each write about 20 visit reports, case summaries and shift handoffs per week, taking 8 minutes each today.\n\n2. Which data must never leave the company?\nSOURCE B: Customer and associate personal data, store performance figures and unreleased product information stay within the company; only de-identified queries could reach a cloud model for complex questions.\n\n3. Which approvals must precede an evaluation?\nSOURCE B: The information security, privacy and change-management review and model licensing are not complete. Existing cloud productivity tools remain in use.\n\n4. What would justify scaling beyond the pilot?\nSOURCE C: A 15-person, four-week evaluation on synthetic records, with a team lead reviewing every draft, would compare preparation time, accuracy, connectivity dependence and staff experience.\n\nBenefits are unproven; no time, accuracy or savings gain has been measured.',
    },
    "code": {
        "title": "A small request. A useful first draft.",
        "label": "Store technology developer acceleration",
        "prompt": (
            "Write a small Python function prioritize_tickets(tickets) that returns a new list "
            "of ticket dictionaries sorted by severity (critical, high, medium, low), then "
            "descending age_hours within each severity (9 hours before 3 hours). Do not mutate "
            "the input. Unknown severities must raise ValueError. Include three checks: "
            "expected IDs T-102, T-103, T-101 for the supplied sample; unchanged input; "
            "rejection of unknown severity using try/except ValueError."
        ),
        "source": (
            "FICTIONAL STORE TECHNOLOGY SERVICE DESK REQUIREMENT\n"
            "A store technology team wants to prototype a repeatable triage helper for store device "
            "and back-office laptop tickets.\n"
            "Input: [{id: 'T-101', severity: 'high', age_hours: 3}, "
            "{id: 'T-102', severity: 'critical', age_hours: 1}, "
            "{id: 'T-103', severity: 'high', age_hours: 9}]\n"
            "Expected order: T-102, T-103, T-101.\n"
            "No connection to a real service desk. Generated code is displayed, never executed."
        ),
        "system": (
            "You are a careful Python coding assistant running locally. Return a single "
            "Python fenced code block containing the requested function and three small "
            "checks. Sort severity ascending, age_hours descending. For the mutation check, "
            "take a copy before calling the function and compare the original after. "
            "For the exception check use try/except ValueError, with else raising AssertionError; "
            "never compare a function result to an exception object. Use no dependencies, "
            "network calls, file access or shell commands. Keep it under 65 lines. "
            "Generated code is a draft for human review."
        ),
        "rehearsal": (
            "```python\n"
            "def prioritize_tickets(tickets):\n"
            "    ranks = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}\n"
            "    for ticket in tickets:\n"
            "        if ticket['severity'] not in ranks:\n"
            "            raise ValueError('Unknown severity: ' + ticket['severity'])\n"
            "    return sorted(tickets, key=lambda t: (ranks[t['severity']], -t['age_hours']))\n\n"
            "tickets = [\n"
            "    {'id': 'T-101', 'severity': 'high', 'age_hours': 3},\n"
            "    {'id': 'T-102', 'severity': 'critical', 'age_hours': 1},\n"
            "    {'id': 'T-103', 'severity': 'high', 'age_hours': 9},\n"
            "]\n"
            "before = [dict(t) for t in tickets]\n"
            "assert [t['id'] for t in prioritize_tickets(tickets)] == ['T-102', 'T-103', 'T-101']\n"
            "assert tickets == before\n"
            "try:\n"
            "    prioritize_tickets([{'severity': 'urgent', 'age_hours': 1}])\n"
            "except ValueError:\n"
            "    pass\n"
            "else:\n"
            "    raise AssertionError('Unknown severity accepted')\n"
            "```"
        ),
    },
    'field': {
        'title': 'From shift walk-through notes to a clear handover.',
        'label': 'Snapdragon-fit: distribution center shift handover',
        'prompt': "Turn the supplied synthetic walk-through notes into a shift handover with exactly three headings: Observed, Follow-up, Open questions. Cite each bullet with [A], [B] or [C]. Preserve the observed counts and status. Include owners or due times only when explicitly supplied. Follow-up must contain only the two agreed commitments: shift-lead reconciliation [A] and Support's 14:00 update [C]. Put the unverified sync status in Open questions. Connectivity has already returned; do not describe it as still absent. Do not invent a fix, a cause, an impact, a deadline or a productivity benefit. Keep it under 160 words.",
        'source': 'FICTIONAL WALK-THROUGH FIXTURE | Contoso Apparel distribution center DC-2 | Shift walk-through | 16 October 2026\n[A] At distribution center DC-2, five inbound trailer checks were logged this shift. Four were entered digitally and one was recorded on paper. The paper record has not been reconciled. The shift lead owns reconciliation; no due time was agreed.\n\n[B] Handheld scanner HS-17 could not sync during a nine-minute Wi-Fi interruption. Connectivity returned, but HS-17 sync status has not been rechecked. Cause and impact on the trailer check records are unknown.\n\n[C] The shift supervisor opened ticket HD-204 for the HS-17 sync check. Support owns the next status update, due at 14:00. A spare scanner has not been approved. No speech recording or image was supplied.',
        'system': 'You draft concise operational handovers for distribution center shift teams using only supplied synthetic notes. Distinguish observations, agreed follow-up and unresolved questions. Every bullet must cite its source. Do not infer that an interruption affected trailer check records or that an issue is fixed. Do not offer repair instructions or invent approvals, owners, deadlines or benefits. Human review is required before any action; you do not perform actions.',
        'rehearsal': 'Observed\n- DC-2 logged five inbound trailer checks: four digital and one on paper. [A]\n- HS-17 could not sync during a nine-minute Wi-Fi interruption; connectivity returned, but sync has not been rechecked. [B]\n\nFollow-up\n- Shift lead: reconcile the paper record; no due time agreed. [A]\n- Support: provide the next update on HD-204 at 14:00. [C]\n\nOpen questions\n- What is the current HS-17 sync status, and what are the cause and impact on the trailer check records? [B]\n- Will a spare scanner be approved? It is not approved now. [C]',
    },
    'meeting': {
        'title': 'Turn a store operations review into a reviewable action register.',
        'label': 'Intel-fit: store operations review actions',
        'prompt': "Create a concise action register from the supplied synthetic meeting transcript, using columns Action, Owner, Due, Source. Include only explicitly agreed actions. Write 'Not assigned' or 'Not agreed' for missing owners or due dates. Follow the register with one separate Open decision. Do not turn a suggestion into an approved action, invent dates, or predict benefits. Keep it under 170 words.",
        'source': 'FICTIONAL TRANSCRIPT FIXTURE | Contoso Apparel store operations review | 16 October 2026\n[A] Store operations manager: \'I will document the current store visit report workflow by 20 October 2026. We have not measured writing time or report quality.\'\n\n[B] District manager: \'I will select ten synthetic store visit records. We have not agreed a due date for that.\'\n\n[C] Vice president of store operations: \'We agree to request an information security and privacy review, but we have not assigned the request or set a date.\'\n\n[D] CIO: \'A two-week local-AI pilot is a suggestion. Funding and the target Intel configuration are not approved. The decision is open.\'\nThis supplied text is a fixture, not a recording or a measured transcription.',
        'system': 'Extract a small action register only from explicit commitments in the supplied synthetic transcript. Cite [A], [B] or [C] for action rows, and [D] for the open decision. Preserve missing information honestly. Do not interpret a proposed pilot as approved, invent dates or owners, claim transcription was performed, or predict customer, quality, time or savings improvements. Human review is required. You do not create tasks in any external system.',
        'rehearsal': 'Action | Owner | Due | Source\nDocument current store visit report workflow | Store operations manager | 20 October 2026 | [A]\nSelect ten synthetic store visit records | District manager | Not agreed | [B]\nRequest an information security and privacy review | Not assigned | Not agreed | [C]\n\nOpen decision: Whether to fund a two-week local-AI pilot and approve the target Intel configuration remains open. [D]',
    },
    "tutor": {
        "title": "Read code like a second language.",
        "label": "Coding tutor (plain English)",
        "prompt": (
            "Explain this Python code in plain English for a learner who is new to code. Give a one-sentence summary, "
            "then a short note for each line, then one everyday analogy, then one sentence the learner could say to a colleague. "
            "Do not run the code or claim it was run.\n\n"
            "```python\n"
            "def daily_summaries(technicians, per_technician):\n"
            "    return technicians * per_technician\n\n"
            "total = daily_summaries(240, 5)\n"
            "print(total)\n"
            "```"
        ),
        "source": (
            "FICTIONAL LEARNER PROFILE | Retail AI literacy: Coding as a second language\n"
            "The learner works in store operations, has never written code, and wants to "
            "follow technical conversations with developers, data analysts and architects.\n"
            "The code in the prompt is displayed for learning only. It is never executed by this app."
        ),
        "system": (
            "You are a patient coding tutor running locally, teaching a learner who is new to code. "
            "Explain only the code supplied in the prompt, in plain English, and define any jargon in brackets. "
            "Use four short sections: Summary (one sentence), Line by line (one bullet per line or block), "
            "Analogy (one everyday comparison), Say it to a colleague (one sentence). "
            "Never claim the code was run or show output as observed; say what it would do. "
            "Do not claim performance, speed, cost or learning benefits. "
            "End by noting that a developer should review and test code before anyone relies on it. "
            "Keep it under 200 words."
        ),
        "rehearsal": (
            "Summary\n"
            "This code defines a small reusable recipe that multiplies two numbers, uses it once, "
            "and would show the answer.\n\n"
            "Line by line\n"
            "- def daily_summaries(technicians, per_technician): defines a function (a named recipe) with two inputs.\n"
            "- return technicians * per_technician multiplies the inputs (* means multiply) and hands the answer back.\n"
            "- total = daily_summaries(240, 5) uses the recipe with 240 and 5 and stores the answer as total.\n"
            "- print(total) would show 1200 on screen.\n\n"
            "Analogy\n"
            "A function is like a recipe card: give it the ingredients and it makes the dish the same way every time.\n\n"
            "Say it to a colleague\n"
            "\"Developers build software from small, named recipes like this, and test each one on its own.\"\n\n"
            "A developer should review and test code before anyone relies on it."
        ),
    },
}

SCENARIOS.update({
    'fleet-health': {
        'industry': 'Store technology',
        'client': 'Contoso Apparel',
        'deck_objective': 'Explain a local drafting pilot that turns a weekly endpoint management and service desk export into a fleet health summary for the store technology team, keeping associate and device data inside the company, with no device, policy or ticket changed.',
        'title': 'Weekly fleet and service desk data to a health summary.',
        'label': 'Store technology: weekly device health summary',
        'prompt': "Draft a review list with three headings: What the data shows, Watch items, Needs an owner. Use '- ' bullets. Cite every bullet by ending it with [A], [B] or [C]. Under What the data shows, list only what [A] records. Under Watch items, list only the items in [B], as written. Under Needs an owner, list only the question store operations asked in [C]. Keep the recorded numbers. Do not determine a root cause or link the Wi-Fi drops to the update, recommend deploying, pausing or rolling back an update, change any device, policy or ticket, or invent figures, devices or dates. Keep it under 180 words. End with: Draft only; the store technology team must review, and no device or policy has been changed.",
        'source': 'FICTIONAL SYNTHETIC FIXTURE | Contoso Apparel | Weekly fleet health export FH-2026-W43, endpoint management and service desk data\n\n[A] The endpoint management export lists 18,420 managed Windows devices; 96.1% are compliant. 412 devices are still pending the October quality update, 287 of them store back-office laptops.\n\n[B] The service desk export shows 1,936 incidents this week against 1,702 last week. The top category is "Wi-Fi drops after resume", with 214 incidents across 37 stores.\n\n[C] Store operations asked whether the Wi-Fi drops are related to the pending update. No root cause has been confirmed, and no change has been made.',
        'system': 'Draft a cited fleet health summary from synthetic endpoint management and service desk notes only. Separate what the data shows, watch items and questions that need an owner. Do not determine a root cause or link the Wi-Fi drops to the update, recommend deploying, pausing or rolling back an update, change any device, policy or ticket, or invent figures, devices or dates. Store technology team review is required.',
        'rehearsal': 'What the data shows\n- 18,420 managed Windows devices; 96.1% are compliant. [A]\n- 412 devices are still pending the October quality update, 287 of them store back-office laptops. [A]\n\nWatch items\n- 1,936 incidents this week against 1,702 last week. [B]\n- The top category is "Wi-Fi drops after resume", with 214 incidents across 37 stores. [B]\n\nNeeds an owner\n- Whether the Wi-Fi drops are related to the pending update, as store operations asked; no root cause has been confirmed, and no change has been made. [C]\n\nDraft only; the store technology team must review, and no device or policy has been changed.',
    },
    'major-incident': {
        'industry': 'Service desk',
        'client': 'Contoso Apparel',
        'deck_objective': 'Explain a local drafting pilot that turns major incident notes into a stakeholder update draft for the incident manager, keeping associate and ticket data inside the company, with nothing sent to stores or stakeholders.',
        'title': 'Major incident notes to a stakeholder update draft.',
        'label': 'Service desk: major incident update draft',
        'prompt': "Draft a review list with three headings: Confirmed so far, Still unknown, Needs the incident manager. Use '- ' bullets. Cite every bullet by ending it with [A], [B] or [C]. Under Confirmed so far, list only what [A] records. Under Still unknown, list only the items in [B], as written. Under Needs the incident manager, list only what Kenji asked for in [C]. Keep the recorded numbers and times. Do not state or guess a cause, promise a fix or restore time, approve or recommend the rollback, or invent stores, systems or times. Keep it under 180 words. End with: Draft only; the incident manager must review, and nothing has been sent to stores or stakeholders.",
        'source': 'FICTIONAL SYNTHETIC FIXTURE | Contoso Apparel | Major incident MI-3317, store scheduling sign-in failures\n\n[A] Since 06:10, associates at 41 stores cannot sign in to Relecloud Scheduler, the store scheduling app. Headquarters users are not affected.\n\n[B] No cause has been confirmed. A conditional access policy change was applied at 05:45, and a rollback is being evaluated.\n\n[C] Kenji, the incident manager, asked for a store leader update by 09:00. Nothing has been sent.',
        'system': 'Draft a cited stakeholder update outline from synthetic major incident notes only. Separate what is confirmed so far, what is still unknown and what the incident manager needs. Do not state or guess a cause, promise a fix or restore time, approve or recommend the rollback, or invent stores, systems or times. Incident manager review is required.',
        'rehearsal': 'Confirmed so far\n- Since 06:10, associates at 41 stores cannot sign in to Relecloud Scheduler, the store scheduling app. [A]\n- Headquarters users are not affected. [A]\n\nStill unknown\n- No cause has been confirmed. [B]\n- A conditional access policy change was applied at 05:45, and a rollback is being evaluated. [B]\n\nNeeds the incident manager\n- Kenji asked for a store leader update by 09:00; nothing has been sent. [C]\n\nDraft only; the incident manager must review, and nothing has been sent to stores or stakeholders.',
    },
    'customer-care': {
        'industry': 'Customer care',
        'client': 'Contoso Apparel',
        'deck_objective': 'Explain a local drafting pilot that turns customer contact notes into a case summary for the customer care team lead, keeping customer personal data inside the company, with no refund, credit or reshipment decision.',
        'title': 'Customer contact notes to a case summary.',
        'label': 'Customer care: case summary for the team lead',
        'prompt': "Draft a review list with three headings: Case history, Still open, Needs the team lead. Use '- ' bullets. Cite every bullet by ending it with [A], [B] or [C]. Under Case history, list only what [A] records. Under Still open, list only the items in [B], as written. Under Needs the team lead, list only the question Jamie asked in [C]. Keep the recorded numbers, dates and order number. Do not decide or promise a refund, credit, reshipment or compensation, blame the carrier or the customer, contact the customer, or invent orders, dates or amounts. Keep it under 180 words. End with: Draft only; a customer care team lead must review, and nothing has been sent to the customer.",
        'source': 'FICTIONAL SYNTHETIC FIXTURE | Contoso Apparel | Customer care case CC-58210, online order delivered incomplete\n\n[A] The customer contacted customer care three times in six days about online order WEB-771204. The order shipped in two parcels, and one parcel was delivered on 21 October 2026.\n\n[B] Carrier tracking for the second parcel has not updated since 22 October 2026. The customer has asked for a refund of the missing item.\n\n[C] Jamie Lin, the customer care agent, asked the team lead whether to reship the missing item or refund it. No refund or reshipment has been issued.',
        'system': 'Draft a cited customer care case summary from synthetic contact notes only. Separate the case history, what is still open and questions for the team lead. Do not decide or promise a refund, credit, reshipment or compensation, blame the carrier or the customer, contact the customer, or invent orders, dates or amounts. Customer care team lead review is required.',
        'rehearsal': 'Case history\n- The customer contacted customer care three times in six days about online order WEB-771204. [A]\n- The order shipped in two parcels, and one parcel was delivered on 21 October 2026. [A]\n\nStill open\n- Carrier tracking for the second parcel has not updated since 22 October 2026. [B]\n- The customer has asked for a refund of the missing item. [B]\n\nNeeds the team lead\n- Whether to reship the missing item or refund it, as Jamie asked; no refund or reshipment has been issued. [C]\n\nDraft only; a customer care team lead must review, and nothing has been sent to the customer.',
    },
    'replenishment': {
        'industry': 'Inventory and allocation',
        'client': 'Contoso Apparel',
        'deck_objective': 'Explain a local drafting pilot that turns a weekly in-stock export into a replenishment review for the allocation team, keeping sales and inventory data inside the company, with no order, transfer or allocation decision.',
        'title': 'Weekly in-stock notes to a replenishment review.',
        'label': 'Inventory and allocation: weekly in-stock review',
        'prompt': "Draft a review list with three headings: What the data shows, Watch items, Needs the allocation lead. Use '- ' bullets. Cite every bullet by ending it with [A], [B] or [C]. Under What the data shows, list only what [A] records. Under Watch items, list only the items in [B], as written. Under Needs the allocation lead, list only the question the allocation analyst asked in [C]. Keep the recorded numbers and dates. Do not decide or recommend an order, transfer, markdown or allocation, forecast sales, or invent figures, products, stores or dates. Keep it under 180 words. End with: Draft only; the allocation lead must review, and no order, transfer or allocation decision has been made.",
        'source': 'FICTIONAL SYNTHETIC FIXTURE | Contoso Apparel | Weekly in-stock export IS-2026-W43, 310 stores\n\n[A] The store in-stock rate is 94.2% this week against 95.0% last week. 18 products are below their safety stock at 40 or more stores.\n\n[B] Two core products, the Everyday Crew Tee in white and in navy, are out of stock at 23 stores. Distribution center DC-2 holds 4,800 units of the two products, and the next supplier receipt is planned for 6 November 2026.\n\n[C] The allocation analyst asked whether to transfer units from lower-selling stores before the weekend. No order, transfer or allocation decision has been made.',
        'system': 'Draft a cited replenishment review from synthetic weekly in-stock notes only. Separate what the data shows, watch items and questions for the allocation lead. Do not decide or recommend an order, transfer, markdown or allocation, forecast sales, or invent figures, products, stores or dates. Allocation lead review is required.',
        'rehearsal': 'What the data shows\n- The store in-stock rate is 94.2% this week against 95.0% last week. [A]\n- 18 products are below their safety stock at 40 or more stores. [A]\n\nWatch items\n- Two core products, the Everyday Crew Tee in white and in navy, are out of stock at 23 stores. [B]\n- Distribution center DC-2 holds 4,800 units of the two products, and the next supplier receipt is planned for 6 November 2026. [B]\n\nNeeds the allocation lead\n- Whether to transfer units from lower-selling stores before the weekend, as the allocation analyst asked; no order, transfer or allocation decision has been made. [C]\n\nDraft only; the allocation lead must review, and no order, transfer or allocation decision has been made.',
    },
    'store-visit': {
        'industry': 'Store operations',
        'client': 'Contoso Apparel',
        'deck_objective': 'Explain a local drafting pilot that turns store visit notes into a district follow-up list for the district manager, keeping associate and store data inside the company, with no store change made.',
        'title': 'Store visit notes to a district follow-up list.',
        'label': 'Store operations: store visit follow-up',
        'prompt': "Draft a review list with three headings: Observed on the visit, Device and IT issues, Needs the district manager. Use '- ' bullets. Cite every bullet by ending it with [A], [B] or [C]. Under Observed on the visit, list only what [A] records. Under Device and IT issues, list only the items in [B], as written. Under Needs the district manager, list only the question the store manager asked in [C]. Keep the recorded numbers and times. Do not decide layout, staffing or schedules, diagnose the device issues, promise repairs, or invent figures, people or times. Keep it under 180 words. End with: Draft only; the district manager must review, and no store change has been made.",
        'source': 'FICTIONAL SYNTHETIC FIXTURE | Contoso Apparel | Store visit SV-0412, Store 0412 Saturday visit\n\n[A] The fitting-room queue reached 14 customers at 13:30. Two of five fitting rooms were closed for repair.\n\n[B] The register 3 receipt printer has been offline since 14:00. Stockroom Wi-Fi drops when the handheld scanners resume.\n\n[C] The store manager asked whether the online pickup counter can move next to the entrance. No store change has been made.',
        'system': 'Draft a cited store visit follow-up list from synthetic store visit notes only. Separate what was observed on the visit, device and IT issues and questions for the district manager. Do not decide layout, staffing or schedules, diagnose the device issues, promise repairs, or invent figures, people or times. District manager review is required.',
        'rehearsal': 'Observed on the visit\n- The fitting-room queue reached 14 customers at 13:30. [A]\n- Two of five fitting rooms were closed for repair. [A]\n\nDevice and IT issues\n- The register 3 receipt printer has been offline since 14:00. [B]\n- Stockroom Wi-Fi drops when the handheld scanners resume. [B]\n\nNeeds the district manager\n- Whether the online pickup counter can move next to the entrance, as the store manager asked; no store change has been made. [C]\n\nDraft only; the district manager must review, and no store change has been made.',
    },
    'line-review': {
        'industry': 'Merchandising',
        'client': 'Contoso Apparel',
        'deck_objective': 'Explain a local drafting pilot that turns line review notes into a sample follow-up list for the product team, keeping unreleased collection details inside the company, with no style, cost or supplier decision.',
        'title': 'Line review notes to a sample follow-up list.',
        'label': 'Merchandising: line review follow-ups',
        'prompt': "Draft a review list with three headings: Agreed in the review, Open items, Needs the product team. Use '- ' bullets. Cite every bullet by ending it with [A], [B] or [C]. Under Agreed in the review, list only what [A] records. Under Open items, list only the items in [B], as written. Under Needs the product team, list only the question the merchandiser asked in [C]. Keep the recorded numbers and dates. Do not decide styles, costs, prices, suppliers or dates, or invent styles, figures or dates. Keep it under 180 words. End with: Draft only; the product team must review, and no style or supplier decision has been made.",
        'source': 'FICTIONAL SYNTHETIC FIXTURE | Contoso Apparel | Line review LR-2027S, Spring 2027 collection (unreleased)\n\n[A] 41 of 48 styles were approved for sampling. The other 7 styles move to a second review on 12 November 2026.\n\n[B] The recycled-cotton fabric lead time is 11 weeks against a 9-week plan. Two colorways have no approved lab dip.\n\n[C] The merchandiser asked whether to drop the two colorways from the line. No style or supplier decision has been made.',
        'system': 'Draft a cited line review follow-up list from synthetic line review notes only. Separate what was agreed in the review, open items and questions for the product team. Do not decide styles, costs, prices, suppliers or dates, or invent styles, figures or dates. Product team review is required.',
        'rehearsal': 'Agreed in the review\n- 41 of 48 styles were approved for sampling. [A]\n- The other 7 styles move to a second review on 12 November 2026. [A]\n\nOpen items\n- The recycled-cotton fabric lead time is 11 weeks against a 9-week plan. [B]\n- Two colorways have no approved lab dip. [B]\n\nNeeds the product team\n- Whether to drop the two colorways from the line, as the merchandiser asked; no style or supplier decision has been made. [C]\n\nDraft only; the product team must review, and no style or supplier decision has been made.',
    },
})


DEFAULT_ASSUMPTIONS = {
    "users": 100,
    "tasks": 4,
    "minutes": 3,
    "days": 220,
    "adoption": 60,
    "hourly": 60,
    "premium": 600,
}
LIMITS = {
    "users": (1, 100000), "tasks": (0, 100), "minutes": (0, 120),
    "days": (1, 366), "adoption": (0, 100), "hourly": (0, 1000),
    "premium": (0, 20000),
}


def calculate(values):
    if not isinstance(values, dict) or set(values) != set(LIMITS):
        raise ValueError("Provide exactly the seven calculator assumptions.")
    for name, (low, high) in LIMITS.items():
        value = values[name]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name} must be a number.")
        if not math.isfinite(value) or not low <= value <= high:
            raise ValueError(f"{name} must be between {low} and {high}.")
    hours = values["users"] * values["tasks"] * values["minutes"] / 60 * values["days"] * values["adoption"] / 100
    capacity = hours * values["hourly"]
    investment = values["users"] * values["premium"]
    return {
        "hours": round(hours, 2),
        "capacity": round(capacity, 2),
        "investment": round(investment, 2),
        "assumptions": values,
        "disclaimer": "Illustrative capacity value, not cash savings or an ROI forecast. "
        "Excludes software, implementation, support, financing and change-management costs. "
        "AI time improvements and adoption must be validated in a pilot. Cloud subscriptions are unchanged.",
    }
