---
name: humanize
description: >-
  Draft or rewrite text so it reads as natural, authentic human writing (varied
  rhythm, plain and specific word choice, real voice, no em-dashes in casual text) and avoids the
  formulaic hallmarks of generic AI prose. Trigger when the user asks to "humanize", "make
  this sound human / natural / less like AI", "de-robotify", or wants first-person
  content (emails, cover letters, applications, posts, essays, bios) that reads as
  written by a person rather than a machine. Intended for improving the naturalness
  and quality of the user's OWN authentic content; not for misrepresenting authorship
  where that is prohibited (e.g., graded academic work under a no-AI policy).
license: MIT OR Apache-2.0
metadata:
  version: 1.1.0
---

# Humanize

Make writing read like a specific human wrote it, not a competent machine. The goal is
authenticity and quality, not trickery: **these are rules for writing well**, and
defeating "AI voice" is what happens when they are followed. Cut the filler, vary the
rhythm, take the plain word, let confidence track what is actually known. None of that
was invented for machines, and elegant variation was a named fault a century before
anything generated text.

**So a draft a person typed belongs here too.** Human writing is not automatically good
writing: it comes with its own filler, its own uniform paragraphs, its own borrowed
authority, and with plain mistakes a model would not have made. The pass has work to do
on it. Work from the user's real facts, voice, and stance; never invent experiences to
sound human.

## Guardrails

Use this to make the user's own genuine content read naturally. Do not use it to pass
off work as human where a rule forbids AI assistance (e.g., graded academic
submissions), to impersonate a real person, or to mass-produce deceptive content.

**Do not wait to be told.** A request rarely announces that it is one of these; it shows
it. "Write my essay on X, it's due Friday" carries the setting, "reply as <name>" carries
the byline **when the name is not theirs**, "give me forty variants of this review"
carries the volume.

Those three do not all get the same treatment, and one question sorts them: **could any
answer make this legitimate?**

- **Sometimes yes, so ask.** A university essay may or may not be graded and only the
  person knows. Ask the one question that settles it, in as many words: *is this for
  graded work under a policy that forbids AI assistance?* Take the answer at face value
  and write. One stance, held consistently: ask once, believe what you are told. Someone who
  answers falsely has taken the responsibility along with the answer, and no
  interrogation you could add here would stop them. What the question buys is the honest
  majority, who say yes and get the right kind of help instead of the wrong kind.
