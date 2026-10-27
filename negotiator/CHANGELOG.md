# Changelog

All notable changes to the `negotiator` skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as defined in the
[repository README](../README.md#versioning).


## [1.0.0] - 2026-10-26

First release. The skill negotiates for the user, and its main job is to read
the other side's message and draft the reply to send. It can also prepare the
user before a negotiation or coach them through one.

### Added

- Three modes, in order of priority. Respond takes a counterpart's message, a
  proposal, or the user's own draft and returns a reply ready to send, with a
  few lines of notes. Prepare builds a compact sheet covering BATNA,
  reservation value, target, opening, the issue map, prepared concessions,
  and the tactics to expect. Mentor explains why a move was made; asked how a
  round went, or once a negotiation closes, it scores the round on ten
  dimensions so the user knows what to practice next.
- Questions before drafting. If a fact that would change the reply is
  missing (the user's limit, their alternative, a deadline, who decides), the
  skill asks for it in one message. It never asks for what it already knows.
  When a fact can't be had, it states the assumption and goes on.
- Tactic detection. Twenty pressure tactics are listed with their responses.
  In every message the skill names the tactic and decides whether to
  neutralize it, ignore it, name it openly, or use it.
- Bluff detection. Any claim the counterpart leans on is tested on its
  content, never on tone: consistency, verifiability, the cost of being
  called, and what is typical of the setting. The claim is classed as
  verified, partly true, unverifiable, or a likely bluff, and the reply tests
  it without accusing anyone. Once a bluff is exposed, that counterpart's
  later claims carry less weight.
- A case file per negotiation, at `.negotiator/<slug>.md` in the working
  directory. Facts, standing instructions, rounds, claims under test, and
  open items live there, so a new session picks up where the last one ended.
  The skill writes to it with each drafted reply, right away when the user
  corrects something or adds a fact, at the start of the next round to record
  what was actually sent, and when the user reports how it ended. The format
  is versioned (`negotiator-case: 1`) and the same everywhere. Without a file
  system, the negotiation lives in the chat: the skill reminds the user once
  per session that the file exists, produces it on request, and resumes from
  it when the user uploads or pastes it.
- An integrity rule. The skill may propose a bluff or a false statement in
  the notes, with its risk spelled out. It never puts one in the text to send
  without the user's explicit approval for that bluff in that round.
  Withholding information needs no approval.
- Diagnosis distilled from a review of negotiation research and practice:
  eight questions, a matrix that picks the approach from the situation, 22
  methods reduced to when to use each and its central move, techniques for
  questions, anchoring, concessions, value creation, impasses, closing, and
  renegotiation, and a table of 24 settings that runs from consumer purchases
  and job offers to public procurement and diplomacy.
- Open tone and tactics. The one fixed rule of style is brevity, and the user
  steers with corrections that stay in force for the rest of the
  negotiation.
- A humanize pass on every text to send, with figures, dates, conditions,
  names, commitments, and the exact wording of calibrated questions and
  conditional trades protected. "Sin humanize" turns the pass off.
- `codex/SKILL.md`, identical to the skill, packaged with
  `codex/agents/openai.yaml` as `codex/negotiator-codex.zip` for Codex and
  ChatGPT.
