# Changelog

All notable changes to the `premortem` skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in the
[repository README](../README.md#versioning).


## [1.1.0] - 2026-09-21

The ChatGPT package gives way to a Codex one. OpenAI documents a single skill
format for Codex and ChatGPT, so one archive now serves both. The rules of the
skill did not change; the version moves because a release ships a different
package than before.

### Added

- `codex/SKILL.md`, identical to the skill, packaged with
  `codex/agents/openai.yaml` as `codex/premortem-codex.zip`, the layout Codex
  and ChatGPT read. The manifest carries the display name, a one-line
  description, and the `$premortem` prompt. The release gate checks the
  variant's text against the skill and every file in the zip against its
  source.

### Removed

- `chatgpt/SKILL.md` and `chatgpt/premortem-chatgpt.zip`. The Codex package
  carries the same text and is the one to upload to ChatGPT.

## [1.0.0] - 2026-09-21

First release. The skill runs a premortem on a plan in any field: it places
the plan in a future where it has already failed, reconstructs the causes,
prioritizes them, and turns the ones that matter into changes, controls,
early signals, and contingencies, delivered as one complete report. With a
team, it produces the workshop kit and processes the team's notes into the
same report.

### Added

- Scope: any plan that exists and can still change. The minimum is an
  objective, a success criterion, and a horizon; a plan with no measurable
  criterion always gets a question or a labeled assumption. The user's or
  the team's own causes enter first and unchanged; the skill's are labeled.
  Report in the user's language, Markdown by default.
- Two modes: analysis by default, the rigorous one, and facilitation when
  the user will run a session with a team.
- Analysis in eight steps: plan sheet with assumptions and base rates,
  failure scenario in the past tense with no cause embedded, cause
  generation with outsider prompts before a fourteen-category sweep and an
  external pass, cause–event–impact formulation, six-criterion qualitative
  prioritization with a separate catastrophic list, treatments that pass
  the what/who/when/verified/if-not test, the second barrel comparing the
  risks of acting and not acting, and an honesty check that declares
  unknowns and absent expertise.
- Facilitation kit: plan sheet, participant guidance, scenario and mirror
  scenario, rules, a 60–90 minute agenda, silent-writing prompts, register
  template, and the variants (asynchronous, anonymous first round, per
  milestone, success premortem, multi-scenario) as one-line options.
- Domain probes applied after free generation, never as the starting point:
  product and software (adoption, technical debt, integrations and data
  quality, security, capacity, support, vendor dependency, cutover and
  rollback, go/no-go, observability), engineering and operations, strategy
  and investment, public policy, health and implementation, personal
  decisions. Handoffs to FMEA, HAZOP, threat modeling, security review, and
  clinical evaluation named where the plan needs them.
- A table of eleven common failures with the correction for each, applied to
  the skill's own output before delivery.
- Deliverables: header, plan sheet, scenario, causes, prioritized-risk table,
  treatment table, changes to the plan, accepted risks, second barrel,
  unknowns, next review, and a Notes block with every assumption, question,
  skipped step, and rejected cause. The report's prose passes through
  humanize when available, with tables, statements, figures, names, and
  thresholds protected. New files only; never overwrite.
- A ChatGPT package in `chatgpt/`, identical to the skill.
