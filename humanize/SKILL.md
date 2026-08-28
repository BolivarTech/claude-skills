---
name: humanize
description: >-
  Draft or rewrite text so it reads as natural, authentic human writing (varied
  rhythm, plain and specific word choice, real voice, no em-dashes) and avoids the
  formulaic hallmarks of generic AI prose. Trigger when the user asks to "humanize", "make
  this sound human / natural / less like AI", "de-robotify", or wants first-person
  content (emails, cover letters, applications, posts, essays, bios) that reads as
  written by a person rather than a machine. Intended for improving the naturalness
  and quality of the user's OWN authentic content; not for misrepresenting authorship
  where that is prohibited (e.g., graded academic work under a no-AI policy).
---

# Humanize

Make writing read like a specific human wrote it, not a competent machine. The goal
is authenticity and quality, not trickery: the same moves that defeat "AI voice" are
the moves that make prose genuinely better. Work from the user's real facts, voice,
and stance; never invent experiences to sound human.

## What the pass may not change

The edit is editorial, never semantic. Rhythm, word choice, sentence length and voice
are yours to move. A fact, name, number, date, version, flag, path, command or a
meaningful ordering is not, and neither is the strength of a claim: a hedge and a
guarantee are different statements, so turning one into the other is a content change
wearing an edit's costume. Leave code and code blocks, signatures and identifiers,
structured docstring fields, reference tables and command examples with their output
exactly as they are. Leave error messages and UI strings alone too, because tests and
users match them verbatim. Rewrite running prose only, then re-read the diff for
meaning drift before handing it back.

## How machine-vs-human is judged (so you know what to move)

Detectors and readers react to two statistical signals plus a set of surface tells.

1. **Perplexity** = how predictable each word is. Language models pick high-probability
   next words, so AI prose is *low-perplexity* (smooth, expected). Humans make less
   predictable, more specific, sometimes slightly-off-but-apt word choices. **Lever:**
   choose the concrete, particular word over the safe generic one.
2. **Burstiness** = variance in sentence length/structure. AI runs medium-medium-medium
   (uniform). Humans mix a long meandering sentence with a two-word jab. **Lever:**
   deliberately vary sentence length; add fragments and one-liners next to long ones.
3. **Surface tells** = cliché vocabulary, formulaic structure, empty "professional"
   filler, perfect symmetry, no concrete detail. One of them is worth naming here
   because it runs the way you would not guess: **elegant variation.** Trained to
   avoid repeating a word, the model reaches for a synonym every time: "the
   system... the platform... the solution... the tool", all naming one thing. People
   repeat the right word because it is the right word, and swapping in a near-synonym
   to dodge repetition is a school-essay habit real writers drop. **Lever:** pick the
   correct noun once and then keep using it. Repetition of the *subject* reads as
   confidence; repetition of *sentence openers and connectives* is the one to break up.

## The AI-tell blacklist (avoid or replace)

**Overused vocabulary:** delve, tapestry, leverage, resonate, navigate (figurative),
realm, landscape, testament, underscore, pivotal, robust, crucial, seamless, foster,
elevate, embark, harness, unlock, streamline, spearhead, meticulous, commendable,
boast, swift, myriad, plethora, nuanced, holistic, vibrant, bustling, ever-evolving,
game-changer, cutting-edge, solid, comprehensive, revolutionary,
"in today's fast-paced world", "in the realm of".

**Filler openers/closers:** "I hope this message finds you well", "It's worth noting
that", "It's important to note", "It's important to remember", "That being said",
"It goes without saying", "In conclusion", "In summary", "In short", "Looking ahead",
"In general terms", "At the end of the day", "When it comes to...", "As we all know".

**Voice tells:** relentlessly neutral/polite tone, no opinion, no concrete detail, no
names/numbers/anecdotes, flawless grammar with zero contractions.

### Structural tells

- Formal transitions in casual text: *furthermore, moreover, additionally,
  consequently, thus, hence.* Cut them or use plain ones (so, and, but, still).
- **Rule-of-three / tricolons** on repeat: "fast, reliable, and scalable"; three
  parallel clauses. Break the pattern: use one item, or two, or an uneven list.
