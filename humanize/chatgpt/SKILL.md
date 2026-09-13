---
name: humanize
description: >-
  Rewrite existing prose so it sounds natural, specific, and appropriate to its
  audience while preserving the writer's meaning and voice. Use when a user asks
  to humanize, de-robotify, or make an existing draft sound less formulaic.
license: MIT OR Apache-2.0
metadata:
  version: 4.2.1
---

# Humanize

Edit existing prose. Do not turn notes into a draft or add new content. Work from
the writer's facts, vocabulary, stance, certainty, audience, medium, and register.
Improve structure before substituting words. Formal writing need not become casual.
Keep each passage in the language it was written in.

## Meaning and voice

The pass is editorial, not semantic. Preserve facts, names, numbers, dates,
versions, paths, commands, meaningful order, claim strength, attribution,
uncertainty, and its reasons. Leave code, code blocks, inline code, signatures,
identifiers, structured fields, tables, command examples and output, error
messages, UI strings, technical symbols, and direct quotations unchanged unless
the user explicitly requests their revision.

Do not invent facts, opinions, anecdotes, comparisons, reactions, habits, or a
persona. Keep useful irregularities and informative asides; correct mistakes, but
do not add typos, false starts, fragments, or awkwardness to simulate a person.
Do not delete a weak claim as filler, transfer an attributed claim to the writer,
or strengthen a hedge. Collapse redundant qualifiers only at the same certainty:
"may potentially possibly reduce X" may become "may reduce X", never "reduces X".
If the effect of a qualifier is unclear, preserve it.

Ask only when essential information is missing and cannot be handled by preserving
the source or using the existing context. Optional improvements do not need approval.

## Review and edit

Review the whole text for meaning, voice, structure, rhythm, filler, repetition,
vocabulary, and register. Change a pattern only when it creates mechanical
repetition, hinders reading, or clashes with the voice or medium. Its presence
alone is not a defect. Return the original only if the complete review finds no
justified improvement.

- **Rhythm:** Vary openings, clause complexity, and sentence length. If more than
  half the sentences cluster around 12 to 20 words, shorten some and let others
  develop, by cutting, reordering, joining, or splitting existing sentences. Do
  not add explanations, examples, or transitions merely to vary length. Use passive voice when the affected thing is the topic or the actor
  is unknown or irrelevant.
- **Paragraphs:** Address repeated structures, excessive headings, identical
  paragraph shapes, and mechanical lists only when they affect reading. Preserve
  chronology, dependencies, and the writer's emphasis.
- **Filler:** Remove empty framing, stage directions, redundant closers, and
  decorative asides only when they add no information or claim force. Familiar
  phrases can convey certainty, emphasis, or stance; they are not automatic filler.
- **Constructions:** Rewrite "It's not just X; it's Y", "This isn't about X; it's
  about Y", and "Not only X, but also Y", preserving both halves and the contrast
  between them: recast the pair as a plain conjunction or as two sentences, keeping
  neither half of the frame, not "not only", "not just", or "no solo", and not
  "but", "sino", or "también"; a colon or dash in place of "sino" keeps the
  construction. Break mechanical tricolons without dropping claims. In casual
  prose, simplify formal transitions that clash with the register; whatever the
  register, a replaced or removed transition keeps its logical relationship.
- **Vocabulary:** Prefer plain verbs and exact nouns. Treat *delve*, *leverage*,
  *seamless*, *foster*, *elevate*, *unlock*, *holistic*, *game-changer*, and
  *cutting-edge* as signals to inspect, never as automatic substitutions.
- **Repetition:** Keep the correct subject noun. Fix repeated openings and
  connectives by changing sentence construction, not by rotating synonyms.

Scan editable prose last for `—`, `–`, `--`, `…`, `“`, `”`, `‘`, and `’`, excluding
protected material and direct quotations before replacing anything. Rewrite
sentences that use an em dash or `--` as a separator, preferring a period, comma,
parentheses, or colon over another dash; a dash that opens or closes dialogue, as
in Spanish, is punctuation and stays. Replace prose-separator en dashes with a
hyphen or restructure; `2010–2015` may become `2010-2015`. Replace curly quotes
with straight quotes and `…` with `...` in ordinary prose. Leave typography inside
protected material and direct quotations unchanged.

## Other languages and delivery

Apply the same semantic and structural criteria in every language. Do not translate
the English word list mechanically. In Spanish, inspect empty framing, automatic
*por ende* or *asimismo*, repeated closing gerunds, *tú*/*usted* drift, and English
sentence patterns in translations. Oral markers must fit the writer's region and
voice. "Sin duda alguna" can express certainty and should remain unless its force
is fully retained elsewhere.

Compare the result with the source for meaning drift, invented material, register,
repetition, and rhythm after deletions. Preserve or reduce length. Allow only the
minimal growth required to avoid ambiguity, preserve meaning, or state a supplied
fact precisely. Do not add summaries, restatements, unsolicited questions, or
incomplete-pass labels. Return the edited text without explaining individual
decisions unless the user requests analysis.

## Boundaries

- "Many experts believe this approach may potentially improve retention." may
  become "Many experts believe this approach may improve retention." Attribution
  and uncertainty remain.
- "The system is reliable" must not become "The system stays up": that narrows
  the claim.
- Remove empty framing from generic personal prose, but keep the personal claim and
  do not add specificity absent from the source.
