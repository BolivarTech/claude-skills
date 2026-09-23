---
name: proofread
description: >-
  Proofread a finished text in Spanish or English: correct spelling, accents,
  grammar, punctuation, and typography against the norm (RAE/ASALE for
  Spanish, Chicago Manual of Style and Merriam-Webster for US English) or the
  project's own style guide, without touching style or voice. Returns the
  corrected text in a new file and a report of every change, the doubts left
  for the author, and the criteria applied; on request it only reports. Use
  when the user asks to proofread, fix typos, check spelling or punctuation,
  or says "corrige la ortografía", "revisa tildes y puntuación", "corrección
  ortotipográfica", "corrección de pruebas", "proofread this", "check for
  typos", "solo revisa la ortografía". Not for rewriting style or voice,
  removing signs of generated text, diagnosing a story, or reviewing attention
  or production.
license: MIT OR Apache-2.0
metadata:
  version: 1.0.0
---

# Proofread

Correct what the norm declares wrong in a finished text: spelling, accents, grammar, punctuation, and typography. Leave style, voice, rhythm, structure, and content alone. The name comes from the printer's proof, the copy checked for errors before the print run; in Spanish the trade is *corrección de pruebas* or *corrección ortotipográfica*. It is not copyediting, which works on clarity and voice: that belongs to the humanize skill and to the review skills.

Proofreading is the last pass. In a writing workflow it runs after the final humanize pass, and again at the end of a production script. Anything edited after it needs proofreading again.

## Authority

Apply, in this order:

1. **The project's style guide or the author's declared criteria.** Look for them in the request, in the document itself (production notes often state them), and in project files the user points to; search no further. When two of them disagree, the most specific wins, the document over the project files, and the report says so. A project convention overrides the general norm. Example: a script project that writes full accents only inside SSML blocks, because they drive the pronunciation of a synthetic voice, and plain text elsewhere. Correcting accents outside the SSML would break the project's convention.
2. **The general norm:**
   - Spanish: RAE and ASALE: *Ortografía de la lengua española* (2010), *Diccionario panhispánico de dudas* (2nd edition, 2025), and the RAE *Libro de estilo* (2018) for typography the DPD does not cover.
   - English, US variant: *The Chicago Manual of Style*, 18th edition (2024), with Merriam-Webster for spelling (the first-listed form). A British text keeps its variant.
3. **When the norm allows options,** follow the option the text already uses most and apply it everywhere. This covers typographic and lexical variants alike (*quizá/quizás*, *translúcido/traslúcido*): an inconsistent variant is unified, a consistent one is left alone. On a tie, use the form the norm prefers: in Spanish the single ellipsis character and angled quotation marks; in English Chicago's spaced ellipsis. The Spanish norm is pan-Hispanic, so regional usage that the norm accepts, such as American *de a una* or *ustedes* for plural address, is not corrected.

Norms change. The rules below were verified against these sources in September 2026; when a rule and a current source disagree, the source wins, and say so in the report.

## What Is Corrected and What Is Not

- **Correct** what the norm declares wrong: a missing or extra accent, broken agreement, a misbuilt dialogue tag, a misspelled prefix, a wrong homophone.
- **Do not correct**:
  - style: anaphora, fragments, deliberate repetition, long sentences, a comma splice used as rhythm in fiction;
  - options the norm allows: *solo* with an accent where the author sees ambiguity, parentheses instead of dashes for an aside, curly or angled quotes used consistently;
  - a character's words: in dialogue, and in documents a character writes inside the fiction (a letter, a diary, a logbook), a grammar or word-choice error may be characterization. Flag it as a doubt; do not change it. Spelling, accents, capitals, punctuation, and typography are corrected there as anywhere else, because a reader cannot hear them as voice: *¿Donde duermo?* becomes *¿Dónde duermo?*, and *alot* becomes *a lot*, while *hubieron* or *there was a lot of nights* stays as a doubt.
- **When in doubt, do not touch it.** List it as a doubt with the rule and the options, and let the author decide. An error that can only be fixed by rewording the sentence, such as *Por cada muchas ventanas*, is also a doubt, with a proposed wording.

### Boundary with humanize

