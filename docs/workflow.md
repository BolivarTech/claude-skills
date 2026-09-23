# From an Idea to a Production Script

This guide shows how the skills in this repository work together, step by step,
from a one-line idea to a finished story and then to a script ready for video
production. Each skill does one job and hands its result to the next. You can
enter at any step: if you already wrote the story, start at step 2.

The [README](../README.md) covers installing and configuring the skills. This
page covers using them.

---

## The Whole Flow

```
idea
 │
 ▼
1. story-writer ──────────► story + decision sheet
 │
 ▼
2. narrative-review ──────► does the story work? → apply the fixes you choose
3. attention-review ──────► does it hold the reader? → apply the fixes you choose
 │
 ▼
4. humanize ──────────────► one pass, if it has not run already
 │
 ▼
5. proofread ─────────────► spelling, grammar, and typography: the story is final
 │
 ▼  (if it becomes a video)
6. video-script (adapt) ──► production script
7. attention-review ──────► does the script hold the viewer?
   video-script (review) ─► production defects
 │
 ▼
8. proofread ─────────────► the script is final
 │
 ▼  (optional)
9. short-clip ────────────► vertical clips to promote the episode
10. premortem ────────────► stress-test the launch plan
```

The order matters. Story problems come before polish, because fixing the plot
changes the sentences. Polish comes before proofreading since every rewrite can
bring new errors, and proofreading goes last: nothing after it should change the
text.

---

## Step by Step

### 1. Write the story: `story-writer`

**Say:** "escribe un cuento sobre…", "write a story from this idea", or hand it
a premise, an image, a character, or a full dossier.

**You get:** the story in a new file, and beside it a decision sheet
(`<name>.ficha.md`) listing what the skill decided where your material left a
gap. The skill reviews its own draft and ends with a humanize pass, so the
text does not read as generated.

**Skip this step** when you wrote the story yourself.

### 2. Check the story: `narrative-review`

**Say:** "revisa mi cuento", "is this ending earned?", "review this chapter".

**You get:** a report with a verdict, the strengths to preserve, and numbered
findings (N1, N2, and so on), each with its location, evidence, and the smallest fix.
The review changes nothing.

**Then say:** "aplica N1 y N3" to apply the findings you pick. The skill edits
only those passages, then runs humanize over the whole text so new lines match
your voice and the rest reads naturally. The change log lists every finding
and every humanize edit separately, so any single edit can be reverted.

### 3. Check that it holds the reader: `attention-review`

**Say:** "revisa la atención de mi guion", "¿esto engancha?", "where do readers
lose interest?".

**You get:** a table of seven stages (recognition, gap, promise, proof,
progress, payoff, transmission) and findings (A1, A2, and so on) on where a reader is
likely to stop and why. Plot and character questions are sent back to
narrative-review; this skill only judges attention.

**Optional for a story that goes straight to video:** the script gets its own
attention review at step 7.

### 4. Polish once: `humanize`

humanize removes the traces that give a text away as generated. It already
runs inside steps 1, 2, and 3. Running it three times costs tokens and wears
the voice flat, so there are two ways to keep it to one pass:

- Let it run inside the last step that applied corrections, and skip this step.
- Or, in steps 2 and 3, add **"sin humanize, lo paso al final"** ("without
  humanize, I'll run it at the end") and run it once here.

When you run humanize on its own over literary prose, tell it the register
and the devices that are style, for example: "this is a gothic story; keep the
dialogue and inciso dashes, the anaphora, the fragments, and the ellipses".
Without that instruction it treats them as it would in an email.

### 5. Proofread: `proofread`

**Say:** "corrige la ortografía", "revisa tildes y puntuación", "proofread
this".

**You get:** the corrected text in a new file and a report with every change
and its rule, the doubts left for you to decide, and the criteria applied to
the whole text. Add **"solo revisa"** to get the report without any change to
the text.

proofread corrects errors against the norm (RAE for Spanish, Chicago for US
English, or your project's own style guide) and never touches style. After it,
the story is final. If you edit it again, proofread again.

### 6. Adapt to video: `video-script`

**Say:** "adapta este relato a video", "guion de producción".

**You get:** a production script: narration, dialogue, cues for image and
sound, and production notes, following your project's production instructions
when you supply them.

### 7. Check the script

- **`attention-review`**: retention of the script. For TikTok, Reels, or
  Shorts it adds feed checks: first frame, sound-off readability, safe zones,
  a payoff with margin before the end.
- **`video-script`** in review mode ("revisa el guion del episodio"): image,
  sound, editing, continuity, accessibility, and production defects.

Run attention-review first: its fixes change the text, and the production
review should look at the final version.

### 8. Proofread the script: `proofread`

The script is a new text, so it gets its own proofreading. It follows the
project's conventions first: for example, full accents inside SSML blocks,
where they drive the synthetic voice's pronunciation.

### 9 and 10. Optional

- **`short-clip`**: turns a moment of the episode into a vertical clip of a few
  seconds: the prompt for the image, the prompt to animate it, and the post
  copy.
- **`premortem`**: imagines the launch plan has already failed and works out
  why, before you commit to it.

---

## Rules That Tie the Steps Together

- **Every step writes a new file** beside the original and never overwrites
  it. You can compare any two versions with `diff`.
- **Reviews diagnose; corrections are on request.** A report never changes the
  text. Only "aplica…" does.
- **humanize runs once per text,** at the last step that edits it. "sin
  humanize" turns it off in any step; "cambia poco" keeps it but limits it to
  errors and clarity.
- **proofread runs last, every time a text is final:** the story, and later
  the script.
- **proofread and humanize never call each other.** humanize removes signs of
  generated text; proofread corrects errors against the norm. The same dash
  can be style in a Spanish dialogue and a giveaway in an English email, which
  is why the calling step tells humanize what to keep.

---

## A Worked Example

1. "escribe un relato de terror sobre un faro donde la luz se apaga sola"
   → `El_faro.md` and `El_faro.ficha.md`.
2. "revisa mi cuento" → N1 to N6. "aplica N1 y N4, sin humanize, lo paso al
   final" → `El_faro.rev1.md` and its change log.
3. "¿engancha desde el principio?" → A1 to A4. "aplica A2, sin humanize" →
   `El_faro.rev2.md`.
4. humanize on `El_faro.rev2.md`, with the style instruction → `El_faro.rev3.md`.
5. "corrige la ortografía" → `El_faro.final.md` and its report.
6. "adapta este relato a video, con las instrucciones del proyecto" →
   `El_faro.guion.md`.
7. "revisa la atención de mi guion", then "revisa el guion del episodio" →
   corrections applied.
8. "corrige la ortografía del guion" → the final script.
