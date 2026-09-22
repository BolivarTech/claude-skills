---
name: design-brainstorm
description: >-
  Turn an idea, feature request, or proposed behavior change into an approved
  design or behavioral specification before any implementation starts. It
  classifies the request as a feasibility spike, a bounded change, or an
  architectural change, explores the repository first, presents the design,
  and stops for approval; when premortem reports or gap registries exist, it
  carries their risks, controls, and open gaps into the design. Use for new
  features, new subsystems, interface changes, ambiguous requests, feasibility
  questions, or when the user says "let's brainstorm this", "design this before
  we build it", "how should we approach this feature", "diseñemos esto antes de
  implementar", "quiero agregar una funcionalidad", "cómo encaramos este
  cambio". Not for implementing an already approved spec or plan, diagnosing a
  bug, postmortems, or ordinary code review.
license: MIT OR Apache-2.0
metadata:
  version: 1.0.0
---

# Design Brainstorm

Clarify intent and turn it into the smallest design that fully satisfies the user's objective.
Explore the repository before proposing changes. No implementation, scaffolding, production-code
edit, or implementation skill begins until the user approves the proposed direction. The amount
of design ceremony may shrink; the approval gate does not.

Work in the user's language. Identifiers, paths, commands, and quoted strings stay as they are.

Repository rules take precedence. If they define SDD, BDD, SBTDD, artifact locations, approval
checkpoints, or a planning workflow, use those instead of inventing parallel documents.

## Classify the request

State the classification briefly so the user can correct it:

- **Spike:** A feasibility question whose deliverable is an answer or recommendation, not
  production code.
- **Bounded:** A focused change to an existing flow whose interfaces and consumers can be
  inspected in the repository.
- **Architectural:** A new project, subsystem, execution route, persistent format, shared
  interface, or change that restructures components or affects several consumers.

When uncertain, choose the heavier path. If repository inspection reveals wider consequences,
upgrade the classification and stop before implementation. Do not downgrade once material hidden
complexity is known.

## Gather context before asking questions

Inspect the smallest useful set of sources:

1. Repository rules and the active spec, plan, and session state.
2. Relevant implementation, tests, public interfaces, and recent history.
3. Existing designs or behavioral baselines for the same objective.
4. Relevant premortem artifacts, when present.

Use a repository index or knowledge graph first when local rules require it. Prefer scoped search
over broad file dumps.

Ask only questions whose answers materially change behavior or scope, and ask one focused
question at a time. When the repository already answers a question, make the safe assumption and
disclose it instead of asking.

Search for premortem material in the repository's declared process directories and in paths such
as:

- `sbtdd/premortem*.md`
- `planning/premortem*.md`
- `**/premortem-*.md`
- `**/premortem-gaps.md`

Process artifacts are often gitignored. Search the declared directories directly or include
ignored files (for example, `rg --files -uu`) instead of relying only on the tracked file list.

Apply the premortem integration section below when a relevant report or gap registry exists.
Ignore unrelated premortems. Never treat a filename match as proof that a report covers the
current objective.

## Choose the path

### Spike

1. Inspect enough context to frame the uncertainty.
2. Present the question, success signal, probe, limits, and what would remain unknown in two or
   three sentences.
3. Obtain approval.
4. Investigate as cheaply as correctness allows.
5. Report evidence and a recommendation. Label any temporary artifact as throwaway; keeping it
   requires a separately classified change.

### Bounded

1. Inspect the existing flow, callers, tests, and constraints.
2. Resolve the questions that remain after inspection, one at a time.
3. Present a short design in chat: behavior, affected interfaces/files, failure handling,
   compatibility, and verification.
4. Identify premortem risks or open gap IDs that constrain the change.
5. Stop and obtain explicit approval.
6. After approval, follow the repository's normal implementation and TDD workflow. Do not create
   a separate plan artifact unless repository rules require one.

### Architectural

1. Establish objective, actors, observable behavior, exclusions, constraints, compatibility,
   success criteria, and unresolved decisions.
2. Decompose the request if it contains independent subsystems that cannot be reviewed or
   verified as one bounded contract.
3. Present two or three viable approaches with trade-offs. Lead with the recommended option and
   explain why it best fits current consumers and constraints.
4. Present the design in reviewable sections. Cover boundaries, data/control flow, errors,
   cleanup, security, compatibility, migration, testing, and operational evidence when relevant.
5. Reconcile applicable premortem findings. Carry open gap IDs into the design rather than
   claiming they are closed by prose.
6. Obtain approval of the design direction.
7. Write the specification at the repository-defined path. When no path is defined, propose one
   and confirm it with the user before writing. If an approved behavioral baseline exists,
   preserve its requirement and scenario IDs and produce the refined spec required by the local
   workflow. If a specification already exists at that path, review it against the baseline,
   the repository, and the gap registry instead of writing a second one; deliver the findings
   and keep both gates.
8. Self-review the written spec and fix unsupported assumptions, placeholders, contradictions,
   ambiguous behavior, missing negative cases, and traceability gaps.
9. Ask the user to review and approve the written specification.
10. Only after approval, transition to the repository-defined planning workflow.

