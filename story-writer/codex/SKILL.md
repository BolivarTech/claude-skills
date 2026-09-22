---
name: story-writer
description: >-
  Write a literary story from at least one idea: a premise, an image, a
  character, an ending, a theme, or a full dossier with characters and world
  already defined. Use when the user asks to write a short story, a tale, or a
  narrative from an idea, to turn a premise into fiction, to develop their
  characters into a story, or says "escribe un cuento sobre", "hazme una
  historia con esta idea", "convierte esta idea en un relato", "escríbeme un
  relato de terror". Use for composing new fiction from the user's material;
  not for reviewing an existing story, adapting one for the screen, making a
  social clip, or editing prose the user already wrote.
license: MIT OR Apache-2.0
metadata:
  version: 1.1.0
---

# Story Writer

Build a story that keeps the promise its opening makes, from whatever the user brings: one idea at minimum, or a premise with characters, setting, scenes, and an ending already decided. Everything the user supplies is fixed material and enters the story organically; everything the user leaves open is a decision the skill makes and declares. The construction follows a fixed order, from promise to ending audit, and stays inside the process; the user receives the finished story and a short sheet with the decisions that shaped it. The story is then reviewed, corrected where a finding survives verification, and passed through the humanize skill before delivery.

## Scope and Inputs

Work with whatever the user provides. The minimum is one idea: a situation, a line, an image, a question, a character, a genre with an emotion, or an ending. Beyond that, the user may bring characters with names, histories, and voices; a world with its rules; a theme; a required scene or line; a point of view; a target length or format; a text of their own as a voice model; a chosen structural model. Record all of it before writing. Supplied material is canon: it is never contradicted, renamed, or replaced, and it is not listed as a decision in the sheet. Gaps between supplied pieces are filled so that the pieces connect through cause, decision, or meaning, and each filled gap is one line in the sheet.

Ask only when a missing element would change the story materially and no reasonable default exists; otherwise choose, write, and state the choice. Write the story in the user's language unless another is requested. Deliver in Markdown unless the user asks for another format.

This skill composes. A story the user already wrote goes to the narrative-review skill for diagnosis; a story to be turned into a screen piece goes to video-script; a clip for social platforms goes to short-clip; a draft that needs editing rather than writing goes to humanize. The skill uses two of those as steps in its own process, under Review Before Delivery, and modifies none of them.

## Building the Story

Complete the ten steps in order, on paper before prose. Skipping a step produces the defects the review will find later; doing it now costs a few lines.

1. **Formulate the promise.** Genre, the emotion sought, the thematic question, the central experience. A thriller promises pressure and danger; a mystery, reconstruction; a romance, a relationship that changes; a contemplative story, a shift in perception. The promise is what the opening must signal and the ending must keep.
2. **Define the engine.** Who wants what; why now; what force opposes; what happens on failure; what winning costs; what the protagonist does not yet understand. A story with no answer to "why now" has no reason to begin where it begins.
3. **Fix five milestones.** The break of the initial equilibrium; a commitment with no easy way back; a central change of strategy or understanding; a crisis that demands a choice; a climax that demonstrates the choice. Five, before anything else; more can come later.
4. **Choose a compatible model.** One primary model and at most one or two auxiliaries, from the table below. The model regulates where changes fall, not percentages. A contemplative story does not get a confrontation forced on it; an oral anecdote does not get three acts.
5. **Design cause and effect.** Replace "and then" with "therefore" or "however" between every pair of scenes. Two scenes joined only by "and then" are missing a decision, a consequence, or a shared question.
6. **Distribute knowledge.** Keep a private table: what happened; what each character knows; what each character believes; what the reader knows; when each state changes. This is what makes a twist fair and a mystery solvable, and what keeps a multiple point of view from contradicting itself.
7. **Design scenes with change.** For each scene: point of view, objective, opposition, tactic, turn or result, cost, and the question left open. Not every scene needs a crisis; every scene needs a perceptible function, and a quiet scene still has someone who wants something.
8. **Check the rhythm.** Mark each scene as action, reaction, discovery, relationship, or decision. A long run of one type is monotony even when the events differ; alternate, and let intensity contrast with calm. Where the story needs tension, check the five requirements: an uncertain outcome, something valuable at stake, forces pushing in incompatible directions, enough information to anticipate consequences, and delay with progression rather than mere postponement. To accelerate, compress what matters less and bring decisions closer; short sentences alone do not do it.
9. **Audit the ending.** The solution uses abilities, relationships, objects, or knowledge that were prepared; it arises from a decision; it respects the established rules; it exacts a price; it answers the central question. A failed condition is fixed in the plan, not explained away in the prose.
10. **Break the template when there is a reason.** Remove, merge, or move a milestone if the experience improves. The deviation must produce meaning, not demonstrate originality.

