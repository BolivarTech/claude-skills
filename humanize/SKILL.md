---
name: humanize
description: >-
  Rewrite existing prose with a natural, consistent voice, varied rhythm, plain
  language, and fewer formulaic AI patterns. Use when the user asks to humanize,
  de-robotify, make text sound natural or less like AI, or improve first-person
  writing such as emails, applications, posts, essays, cover letters, and bios.
  Use for editing an existing draft, not composing from notes or from scratch.
license: MIT OR Apache-2.0
metadata:
  version: 4.1.0
---

# Humanize

Edit existing prose. Do not expand notes into a draft or compose new content;
treat any requested expansion as a separate task. Work from the writer's facts,
vocabulary, stance, and certainty, regardless of who drafted the text. Edit the
writing; do not manufacture a persona. Human writing can still be stiff,
repetitive, vague, or overworked. Improve structure before substituting words.

## Meaning and voice

The pass is editorial, not semantic: change rhythm, syntax, word choice, sentence
length, paragraph entry, and presentation, never what the text asserts or who
asserts it. Rewrite running prose only. Unless the user authorizes content
changes, preserve facts, names, numbers, dates, versions, paths, flags, commands,
and meaningful order, including chronology and argument dependencies; the breadth
and strength of claims, attribution, uncertainty, and its reasons; code blocks,
inline code, signatures, identifiers, structured docstring fields, reference
tables, command examples and output, error messages, UI strings, and technical
symbols such as `×`, `÷`, and `≈`. Preserve direct quotations verbatim,
punctuation included, unless the user explicitly asks to edit them; a request to
humanize the surrounding text does not cover the quote.

Infer audience, medium, formality, verbosity, grammatical person, contractions,
and regional or domain vocabulary from the request and source. Keep one register
across the document and preserve the existing one when no preference is given:
formal writing need not become chatty, and useful technical terms stay. Keep
each passage in the language it was written in.

Never invent opinions, anecdotes, comparisons, reactions, habits, or specific
facts; use details from the supplied material or keep the wording general.
Preserve informative asides and useful irregularities, but correct mistakes. Do
not add typos, false starts, fragments, or awkwardness to simulate a person.

Do not delete a weak claim as filler, transfer an attributed claim to the writer,
or strengthen a hedge. Collapse redundant qualifiers only at the same certainty:
"may potentially possibly reduce X" can become "may reduce X", never "reduces X".
If a qualifier's effect is unclear, preserve it. Ask only when missing
information prevents completion and cannot be handled by preserving the source or
using existing context; optional improvements need no approval and do not make an
edit incomplete.

## Editorial checks

Review the entire text for meaning, voice, structure, rhythm, filler, repetition,
and vocabulary; a first impression of naturalness does not excuse the review.
Apply changes that fit the voice and address a problem in the draft, and return
the original only when the full review finds no justified improvement. Do not
maximize variation or force every sentence into a new shape.

- **Rhythm:** Vary openings, clause complexity, and sentence length. If more than
  half the sentences cluster around 12 to 20 words, shorten some and let others
  develop. Do so by cutting, reordering, joining, or splitting existing
  sentences; do not add explanations, examples, or transitions to vary length,
  nor manufacture fragments, parentheticals, or unusual syntax. Passive voice is
  appropriate when the affected thing is the topic or the actor is unknown or
  irrelevant. After removing filler, join short sentences that form one thought
  if the rhythm has gone flat.
- **Paragraphs:** Address repeated topic/support/conclusion structures, identical
  paragraph lengths, excessive headings, mechanical three-part lists, and
  consecutive paragraphs that open with the same subject; vary those by opening
  with the object, a circumstance, or the verb, not by renaming the subject.
  Open with an existing example, consequence, number, or objection where it
  helps.
  Keep the writer's distribution of emphasis unless the source supports a change.
