# Changelog

All notable changes to the `attention-review` skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in the
[repository README](../README.md#versioning).


## [1.0.0] - 2026-09-22

First release. The skill reviews how a piece earns and holds its audience's
attention and says where people are likely to stop, why, and what to change.
It covers explainers, videos, podcasts, talks, classes, articles, threads,
posts, and stories, and it never claims to predict views or reach.

### Added

- Seven stages checked in the order the audience needs them: recognition,
  gap, promise, proof, progress, payoff, and transmission, each with its
  checks and typical failures, plus an expository and a narrative reading of
  every stage. The insight test ("I used to think ___. Now I understand ___,
  because ___") separates information from a payoff.
- Boundaries with the neighboring skills. In a story, only the attention
  layer is reviewed; plot, character, and the fairness of a twist go to
  "Outside this review" and to narrative-review. In a production script, the
  review judges what the audience hears and sees, reads the words inside
  markup such as SSML, and leaves shots, sound, and continuity to
  video-script. Hybrid pieces use each reading where it applies. Continuity
  of events in a story also goes to narrative-review, and questions a chapter
  leaves open on purpose for later installments count as transmission when
  the chapter answers its own central question.
- Paratext read the same way in any piece, prose included: labels, ratings,
  and framing notes are packaging and part of the promise, a teaser for the
  next installment is transmission, and credits and production lines are
  ignored. Author's notes appended to a piece are not reviewed but read as
  stated intent. Text that works against that intent becomes a finding rated
  as if the intent holds, with both directions offered and the verdict
  stated both ways.
- A reading for humor: recognition, expectation, turn, punchline, and social
  identification, with its own checks and common failures.
- Feed checks that apply only to short vertical video: first frame and
  opening text, sound-off readability, safe zones, early proof, a payoff with
  margin before the end, the loop, duration, one call to action, and
  watermarked reposts. Platform limits carry the date they were verified.
- Performance data used when supplied, from analytics and retention curves
  to comments and reader reactions, with each symptom mapped to the stage
  most likely to explain it. Without data the review runs in full and ends
  with one line on which data would help.
- Ethical limits reported as findings: unpaid suspense, exaggerated data,
  irrelevant credentials, manufactured urgency, fear, or anger, unsourced
  medical, legal, financial, or security advice, and fiction framed as true
  that hands the audience claims it could act on.
- Findings verified before they are reported, each with a real location, a
  type (supported problem, interpretive risk, or editorial preference) decided
  by the evidence for the defect rather than by its effect, a
  priority, and a confidence level kept separate from the priority. The
  central question is the one the opening raises and the piece commits to
  answer, and it decides what counts as the main payoff.
- A report in the user's language with verdict and scope, strengths to
  preserve, a status table by stage, prioritized findings, a revision plan
  ordered by dependency, and what falls outside the review. A numeric score
  appears only on request or when two versions of the same piece are
  compared, always broken down by criterion.
- Corrections applied only on request and only to the chosen findings, with
  the rest of the piece byte for byte, including markup and cues, and no
  invented proof.
- `codex/SKILL.md`, identical to the skill, packaged with
  `codex/agents/openai.yaml` as `codex/attention-review-codex.zip` for Codex
  and ChatGPT.