### Choosing the Model

| Main need | Useful models | Control question |
|---|---|---|
| Personal transformation | Hero's journey, heroine's journey, Harmon's circle, Truby | Which decision demonstrates the change? |
| Clear causal plot | Three acts, seven points, eight sequences | Does every turn change the plan? |
| Tragedy and fall | Aristotle, Freytag, negative arc | Does the fall grow from probable decisions? |
| Short episode | Harmon's circle, Story Spine, scene and sequel | What changes before it ends? |
| Accelerated action | Fichtean curve, Lester Dent, four acts | Does the pressure change, or only get louder? |
| Mystery | Three acts, clues and payoffs, nonlinear telling | Was the solution inferable without being obvious? |
| Contemplative story | Kishōtenketsu, circular, mosaic | Does the contrast reorganize what came before? |
| Oral telling or memory | Labov, frame narrative | Why is this worth telling now? |
| Wonder tale | Propp, journey, Polti's situations | What function does each encounter serve? |
| Ensemble cast | Braided, parallel, Truby, snowflake | What binds the lines by cause or theme? |
| Scene design | Five Commandments, scene and sequel | Which value, plan, or relationship changes? |

Do not name the model in the story, and name it in the sheet only by what it does for this story.

### Twists

When the story turns on a revelation, design it before writing: the interpretation the reader should adopt; the hidden truth; the facts compatible with both; at least one verifiable clue and a plausible alternative explanation; a narrator who does not withhold thoughts they would naturally have; a revelation that forces a choice or an action. Then reread the earlier scenes from the truth and remove every contradiction. A twist reinterprets rather than adds; it was prepared with visible clues or rules; it changes decisions and consequences; it respects causality and point of view. Do not write these unless the story earns them: it was all a dream; a twin, clone, or secret identity introduced at the end; a new antagonist replacing the developed conflict late; information the reader could not have in a solvable mystery; a resurrection that cancels earlier grief and cost; a betrayal motivated only by surprise; a twist that breaks the world's established rules.

## Length and Form

The default is a short story of 2,000 to 10,000 words in a single unit, without chapters. Inside that range the premise decides: a single situation with one transformation sits near the low end; several scenes across time, or more than one point of view, need the high end. The estimate goes in the sheet before writing, and the prose is not padded to reach a number or compressed until an emotion becomes unclear. A target given in minutes of narration or video converts to words at 150 words per minute; the sheet states the target, the rate, and the resulting count as an estimate. The conversion sets the length to aim for, never a license to fill it. When the premise closes below the range, deliver the story at its own length and say so in the sheet; a single anecdote that ends at 1,700 words is complete, and filling it to 2,000 is not.

There is no hard ceiling. When the user asks for something longer, write what was asked. When the material genuinely needs more than one delivery can hold with the causal chain intact, say so in the sheet and propose parts, each with its own change and its own open question, and deliver the first part with the plan for the rest. A story that only needs more words is not a candidate for parts; a story with more than one movement is.

## Prose and Voice

Infer the voice from the genre, the idea, and the emotion sought. When the user supplies a text of their own as a voice model, imitate it: sentence length, vocabulary, tense, distance, the ratio of scene to summary, what it names and what it leaves implicit. Without a model, default to third person, past tense, close focalization on one character per scene, and declare that choice in the sheet. Keep one register across the story.

