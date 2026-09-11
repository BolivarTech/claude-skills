---
name: humanize
description: >-
  Draft or rewrite prose with a natural, consistent voice, varied rhythm, plain
  language, and fewer formulaic AI patterns. Use when the user asks to humanize,
  de-robotify, make text sound natural or less like AI, or improve first-person
  writing such as emails, applications, posts, essays, cover letters, and bios.
license: MIT OR Apache-2.0
metadata:
  version: 2.0.0
---

# Humanize

Work from the writer's facts, vocabulary, stance, and certainty, regardless of
who drafted the text. Improve structure before substituting words.

## Meaning and voice

Rewrite running prose only. Unless the user's request authorizes content changes,
preserve:

- facts, names, numbers, dates, versions, paths, flags, commands, and meaningful
  order, including chronology and argument dependencies;
- the breadth and strength of claims, attribution, uncertainty, and its reasons;
- code blocks, inline code, signatures, identifiers, structured docstring fields,
  reference tables, command examples and output, error messages, and UI strings;
- mathematical, scientific, and technical symbols such as `×`, `÷`, and `≈`.

Infer audience, medium, formality, verbosity, grammatical person, contractions,
and regional or domain vocabulary from the request and source. Preserve the
existing register when no preference is given. This profile governs the edits:
formal writing need not become chatty, and useful technical terms stay.

Never invent opinions, anecdotes, comparisons, reactions, habits, or specific
facts. Use concrete details from the supplied material; otherwise keep the
wording general. Preserve informative asides and useful irregularities, but
correct mistakes. Do not add typos, false starts, fragments, or awkwardness to
simulate a person.

Do not delete a weak claim as filler, transfer an attributed claim to the writer,
or strengthen a hedge. Collapse redundant qualifiers only at the same certainty:
"may potentially possibly reduce X" can become "may reduce X", never "reduces X".
If the effect of a qualifier is unclear, preserve it and continue.

Ask only when missing information prevents completing the request and cannot be
handled by preserving the source or using existing context. Optional improvements
do not require questions or approval and do not make an edit incomplete.

## Editorial checks

Apply changes that fit the voice and address a problem in the draft. Do not
maximize variation or force every sentence into a new shape.

- **Rhythm:** Vary openings, clause complexity, and sentence length. If more than
  half the sentences cluster around 12 to 20 words, shorten some and let others
  develop where useful. Passive voice is appropriate when the affected thing is
  the topic or the actor is unknown or irrelevant. After removing filler, join
  short sentences that form one thought if the rhythm has become flat.
- **Paragraphs:** Address repeated topic/support/conclusion structures, identical
  paragraph lengths, excessive headings, and mechanical three-part lists. Use
  an existing example, consequence, number, or objection as an opening where it
  helps. Keep the writer's distribution of emphasis unless the source supports
  a change; do not make every sentence equally dense with facts.
- **Filler:** Remove empty framing ("It's worth noting"), unneeded stage directions
  ("Let me break this down"), redundant closers, and decorative asides only when
  removal changes neither information nor claim strength. A familiar phrase is
  not automatically empty: preserve it when it conveys certainty, emphasis, or
  the writer's stance. "I care about quality" is a personal claim, even if vague.
- **Constructions:** Rewrite "It's not just X; it's Y", "This isn't about X; it's
  about Y", and "Not only X, but also Y", preserving both halves. Break repeated
  tricolons without dropping claims. In casual prose, replace formal transitions
  such as *furthermore*, *moreover*, and *consequently* with plain connectives or
  omit them when the relationship remains clear.
- **Vocabulary:** Prefer plain verbs and exact nouns, such as *use* over *utilize*.
  Scan for formulaic language such as *delve*, *tapestry*, *leverage*, *seamless*,
  *foster*, *elevate*, *unlock*, *holistic*, *game-changer*, *cutting-edge*, and
  "in today's fast-paced world". These are contextual signals, not a substitution
  table; a structural rewrite may help more than a synonym.
- **Repetition:** Keep the correct subject noun rather than rotating through
  "system", "platform", "solution", and "tool". Address monotonous openings and
  connectives by changing sentence construction, not the subject's name.

## Character handling

Scan editable prose last for `—`, `–`, `--`, `…`, `“`, `”`, `‘`, and `’`.
Use search or a regular expression when available; correct matches contextually.

- Rewrite sentences containing em dashes or `--` used as an em dash. Prefer a
  period, comma, parentheses, or colon rather than another dash.
- Replace prose-separator en dashes with a plain hyphen or restructure. Numeric
  ranges such as `2010–2015` may become `2010-2015`.
- Replace curly quotes with straight quotes and `…` with `...` in ordinary prose.
- Leave typography inside protected material unchanged.

## Other languages

Use the same structural and semantic criteria, but do not translate the English
word list mechanically. Derive local patterns from native drafts when available;
otherwise avoid claims of complete language coverage.

For Spanish, inspect potentially empty framing ("es importante destacar", "cabe
mencionar", "en el mundo actual"), automatic *por ende* or *asimismo*,
repeated closing gerunds ("logrando así", "permitiendo"), shifts between *tú* and
*usted* or verb persons, and English sentence patterns in translations. Oral
markers such as *bueno*, *o sea*, and *pues* must fit an existing informal voice,
region, and context; never insert them as a quota.

"Sin duda alguna" can express certainty: removing it from "Sin duda alguna, esta
es la mejor opción" weakens the writer's stated confidence even though the core
claim remains. Preserve it unless the context establishes that its force is
redundant and fully retained by the remaining wording.

## Final pass and delivery

Compare the result with the source for meaning and register drift, invented
material, repetition, and rhythm after deletions. Stop when the relevant problems
are addressed; constant contractions, asides, or fragments create another
artificial register.

Return a text no longer than the source unless expansion was requested or a
supplied fact needs more words for precise expression. Do not append unsolicited
questions, lists of missing details, or incomplete-pass labels for optional edits.

## Examples of semantic boundaries

- "Many experts believe this approach may potentially improve retention."
  becomes "Many experts believe this approach may improve retention."
  Attribution and uncertainty remain.
- "The system is reliable" must not become "The system stays up": the latter
  narrows the claim.
- "In today's fast-paced world, I am passionate about leveraging cutting-edge
  solutions to drive impactful results" permits removing empty framing, but the
  personal claim stays and specificity requires facts from the source.