- **Filler:** Remove empty framing ("It's worth noting"), stage directions ("Let
  me break this down"), redundant closers, and decorative asides only when
  removal changes neither information nor claim strength. A familiar phrase may
  carry certainty, emphasis, or stance: "I care about quality" is a personal
  claim, even if vague.
- **Constructions:** Rewrite "It's not just X; it's Y", "This isn't about X; it's
  about Y", and "Not only X, but also Y", preserving both halves and the
  contrast between them: recast the pair
  as a plain conjunction or as two sentences, keeping neither half of the frame,
  not "not only", "not just", or "no solo", and not "but", "sino", or
  "también"; a colon or dash in place of "sino" keeps the construction. Break repeated tricolons without
  dropping claims. In casual prose, replace formal transitions
  such as *furthermore*, *moreover*, and *consequently* with plain connectives or
  omit them. Whatever the register, a replaced or removed transition keeps its
  logical relationship.
- **Vocabulary:** Prefer plain verbs and exact nouns, such as *use* over
  *utilize*. Scan for *delve*, *tapestry*, *leverage*, *seamless*, *foster*,
  *elevate*, *unlock*, *holistic*, *game-changer*, *cutting-edge*, and "in
  today's fast-paced world". These are contextual signals, not a substitution
  table: replace wording for imprecision, redundancy, or register mismatch. A
  superlative, intensifier, or evaluative adjective is part of the claim's
  strength; drop it only when another word in the sentence already carries it.
  Prefer a structural rewrite to a synonym where it helps more.
- **Repetition:** Keep the correct subject noun rather than rotating through
  "system", "platform", "solution", and "tool". Fix monotonous openings and
  connectives by changing sentence construction, not the subject's name.

## Character handling

Scan editable prose last for `—`, `–`, `--`, `…`, `“`, `”`, `‘`, and `’`, with a
search or regular expression when available, excluding protected material and
direct quotations from the search before replacing anything, and correct
matches contextually.
Rewrite sentences that use an em dash or `--` as a separator, preferring a
period, comma, parentheses, or colon over another dash; a dash that opens or
closes dialogue, as in Spanish, is punctuation and stays. Replace
prose-separator en dashes with a hyphen or restructure; `2010–2015` may become
`2010-2015`. Replace curly quotes with straight quotes and `…` with `...` in
ordinary prose. Leave typography inside protected material and direct
quotations unchanged.

## Other languages

Apply the same structural and semantic criteria, but do not translate the
English word list mechanically; derive local patterns from native drafts when
available and otherwise avoid claiming complete coverage.

For Spanish, inspect potentially empty framing ("es importante destacar", "cabe
mencionar", "en el mundo actual"), stage directions ("a continuación
analizaremos", "veamos"), automatic *por ende* or *asimismo*, repeated
closing gerunds ("logrando así", "permitiendo"), shifts between *tú* and *usted*
or verb persons, and English sentence patterns in translations. Oral markers
such as *bueno*, *o sea*, and *pues* must fit an existing informal voice, region,
and context; never insert them as a quota. "Sin duda alguna" can express
certainty: removing it from "Sin duda alguna, esta es la mejor opción" weakens
the writer's stated confidence even though the core claim remains. Preserve it
unless the context shows its force is redundant and fully retained.

## Workflow and delivery

1. Identify voice, audience, medium, and register.
2. Freeze protected material and flag any change that could alter claims,
   attribution, certainty, or meaningful order.
3. Edit structure, language, rhythm, repetition, and characters, in that order.
4. Compare source and result for meaning and register drift, invented material,
   repetition, rhythm after deletions, and unnecessary growth.

Stop when the relevant problems are addressed; constant contractions, asides, or
fragments create another artificial register. Preserve or reduce length,
allowing only the minimal increase needed to avoid ambiguity, preserve meaning,
or state a supplied fact precisely; add no unrequested summaries, restatements,
or explanations. Do not add a title, unsolicited questions, lists of missing
details, or incomplete-pass labels for optional edits, before or after the text. Assess internally and return the
edited text without explaining individual decisions unless the user asks for an
analysis.

## Examples of semantic boundaries

- "Many experts believe this approach may potentially improve retention."
  becomes "Many experts believe this approach may improve retention."
  Attribution and uncertainty remain.
- "The system is reliable" must not become "The system stays up": the latter
  narrows the claim.
- "In today's fast-paced world, I am passionate about leveraging cutting-edge
  solutions to drive impactful results" permits removing empty framing, but the
  personal claim stays and specificity requires facts from the source.
- A quotation that reads "he called the plan “final”" keeps its curly quotes
  even when the surrounding prose is normalized to straight ones: the
  characters inside a quotation are part of what was said.
- Three consecutive paragraphs beginning "The report…", "The report…", "The
  report…" become, for instance, "The report…", "In its second part, the
  report…", "What the report leaves out…": same subject, different entry
  point.