- **Negative parallelism:** "It's not just X — it's Y", "This isn't about X; it's about
  Y", "Not only X, but also Y." A signature AI cadence. Kill it. The ban is on the
  construction, not on the words: "not only" inside an ordinary sentence is fine.
- **Self-explanation and stage directions.** "In this section I'll explain...", "Let me
  break this down", "It's worth examining why", a paragraph whose whole job is to
  announce the next paragraph. The model narrates its own structure because it is
  assembling one as it goes; a person just makes the point. Cut the announcement and
  keep what it was announcing. A heading and a first line that names the subject
  already do this work.
- Rigid Intro → Point → Point → Point → Conclusion shape; every paragraph the same
  length; a header over every 60 words.
- Empty fluff sentences that sound polished but add zero information.

### Punctuation you cannot type

- **Em-dashes (`—`). The single strongest tell. Default to zero.**
  Most people cannot type one: it is on no standard keyboard, so a human writing at
  speed reaches for a comma, a period, or a plain hyphen. Em-dashes are everywhere
  in *edited* prose (books, magazines, anything a copy editor touched), which is
  exactly what the training corpus over-represents. The model produces them
  constantly; the ordinary writer almost never does.
  - **Casual first-person text** (email, Slack, DMs, cover letters, posts): use
    **none**. "on your end — just let me know" is a giveaway. A person writes
    "on your end. Just let me know" or "on your end, just let me know".
  - **Edited long-form** (essay, article, docs): one or two in the whole piece at
    most, and only where nothing else does the job.
  - **Do not swap the character, restructure the sentence.** Replacing `—` with
    `–` or `--` reads just as machine-made; they are the same tell in a cheaper
    costume. Reach for a period first, then a comma, then parentheses or a colon.
    The period is usually the better edit anyway, because it also breaks the
    uniform sentence length the em-dash was propping up.
- **The rest of the not-on-the-keyboard family.** The em-dash is the loudest, but
  it is one member of a set, and the same logic convicts all of them: a person
  typing has no key for these, so their presence means a publishing pipeline or a
  machine. Curly quotes plus an em-dash together are the most recognizable
  typesetting signature there is.
  | Character | What a person actually types |
  |---|---|
  | `…` ellipsis | `...` three periods |
  | `“ ” ‘ ’` curly quotes | `" '` straight quotes |
  | `–` en-dash | `-` plain hyphen |
  | `×` `÷` `≈` | `x` `/` `~` |
  Autocorrect in Word or Google Docs *does* produce curly quotes and `…`, so in a
  document drafted there they are unremarkable. In anything typed straight into an
  email client, a chat box or a code-adjacent tool, they are not.
- **Semicolons in casual text.** Same shape of tell as the em-dash, for a different
  reason: the character is on the keyboard, but most people are not confident they
  are using it right, so they avoid it. The model has no such doubt and deploys one
  correctly every time, which is exactly what gives it away. A textbook-perfect
  semicolon joining two independent clauses in a Slack message is close to a
  signature. **In email, chat and other quick first-person writing, aim for zero;
  a period almost always does the same work.** In edited long-form they are fine,
  and some writers genuinely love them, so the rule is *do not introduce* them. If
  the writer's own drafts are full of semicolons, keep them: that is their voice.

### Order that is optimal every single time

Careful here, because good writing *is* well ordered and the fix is not to scramble
it. The tell is narrower: a model arranges every unit the same optimal way, most often
topic sentence first, then support, then a tidy landing. Do that in all eight
paragraphs and the uniformity itself becomes the signal, the same way uniform sentence
length does.

Real writing carries traces of the order the thinking happened in. A point gets made
and then qualified two paragraphs later, when the writer thought of the objection.
Sometimes the concrete example lands before the claim it supports, because that is the
bit they wanted to say. In email, people routinely bury the actual ask under context
and it arrives in the last line.

**Lever:** vary how paragraphs *enter*. Let some open on the example, a number, an
objection or a plain statement of consequence instead of the thesis. And when the
writer's own draft has an order that carries their reasoning, do not straighten it
into the optimal one; the crooked version is the evidence a person wrote it.

