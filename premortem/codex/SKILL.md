---
name: premortem
description: >-
  Run a premortem on a plan, project, decision, launch, migration, investment,
  policy, or personal choice in any field: imagine it has already failed,
  reconstruct the causes, prioritize them, and turn them into changes, controls,
  early signals, and contingencies in a complete report, or produce the kit to
  run the session with a team. Use when the user asks for a premortem or
  pre-mortem, asks what could make a plan fail, wants a plan's risks analyzed
  before committing, or says "haz un premortem de este plan", "qué podría hacer
  fracasar esto", "imagina que fracasó", "analiza los riesgos antes de empezar",
  "run a premortem on this". Not for postmortems, incident reviews, or
  retrospectives on what already happened, and not a substitute for a technical
  risk analysis or a security audit.
license: MIT OR Apache-2.0
metadata:
  version: 1.1.0
---

# Premortem

Take a plan that exists and can still change, place it in a future where it has already failed, and work backwards: what happened, which of it matters, and what the plan does about it now. The method is the same for a product launch, a data migration, a public policy, a clinical program, a hire, an investment, or a career move; the object changes, the procedure does not. The report that comes out is a set of risk hypotheses with a treatment for each one that matters, never a prediction and never a technical audit. A premortem earns its cost only when it changes the plan or the way the plan is watched; a list of interesting risks with nothing decided is the failure mode this skill exists to avoid.

## Scope and Inputs

Work from the plan the user brings: a document, a summary, a proposal, a ticket, a paragraph. The minimum to analyze is an objective, a criterion that says what success looks like, and a horizon. Record everything else the plan states before starting: scope and exclusions, milestones, budget and resources, assumptions, dependencies, constraints, and any reference data or comparable cases. What the user supplies is the plan as given; the skill does not redesign it, rename its parts, or argue with its goal. What the plan leaves unstated becomes either a question or a declared assumption.

Ask only when the missing element would change the analysis and no defensible default exists. A plan with no measurable success criterion is the one case that always gets a question: "the digital transformation" produces generalities, and "migrate 80% of customers to the new platform before June 30 without raising cancellations above 2%" produces risks someone can check. When the user cannot answer, propose the most concrete reading of their goal, label it as the skill's assumption, and analyze that. Otherwise choose, analyze, and state the choice in the Notes.

If the user has already written their own causes, or brings notes from a team session, those enter the analysis first and unchanged. Anything the skill adds is labeled as its own, so the humans' reading of their plan stays visible and separate. This follows the one sequencing rule of the method: human generation before model generation, because whoever speaks first sets the boundaries of what the rest will think of.

Write the report in the user's language unless another is requested. Deliver in Markdown unless another format is asked for.

This skill analyzes a plan before it runs. Something that already failed goes to a postmortem or a retrospective, which works from evidence rather than imagination. A plan that needs component-by-component failure analysis, hazard study, threat modeling, or a security or compliance audit gets a premortem as the opening pass and a handoff to that method, named in the report; the premortem finds hypotheses, it does not verify controls. In medicine, aviation, infrastructure, safety-critical systems, and regulated finance the premortem is an exploratory complement and the report says so.

## Choosing the Mode

Two modes. **Analysis** is the default and the one to be rigorous about: the user supplies a plan and receives the complete premortem report. **Facilitation** applies when the user says they have a team and will run a session: the skill produces the workshop kit, then processes the team's notes into the same report once they arrive. When the user's intent is unclear and there is a plan in the message, analyze it. When the user asks for the kit, the agenda, the scenario to read aloud, or how to run the session, facilitate.

## Analysis Mode

Complete the eight steps in order. Each one leaves something on paper that the next one uses; skipping ahead produces the defects listed under Common Failures.

### 1. Plan Sheet

Restate the plan in a fixed sheet before analyzing it: decision or plan under analysis; objective and measurable success criteria; definition of failure, in the plan's own terms; scope and exclusions; time horizon; budget and resources; milestones; assumptions; dependencies; constraints; base rates known (how long comparable efforts took, how often they overran, what adoption or defect or churn rates similar cases showed) and base rates missing. Every line that the plan did not state and the skill filled is marked as an assumption. The sheet is what makes every later risk checkable against something: a cause that contradicts no line of the sheet is probably not about this plan.

### 2. Failure Scenario

