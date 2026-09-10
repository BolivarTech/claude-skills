# Changelog

All notable changes to the `humanize` skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in the
[repository README](../README.md#versioning).


## [1.1.0] - 2026-09-10

Additions folded into the existing levers, and the removal of a detour into detector
evasion.

### Added

- A voice profile as the first step, before any sentence is touched. The levers now
  have a target to aim at. Without one they drift toward generic informality, which is
  a register of its own and a machine's.
- The point that word substitution alone fixes nothing. Swapping a blacklisted word for
  its plain synonym leaves the sentence with the shape that gave it away, so a line that
  reads generated gets rewritten rather than re-worded.
- Unresolved digressions and ideas raised then dropped, as marks worth preserving, with
  the boundary against the cut-filler lever written out: a digression that shows how the
  writer got somewhere stays, one that shows nothing goes.
- The writer's own figure of speech, under the same constraint that already governs an
  exact number. An invented comparison is the same cheat as an invented statistic.
- A lever for sentence shape, separate from sentence rhythm, carrying the three axes a
  draft can be flat on independently: how the sentence opens, clause complexity, and
  voice. Fifteen sentences that all start on the subject read uniform however much their
  lengths vary, and every opener can differ while every sentence stays a single clause.
- Passive voice as a legitimate choice when the patient is the topic. Style guides say
  avoid it, models trained on them write almost none, and a draft with zero passive
  constructions is as uniform as one with zero short sentences.
- A counterweight to the specificity lever, matching the one the rhythm lever already
  carried. Applied to every sentence, specificity yields prose where each line holds a
  figure, which is uniformity that passes for rigor. Density is meant to vary.
- Inarticulate doubt, distinct from the attributed kind already covered: a writer
  circling something they cannot name, saying it several ways because none of them fits.
  It is not elegant variation, and a model does not produce it.
- Absence as a tell. The lists here catalogue what a model overproduces, but casual
  writing carrying none of the small oral markers a person drops in reads just as
  machine-made. Spanish shows this more plainly, where a text with no *bueno*, *o sea* or
  *pues* reads translated even when every word is right.
- Dropping a connective entirely and letting two sentences sit side by side, as an
  alternative to replacing a formal transition with a plain one.

### Changed

- Register now holds explicitly at the level of the document. A single word out of
  register inside a sentence is a person reaching for the word they think in, not drift.
- The imperfections lever states that *keep* is its verb. Preserving what a draft
  carries is the instruction; manufacturing asides, self-corrections or typos is
  fabrication under the same rule that forbids an invented number.

### Removed

- The detector-evasion material, including the advice to tune a draft against GPTZero or
  Originality.ai. The stated goal is prose that reads well to a person; optimizing
  against a classifier pulls toward the overcorrected register the skill already warns
  about, and aims at a judge nobody controls.
- The instruction to insert typos, staged self-corrections and conversational filler.
  These degrade the writer's work and contradict both the cut-filler lever and the rule
  against inventing what the writer did not say.
- Roughly ninety lines that restated levers already present, in cruder form and without
  the reasoning that made the originals useful.

### Fixed

- An em-dash used as ordinary punctuation inside an example offered for imitation, in a
  skill whose loudest rule is to default to zero of them.
- A grammatical slip ("If a sentence for looks like") in a section about writing
  quality.
- The hedging lever ordered the content change the fidelity boundary forbids. "State
  what you know flatly and strip the qualifiers off it" is not executable by an editor
  working on someone else's draft, who cannot know what the writer knows, so the only
  reading left was to strip every qualifier and turn hedges into guarantees. It now
  names a test readable in the text itself, keeps a hedge that carries a reason or a
  source, collapses a stack to one qualifier instead of deleting it, and escalates the
  undecidable case to the writer.
- The em-dash rule rested on a wrong reason. "Most people cannot type one" overstates
  it, and the autocorrect carve-out below it covered curly quotes while omitting the
  character the rule is about, even though Word and Docs substitute an em-dash for a
  spaced hyphen by default. The guidance stands; the justification now says what is
  actually true, and the carve-out names the em-dash.
- "Absence is a tell" had no test, so nothing could contradict it. It now carries a
  four-item count scoped to casual first-person text, says that zero of all four is the
  only reading the count supports, and states that a flat register in someone else's
  draft is raised with the writer rather than patched by sprinkling markers in.

### Changed

- The guardrails moved from the last section to the second, ahead of the fidelity
  boundary, and gained a refusal protocol: name the limit in one sentence before writing
  anything, offer the nearest legitimate alternative, and never ship the text with a
  disclaimer attached, since the disclaimer does not travel with it.

## [1.0.0] - 2026-08-28

First published version.

### Added

- A fidelity boundary that scopes the pass to running prose. Facts, numbers, versions,
  flags, paths, claim strength, code blocks, signatures, error messages and UI strings
  are out of bounds, which is what makes the skill safe to run over a README or a
  changelog instead of only over first-person writing.
- Guidance for languages other than English, with the Spanish tells worked out and the
  two checks English does not need: register drift between tú and usted, and rhythm
  inherited from a translation.
- A repair for the rhythm the cut pass flattens. Deleting filler pulls every sentence
  toward the mean, so the fix after a heavy cut is to join two short sentences that are
  really one thought, not to sprinkle in fragments.
- Laundered attribution as a named tell: "many experts believe", "it is widely accepted
  that", "most people think".
- Self-explanation and stage directions as a structural tell.
- Nine entries on the blacklist: solid, comprehensive, revolutionary, "that being said",
  "it goes without saying", "in short", "looking ahead", "in general terms" and
  "it's important to note".

### Changed

- The signal model now counts two statistical signals rather than three. Elegant
  variation moved to the surface tells, where it belongs, since no detector measures it.
- Lever 2 no longer pulls toward inventing detail. Specificity has to come out of the
  writer's material, and a plausible invented figure is worse than the vague sentence it
  replaced.
- "Not only X, but also Y" is banned as a construction rather than as a word pair.
- The blacklist split into four subsections, so the reasoning on optimal ordering and on
  hedging is no longer buried inside a third-level bullet.

[1.0.0]: https://github.com/BolivarTech/claude-skills/releases/tag/humanize-v1.0.0