### Hedging, and where it sits

Stacks are the obvious half ("it's important to consider that it may potentially..."):
cut them. The subtler half is the *distribution*. A model softens everything at roughly
one rate no matter how much it actually knows, so it hedges claims that are plainly
true and then states invented specifics with total confidence. The uncertainty is
decorative; it does not track knowledge.

A person's doubt is unevenly spread and **attributed**: flat assertion on what they
know cold, explicit doubt exactly where they are guessing, and usually a reason for it.
"It shipped in March, though I'd have to check the tag" reads human because the hedge
is earned and sourced. "It may potentially have shipped around March" reads generated
because it hedges without saying why.

A third form is laundered attribution: "many experts believe", "it is widely accepted
that", "most people think". These borrow authority from a source that is never named,
which is the same decorative uncertainty wearing a citation's clothes. Name who, or
drop the frame and make the claim in your own voice.

**Lever: if it is true, assert it.** State what you know flatly and strip the
qualifiers off it. Where you genuinely do not know, say so in specific terms and name
what would settle it. And if a claim is not worth that sentence, cut the claim. What
you must not do is keep it and blur it. Confidence that varies with actual knowledge
is both more human and more honest.

## Humanizing levers (apply after a first honest draft)

1. **Vary rhythm (burstiness).** Read it and mark sentence lengths. If they cluster at
   12 to 20 words, break some. Drop in a short one. A fragment, even. Then let one
   sentence run long and a little unruly. Rhythm is the strongest human signal.
   Do this pass twice, and make the second one count. Cutting filler (lever 4) is
   subtractive, and every deletion pulls a sentence toward the mean, so a draft that
   varied before the cut comes out flat after it. When that happens the repair is to
   *join*, not to fragment: find two short sentences that are really one thought and
   run them together. Reaching for a fragment is the reflex, and it is how you end up
   in the second artificial register.
2. **Raise perplexity with specificity.** Replace generic nouns/verbs with the exact
   thing: not "improved performance" but "cut cold-start from 4.2s to 900ms". Concrete
   detail is inherently less predictable and more credible. But the specificity has to
   come out of the writer's material. If the draft does not carry the exact number,
   ask for it or leave the sentence vague and say the number is missing. A plausible
   invented figure is worse than the vague sentence it replaced, because it reads true.
