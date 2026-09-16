# Changelog

All notable changes to the `short-clip` skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in the
[repository README](../README.md#versioning).


## [1.0.0] - 2026-09-16

First release. The skill turns an idea, meme, phrase, anecdote, or reference
image into a vertical clip of about ten seconds and returns the two prompts the
generation tools consume: one for the reference image and one that animates it
with its dialogue and sound. Post copy is added when a platform is named. The
narrative work stays inside the process.

### Added

- Scope: one generated clip, 9:16, about ten seconds, the user's language, no
  questions unless a missing detail changes the concept. A narration with a
  production plan is sent to `video-script`; a text to be reviewed, to
  `narrative-review`.
- A phrase-or-story gate before any structure is chosen: a phrase is converted
  into character, interaction, change, and consequence, or reported as better
  served by a still. A one-sentence test for setup plus turn fixes the scale.
- An architecture table for anecdote, perspective-shift humor, visual joke,
  everyday problem, pursuit, horror or suspense, and reflection, each with its
  control question, and the frame-shift pattern as the default when the
  material admits it.
- Turn design: first reading, hidden truth, facts compatible with both, visible
  consequence, and the second-viewing test. The hook is a promise the ending
  pays; emotional contrast and a change of genre inside the clip are part of
  the payload; the piece ends after the strongest reaction and leaves a space
  the viewer completes.
- Beats and timing for eight to twelve seconds, with the reference rate of two
  and a half words per second shared with `video-script`.
- Voice rules: voiceover, dialogue, and on-screen text kept separate; voice and
  image never say the same thing; lip sync for a visible speaker; mouths closed
  under voiceover; original music.
- The image prompt: it opens by naming the visual style, the user's or one
  chosen and stated, and declares a person an original fictional character; an
  invariant list written once and repeated in the animation prompt; one
  central relationship legible on a phone in a glance; no text, subtitles,
  logos, or watermarks unless requested; no likeness of a real, identifiable
  person without the user's stated right to use it.
- The animation prompt as a timed sequence, with narrative progression required
  in every segment; a camera move over a still frame does not count.
- Platform copy only when a platform is named: it adds a layer and a reason to
  reply instead of repeating the clip. Reach is never promised.
- A common-mistakes table of ten symptoms with their corrections, a final check,
  and a deliverables format: concept, image prompt, animation prompt, post copy,
  and notes: one line per check the original material failed, with what was
  changed or proposed, and one line per choice made for a missing detail.
- A ChatGPT package in `chatgpt/`, identical to the skill.
