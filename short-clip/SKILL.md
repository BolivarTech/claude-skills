---
name: short-clip
description: >-
  Turn an idea, meme, phrase, anecdote, or reference image into a vertical
  clip of a few seconds for TikTok, Instagram Reels, or YouTube Shorts: one
  prompt that generates the reference image and one prompt that animates it
  with its dialogue, plus post copy when a platform is named. Use when the
  user asks for a reel, a short, a TikTok, to animate an image or a meme, to
  turn a joke or an anecdote into a clip, or says "hazme un reel", "un short
  con esto", "anima esta imagen", "convierte este meme en video", "dame el
  prompt para animarlo". Not for adapting a narration into a production
  script, for diagnosing a story, or for text with no clip to make.
license: MIT OR Apache-2.0
metadata:
  version: 1.0.0
---

# Short Clip

Turn the user's material into a clip of about ten seconds in which something happens, the viewer's reading of the situation changes, and the ending leaves a reaction for the viewer to imagine. The deliverable is two prompts: one that generates the reference image and one that animates it with its dialogue and sound. The narrative work stays inside the process; the user receives what the generation tools consume. Preserve the premise, tone, characters, required wording, and chosen platform. Do not force every idea into one formula: select the architecture by the intended effect.

## Scope and Inputs

Work with whatever the user provides: an idea, anecdote, meme, phrase, or dialogue; a reference image; a genre, emotion, or audience; a platform, duration, and format; required dialogue, voiceover, music, or sound; the target generation tool, if named.

The unit is one generated clip. Assume a vertical 9:16 video of about ten seconds, a general audience, the user's current language, and no lip-sync tool unless one is named. Ask only when a missing detail would change the concept or prevent a requested element; otherwise choose and state the choice in one line.

This skill does not produce a production script with scenes, shot lists, and delivery specifications, and does not diagnose a story. A narration with a production plan belongs to the video-script skill; a text to be reviewed belongs to the narrative-review skill.

## Phrase or Story

Before choosing a structure, decide what the material is. A phrase is a thought illustrated: an attitude, a caption, a recognizable feeling with nothing happening around it. A story has a character, an interaction, a change, and a consequence. A phrase produces recognition; a story produces a question, and only a question keeps a viewer past the first second.

When the material is a phrase, convert it before writing anything: give it a character with an intention, an interaction that carries the phrase, a fact that changes how the phrase reads, and a visible consequence. When no conversion keeps the user's meaning, say that the material carries a still image or a caption better than a clip, and offer the conversion as an option.

The test that fits the scale: state the setup and the turn in one sentence. If it needs two, the clip needs more seconds than it has; cut context until it fits.

## Selecting the Architecture

Choose one primary model and, when useful, one supporting technique. Do not name the model in the response unless the user asks. Every architecture must satisfy the same four conditions: the opening raises a question or an emotion within the first seconds; the middle gives only the context needed to understand the situation; at least one thing changes in expectation, situation, or understanding; the piece ends immediately after the strongest reaction, consequence, or image.

| Material or intended effect | Architecture | Control question |
|---|---|---|
| Personal anecdote | Orientation, complicating action, evaluation, resolution, coda; the on-screen title carries the abstract | Why is this worth telling now? |
| Humor built on a perspective shift | Introduction, development, turn or contrast, integration | Does the turn reorganize what came before? |
| Visual joke | Setup, expectation, contrary result, reaction | Does the image pay what the setup promised? |
| Everyday problem | Equilibrium, disruption, reaction, new equilibrium | What is different at the end, and who paid for it? |
| Character pursuing something | Comfort, desire, attempt, cost, result, change | Which action shows the change? |
| Horror or suspense | Normality, anomaly, progressive delay, revelation, consequence | Does the delay progress, or only postpone? |
| Emotional reflection | Concrete situation, observation, discovery, new perspective | Does the contrast produce a new perception? |

**Frame shift.** When later information can turn an ordinary situation into something absurd, unsettling, or unexpected, prefer this pattern: everyday situation, ambiguous setup, revelation that changes the frame, reaction, optional coda. The setup must support both the first reading and the revelation; the reaction demonstrates the consequence without repeating the explanation. It carries the strongest change a clip of this length can hold, and its universal opening lets a viewer outside the genre follow it. It is a default when the material admits it, not a requirement.

## Designing the Turn

