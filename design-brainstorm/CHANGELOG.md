# Changelog

All notable changes to the `design-brainstorm` skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in the
[repository README](../README.md#versioning).


## [1.0.0] - 2026-09-21

First release. The skill takes an idea, a feature request, or a proposed
behavior change and turns it into the smallest design that satisfies the
objective, then stops for approval before anything gets built. It explores
the repository first, classifies the request, and scales the ceremony to
the classification without ever dropping the approval gate. When premortem
reports or gap registries exist for the same objective, their risks,
controls, and open gaps enter the design with their IDs intact.

### Added

- Three paths, chosen by the user-correctable classification: a spike, whose
  deliverable is an answer; a bounded change to an existing flow, designed in
  chat; and an architectural change, which gets two or three approaches with
  trade-offs, a sectioned design, and a written specification at the
  repository-defined path. A specification already at that path is reviewed
  against the baseline, the repository, and the gap registry, not rewritten.
  When uncertain, the heavier path; upgrades happen when inspection reveals
  hidden complexity, downgrades never.
- Context first: repository rules, active spec and plan, implementation,
  tests, public interfaces, recent history, existing baselines, and premortem
  artifacts, searched in the declared process directories and including
  gitignored files. Questions only when the answer changes behavior or scope,
  one at a time; what the repository already answers becomes a disclosed
  assumption.
- Design discipline: fixed objective and scope, simplest complete design with
  a current consumer, reuse before new machinery, behavior separated from
  implementation choices, facts distinguished from assumptions and decisions,
  exact identifiers and claim strength preserved, boundaries for empty and
  malformed input, unavailable dependencies, timeout, cancellation, cleanup,
  concurrency, security, and compatibility. Evidence inherited from an earlier
  artifact is re-verified against the current tree before the design relies
  on it.
- Approval gates per path, with read-only exploration allowed before them.
  At each gate the decisions only the user can make are listed with a
  recommendation, and approval waits until they are answered or deferred.
  Approval of a design or a spec authorizes nothing else: no implementation,
  commits, remote changes, or releases.
- Premortem integration: relevance check against subject, artifact, version,
  and date; evidence extraction including the second barrel; each finding
  classified as covered, clarification, planning obligation, implementation
  gap, external evidence, out of scope, or scope expansion. Prose never
  closes a gap. A section for repositories with a behavioral baseline, such
  as SBTDD, preserves every requirement and scenario ID in the refined spec.
- Output scaled to the path, always stating what is approved, what remains
  open, and what the next authorized workflow step is. The direction gate of
  an architectural change presents classification, verified evidence,
  approaches with the recommendation, premortem reconciliation, and the user
  decisions. The work happens in the user's language.
- A Codex package in `codex/`, identical to the skill plus
  `agents/openai.yaml`; the same package serves ChatGPT.
