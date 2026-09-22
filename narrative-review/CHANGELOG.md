# Changelog

All notable changes to the `narrative-review` skill. The format follows
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
  `codex/agents/openai.yaml` as `codex/narrative-review-codex.zip`, the layout Codex
  and ChatGPT read. The manifest carries the display name, a one-line
  description, and the `$narrative-review` prompt. The release gate checks the
  variant's text against the skill and every file in the zip against its
  source.

### Removed

- `chatgpt/SKILL.md` and `chatgpt/narrative-review-chatgpt.zip`. The Codex package
  carries the same text and is the one to upload to ChatGPT.

## [1.0.0] - 2026-09-15

First release. The skill reads a story, synopsis, scene, screenplay, or
interactive route, reconstructs its promises and causal chain, and returns a
prioritized, evidence-based diagnosis with the smallest correction for each
cause. On request it applies the corrections it found, finding by finding.

### Added

- Scope rules: identify the material, the author's intent, and the inferred
  conventions; mark what a fragment or synopsis cannot prove as not assessable.
- A lens table for causal, transformation, tragic, accelerated, screenplay,
  scene-level, contemplative, temporal, equilibrium, oral, ensemble, and
  interactive designs. No template is imposed.
- Criteria for promises, twists, weak twist forms, unreliable narrators, and
  the difference between deus ex machina, diabolus ex machina, and a prepared
  complication.
- The modes a passage can rely on (suspense, surprise, mystery, curiosity),
  dramatic irony, MacGuffin, cliffhanger, the five requirements of tension,
  and a five-condition audit of the ending for stories that resolve a conflict.
- A table of twenty-four devices with the evidence that makes each a problem
  and the alternative to rule out before assigning the label.
- Subplots, active settings, non-personal opposition, conflict between
  legitimate values, the disillusionment arc, and the note that a direct
  confession can carry more drama than subtext.
- Dialogue checks: each line pursues something, physical action anchors the
  exchange, tags stay plain unless a variation adds meaning, emotion shows in
  behavior before the narrator names it, and quick exchanges alternate with
  pauses. A quiet exchange still has someone who wants something; conflict is
  not required in every scene.
- A five-step verification per finding, priority separated from confidence,
  and a diagnostic checklist covering structure, characters, information,
  scenes, and coherence.
- A report format: verdict and scope, strengths to preserve, status by area,
  prioritized findings, and a revision plan ordered by dependency.
- An Applying Corrections section: rewrite only selected findings, touch only
  the cited passages, imitate the neighboring voice in every inserted line,
  keep the factual content of a planted rule or clue fixed, deliver the full
  text with a per-finding change log, and run a second review on the result.
  When the humanize skill is available, it polishes the inserted lines only,
  with the author's text supplied as protected material for voice.
- A ChatGPT package in `chatgpt/`, identical to the skill.