Write the scenario in the past tense, with a date beyond the horizon, an unequivocal outcome, and consequences someone could have observed: costs, delays, incidents, abandonment, an independent review's verdict. Wide enough not to suggest a cause. "It is September 30, 2027. The migration is now considered a failure: the cost doubled, there were two outages that made the news, and a third of the priority customers refused to complete the change. An independent review concluded the outcome was avoidable. What happened?" is a scenario. "We failed because the vendor was late" is an explanation wearing a scenario's clothes, and it anchors everything that follows to the vendor. The test for each sentence of the scenario: it states something the success criteria measure or something a third party saw. A sentence about the team, a supplier, a tool, or a decision ("an engineer resigned in May", "the vendor cut access") is a cause, and it leaves the scenario for step 3.

For the second barrel (step 7) prepare the mirror scenario now: same date, the plan was not executed or was cut back so far that the opportunity was lost, and the outcome was also bad.

### 3. Generating Causes

Generate before classifying. Speak from inside the scenario: "the users left", not "the users might leave". Produce at least ten causes for a plan of ordinary size, more for a large one, and for each one say what specifically happened rather than naming a theme. Include at least one cause the plan's own team would be unlikely to raise, at least two that come from outside the organization, and at least one combination of small failures that produced the collapse together. The prompts that widen the search:

- Which assumption in the sheet turned out to be false?
- Which signal was visible early and got rationalized?
- Which dependency failed, and what did it take down with it?
- What did the people closest to the work know that never reached whoever decided?
- Which incentive produced behavior that worked against the plan?
- Which ethical, legal, privacy, or reputational problem was underestimated?
- Which rare event had consequences the plan could not absorb?
- What did an adversary, a competitor, or a regulator do?

Only after the free generation, sweep the categories as a checklist to find gaps: strategy and value proposition; customers, users, or affected population and their adoption; scope and requirements; schedule and capacity; technology, architecture, and data; quality and verification; people, skills, and incentives; suppliers and dependencies; finances; legal, ethics, privacy, and compliance; security and continuity; governance and decision rights; communication and reputation; political, economic, environmental, or social context. Then a second explicit pass on external causes, because a team's causes cluster around what it controls. Then the domain probes below for the plan's field, if it has one. The categories are a checklist after the fact, never the starting point: starting from them produces one dutiful risk per box and nothing surprising.

A cause is a hypothesis. Fluency is not probability, and a vivid story displaces a dull, frequent failure; the next steps exist to correct for that, so do not filter here.

### 4. Formulating Risks

Consolidate duplicates without erasing causal differences: two causes that lead to the same event through different mechanisms are two risks. Rewrite each one as

> **Because of [cause], [event] could occur, causing [impact].**

"Poor communication" is a complaint. "Because support does not receive the new guide before launch, agents give customers instructions that contradict the product, raising repeat contacts and cancellations" is a risk: a condition someone can observe, an event, a measurable impact. A cause that blames a group ("the team is not up to it") is rewritten into the observable condition that makes it true or false. Each risk gets an identifier and a line stating what evidence or base rate supports it, or that none is known.

### 5. Prioritizing

Score each risk on six criteria, 1 to 5, qualitative: plausibility; impact; early detectability; speed of materialization; capacity to intervene once it starts; and confidence in the assessment itself. The scale orders the discussion; it measures nothing, and the report says so. Rank by judgment over the six columns, not by a product of numbers. Keep a separate short list for risks of low plausibility and intolerable consequence; they do not compete with the rest on the same scale. A risk that only a specialist would recognize outranks a popular one when the specialist's mechanism holds; expertise is not a vote. A confidence of 1 or 2 is a flag to name the missing expert or data, not a reason to drop the risk.

### 6. Treatment

For each priority risk decide: the assumption to validate and how; the preventive action that lowers plausibility; the control that lowers impact; the early indicator and the threshold that triggers escalation; the contingency to execute when the threshold is crossed; who owns it; when it is due; and the residual risk accepted after all that. An action passes only if it answers what, who, when, how it is verified, and what happens if it is not done. "Communicate better", "stay alert", and "improve coordination" fail the test and do not appear in the report. "Publish the support guide, train 90% of the support staff, and pass a competence check before May 15, owner: head of support" passes. Treatment options are prevention, reduction, transfer, conscious acceptance, or avoidance; acceptance names the authority that accepts and a review date.

When the user's plan names no people, owners are roles ("whoever owns the vendor relationship") and the Notes say the names are pending.

### 7. Second Barrel

Run the mirror scenario: the plan was not executed, or was diluted until it lost its point, and the outcome was also bad. Generate its causes, formulate its risks, and compare. This is what keeps the exercise from rewarding caution by default: a list of thirty ways to fail says nothing about whether not acting fails worse. The comparison is stated as such, with the reversibility of each path, the cost of delay, and what a pilot or a staged commitment would buy. Skip this step only when the plan has no real alternative of not acting, and say so in the Notes.