Before writing, separate the audience's first interpretation, the hidden truth or unexpected fact, the facts compatible with both readings, and the visible consequence of the revelation. A valid turn reinterprets earlier information, respects causality, and changes a reaction, decision, or outcome. Avoid random surprises, information the audience could never anticipate, and contradictions created only for impact. The test is double: the first viewing surprises; the second shows that the setup never cheated. A clip is rewatched, so the second viewing is part of the design, not an afterthought.

The hook is a promise. Whatever the opening makes the viewer ask, the ending answers or transforms; a hook that the body does not pay is the fastest way to lose the viewer who stayed. Contrast is part of the payload: a clip that moves through two or three emotions (flirtation, discomfort, fear, laughter) lands harder than one that stays in a single register, and a change of genre inside the clip is the strongest form of frame shift.

End after the strongest reaction. Do not explain the punchline after it lands. Leave a space the viewer completes: the face we do not see, the thought we infer, the decision that comes next. A clip that delivers everything finished gives the viewer nothing to add, and nothing to say in the comments.

## Beats and Timing

Define, in this order and for internal use: hook, open question, setup, central change, reaction or punchline, final image. Then distribute them across the duration. For a clip of eight to twelve seconds, a flexible reference:

| Segment | Function |
|---|---|
| Opening | Visual or verbal hook; the situation is legible before anyone speaks |
| First third | Minimum context and setup |
| Second third | Complication or turn |
| Ending | Reaction, consequence, or punchline, then cut |

Adapt the number of beats to the idea. Do not stretch a joke to fill the runtime or compress an emotion until it becomes unclear. Spoken material fits when it stays near two and a half words per second, the same reference rate the video-script skill uses; about twenty-five words in ten seconds, fewer when a pause or a reaction needs the time. When the dialogue does not fit, cut context before cutting the turn.

## Voice, Dialogue, and Sound

Separate voiceover, character dialogue, and on-screen text, and mark which is which in the animation prompt. Preserve verbatim any wording the user marks as exact. Differentiate voices through intention, rhythm, and attitude, not only through labels. Specify a pause or an emphasis only when it improves the delivery.

Voice and image do not say the same thing. The voice prepares an interpretation and the image modifies it, or the image sets the situation and the voice changes what it means. A voiceover that describes what the frame already shows adds no information and no curiosity; when that is all a line does, cut the line or change the image.

When a visible character speaks, request lip synchronization for that character. For voiceover, require visible characters to keep their mouths closed unless another action justifies the movement. Use music and effects to support pacing; they never cover dialogue. Request original music and avoid recognizable copyrighted melodies unless the user supplies a licensed track or controls the rights.

## The Image Prompt

The first prompt generates the reference image, and it fixes everything the animation must keep constant. It opens by naming the visual style: the one the user asked for or, when none was named, one chosen and stated in a line of the response. When the image shows a person, the prompt declares the character original and fictional; a described face with no style and no such declaration reads as a request for a real likeness, and some tools respond by asking for the user's photos. Before writing it, list the invariants: identity and face, age, wardrobe, anatomy and hands, the objects in the scene and which hand or side holds each one, existing text, environment, light, and lens feel. The same list is repeated in the animation prompt; a detail that is not fixed here will drift there.

Compose for the clip, not for a poster. One central relationship, legible on a phone in a single glance: the viewer must find the point without searching, so a scene with many objects, lights, and decorative elements competes with the joke. The frame is 9:16 with the subject placed where the platform interface will not cover it. Text inside the image only when the user asks for it, short enough to be read at once on a small screen. No subtitles, captions, logos, or watermarks unless explicitly requested.

When the user supplies the image, skip generation and extract the invariants from it by description; the list still gets written, because the animation prompt needs it. For an image that contains text, preserve, remove, or replace it according to the request; when removing, instruct the tool to reconstruct the background coherently. Do not build the prompt around the likeness of a real, identifiable person unless the user states the right to use it.

## The Animation Prompt

The second prompt describes the clip as a timed sequence. Specify:

1. Duration, aspect ratio, and the reference image as the opening frame.
2. The visual style and the invariant list from the image prompt: what must remain constant.
3. Actions and expressions in chronological order, with the second at which each begins.
4. Camera, lighting, and environmental motion, each with a narrative reason.
5. Exact dialogue and voiceover, with language, voice, intention, and synchronization requirement.
6. Music, ambience, and sound effects.
7. Final frame or reaction.
8. Constraints and defects to avoid.