3. **Use a real voice.** First person, a clear stance, mild opinion. Contractions
   (I'm, it's, don't). An aside in parentheses. Start a sentence with *And* or *But*
   when it lands.
4. **Cut filler ruthlessly.** Delete any sentence that would survive as "generic advice."
   If removing a clause loses no meaning, remove it.
5. **Break symmetry, and let interest decide where.** Uneven paragraph lengths, no
   three-of-everything, one point getting two sentences and the next getting five.
   But the shape is the symptom; the cause is that **a machine finds every point
   equally interesting and a person does not.** AI gives each item the same depth
   *and the same enthusiasm*. A person disposes of the obvious in four words and
   then spends a paragraph on the one thing they actually care about, because that
   is where their attention genuinely went. So do not redistribute length at random:
   decide which point the writer would lean on, give it the room, and let the rest
   get short. Uneven emphasis that tracks real interest is far harder to fake than
   uneven line counts, and it is what makes a text feel authored rather than
   generated.
6. **Prefer plain words.** "use" not "leverage/utilize", "help" not "facilitate", "big"
   not "robust", "start" not "embark/spearhead". This is about register, not about
   probability: keep the plain word for the action and the specific word for the thing.
7. **Keep small imperfections.** A one-word sentence. A sentence that trails into a
   qualifier. Real writing isn't buffed to a mirror finish.
8. **Localize.** Idioms, a concrete reference, the writer's actual domain vocabulary.
   Things a model averaging the internet wouldn't reach for.

## Working in languages other than English

The blacklist above is English. The levers are not. Rhythm, specificity and
cut-the-filler transfer to any language, and so does the character scan, because the
em-dash and the curly quote are typographic facts rather than English ones. What does
not transfer is the vocabulary, and it has to be rederived per language rather than
translated.

Spanish has its own set: "es importante destacar", "en el mundo actual", "cabe
mencionar", "sin duda alguna", *por ende* and *asimismo* as default connectives, a
gerund closing every other sentence ("logrando así...", "permitiendo..."), and naming
the subject with a fresh synonym each time, a habit Spanish schooling rewards even
harder than English schooling does.

Two checks English does not need. Register in Spanish rides on tú/usted and on verb
person, so a draft that drifts between them reads stranger than anything on the list
above. And translated text keeps English word order and English sentence length, which
produces prose that is grammatical and still obviously not written by a native speaker;
if the source was translated, reset the rhythm in the target language instead of
polishing the translation.

## When to stop (overcorrection is its own tell)

These are levers, not a score to maximize. Pushed to the limit they produce a second
artificial register: fragments in every paragraph, a contraction forced into every
clause, a wry aside after each point, studied casualness throughout. **Aggressively
informal AI is still AI**, and a reader clocks it just as fast.

The target is one specific person's voice, not maximum informality. Three checks:

- **Register has to hold.** A single document gets one voice. Humanizing edits applied
  unevenly produce drift, a chatty opening bolted onto a formal middle, which reads
  stranger than the uniform version you started with.
- **Match the person and the medium.** Some people write formally and it is authentic.
  A lawyer's client letter should not acquire sentence fragments. Ask what *this*
  writer sounds like, not what "human" sounds like in the abstract.
- **Stop when the tells are gone.** Once the clichés, the filler and the punctuation
  are handled and the rhythm varies, stop. Further edits start adding artifacts rather
  than removing them.

## Workflow

- **Human-first is best:** get the user's raw facts/voice, draft plainly, then polish
  *their* voice rather than generating slick prose and sanding it down.
- **Self-check pass (read aloud):** Where does it sound like a brochure? Which sentence
  is filler? Where are three-in-a-row patterns? Where is every sentence the same length?
- **Character scan (do this last, it is mechanical):** search the draft for `—` `–`
  `--` `…` `“` `”` `‘` `’`. In casual text the target count is zero. For dashes,
  rewrite the sentence rather than substituting another mark; for the others, just
  type what a keyboard types. This one check catches the most recognizable tells in
  the whole list and it takes seconds, which is why it goes last: it is the only
  item here that needs no judgment. Count semicolons in the same pass; in casual
  text every one is a candidate for a period.
- **Repetition check:** find the thing the text is about and count the names it is
  given. If one subject collected three synonyms, pick the best and use it every
  time. Then look at how sentences *start*: that is the repetition worth breaking.
- **Length:** match the medium. A cover letter or email should be shorter than the AI
  instinct to over-explain.

## Quick before → after

- ❌ "In today's fast-paced world, I am passionate about leveraging cutting-edge
  solutions to drive impactful results." → ✅ "I like problems that are actually hard.
  Last year I rewrote our build pipeline and shipped it in three weeks."
- ❌ "The system is fast, reliable, and scalable, ensuring seamless performance." →
  ✅ "It's fast, and it hasn't fallen over once in six months of production."
- ❌ "It's not just about writing code — it's about solving real problems." → ✅ "The
  code is the easy part. Figuring out what to build is the job."
- ❌ "Many experts believe this approach may potentially improve retention." → ✅ "It
  lifted retention about four points. That was one cohort, so treat it as a signal
  rather than a result."
- ❌ "I've attached the draft — let me know what you think." → ✅ "I've attached the
  draft. Let me know what you think." (The em-dash was doing nothing a period
  cannot. Note the fix also shortens the sentence, which helps rhythm.)
- ❌ "Happy to adjust the scope — whatever works on your end — just let me know." →
  ✅ "Happy to adjust the scope. Whatever works on your end, just let me know."

## Guardrails

Use this to make the user's own genuine content read naturally. Do not use it to pass
off work as human where a rule forbids AI assistance (e.g., graded academic
submissions), to impersonate a real person, or to mass-produce deceptive content.
