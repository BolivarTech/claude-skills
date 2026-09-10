# Changelog

All notable changes to the `humanize` skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in the
[repository README](../README.md#versioning).


## [1.1.0] - 2026-09-10

Improve on humanize rules.

### Added

Advanced levers for deep humanization was added with rules to improve the reading

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