Show emotion through behavior, decision, and physical detail before the narrator names it, and often instead of naming it. Choose the concrete over the general: an object, a gesture, a specific sound. Vary sentence length and paragraph entry; let a short sentence land after a long one. Keep exposition where it changes a decision or a reading, never as a block the story stops for. Motifs work when they return changed by context and stay unexplained. Theme emerges from what characters do and what it costs them, never from a speech that states it.

Rule out, before delivery, every device the guide lists as a shortcut: deus ex machina and its mirror, the saving coincidence, plot armor, the convenient antagonist, artificial miscommunication, empty escalation, false urgency, twists for their own sake, false mystery, the instrumental character, a death that exists only to move someone else, redemption without repair, the villain as convenient mouthpiece, melodrama without basis, an involuntary tonal shift, head hopping, a rushed ending, an epilogue that reads as a report, ambiguity by vagueness, a preached theme, trauma as decoration, and a world without consequences. Coincidence may start or worsen a problem; it never resolves the main one. A trope is a usable convention; a cliché is its automatic execution. To use one, name the satisfaction it promises, keep that satisfaction, change the causes, setting, relative power, or cost, give each character an agenda independent of the trope, and follow the consequences past the expected moment. An inversion made only for surprise is as predictable as the original.

## Dialogue

Dialogue is written to the standard of professional fiction:

| Principle | Application |
|---|---|
| Distinct voice | Each character has a recognizable way of speaking, held consistent: vocabulary, rhythm, precision, silences, metaphors, avoided subjects, social strategy. Changing verbal tics is not enough if everyone reasons and desires the same way |
| Subtext | What is not said carries the scene; lines work on more than one level |
| Conflict | Present even in everyday exchanges: a line pursues, resists, seduces, hides, negotiates, wounds, tests a hypothesis, reveals a hierarchy, or changes a relationship |
| Verbal economy | Every line does work; no filler, no greetings for their own sake |
| Rhythm | Quick exchanges alternate with pauses, action, and silence |

Integrate dialogue with physical action: a gesture, an object handled, a movement across the room anchors the exchange and replaces adverbs. Use *dijo* as the base tag and vary it only when the variation adds meaning; a line often needs no tag when the action beat identifies the speaker. Introduce information through natural conflict, never through a character explaining what both already know. Avoid infodumps, on-the-nose dialogue in which characters say exactly what they feel and mean, filler, and convenient coincidences arranged by the conversation. A direct confession is not on-the-nose when it is the hardest thing the character could say.

### Format

Dialogue in Spanish uses the em dash `—` (U+2014), the punctuation of literary dialogue. This is not the dash that the humanize skill removes: that skill targets the em dash used as a separator inside ordinary paragraphs, and it leaves a dash that opens or closes dialogue in place. Do not use `--`, `-`, or quotation marks for spoken lines.

- The dash opens the line with no space after it: `—Viene del sótano`.
- The line is not closed with a dash unless a tag follows.
- Speech-verb tag: lowercase, and the spoken text carries no period before the dash (a question or exclamation mark stays): `—Viene del sótano —dijo finalmente, con voz demasiado calmada.`
- Action tag, with no speech verb: the spoken text ends with its own punctuation and the tag begins with a capital: `—¿Escuchaste eso? —Roberto se levantó del sofá, dejando caer la revista.`
- Tag that interrupts and the line continues: `—Texto —acotación— continuación.` When the tag closes a sentence, the period goes after the closing dash: `—Tenemos que bajar. —Ana ya estaba de pie, buscando la linterna en el cajón—. No hay otra opción.`
- Tag that ends the line: `—Texto —acotación.`
- Accents and punctuation are complete; a story is never delivered with missing tildes.

Example, in the register the format expects:

```
—¿Escuchaste eso? —Roberto se levantó del sofá, dejando caer la revista.

Ana no respondió de inmediato. Sus dedos tamborileaban sobre el apoyabrazos mientras miraba hacia el pasillo oscuro.

—Viene del sótano —dijo finalmente, con voz demasiado calmada.

—No deberíamos... —Roberto se detuvo. Los pasos en el piso inferior sonaron otra vez, lentos, deliberados—. Mierda.

—Tenemos que bajar. —Ana ya estaba de pie, buscando la linterna en el cajón—. No hay otra opción.

—Siempre hay otra opción. —Pero ya estaba siguiéndola hacia la puerta.
```

