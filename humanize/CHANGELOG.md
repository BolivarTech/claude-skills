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

- A fallback for when there is nobody to ask. A single-turn call or a batch job has no
  reply channel, and the three flagged operations do not become permitted because the
  question cannot be delivered: the edits still happen, those three still do not, and what
  would have been raised goes at the end of the output.
- The exemption that says naming one of these characters is not using one. Quoting a line
  to show the tell is discussing the mark, not emitting it. Left unstated, it drew the same
  false finding from every reviewer who read the file.

- Errors, voice and tells as three separate things. A tell goes, an error gets fixed, and
  voice stays even where it breaks a rule on the page. The document had no instruction for
  a plain mistake at all, and its only mention of grammar listed flawless grammar as a
  tell, so a draft with a slipped agreement got nothing. Where an intended fragment and an
  accidental one cannot be told apart, it counts as voice: that error costs a small
  roughness, the other edits a person's style out from under them.
- The rule that the levers which *add* only run while you are drafting. Dropping in a
  fragment or a contraction is writing; doing it to somebody else's finished text is
  manufacturing the marks the imperfections lever forbids. The reconciliation existed in
  three places and had never been stated once.
- A batch output says at the top that the pass is incomplete, not only at the bottom what
  is missing. A pipeline strips a trailing note and hands the text on as final.

### Changed

- The opening states the thesis instead of implying it: these are rules for writing well,
  and defeating AI voice is what happens when they are followed. A draft a person typed
  belongs here too, because human writing is not automatically good writing. Elegant
  variation was a named fault a century before anything generated text.

### Fixed

- The laundered-attribution paragraph still said to drop the frame and make the claim in
  your own voice, which is the operation the content-change table puts on the question
  side. Building that table updated the hedging lever and the example and left this
  paragraph behind. It now raises the frame instead of removing it.
- Whose draft it is was assumed rather than established, right after a rule that turns on
  the answer. Text produced in the conversation is yours to shape, text the person pasted
  in is theirs, and an unclear case is treated as theirs until they say otherwise.
- The register test contradicted itself in three consecutive sentences. "If all four are
  absent" and "one instance of any one clears it" were followed by "one of each is all the
  rule ever needed", which reads as requiring all four. Presence of any one clears it.
- The before-and-after examples taught what the rules forbid. Their rewrites invented a
  build pipeline, three weeks, six months of production, four retention points and a
  cohort, none of which appeared in the text being rewritten, and one of them swapped the
  original assertion for a different one. Every rewrite is now built only from what its
  own "before" contained, and the vague opener has no rewrite at all, because prose
  carrying no facts cannot be made specific without borrowing facts from somewhere. The
  laundered-attribution example now demonstrates the edit-versus-question split instead of
  contradicting it.
- The character scan overrode the writer's own semicolons. The voice rule wins.
- The character scan called itself mechanical and left the impression that reading for the
  characters was enough. Finding every instance of a mark in a long draft is what a find
  box is for, and reading for them misses one nearly every time. Search, do not skim.
- Inference and questioning read as competing instructions in the guardrails. Inference
  raises the question; it never answers it.

### Removed

- Twelve lines of restatement. The punctuation block named the two media and their
  examples a second time inside the em-dash bullet, and told the Word autocorrect story
  twice, once for dashes and once for quotes. The autocorrect note is now one bullet
  covering the whole family, which is also where it belonged.
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

- The line between an edit and a question. Three operations the levers find are real
  improvements and still change what the text asserts or who asserts it: deleting a weak
  claim, stripping a borrowed attribution, and removing a hedge. They are now named in
  the reply for the writer to decide, not performed. Collapsing a stack of qualifiers
  stays an ordinary edit, since it leaves the assertion at the same strength.

### Changed

- The guardrails no longer wait to be told. A request rarely announces that it falls
  outside the limits, it shows it, so the rule now reads the shape of the ask and settles
  it with one question before writing.
- The voice profile names whose voice it is: the person who will sign the text. Building
  toward anyone else's is the impersonation the guardrails rule out, decided at the
  profile step rather than discovered later.
- The em-dash section separates the output rule from the input diagnostic. What to emit
  is settled by the medium alone and Word changes nothing about it; what an em-dash tells
  you about a draft you are reading is weaker in a document Word autocorrected. Mixing
  the two read as licence to emit them.
- The specificity lever says where a missing number gets reported: in the reply, never as
  an annotation left inside the deliverable.
- The guardrail question holds one stance instead of two. It asked, then told the reader
  both to take the answer at face value and not to be credulous, which is no instruction
  at all. It now asks once and believes the answer, on the grounds that someone who
  answers falsely takes the responsibility with it and no amount of interrogation would
  stop them anyway.
- The character scan states its target per medium, matching the rule it enforces: zero in
  casual text, one or two in edited long-form. Left open, it stripped long-form pieces to
  zero and contradicted the allowance above it.
- Rederiving a blacklist for another language has a procedure: the writer's own drafts,
  then what a model overproduces in that language, then an honest note that coverage is
  thin. A translated list flags words the target language does not overuse and misses the
  ones it does.
- The register test asks presence, not counts. It listed four things to tally, which is
  arithmetic over a long draft and comes back different each run. The rule only ever
  needed one of each to clear, so it now asks whether each appears at all. The character
  scan and the repetition check drop their counts for the same reason.
- Casual text and edited long-form get a test instead of being assumed. Several
  punctuation rules split on that distinction and none of them said how to decide it: the
  question is whether anything stands between the typing and the reader. Unclear cases
  default to casual, because a long-form piece with zero em-dashes loses a little polish
  while a casual message with two loses the point of the pass.
- An unanswered question is not a yes. The guardrail asked one question and handled only
  a clear answer; a reply that dodges, that settles nothing, or a person who insists after
  being declined now lands on the prohibited branch rather than on the model's improvisation.
- Where the subject noun is also the sentence opener, both repetition rules land on one
  word. The fix is to move the subject, not rename it.
- The voice profile takes precedence over the levers. Where a lever would push the text
  away from the profile it does not apply, so a terse writer does not acquire asides and
  a formal one does not acquire contractions.
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
