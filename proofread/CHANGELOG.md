# Changelog

All notable changes to the `proofread` skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in the
[repository README](../README.md#versioning).


## [1.0.0] - 2026-09-23

First release. The skill proofreads a finished text in Spanish or English: it
corrects what the norm declares wrong in spelling, accents, grammar,
punctuation, and typography, and leaves style, voice, rhythm, and content
alone. It is the last pass of the writing workflow, after humanize, and of a
production script.

### Added

- An order of authority: the project's style guide or the author's declared
  criteria first, then RAE and ASALE for Spanish (*Ortografía* 2010, the
  *Diccionario panhispánico de dudas* 2nd edition, the RAE *Libro de estilo*)
  and *The Chicago Manual of Style* 18th edition with Merriam-Webster for US
  English. A British text keeps its variant. Where the norm allows options,
  the text's majority choice is applied everywhere.
- Rules verified against those sources in September 2026, among them the
  current status of the accent on *solo*, Latin phrases in italics, the
  dialogue raya, and Chicago 18's capital after a colon before a complete
  sentence.
- A boundary with humanize: proofread corrects errors, never style, and never
  adds a new em dash in English, where the dash is also a sign of generated
  text. Errors inside dialogue may be characterization and are flagged, not
  changed.
- Scripts: words inside SSML are corrected and tags stay byte for byte, a
  project convention on accents wins over the norm, and figures or acronyms
  that will be read aloud are checked for how they sound.
- Deliverables: the corrected text in a new file beside the original, with the
  same line endings, and a report listing every change with its rule, the
  doubts left for the author, and the criteria applied. An "only review" mode,
  on request, reports without touching the text.
- `codex/SKILL.md`, identical to the skill, packaged with
  `codex/agents/openai.yaml` as `codex/proofread-codex.zip` for Codex and
  ChatGPT.