- humanize removes the signs of generated text and improves naturalness; proofread corrects errors against the norm. Neither calls the other.
- The dash is the boundary case:
  - In Spanish, the raya of dialogue and of narrative asides is the norm. Correct its form (spacing, surrounding punctuation), never its presence.
  - In English, Chicago accepts the em dash for asides and interruptions, but it is also one of the most typical signs of generated text. **Never add a new em dash.** Correct only the form of the dashes the text already has. If humanize replaced a dash with commas or parentheses, keep that: both are correct.
- The same holds for ellipses: unify their form by each language's norm, without deciding whether they belong.

### Never touched

- Markup, such as SSML tags, the syntax of cues like `[VISUAL:]` or `[SFX:]`, code blocks, metadata, and production notes, including their prose. Inside SSML, correct the words and leave the tags byte for byte. Text the audience will see on screen is corrected even when it sits inside a cue; the cue syntax around it is not.
- The author's appended notes, titles of other people's works, and verbatim quotations from another source. A quotation is corrected only for a transcription error that can be checked. A document the fiction itself quotes, such as a logbook entry or a letter, is a character's document, not an outside quotation: it is corrected like one.
- The file's line endings, paragraph structure, and whitespace at the end of lines (in Markdown, two trailing spaces are a line break). Read the file as bytes, keep CRLF or LF as found, and write the corrected text to a new file beside the original. Never overwrite the original.

## Procedure

1. **Identify the text:** language and variant; literary prose, script, email, or document; any project style guide or author criteria in the request or the files.
2. **Read the whole text before correcting,** and fix the criteria for the document: kind of quotation marks, ellipsis form, numbers in words or figures, italics or quotes for thoughts. When the text already chooses, follow its majority choice.
3. **Correct** passage by passage what the norm declares wrong, leaving style alone.
4. **List the doubts:** options the norm allows, possible style decisions, errors inside dialogue, and clashes between the project guide and the norm.
5. **Verify** by command: nothing was added that the text did not have (new em dashes in English, accents outside SSML in a project that does not use them); the counts of `\r\n` and `\n` bytes match the original, counted on the bytes rather than with a line-oriented tool; and every change in a word-level diff between the original and the corrected file maps to a report line, and every report line to a change.

## Spanish

### Accents

- General rules: agudas with an accent when they end in a vowel, -n, or -s not preceded by another consonant; llanas when they end in any other consonant or in -ch; esdrújulas and sobresdrújulas always; monosyllables never, except diacritics (*fue, dio*, not *fué, dió*).
- Hiatus: a stressed closed vowel next to an unstressed open one always takes the accent, even across *h*: *río, raíz, búho, prohíbe*.
- Orthographic monosyllables take no accent, mandatorily since 2010: *guion, truhan, ion, fie, fio, lie, lio, guio, crio, rio, hui*. Keep them apart from *fío, lío, río, crío*.
- Diacritics: *tú/tu, él/el, mí/mi, té/te, sí/si, dé/de, sé/se, más/mas*; *qué, cuál, quién, cómo, cuándo, cuánto, dónde* when interrogative or exclamative; *aún* ('todavía') vs *aun*. The conjunction *o* never takes one, not even between figures.
- *Solo* and the demonstratives: with no ambiguity, no accent (*Solo quiero agua*, not *Sólo*); where the writer judges there is a risk of ambiguity, the accent is optional, and only in pronoun uses of the demonstratives. *Esto, eso, aquello* never take one. The 2023 RAE note changed the wording, not the rule. Remove an accent without ambiguity; keep one in an ambiguous case.

### Capitals

- After a colon, lowercase by default. Capital after a letter greeting, before a verbatim quotation, after headings followed by text, and after *ejemplo:* and similar when an independent sentence follows.
- After ? or !: a capital when the question or exclamation is the whole sentence; lowercase when it only opens the sentence (*¿Qué puedo hacer?, me pregunto*); lowercase when it sits inside it (*Marina, ¿puedes venir?*).
- Days, months, and seasons are lowercase unless part of a proper name: *el 14 de marzo*. Offices and titles are lowercase: *el presidente, la reina, el papa*.
- Titles of works capitalize only the first word and go in italics: *Cien años de soledad*. Periodicals and collections capitalize every significant word. Institutions capitalize every significant word.

### Prefixes