Progression is narrative, not mechanical. A camera move over a still frame is still a still frame; smoke, candles, or a drifting background do not substitute for a change. Every segment of the clip changes something the viewer can see: a gaze, an action, a discovery, a reaction. Repeat the high-risk invariants at the end of the prompt: identity, face, anatomy, hands, number of objects, which side holds each object, clothing, existing text, and environment design.

Write the prompts in English unless the user asks for another language; keep every line of dialogue in the language the user requested. Preserve exact wording inside the prompt with quotation marks so the tool does not paraphrase it.

## Platform Copy

Produce copy only when the user names a platform or asks for it. Keep the narrative core and adjust the presentation:

- **TikTok:** immediate entry, conversational tone, and a short description that complements the video.
- **Instagram Reels:** strong visual clarity, a shareable payoff, and concise post copy.
- **YouTube Shorts:** a premise understandable without prior context and a title that presents the anomaly or the outcome.

The description does not repeat what the clip already said; it adds identification, complicity, or a second comedic layer, and it gives the viewer something to answer: a question, a position to contradict, a "what would you have done". Use a small set of relevant hashtags and no unrelated ones.

Do not promise reach or attribute performance to a single variable. Distribution tests a clip on a small first audience, and two pieces of similar quality can perform very differently. When the user asks for optimization, consider the hook, retention, completion rate, rewatches, shares, comments, visual clarity, audio, and the first audience, and present them as levers, not guarantees.

## Common Mistakes

| Symptom | Correction |
|---|---|
| A phrase illustrated: attitude, caption, feeling, nothing happens | Convert it into a story with character, interaction, change, and consequence, or recommend a still |
| The whole joke is visible from the first frame | Move the payoff to the last third; the opening shows the situation, not the result |
| The turn is a surprise that nothing prepared | Find the facts compatible with both readings; if there are none, it is not a turn |
| Nobody changes conduct after the turn | Give the revelation a visible consequence: someone stops, leaves, goes silent, decides |
| Image, text, and voice communicate the same thing | Assign each channel a different job; cut the channel that only repeats |
| The clip stays in one emotion | Add a second register the turn moves into: from ordinary to unsettling, from flirtation to fear |
| The frame needs searching: many objects, lights, decorations, long text | Reduce to one central relationship; text that reads in a glance |
| Camera drift over a still image sold as motion | Replace it with a change the viewer sees: gaze, action, discovery, reaction |
| The hook promises what the ending does not pay | Rewrite the ending to answer the opening question, or rewrite the hook to promise what the clip has |
| The description repeats the clip | Use it for a second layer and a reason to reply |

## Final Check

Before responding, verify:

- Can the setup and the turn be stated in one sentence?
- Does the opening create a question or an emotion, and does the ending pay it?
- Does every segment change something visible?
- Does the setup survive a second viewing?
- Does the piece end without explaining the punchline, with something left for the viewer to complete?
- Does the dialogue fit the runtime at the reference rate?
- Do the two prompts share the same invariant list?
- Is the image legible on a phone in one glance?
- Does the output match the requested format, language, and tool?

If any check fails, revise before delivering. When the material as the user gave it failed a check and the revision changes something the user specified, or when the fix is offered as an option rather than applied, say so in the response: one line per check, naming the check, what was found, and what was changed or proposed. It is a note, not a report; the diagnosis stays inside the process, and the user sees what was reviewed, what was found, and what is proposed.

## Deliverables

Return the prompts and nothing else unless the user asks for more. The structure, beats, and script are working material; include them only on request. Alternative endings only when the user asks for them or when the material admits two meaningfully different turns.

**Concept:** one sentence with the setup and the turn.

**Image prompt:** the reference image, with its invariant list.

**Animation prompt:** the timed sequence with dialogue, voice, sound, final frame, and the invariant list repeated.

**Post copy:** title, description, and hashtags, only when a platform was named or copy was requested.

**Notes:** one line per check the original material failed, with the change made or proposed, and one line per choice made for a missing detail. Nothing else.

Write the concept and the copy in the user's language; write the prompts as specified under The Animation Prompt.

## Example Use

"Use /short-clip to turn this meme into a ten-second TikTok. The image is attached; keep the exact line written on it and the second character's reaction. Give me the prompt to regenerate the image without the caption and the prompt to animate it with the dialogue, plus the post description."