Do not commit a design or spec unless the user has explicitly authorized a commit.

## Design discipline

- Keep the user's objective and scope fixed. A risk control may constrain an implementation; it
  does not silently create a new product feature.
- Prefer the simplest complete design with a current consumer.
- Reuse compatible repository and sibling implementations before proposing new machinery.
- Separate observable behavior from implementation choices. Put behavior in the spec and design
  choices in the plan unless the choice is externally visible.
- Distinguish verified facts, inherited requirements, assumptions, decisions, and unresolved
  evidence.
- Preserve exact identifiers, versions, hashes, paths, flags, error strings, and claim strength.
- Include boundaries for empty and malformed input, unavailable dependencies, timeout,
  cancellation, cleanup, concurrency, security, and compatibility when they can affect the
  objective.
- Do not present mocks, inspection, or old command output as live integration evidence.
- Re-verify evidence recorded by an earlier artifact against the current tree before the design
  relies on it, and record the date or revision of the check.

## Approval gates

Every path has an approval before action:

- Spike: approve the probe before investigation that creates artifacts or spends external
  resources.
- Bounded: approve the short design before implementation.
- Architectural: approve the design direction before writing the final spec, then approve the
  written spec before planning.

At each gate, list the decisions that only the user can make, with a recommendation for each;
approval is not requested until they are answered or explicitly deferred.

Read-only repository exploration is allowed before approval. Approval for brainstorming or a spec
does not authorize implementation, commits, remote changes, releases, or other external
mutations.

## Premortem integration

Use this section only when a premortem report or gap registry matches the brainstorming
objective.

### Determine relevance

A report is relevant when its subject, target artifact, version, and decision match the current
request. Check its date or source revision and whether later rule, scope, backend, interface, or
baseline changes invalidate it.

If relevance is uncertain:

- State what matches and what may be stale.
- Use findings that remain technically true.
- Do not import conclusions that depend on changed assumptions.
- Recommend a new premortem only when the current trigger policy requires one or the user asks.

### Extract useful evidence

Read the report and any linked gap registry. Capture:

1. The imagined failure and success condition.
2. Prioritized failure causes and their evidence.
3. Preventive controls, early signals, contingencies, and owners when recorded.
4. Changes already applied to the baseline or design.
5. Accepted risks, if the acceptance authority is explicit.
6. Open implementation or external-evidence gaps and their stable IDs.
7. Assumptions, unknowns, handoffs, and review triggers.
8. The "second barrel" or status-quo alternative, including reversibility and the cost of not
   acting.

Do not treat generated causes as verified facts. Preserve their stated confidence and evidence.

### Reconcile with the design

For every relevant finding, classify it as:

- **Already covered:** cite the requirement, scenario, design section, or existing control.
- **Clarification:** tighten an existing behavior without changing scope.
- **Planning obligation:** carry it into a task, gate, owner, or dependency.
- **Implementation gap:** preserve its gap ID and required closure evidence.
- **External evidence:** name the real backend, platform, account, reviewer, or release artifact
  needed to close it.
- **Out of scope:** explain why it does not apply to the approved objective.
- **Scope expansion:** present it separately and require user approval before adding it.

Prose does not close an implementation or external-evidence gap. Update a gap status only after
the cited evidence exists. A closed planning ambiguity may remain an open runtime risk.

### Use with a behavioral baseline

When a behavioral baseline (for example SBTDD's `spec-behavior-base.md` and `spec-behavior.md`)
and premortem artifacts coexist:

1. Treat the behavioral baseline as the source contract.
2. Use the premortem to find missing boundaries, negative scenarios, controls, and evidence.
3. Verify whether premortem corrections are already present in the baseline.
4. Inspect the repository and record evidence for each refinement.
5. Preserve every baseline requirement and scenario ID in the refined spec.
6. Add no behavior solely because the premortem imagined it; obtain approval for new scope.
7. Include a reconciliation table from requirements and scenarios to repository evidence and
   open gap IDs.

If the premortem records an exact sibling revision, pin, fixture hash, or release artifact, carry
that value into the spec. If it records only "latest" or a mutable branch, resolve and record an
immutable reference before treating it as reproducible.

### Required outcome

The design or spec must make clear:

- Which premortem findings changed or constrained the design.
- Which findings were already covered.
- Which gap IDs remain open and what evidence closes them.
- Which assumptions still need user approval or runtime proof.
- Why the proposed path is preferable to the status quo when the report contains a second-barrel
  analysis.

Do not rerun or rewrite the premortem merely to make the design look complete. Preserve the report
as analysis and use the gap registry as the live closure interface.

## Output

Scale the result to the path:

- Spike: question, probe, findings, remaining uncertainty, recommendation.
- Bounded: concise in-chat design and approval request.
- Architectural, at the direction gate: classification, verified evidence, approaches with
  the recommendation, premortem reconciliation, and the user decisions.
- Architectural, after approval: repository-defined Markdown specification with requirements,
  scenarios or acceptance examples, constraints, exclusions, evidence, assumptions, decisions,
  premortem reconciliation, and traceability.

The final artifact must say what is approved, what remains open, and what the next authorized
workflow step is.