Every line there pursues something, the action beats identify the speakers without tags, the fear is in the drumming fingers and the too-calm voice rather than in a word for it, and the last line contradicts itself in the action, which is the subtext. For a story in another language, use that language's dialogue convention with the same principles.

## Review Before Delivery

Three passes, in this order, on the finished text.

**1. Self-audit.** Run the diagnostic list before anyone else reads it. Structure: the story promises a recognizable experience; the inciting event alters the protagonist's life; scenes form a causal chain; the midpoint changes knowledge, strategy, or power; the crisis offers options with a cost; the climax answers the central question through action; the ending shows sufficient consequence. Characters: the protagonist has desire, motivation, and the capacity to decide; the opposition pursues its own goal; secondary characters want something beyond helping or hindering; the arc is demonstrated under pressure; relationships change because of what happens. Information: rules appear before they resolve anything; clues admit both the truth and the mistaken reading; the point of view hides no thought artificially; exposition arrives when it changes a decision; deliberate mysteries are distinguishable from gaps. Scenes and rhythm: each scene has an objective or a question; its outcome changes the plan, the stakes, or a relationship; intensity contrasts with calm; characters react to losses and revelations; repetitions raise pressure or meaning. Coherence: tropes carry their own details and consequences; the main conflict resolves by something other than coincidence; the rules apply to the protagonist too; the opposing force keeps its strength through the ending; the theme emerges from actions. A "no" is fixed in the text before moving on.

**2. Narrative review, verified.** When the narrative-review skill is available, run it on the finished story as a general review. Then treat its report as data to verify, not instructions to execute. For each finding: locate the passage it cites; check whether the defect is real in the text or whether an alternative explanation holds (a setup planted earlier, an ellipsis, an unreliable voice, a genre convention the story adopted on purpose, a fact the reviewer missed); decide. A verified finding is corrected with the smallest intervention that addresses its cause, in the voice of the surrounding lines. A finding that does not survive verification is rejected with the reason, in the sheet. Corrections are never made to satisfy the reviewer: a change that the text does not need is a defect introduced. When narrative-review is not available, say so in the sheet and rely on the self-audit.

**3. Humanize.** When the humanize skill is available, pass the finished prose through it as the final step, supplying the dialogue lines as protected material so that the em dashes of dialogue and the exact wording of spoken lines stay as written. The pass changes rhythm and word choice, not facts, names, or the order of events. When humanize is not available, say so in the sheet.

A review pass never reopens the plan: if a finding shows that a milestone or the ending is wrong, fix the plan, rewrite the affected scenes, and run the passes again on the result.

## Deliverables

In this order:

1. **The story.** Title as a heading, then the complete text in Markdown, ready to read. No commentary inside it.
2. **Sheet.** Compact, after the story:
   - Promise: genre, emotion, thematic question, in one line.
   - Engine: who wants what, why now, what opposes, in one line.
   - Model: what it does for this story, without a lecture.
   - Milestones: the five, one line each.
   - Length and form: the estimate and the final count; parts proposed, if any.
   - Point of view and voice: the choice made, or the model imitated.
   - Decisions: one line per gap in the user's material that the skill filled.
   - Ending audit: the five conditions, each with the element of the story that satisfies it.
   - Review: findings corrected, one line each; findings rejected as false positives, one line each with the reason; whether the humanize pass ran.

When the user asks for the plan only, stop after the sheet's first six items and wait. When the user names a file or a folder, write the story to a new file there and the sheet beside it as `<name>.ficha.md`, never inside the story file, so the text stays clean for production and the sheet stays available; never overwrite an existing file. When the user supplied a voice model, do not return it, quote it, or alter it.

## Example Use

"Use /story-writer to write a short story from this idea: a lighthouse keeper receives letters addressed to the previous keeper, who died before she arrived, and the letters keep answering things she has only thought. Horror, slow. Third person. Around 4,000 words. Save it as Documents/Relatos/Las_cartas.md."