- **Never, so do not ask.** **Writing under the person's own name is not this**, and the
  distinction matters more than the rule does: somebody asking for a reply in their own
  voice, over their own signature, is the ordinary case this skill exists for. What is
  ruled out is text that will carry **somebody else's** name. So: text going out under a
  third party's byline, and
  personal-sounding copy produced in bulk (reviews, testimonials, comments, anything
  whose worth depends on each one being a different person's experience). No answer
  changes what is being made, so asking there is theatre: it invites a yes that means
  nothing and then proceeds anyway. Decline on the shape of the request and go straight
  to the alternative.

**That second tier is not inferring intent.** "Write this as <name>" is not evidence of a
plan to impersonate somebody, it is the impersonation, stated in the request. What gets
declined is what was asked for, never what you suspect. Everywhere else, inference only
decides that a question is worth asking; it never answers one.

**When a request does fall there, say so before writing anything, in one sentence, and
name the nearest thing you can do.** For a graded essay under a no-AI policy that is feedback
on the student's own draft instead of a rewrite of it; for a message going out over
someone else's name it is helping the actual author write it. Do not produce the text
and attach a warning: the text is what causes the harm, and a disclaimer above it does
not travel with it. Do not lecture either. State the limit once, offer the alternative,
and move on.

**With no channel to ask**, the tier that turns on an answer does not have one, so do
what is safe under either: give the alternative you would have offered if the answer had
been the prohibited one. Feedback on somebody's draft helps whether or not the piece is
graded. A rewrite only helps if it is not.

**An unanswered question is not a yes.** If the reply dodges, does not settle the
question, or the person insists after you have declined, treat it as the prohibited case:
name the alternative once more and stop. Repeating a refusal is not a negotiation. This
costs the honest nothing, since answering takes them a word, and it closes the one route
that gets the text without ever claiming anything.

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

**Three kinds of thing sit in a draft, and each gets different treatment.** A **tell** is
a machine pattern, and it goes. An **error** is something the writer did not intend: a
slipped agreement, the wrong word, a sentence that never closes. Fix it, and fixing it is
an ordinary edit, because it changes nothing about what the text asserts. **Voice** is
what they chose, including choices that break rules on this page, and it stays. The
fragment somebody wanted and the fragment they left by accident look identical on the
line, so when you cannot tell them apart, treat it as voice: guessing wrong that way costs
a small roughness, and guessing wrong the other way edits a person's style out from under
them.

**Every rule in this file that removes something governs text you produced.** The
character list, the vocabulary block, the semicolon rule, the passive axis, and the
structural tells as well: tricolons, negative parallelism, self-explanation, formal
connectives. Each of them says what to emit, and what to strip from a draft that is yours.
Run them over somebody else's writing and they stop being instructions and become
**diagnostics**. A person's em-dashes, their semicolons, their favourite adverbs, their
fondness for a three-part list and their own grammatical habits are voice, and voice beats
every rule on this page. What you do with a diagnostic is say what you found and
ask, the same as with the three operations above. This is the rule the semicolon
exception, the em-dash exception and the levers-that-add restriction are each an instance
of; when one of them seems to fight an example, read the example as operating on your own
draft, because it is.

**Tell or voice, when the pattern is one somebody could genuinely have.** A tell runs at
machine rate: every paragraph, without variation, whether or not it fits. A habit turns up
sometimes, where it lands. Three tricolons in nine paragraphs is a writer who likes the
figure; nine in nine is the model. Where the rate is genuinely ambiguous it counts as
voice, for the same reason an ambiguous imperfection does.

**Some improvements are real and still not yours to make, so they leave as questions
rather than edits.** The test is one line: *does the operation change what the text
asserts, or who asserts it?* Rewording a sentence does not. Three things do, and every
one of them is a genuine improvement the levers below will find:

| Operation | Why it is not an edit |
|---|---|
| Deleting a claim that is not worth its sentence | Removing an assertion is a content change, however weak the assertion |
| Turning "many experts believe X" into "X" | The claim moves from borrowed authority to the writer's own name |
| Removing a hedge so a qualified statement reads flat | A hedge and a guarantee are different statements |

Collapsing a *stack* of qualifiers to one is not on this list: "it may potentially
possibly reduce X" and "it may reduce X" assert the same thing at the same strength, so
that one is an ordinary edit. Everything on the list gets named in the reply, with what
you would do and why, and the writer decides. **Flagging costs a sentence; guessing
wrong ships a claim the author never made.**

**When there is nobody to ask** (a single-turn call, a batch job, anything with no reply
channel), the question does not evaporate and it does not become permission. Make the
edits that are edits, leave those three operations undone, and put what you would have
raised at the end of the output. **A question you could not deliver is not permission
either**, which is the same principle as the guardrail rule further up, applied to a
missing channel rather than to a dodged answer.
**Say at the top that the pass is incomplete**, not only at the bottom what is missing. A
pipeline strips a trailing note and hands the text on as finished; a text that announces
itself as partial survives that.

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
   Where the subject is also the opener, both rules land on one word, and the way out is
   to **move it, not rename it**: put a clause or a phrase in front so the noun survives
   and the opening changes.

### Past the word list

A draft can be clean of every word below and still read machine-made, because the
loudest tells are structural: how sentences are shaped, how paragraphs enter, where the
emphasis falls. So swapping a listed word for its plain synonym fixes almost nothing on
its own. The sentence keeps the shape it had. When a line reads generated, rewrite the
line: change its construction and the order its parts arrive in, not just its
vocabulary.

## The AI-tell blacklist (avoid or replace)

**Overused vocabulary** (data, not prose; scan against it, do not read it):

```
delve, tapestry, leverage, resonate, navigate (figurative), realm, landscape, testament,
underscore, pivotal, robust, crucial, seamless, foster, elevate, embark, harness,
unlock, streamline, spearhead, meticulous, commendable, boast, swift, myriad, plethora,
nuanced, holistic, vibrant, bustling, ever-evolving, game-changer, cutting-edge, solid,
comprehensive, revolutionary, "in today's fast-paced world", "in the realm of".
```

**Filler openers/closers:** "I hope this message finds you well", "It's worth noting
that", "It's important to note", "It's important to remember", "That being said",
"It goes without saying", "In conclusion", "In summary", "In short", "Looking ahead",
"In general terms", "At the end of the day", "When it comes to...", "As we all know".

**Voice tells:** relentlessly neutral/polite tone, no opinion, no concrete detail, no
names/numbers/anecdotes, flawless grammar with zero contractions.

That last one runs the other way, and the direction is worth holding onto. Every list
here catalogues what a model *over*produces, but absence is a tell too: casual writing
carrying none of the small oral markers a person drops in reads as machine-made as
writing stuffed with *delve*.

It needs a test or it is unfalsifiable, so here is one. It applies only to casual
first-person text **of three sentences or more**: a two-sentence message can carry none of
the four and mean nothing by it. Look for four things and ask of each only whether it appears **at
all**: a contraction, a sentence opening with *And*, *But* or *So*, a parenthetical, a
sentence under five words. **It fails only if all four are absent, and it passes on a
single instance of any one of them.** There is no partial result and nothing here is
tallied: presence is all the rule ever needed, and a count run twice over a long draft
comes back with two different numbers. A thin showing in formal or technical writing is
not a finding at all.

If the draft is yours, fix it with the rhythm and voice levers. If it is the writer's,
**say the register reads flat and ask**: sprinkling markers into someone else's text is
fabrication.

### Structural tells

- Formal transitions in casual text: *furthermore, moreover, additionally,
  consequently, thus, hence.* Cut them or use plain ones (so, and, but, still). Often
  the better edit is to drop the connective and set the two sentences side by side.
  The reader supplies the link, and the seam stops sounding assembled.
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

**Naming one of these characters is not using one.** Quoting a line to show the tell, or
writing the mark inside backticks to talk about it, is discussing the character rather
than emitting it, and the scan does not apply to that. The rules below govern the prose
you produce.

Several rules below split on casual text versus edited long-form, so settle which one you
have before applying them. **The test is whether anything stands between the typing and
the reader.** Email, chat, DMs, a cover letter, a social post, a commit message: typed
into a box and read as typed, so casual. An essay, an article, documentation, a README, a
report: revised before anyone sees it, so edited long-form. A cover letter sits on the
line, since it gets revised like long-form and arrives like a personal message. The
default sends it to casual, which is the right call here: an em-dash in a cover letter
reads generated however many drafts it took.

**When it is genuinely unclear, treat it as casual**, because the error is not symmetric.
A long-form piece carrying zero em-dashes reads perfectly well and loses nothing. A casual
message carrying two reads generated. One direction costs a little polish, the other
costs the whole point of the pass.

- **Em-dashes (`—`). The single strongest tell. Default to zero.**
  No single key produces one, so typing it takes a deliberate act: a shortcut most people never
  learned, a menu, or an editor that substitutes it. Writing at speed a person reaches
  for a comma, a period or a plain hyphen. Meanwhile *edited* prose is full of them, and
  edited prose is what the training corpus over-represents.
  - **Casual:** none. "on your end — just let me know" is a tell. A person writes
    "on your end. Just let me know" or "on your end, just let me know".
  - **Edited long-form:** one or two in the whole piece, only where nothing else does
    the job.
  - **The writer's own em-dashes stay.** Somebody who learned the shortcut and reaches
    for one deliberately is exercising voice, and the rule here is *do not introduce*,
    exactly as it is for semicolons. What this section governs is dashes you would add,
    and dashes in a draft you produced yourself.
  - **Do not swap the character, restructure the sentence.** Replacing `—` with
    `–` or `--` reads just as machine-made, the same tell in a cheaper costume. Reach for
    a period first, then a comma, then parentheses or a colon. **This applies to the
    em-dash and only to it.** An em-dash is doing structural work by joining clauses, so
    swapping the mark leaves behind the structure that gave it away. An en-dash in
    "2010–2015" does no such work: it is a typographic variant of a hyphen, and
    substituting the plain character is the entire fix, which is what the table prescribes. The period is usually the
    better edit anyway, because it also breaks the uniform sentence length the em-dash
    was propping up.
- **The rest of the not-on-the-keyboard family.** The same logic convicts all of them: a
  person typing has no key for these, so their presence means a publishing pipeline or a
  machine. Curly quotes plus an em-dash together are the most recognizable typesetting
  signature there is.
  | Character | What a person actually types |
  |---|---|
  | `…` ellipsis | `...` three periods |
  | `“ ” ‘ ’` curly quotes | `" '` straight quotes |
  | `–` en-dash | `-` plain hyphen |
  | `×` `÷` `≈` | `x` `/` `~` |
- **What you emit and what you infer are different questions**, for this whole family.
  Output is settled by the medium alone: in casual text you emit none of these, ever, and
  Word changes nothing about that. Reading someone else's draft is softer, because Word
  and Google Docs produce em-dashes, curly quotes and `…` by default, so in a document
  drafted there they are weak evidence about who wrote it. Typed straight into an email
  client, a chat box or a code-adjacent tool, they stay strong.
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
topic sentence first, then support, then a tidy landing. Do that in every
paragraph and the uniformity itself becomes the tell, the same way uniform sentence
length does.

Real writing carries traces of the order the thinking happened in. A point gets made
and then qualified two paragraphs later, when the writer thought of the objection.
Sometimes the concrete example lands before the claim it supports, because that is the
bit they wanted to say. In email, people routinely bury the actual ask under context
and it arrives in the last line.

**This does not licence resequencing.** The fidelity rule freezes meaningful ordering and
that stands: steps in a procedure, a chronology, an argument whose parts depend on each
other. What varies here is where a paragraph *starts*, never where it sits. Moving the
example to the front of its own paragraph changes nothing about what follows it.

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
which is the same decorative uncertainty wearing a citation's clothes. Raise it: ask who
those experts are, or whether the writer would rather make the claim in their own voice.
Dropping the frame yourself is not the fix, because it moves the claim onto their name,
which the table near the top puts on the question side.

A fourth form is doubt the writer cannot articulate. Something is off and they cannot
name what, so they circle it, saying the same thing two or three
ways without landing on any of them. Not elegant variation, which swaps synonyms for one
noun: this is one proposition approached from several sides because none of them fits. It is a strong signal, and
a model does not produce it: it states things once, cleanly, whether or not it knows
them. Keep it where the draft has it. Never stage it.

**Lever: strip the hedge that carries no information.** The text shows you which is
which, so you never have to guess at what the writer knows. Stacked qualifiers collapse
to one, they do not vanish: "it's important to consider that it may potentially reduce
X" becomes "it may reduce X", never "it reduces X". The stack was the noise. The hedge
underneath may not be. **Which one survives:** the frames that are not hedges at all
("it's important to consider that", "it could be argued that") are filler and go entirely.
Of the real hedges, keep one and take the plainest, *may* over *potentially*, *might* over
*conceivably*. Where two sit at different strengths, keep the weaker one, because that is
where the writer's own caution was set. A hedge laundered to an unnamed authority, or applied at the same
rate as every other claim in the draft, is worth raising, but **removing it is a change
of claim strength and therefore a question, not an edit** (see the table above). Name it
in the reply and let the writer answer. A hedge that gives a reason or a source is
carrying content and stays exactly as written, no question needed. When you cannot tell
which one you have, that is also a question, and inventing a source to settle it is
worse than asking. Where the writer genuinely does not know, say so in specific terms
and name what would settle it. If a claim is not worth its sentence, **say so and let
them cut it**. What must not happen is keeping it and blurring it. Confidence that varies
with actual knowledge is both more human and more honest.

## Humanizing levers (apply after a first honest draft)

**Name the voice before you touch a sentence.** Formal or casual, terse or verbose,
jargon or plain, contractions or none, the words this writer reaches for and the ones
they never use. Take it from their own drafts when you have them, from the medium and
the reader when you don't. **The voice you build is the voice of whoever will sign the
text.** Writing toward the voice of someone who is not the signer is the impersonation
the guardrails rule out, and the profile step is where that gets decided rather than
discovered later. Every lever below is applied *toward* that profile, and **where a
lever would push the text away from it, the profile wins and the lever does not apply**.
A terse writer does not acquire asides because lever 4 mentions them, and a formal one
does not acquire contractions. **The levers that add only run while you are drafting.**
Dropping in a fragment, a contraction or an aside is writing; doing it to somebody else's
finished text is manufacturing the marks lever 8 forbids. On a draft that is theirs the
pass removes tells and fixes errors, and anything it would have added becomes a
suggestion instead.

Whose draft it is is usually plain from how the work arrived: text you produced in this
conversation is yours to shape, text they pasted in is theirs. **When it is not plain,
ask, and treat it as theirs until you have the answer.** The costs are lopsided the same
way they are everywhere else here. Holding a fragment back from your own draft loses a
little rhythm; adding one to somebody else's puts words in their mouth. Without that target the levers drift toward generic
informality, and that is a register too. A machine one.

1. **Vary rhythm (burstiness).** Read it and mark sentence lengths. If they cluster at
   12 to 20 words, break some. Drop in a short one. A fragment, even. Then let one
   sentence run long and a little unruly. Rhythm is the strongest human signal.
   Do this pass twice, and make the second one count. Cutting filler (lever 5) is
   subtractive, and every deletion pulls a sentence toward the mean, so a draft that
   varied before the cut comes out flat after it. When that happens the repair is to
   *join*, not to fragment: find two short sentences that are really one thought and
   run them together. Reaching for a fragment is the reflex, and it is how you end up
   in the second artificial register.
2. **Vary the shape, not only the length.** Three axes, and a draft can be varied on
   one while flat on the other two.
   - **How the sentence opens.** An adverb, a prepositional phrase, a subordinate
     clause ahead of the subject; once in a while a fronted phrase for emphasis
     ("Changing strategy, that's what they decided"). Fifteen sentences that all start
     on the subject read uniform however much their lengths differ.
   - **Clause complexity.** Simple, compound, complex. Every opener can vary and every
     sentence still be a single clause.
   - **Grammatical voice.** Passive is the right choice when the patient is the topic
     or the actor does not matter: "the migration was rolled back twice before anyone
     filed a bug" puts the migration where the sentence is looking, and naming an actor
     just to force the active would add a fact the writer did not have. Style guides
     all say avoid the passive, so a model trained on them writes almost none, and a
     draft with zero passive constructions is as uniform as one with zero short
     sentences. What shows through there is the rule, not the writer.
3. **Raise perplexity with specificity.** Replace generic nouns/verbs with the exact
   thing: not "improved performance" but "cut cold-start from 4.2s to 900ms". Concrete
   detail is inherently less predictable and more credible. But the specificity has to
   come out of the writer's material. If the draft does not carry the exact number, ask
   for it, or leave the sentence vague and report the gap **in the reply, never inside
   the deliverable**: a "[number missing]" left in the prose ships an annotation to
   whoever reads it next. With no reply channel at all, the vague sentence stands as
   written and the gap goes in the partial-output note; a batch job is never a reason to
   supply the figure yourself. A plausible
   invented figure is worse than the vague sentence it replaced, because it reads true.
   This lever needs a counterweight the way lever 1 does. Applied to every sentence it
   produces prose where each line carries a figure, and that is uniform in a way that
   passes for rigor. Real writing runs dense where the facts are and thins out where the
   writer is working something through. Vary the density between paragraphs, and let the
   thin ones be thin.
4. **Use a real voice.** First person, a clear stance, mild opinion. Contractions
   (I'm, it's, don't). An aside in parentheses. Start a sentence with *And* or *But*
   when it lands. **Those are first-person markers, so they apply when the profile is
   first-person.** A third-person piece gets the stance and the plain words without the
   *I*; installing one because this lever mentions it is the drift the profile rule
   forbids.
5. **Cut filler ruthlessly.** Delete any sentence that would survive as "generic advice."
   If removing a clause loses no meaning, remove it. **Filler asserts nothing**, which is
   exactly why cutting it is an edit: there is no claim to lose. A weak claim is not
   filler, and deleting one sits on the question side of the table above. Same test as
   everywhere else: does removing this change what the text asserts?
6. **Break symmetry, and let interest decide where.** Uneven paragraph lengths, no
   three-of-everything, one point getting two sentences and the next getting five.
   But the shape is the symptom; the cause is that **a machine finds every point
   equally interesting and a person does not.** AI gives each item the same depth
   *and the same enthusiasm*. A person disposes of the obvious in four words and
   then spends a paragraph on the one thing they actually care about, because that
   is where their attention genuinely went. So do not redistribute length at random:
   decide which point the writer would lean on, give it the room, and let the rest
   get short. Uneven emphasis that tracks real interest is far harder to fake than
   uneven line counts, and it is what makes a text feel authored rather than
   generated. When you cannot tell which point they would lean on, **leave the
   distribution alone**: redistributing at random is the failure this lever exists to
   prevent.
7. **Prefer plain words.** "use" not "leverage/utilize", "help" not "facilitate", "big"
   not "robust", "start" not "embark/spearhead". This is about register, not about
   probability: keep the plain word for the action and the specific word for the thing.
8. **Keep small imperfections, and *keep* is the operative verb.** A one-word sentence.
   A sentence that trails off into a qualifier, which has finished its thought and then
   softened it ("it shipped in March, though I would have to check"). That is a choice,
   and it is not the same as a sentence that never closes ("the thing about the migration
   is that when we"), which is a slip and belongs with the errors. A side note that never gets resolved, or
   an idea raised and dropped because the writer assumed the reader would follow. Real
   writing isn't buffed to a mirror finish, and those marks are where the thinking
   shows. What you must not do is manufacture them. An invented aside, a staged
   self-correction, a typo added on purpose: all fabrication, the same rule as an
   invented number, and a reader who catches one reads sloppy rather than human.
   Preserve what the draft already has.
   This is also where the line against lever 5 runs. A digression that shows how the
   writer got somewhere is not filler; one that shows nothing is. Cut by what it
   reveals, not by whether it advances the argument. "(We tried the other order first and
   it was worse.)" stays: it carries a fact about how the work went. "(Which is
   interesting.)" goes: it carries nothing. The test is whether deleting it loses
   information about the writer or their subject, not whether the argument survives
   without it.
9. **Localize.** Idioms, a concrete reference, the writer's actual domain vocabulary.
   Things a model averaging the internet wouldn't reach for. A comparison of the
   writer's own belongs here too, drawn from what they actually work on: "it was like
   nailing jelly to a wall" does the job that an exact number does elsewhere. Same
   constraint as the number, though. An invented figure of speech is the same cheat as
   an invented statistic, and one comparison that lands beats four that decorate.

## Working in languages other than English

The blacklist above is English. The levers are not. Rhythm, specificity and
cut-the-filler transfer to any language, and so does the character scan, because the
em-dash and the curly quote are typographic facts rather than English ones. What does
not transfer is the vocabulary, and it has to be rederived per language rather than
translated. Rederiving means three things, in this order: read the writer's own drafts in
that language and note the words they use and the ones they never do; then apply the
levers, which cross languages intact, because uniform rhythm and empty filler are not
English-specific; and where there are no drafts to read, **say the coverage is thin and
work from the levers alone**. A translated list is worse than no list, because it flags words the target
language does not overuse while missing the ones it does.

Spanish has its own set: "es importante destacar", "en el mundo actual", "cabe
mencionar", "sin duda alguna", *por ende* and *asimismo* as default connectives, a
gerund closing every other sentence ("logrando así...", "permitiendo..."), and naming
the subject with a fresh synonym each time, a habit Spanish schooling rewards even
harder than English schooling does.

Spanish also shows the absence side more plainly than English does. A model writing
casual Spanish produces almost no oral markers, so a WhatsApp message or an informal
email with zero *bueno*, *o sea*, *pues* reads translated even when every word in it is
correct. There the tell is that they are missing, not that they are there.

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

- **Register has to hold, and it holds at the level of the document.** A single document
  gets one voice. Humanizing edits applied unevenly produce drift, a chatty opening
  bolted onto a formal middle, which reads stranger than the uniform version you started
  with. One word out of register inside a sentence is a different thing, and often a
  good one: it is a person reaching for the word they actually think in. What to avoid
  is drift across paragraphs and sections, not the single odd word.
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
- **Character scan (do this last, and run it as a search):** look for `—` `–`
  `--` `…` `“` `”` `‘` `’`, which are U+2014, U+2013, a literal double hyphen, U+2026,
  U+201C, U+201D, U+2018 and U+2019, plus `×` `÷` `≈` (U+00D7, U+00F7, U+2248) from the
  table above. **The target depends on the medium, the same way the rule
  above does: zero in casual text, and in edited long-form one or two dashes in the whole
  piece, kept only where nothing else does the job.** Do not strip a long-form piece to
  zero on the strength of this scan. **For the em-dash**, rewrite the sentence rather than
  substituting another mark. **For the en-dash and `--`**, the plain hyphen is the whole
  fix, since neither is doing structural work. For the rest, just type what a keyboard
  types. This check
  catches the most recognizable tells in the whole list, and it is the only step here that
  needs no judgment at all. It is also the one you are worst at doing by eye: finding
  every instance of a character in a long draft is what a find box or a regex is for, and
  reading for them misses one nearly every time. **Search, do not skim.** Look for semicolons in the same pass; in casual
  text every one is a candidate for a period, **unless the writer's own drafts use
  them**, and then the voice wins and they stay where they are.
- **Repetition check:** find the thing the text is about and list the names it is
  given. If one subject collected three synonyms, pick the best and use it every
  time. Then look at how sentences *start*: that is the repetition worth breaking.
- **Partial pass:** if anything went to the writer as a question instead of an edit, and
  there was no channel to deliver it, the output says at the top that the pass is
  incomplete and lists what was raised at the bottom.
- **Length:** match the medium. A cover letter or email should be shorter than the AI
  instinct to over-explain.

## Quick before → after

**Every ✅ below is built only out of what its ❌ already contained.** Nothing is added,
**and nothing is narrowed**: trading a broad claim for a specific one changes what the text
asserts even when it invents no fact.
That constraint is the point of the section: a rewrite that needs a new fact is not a
rewrite, and examples get imitated harder than rules do.

- ❌ "In today's fast-paced world, I am passionate about leveraging cutting-edge
  solutions to drive impactful results." → ✅ **Nothing to rewrite.** The sentence names
  no problem, no work and no result, so there is no specific version of it that does not
  come from somewhere else. Ask what they actually built and how it went, then write
  that. Vague prose cannot be turned specific by the pass alone. And this is not lever 5
  territory: the sentence is empty of *content*, not of *claim*, so cutting it outright
  would delete an assertion somebody made about themselves. In your own draft it goes. In
  theirs it becomes the question.
- ❌ "The system is fast, reliable, and scalable, ensuring seamless performance." →
  ✅ "It's fast and reliable. It scales." (All three claims survive at their original
  breadth. What goes is "ensuring seamless performance", which asserted nothing the other
  three had not, and the tricolon rhythm. Note the ✅ does **not** trade "reliable" for
  "it stays up": uptime is narrower than reliability, and that swap would be a claim
  change wearing a rewrite's clothes.)
- ❌ "It's not just about writing code — it's about solving real problems." → ✅ "Writing
  code isn't the whole job. Solving the real problem is." (Same claim, both halves intact.
  The negative-parallelism cadence and the em-dash are what leave.)
- ❌ "Many experts believe this approach may potentially improve retention." → ✅ "Many
  experts believe it may improve retention." **and then a question.** Exactly one thing
  changed: "may potentially" collapsed to "may", which is an ordinary edit. **The
  attribution stays in the text**, because dropping it moves the claim onto the writer's
  own name. That gets raised beside the draft, not performed in it, in as many words:
  *"Who are the experts here? I left the attribution alone, because dropping it would put
  the claim in your name. If you would rather assert it yourself, say so."* Two further changes are available here
  and neither is yours, which is why the ✅ is still hedged and still attributed.
- ❌ "I've attached the draft — let me know what you think." → ✅ "I've attached the
  draft. Let me know what you think." (The em-dash was doing nothing a period
  cannot. Note the fix also shortens the sentence, which helps rhythm.)
- ❌ "Happy to adjust the scope — whatever works on your end — just let me know." →
  ✅ "Happy to adjust the scope. Whatever works on your end, just let me know."
