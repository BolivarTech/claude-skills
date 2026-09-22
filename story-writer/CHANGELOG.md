# Changelog

All notable changes to the `story-writer` skill. The format follows
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
  `codex/agents/openai.yaml` as `codex/story-writer-codex.zip`, the layout Codex
  and ChatGPT read. The manifest carries the display name, a one-line
  description, and the `$story-writer` prompt. The release gate checks the
  variant's text against the skill and every file in the zip against its
  source.

### Removed

- `chatgpt/SKILL.md` and `chatgpt/story-writer-chatgpt.zip`. The Codex package
  carries the same text and is the one to upload to ChatGPT.

## [1.0.0] - 2026-09-16

First release. The skill writes a literary story from at least one idea, or
from a dossier with characters, world, and ending already decided, following
a ten-step construction from promise to ending audit. The story is then
reviewed, corrected where a finding survives verification, passed through
humanize, and delivered with a sheet of the decisions that shaped it.

### Added

- Scope: one idea at minimum; supplied characters, world, scenes, endings,
  and voice samples are canon and enter organically, never contradicted or
  listed as decisions. Gaps are filled and declared. Story in the user's
  language, Markdown by default.
- The ten construction steps: promise, engine, five milestones, compatible
  model, cause-and-effect chains, a private knowledge table, scenes with
  change, rhythm, ending audit, and breaking the template only with a reason.
- A model table by main need with a control question per row, and a twist
  design method with the forms to avoid.
- Length: 2,000 to 10,000 words by default, decided by the premise; no hard
  ceiling; parts proposed only when the causal chain needs more than one
  delivery. A target in minutes converts at 150 words per minute and is
  declared as an estimate. A premise that closes below the range is
  delivered at its own length and declared, never filled.
- Prose rules: voice inferred or imitated from a supplied sample, third person
  past by default and declared, emotion through behavior, exposition only
  where it changes a decision, and the guide's list of shortcuts ruled out.
- Professional dialogue: five principles, action-anchored lines, `dijo` as the
  base tag, no infodumps or on-the-nose lines; the Spanish em-dash format with
  its tag cases and a worked example. The em dash of dialogue is declared as
  punctuation the humanize skill leaves alone.
- Three review passes before delivery: a self-audit from the diagnostic list;
  narrative-review run on the story with every finding verified, corrected
  only when real and rejected with a reason when not; humanize as the final
  pass with dialogue protected.
- Deliverables: the story, then a sheet with promise, engine, model,
  milestones, length, point of view, decisions, ending audit, and review
  results. A plan-only mode. When the story goes to a file, the sheet goes
  beside it as `<name>.ficha.md`. New files only; never overwrite.
- A ChatGPT package in `chatgpt/`, identical to the skill.