- Joined to a one-word base, *ex-* included since 2010: *exnovio, antimafia, posguerra, exjugador del Real Madrid*; not *ex-novio* or *ex novio*.
- Separate before a multiword base: *ex primer ministro, pro derechos humanos*.
- Hyphen before a capital or a figure: *anti-OTAN, sub-21, pre-1945*. Letter-and-figure codes that are not prefixes may skip it: *5G, 11S*.
- *pos-* is recommended over *post-*, except before *s-*. Prefixes take no accent: *super-8*.
- After a vowel-final prefix, *r* doubles: *antirrobo, microrrelato, vicerrector*.

### Numbers

- In literary and non-technical text, words are preferred: one-word numbers, round numbers of two words, and 31 to 99. Figures for numbers of four or more words, years, and decimals. Do not mix within a series or inside one numeral (*154 mil* is wrong), except with *millón*: *327 millones*.
- Times: words are preferred in narrative (*a las once y once*); figures with the 24-hour model or where precision matters (*11:11*, *19:15 h*). Figures in literary narration are a less recommended option, not an error: list them as a doubt. Inside a document a character writes, such as a logbook entry, figures are natural and are not flagged. Hours and minutes are separated by a colon, never a comma.
- A space before %: *25 %*. Thousands grouped by thin spaces (*8 327 451*), never a point or comma; optional in four-digit numbers; never in years, pages, or codes.
- Ordinals: *1.º, 2.ª, 3.er*. Centuries in Roman numerals after the noun, never Arabic: *siglo XXI*, not *siglo 21*. The norm recommends small capitals; in plain text or Markdown, where they are not available, capitals are the accepted substitute.

### Raya

**Dialogue** (DPD 2nd ed.):

- The raya opens each turn with no space: *—¿Cuándo volverás?*
- A narrator's comment goes between rayas, attached to what it encloses. No closing raya if the character does not speak again: *—Espero que salga bien —dijo Azucena.*
- With a speech verb, the comment starts lowercase even after ? or !: *—¡Qué le vamos a hacer! —exclamó.*
- Without a speech verb, after a complete sentence, the speech ends with its own period and the comment starts with a capital: *—No se moleste. —Cerró la puerta.* If the speech resumes, the period goes after the closing raya: *—Me voy. —Se levantó—. No hace falta…*
- The punctuation of an interrupted speech goes after the closing raya: *—Está bien —dijo Carlos—; lo haré.*
- Criterion: the DPD keeps lowercase-without-period for speech verbs only; the RAE *Libro de estilo* extends it to verbs of gesture (*—Sí —sonrió Silvia*). Follow the DPD; the other form is valid, so list it as a doubt, never correct it.

**Narrative asides:** the closing raya is required even at the end of a sentence, with the period after it: *Esperaba a Emilio —un gran amigo—.* The raya (—) is not the hyphen (-) or the minus sign (−); the hyphen joins elements and marks ranges.

### Quotation marks, ellipses, opening marks