### 8. Honesty Check

Before writing the report, verify: every risk is a hypothesis and the report does not read as a forecast; the unknowns are declared, including risks the skill could not assess and the expertise that was absent; the base rates the plan needs and does not have are listed; the confidence column has real variation; the handoffs to technical methods are named where the plan needs them; and the report ends with decisions to make, not with a list to admire. A smooth analysis that produced no surprise is a warning sign, not a success; go back to step 3 and run the external pass and the "nobody would mention this" prompt again.

## Facilitation Mode

When the user will run a session with a team, deliver the kit, not the analysis. The kit contains:

1. **Plan sheet** as in step 1, filled from what the user supplied, with the gaps marked for the plan's owner to close before the session.
2. **Participant guidance**: five to ten people as a working range; the decision owner, those who will execute, operations and support, the technical profiles, finance, legal, security, or compliance when relevant, someone close to the user or affected population, one independent participant, and someone who has seen a comparable failure. Not only the people who designed the plan: suppliers, operators, and front-line staff see dependencies that leadership does not. The facilitator should not be the person most committed to the plan.
3. **Failure scenario** as in step 2, ready to read aloud, and the mirror scenario for the second barrel.
4. **Rules** to declare at the start: the exercise judges the plan, not the people; causes can be technical, human, political, commercial, or external; nothing is rebutted during generation; rank does not decide validity; uncomfortable, ethical, and reputational risks are admissible.
5. **Agenda** for 60 to 90 minutes: present the plan (5–10 min, questions of clarification only); declare the rules (2); read the scenario and move the room into the past tense (2); silent individual writing, one cause per note, at least five each and one that nobody else will say (5–10); collect in rounds without debate, starting with the least senior or in random order, the owner speaks last (10–15); sweep the categories for gaps (5); group and formulate as cause–event–impact (10); prioritize (10–15); design treatments (15–25); second barrel (10); close with the owner's decisions: changes accepted, investigations pending, risks accepted and by whom, decisions postponed, next review (5). Distribute the record within 24–48 hours and put the actions where the team's work already lives.
6. **Silent-writing prompts** from step 3, for the participants.
7. **Register template** matching the report structure under Deliverables.

Offer the variants as one-line options when the situation calls for them: asynchronous collection before a date, with uniform instructions and late participants kept from seeing early answers; an anonymous first round when fear or politics would silence people, with a channel afterwards for detail; a shortened repeat before each milestone, with the scenario updated rather than the old list copied; a success premortem as a complement, including how an overwhelming success would break capacity or quality; separate rounds for technical, commercial, ethical, and operational failure when the decision is large enough to justify the duplication.

When the notes come back, process them through steps 4 to 8: the team's causes first and unchanged, the skill's additions labeled as an additional participant, then formulation, prioritization, treatment, second barrel, and the honesty check. Do not generate causes before the team has written theirs.

## Domain Probes

The probes are applied at the end of step 3, after free generation and the category sweep, as questions to check against what was already found. A plan in a field not listed here runs the method unchanged; the probes add coverage, they do not define it.

**Product and software.** The longest list, because software plans fail in ways that hide inside the plan's own vocabulary. Adoption: was the problem the user's priority or an internal one, and what did the pilot's retention look like? Technical debt: which shortcut taken to hit the date became the thing that could not be changed later? Integrations and data quality: which upstream data did the plan assume clean, and what fraction of critical records failed to reconcile? Security: which threat was out of scope until it was not? Scalability and capacity: what did the load look like at the peak the plan did not model? Support: could the support function absorb the first weeks, and had anyone rehearsed the volume? Vendor and platform dependency: which single supplier, API, or license had no fallback? Migration and cutover: was there a rollback that had been exercised, and a point after which rollback stopped being possible? Go/no-go: who could say no to the public date, on what criteria, and was the defect trend actually falling in the last two iterations? Observability: would the early indicators in the treatment table have been visible in the telemetry the plan was going to have? Any risk here that needs component-level analysis, threat modeling, or a security review is handed off by name.

**Engineering and operations.** Interfaces between subsystems, maintainability, tolerances, spare parts, capacity, human factors, continuity, supply chain. Technical risks are handed off to FMEA, HAZOP, testing, or reliability analysis; the premortem names them, it does not resolve them.

**Strategy and investment.** A false thesis, competitor reaction, liquidity, incentives, regulation, irreversibility, opportunity cost. Base rates and the second barrel are mandatory here, because the cost of inaction is where this domain's risks hide.

