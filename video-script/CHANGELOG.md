# Changelog

All notable changes to the `video-script` skill. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions
follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in
the [repository README](../README.md#versioning).


## [1.0.1] - 2026-09-15

Aligned with the general production guide the skill's defaults derive from.

### Changed

- The production-instructions intake item now names the eight fields a
  project's document fixes: project and piece code, platform and delivery,
  tools per function, voices and markup, segment limits, asset references,
  master-script format, and canon order.
- The lip-sync limit states when it does not apply: a piece that shows
  characters in attitude, from behind, or in detail uses no lip sync.


## [1.0.0] - 2026-09-15

First release. The skill turns a narration, story, treatment, or research
dossier into a production-ready audiovisual script, or reviews an existing
script, shot list, storyboard, animatic, or cut plan, and on request applies
the corrections it found. The criteria come from a guide on adapting narration
and reviewing screen works and from a production-instructions document for an
audio-first pipeline. The skill is project-neutral: a project's own production
instructions govern names, limits, tools, and delivery, and the built-in values
are defaults labeled as proposals.

### Added

- Three modes: convert, review, and review and revise. A combined request
  converts first and reviews the result. Ordinary production choices are made
  without asking; uncertain project data is marked `PENDIENTE`.
- A statement of what the skill can read: text and still images only. A cut is
  reviewed through transcripts, timeline exports, frames, or the user's notes,
  and any pass without evidence in the material is reported as not assessable.
- Intake: source hierarchy and canon authority, target, an explicit fidelity
  hierarchy, production frame, whether audio already exists, output scope, and
  rights before anything else.
- A thirteen-step adaptation method: extraction reading from four
  perspectives, the central-experience sentence, adaptation thesis,
  audiovisual motor, point of view and device, sequence map, translation of
  interiority with the voiceover rule, the eight adaptation operations with
  their canon record, spoken text written for breath and performance, a
  duration rule (existing audio first; otherwise 150 words per minute for
  Spanish narration, labeled `ESTIMADO` with a 10% margin), complementary
  channels, the development ladder, and a self-review before delivery.
- A format table for shorts, features, series, documentary, animation and
  generated imagery, archive, educational, music, vertical and social, and
  interactive pieces, with a check on the opening hook and chapter boundaries
  for streaming and social targets.
- The audio-first workflow in six steps, with the rule that no shot or asset
  duration is assigned before establishing whether audio exists.
- Image, sound, editing, and previsualization criteria: the reason behind a
  shot, geography before discontinuity, continuity tracking for generated
  material, sound layers and perspective, music judged by function, entry and
  exit points, and intention-led shot lists.
- A review method with a stage table stating what each stage allows to assess,
  seven passes in order, and a finding format with identifier, priority,
  confidence, location, evidence, mechanism, impact, minimal correction,
  alternatives, what to preserve, and how to verify. Priority is separate from
  confidence.
- A table of twenty-one frequent artifacts, each with a diagnostic test and a
  correction target, from literal prose translation to technical correction
  that erases intention.
- Production instructions as an intake item: when the project supplies them,
  they govern every production value in the deliverable.
- The production master-script format: its ten-part order, style rules, state
  labels (`VERIFICADO`, `CONFLICTO`, `PENDIENTE`, `CONFIRMADO`), default
  production constraints (asset naming, generated video and lip-sync segment
  limits, caption rules, delivery specifications) that a project's instructions
  replace, and the full template with the default headings and markup.
- Deliverables for each mode, a revision plan ordered by dependency, and an
  Applying Corrections section that freezes facts, quotations, timings, and
  identifiers, edits only cited passages, and rechecks downstream totals.
- Conditional use of the narrative-review skill for the narrative pass on
  fiction and of the humanize skill on newly drafted spoken text only.
- A ChatGPT package in `chatgpt/`, identical to the skill.