- Quotation marks: angled first in print, then double, then single: *«…“…‘…’…”…»*. Consistent use of typographic double quotes (“ ”) is not an error; switching them to angled is a criterion, listed as a doubt. Straight quotes (") in a plain-text or Markdown file are the file's typography: do not convert them to curly or angled ones unless asked, and record this once under criteria, not also as a doubt. The period, comma, semicolon, and colon go after the closing mark, and a period is still added after *?», !», …»*.
- Uses: verbatim quotations; a character's thoughts (*«Esto empieza mal», pensó*); ironic or special senses; titles of parts of a work. Metalinguistic use takes italics in print. Italics plus quotes is redundant.
- Ellipses: exactly three, attached to the previous word, followed by a space; no extra period at the end of a sentence; punctuate as if they were absent; before the closing ? or ! when the utterance is incomplete, after it when complete; *[…]* for omissions; never with *etc.* The RAE says nothing about the single character versus three periods: accept both and unify by the text's majority.
- ¿ and ¡ are required, placed where the question or exclamation begins; tag questions, connectors, and initial subordinate clauses stay outside: *Es tuyo, ¿no?*

### Italics, abbreviations, symbols

- Italics: unadapted foreign words and Latin phrases, without accents (*ballet*, *a priori*, *statu quo*, in italics since 2010); titles of works; metalinguistic use in print. Nicknames take a capital and no italics (*el Greco*). Thoughts in italics are an editorial convention, not the norm (the norm is quotation marks); respect it when consistent.
- Siglas are invariable: *las ONG*, not *ONGs*. Symbols take no period and no plural, with a space after the figure: *25 km, 33 dB*. Abbreviations end in a period and keep their accent: *pág.*, *EE. UU.*

### Grammar (DPD 2nd ed.)

These are the most frequent cases, not the full scope: any grammar error the DPD describes is corrected, such as a missing *a* before a personal direct object (*oyó a alguien*).

- *Le(s)* as the direct object of a masculine person is not incorrect, singular and plural; never for things (*El libro le leí* is wrong). Laísmo (*La dije*) and loísmo are improper.
- Queísmo (*Me acuerdo que* → *de que*) and dequeísmo (*Pienso de que* → *que*).
- Impersonal *haber* is always singular: *hubo muchas noches*, not *hubieron*; *va a haber*, not *van a haber*.
- *En base a* is wrong (*con base en, sobre la base de*); *a nivel de* only when it keeps the sense of level or rank.
- *Le* with a plural referent is a widespread discordance that the DPD does not mark as an error: a doubt, not a correction.
- *sino/si no*, *porque/por que/porqué/por qué*, *a ver/haber*, *echo/hecho*: correct by function.

### Spacing

Never more than one space between words; no space after ¿ ¡ « or before their closing signs; a non-breaking space inside abbreviations, between a number and its symbol, and between digit groups.

## English (US)

Chicago 18th edition section numbers in parentheses.

### Changes in the 18th edition that trip proofreaders

- **Capitalize after a colon when a complete sentence follows** (6.67): *She knew one thing: The house was empty.* This reversed the 17th edition and contradicts habit; check every colon.
- Singular *they* is accepted, formal writing included (5.51): do not correct it.
- In title case, prepositions of five letters or more are capitalized (8.160): *Much Ado About Nothing*.
- A title before a name keeps its capital even with an adjective (8.22): *former President Carter*.

### Punctuation

- Serial comma (6.19): *red, white, and blue*.
- An apostrophe the correction adds follows the file's typography: straight in a file with straight quotes, curly (’) in one with curly quotes.
- Em dash closed up, no spaces (6.91); en dash for ranges and compounds with an open element (6.83, 6.86): *pages 3–5*, *pre–Civil War*. Never add a new em dash (see the boundary with humanize).
- Interrupted speech ends with an em dash and nothing else (12.42): *"Don't inter—"*; when the narration cuts in, the dashes go outside the quotation marks. Trailing speech takes an ellipsis (12.43).
- Ellipses: Chicago's form is three spaced periods (". . .", 12.68), set off by a space from the preceding word (*one by one . . .*); the single character is accepted. Three unspaced periods ("...") are not Chicago's form: unify by the text's majority. In fiction, always three, even after a complete sentence; a question mark or exclamation point is kept. Four dots only for omissions in quotations.

### Dialogue

- Periods and commas go inside the closing quotation mark (6.9): *"Go," she said.*, not *"Go", she said.* Semicolons and colons go outside. Question marks and exclamation points go inside only when they belong to the quotation (6.10).
- A speech verb takes a comma; an action beat takes a period: *"So up there," Joe said.* but *"So up there." Joe pointed at the window.* (*"So up there," Joe pointed* is wrong).
- A new paragraph for each change of speaker (12.40); in a multiparagraph speech, opening quotes on each paragraph and a closing quote only at the end (12.45); quotes within quotes, double then single (12.30).
- Direct address takes a comma (6.57): *"Thanks, Mom."*

### Numbers, capitals, italics

- Spell out zero through one hundred and round multiples in running text (9.2); be consistent in the immediate context (9.7). In dialogue, spell out whenever it is not awkward; years in figures (12.51).
- Times (9.39): *four o'clock, half past ten*; exact times in figures with lowercase *a.m.* and *p.m.* with periods: *11:11 p.m.*, not *11:11 pm*. Full capitals (*11:11 PM*) go to the doubts rather than being corrected: Chicago's alternative small-capital form was not verified for this edition. In fiction narration, exact times in figures are acceptable; spelling them out is an option, listed as a doubt only when the text mixes both forms.
- *80 percent* in nonscientific text (9.20); spell out a number that starts a sentence (9.5); *the 1980s*, not *the 1980's* (9.35).
- Title case (8.160): lowercase articles, *and, but, for, or, nor*, *to*, *as*, and prepositions of four letters or fewer; capitalize the first and last words.
- Offices capitalized before a name, lowercase elsewhere (8.20–8.22). Kinship terms capitalized when used as a name, lowercase after a possessive: *Hey, Mom*; *my mom* (8.37).
- Italics for titles of books, films, and periodicals; quotation marks for stories, chapters, poems, and episodes (8.164, 8.179). Foreign words not in Merriam-Webster in italics (7.55). Thoughts in quotation marks, italics, or nothing, at the author's choice (12.49): do not normalize a consistent choice.

### Hyphens, possessives, usage

- Compound modifiers hyphenated before the noun, open after it (7.91): *a well-known author*, *the author is well known*. No hyphen after an *-ly* adverb (7.93). Prefixes closed as a rule (*nonviolent, reelect*), hyphenated before a capital or numeral, before a double *a* or *i*, or to avoid misreading (7.96).
- *James's*, *the Joneses' house*, *Achilles' heel* (7.16–7.19).
- Agreement (*There were a lot of nights*); *affect/effect*, *lay/lie*, *fewer/less*.
- *a lot*, never *alot*; *its/it's*, *their/there/they're*, *your/you're*, and similar pairs are spelling: corrected in dialogue too, because a reader cannot hear an apostrophe. *All right* in formal prose; *alright* acceptable in informal dialogue.
- Pronoun case (*between you and me*), dangling modifiers, and comma splices: flag them. In dialogue and fiction they may be deliberate.
- Merriam-Webster's first form: *toward, judgment, gray*. *OK* and *okay* are both standard: pick the text's majority and unify.

### British texts

Do not "correct" *colour, grey, travelling*, single quotation marks first, punctuation outside the quotes by sense, *-ise* or *-ize* used consistently, or day-month-year dates.

## Scripts

- Correct what is heard or read: narration, dialogue, on-screen text, and subtitles. Leave tags, cues, and production notes as they are.
- Inside SSML, correct the words and keep the tags byte for byte. A missing accent changes the synthetic voice's pronunciation: report it as an error with an audio effect.
- The project's convention wins (Authority, 1). If the project writes plain text outside the SSML, only what the convention declares is exempt there, such as accents or opening ¿ ¡; other errors in text the audience sees or hears, such as grammar or a wrong homophone, are still corrected.
- In text a synthetic voice will read, punctuation is also prosody: a comma or colon adds a pause. Apply a change the norm requires and note its audio effect; a change the norm only recommends, such as a comma before *pero*, goes to the doubts.
- Numbers and acronyms that will be read aloud are also checked for how they sound: an acronym the voice will spell out letter by letter, or a figure it could read two ways, goes to the doubts.

## Deliverables

**By default, proofread corrects:**

1. **The complete corrected text**, in a new file beside the original, which is never overwritten. Same line endings; markup, cues, and the author's notes intact.
2. **A separate report** in the user's language with these sections:
   - **Changes applied:** one per line, with location in the original's numbering, text before, text after, and the rule. Enclose the before and after text in the report's own quotation marks, or in backticks when the text already contains quotation marks. Example: *L3: «ex-guardián» → «exguardián» (prefix joined to a one-word base, OLE 2010)*.
   - **Doubts not applied:** the rule, the options, and why it was not decided.
   - **Criteria applied:** the choices made for the whole document, such as quotation marks, ellipsis form, numbers, the project guide used and where it was found, and the line endings found.
   - **Noticed outside proofreading**, only when there is something: one line per issue that is not orthotypographic, such as a point-of-view slip or a factual contradiction, with its location and the skill that covers it. Nothing here is changed.

**In "only review" mode** (*solo revisa*), which runs only when the user asks for it, deliver the same report with the changes as proposals and do not modify the text.

When the text has no errors, say so, deliver no new file, and still list any doubts and the criteria observed.

## Example Use

"Use /proofread on this chapter. It is Spanish literary prose; keep the dialogue rayas and my repetitions. Give me the corrected file and the report."