**Public policy.** Local implementation, behavior of the actors the policy assumes, equity, legitimacy, second-order effects, regulatory capture, administrative capacity. The affected population is a participant or a perspective the skill simulates and labels as simulated, never left out.

**Health and implementation.** Access, workflow, trust, safety, equity, adherence, sustainability. The premortem does not replace clinical, ethical, regulatory, or patient-safety evaluation and the report says so.

**Personal decisions.** Career, relocation, a venture, a financial commitment. Separate reversible from irreversible risks, ask what an outside observer with comparable cases would say, and keep the list from becoming a container for unspecific anxiety: a personal premortem ends with three to five decisions, not thirty worries.

## Common Failures

Apply this table to the skill's own output before delivering; each row is a symptom the analysis can show and the correction that removes it.

| Symptom in the analysis | Correction |
|---|---|
| The scenario contains a cause | Rewrite it as date, outcome, observable consequences only |
| Every cause is internal and controllable | Run the external pass: market, regulation, suppliers, climate, adversaries, reputation |
| A risk reads as a complaint about people | Rewrite as observable condition, event, impact |
| Priority follows the number of mentions | Re-rank by mechanism, impact, base rate, and expertise; mark low-confidence rows |
| The list is long and every action looks unsafe | Second barrel, reversibility, pilot options, exposure limits |
| An action is "be careful" or "coordinate better" | Owner, date, deliverable, indicator, threshold, contingency, or delete it |
| The report ends with a list and no decision | Add the owner's decision block: changes, investigations, accepted risks, next review |
| The analysis was smooth and confirmed the plan | Declare the unknowns, name the absent experts, repeat step 3 with the outsider prompts |
| Causes were generated before the user's own | Restart: the user's causes first, the skill's labeled second |
| The plan was analyzed before it had a success criterion | Ask for it or propose one and mark it as an assumption |
| The premortem is being used where a technical audit is required | Keep the premortem as the opening pass and name the method the plan needs |

## Deliverables

In this order, in the user's language, as one Markdown document:

1. **Header**: plan or decision analyzed, date of the analysis, horizon of the scenario, plan version if any, mode (analysis or facilitation), sources the user supplied.
2. **Plan sheet**: the sheet from step 1, assumptions marked.
3. **Scenario**: the failure scenario in the past tense; the mirror scenario when the second barrel ran.
4. **Causes generated**: the user's or the team's first, unchanged, then the skill's, labeled as such.
5. **Prioritized risks**: a table with identifier, the cause–event–impact statement, evidence or base rate, plausibility, impact, speed, detectability, intervenability, confidence; the catastrophic-but-improbable list below it.
6. **Treatment**: a table with identifier, assumption to validate, prevention, control, early indicator and threshold, contingency, owner, date, residual risk.
7. **Changes to the plan**: what the analysis recommends changing, one line each, ready to accept or refuse.
8. **Accepted risks**: risk, justification, accepting authority, review date.
9. **Second barrel**: the risks of not acting and the comparison with acting, or the reason the step was skipped.
10. **Unknowns**: risks the analysis could not assess, base rates missing, expertise absent, handoffs to technical methods.
11. **Next review**: date or condition that triggers a repeat, with the scenario to update.
12. **Notes**: one line per assumption the skill made, per question it asked, per step it skipped and why, per cause it rejected as generic or invented, and whether the humanize pass ran.

In facilitation mode the first delivery is the kit, in the order of that section, and the report follows once the notes arrive. When the user asks for the plan sheet and scenario only, stop after item 3 and wait.

Before delivery, when the humanize skill is available, pass the report's prose through it with the tables, the cause–event–impact statements, the scenario's date and figures, names, thresholds, owners, dates, and identifiers supplied as protected material, so that rhythm and wording change and no fact, number, name, or strength of claim does. A hedge and a certainty are different risk statements; the pass changes neither into the other. When humanize is not available, say so in the Notes. The same applies to the kit.

When the user names a file or a folder, write the report to a new file there; never overwrite an existing file. When the user supplied a plan document, do not return it, quote it at length, or alter it.

## Example Use

"Use /premortem on this plan: migrate our 4,000 customers from the legacy billing system to the new platform between March and June, with two engineers, keeping churn under 2% and no billing errors in the first two cycles. Here is the plan document. Save the report as docs/premortem-billing-migration.md."

"Use /premortem to prepare a session: we are eight people deciding whether to open a second clinic in the north of the city by next year. Give me the kit and I will send you the team's notes afterwards."
