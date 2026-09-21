# Claude Skills — A Skill Collection for Claude Desktop and Claude Code

[![Claude](https://img.shields.io/badge/Claude-skills-blueviolet.svg)](https://support.claude.com/en/articles/12512176-what-are-skills)
[![Runtime](https://img.shields.io/badge/runtime-none-success.svg)](#requirements)
[![Skills](https://img.shields.io/badge/skills-6-blue.svg)](#skills)
[![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](#license)

Each directory contains a Claude skill. Claude Desktop and claude.ai install skills
from a ZIP; Claude Code reads them directly from disk.

A skill is a Markdown file containing instructions you would otherwise repeat each
session. Claude loads it when the conversation matches its description. Until then,
the body stays outside the context window, so its length adds no cost to those turns.

---

## Skills

| Skill | Version | What it does |
|-------|---------|--------------|
| [`humanize`](humanize/) | [4.2.2](humanize/CHANGELOG.md) | Rewrites existing prose for a natural voice while preserving meaning and limiting unnecessary changes |
| [`narrative-review`](narrative-review/) | [1.0.0](narrative-review/CHANGELOG.md) | Diagnoses a story's promises, structure, characters, twists, and weak devices, with evidence and the smallest fix for each |
| [`video-script`](video-script/) | [1.0.1](video-script/CHANGELOG.md) | Turns a narration into a production-ready audiovisual script, or reviews a script or cut plan for narrative, image, sound, pacing, and production defects |
| [`short-clip`](short-clip/) | [1.0.0](short-clip/CHANGELOG.md) | Turns an idea, meme, or image into a ten-second vertical clip: the prompt for the reference image and the prompt that animates it, with post copy when a platform is named |
| [`story-writer`](story-writer/) | [1.0.0](story-writer/CHANGELOG.md) | Writes a literary story from one idea or a full dossier, reviews it, applies the verified corrections, and delivers it with the decisions that shaped it |
| [`premortem`](premortem/) | [1.0.0](premortem/CHANGELOG.md) | Places a plan in a future where it already failed, reconstructs and prioritizes the causes, and delivers a report with treatments, early signals, and the risks of not acting; or the kit to run the session with a team |

---

## humanize

Humanize edits existing drafts to improve naturalness, clarity, and rhythm while
preserving the writer's voice. It does not draft from notes or add new content.

**Review every draft.** The skill checks meaning, voice, structure, rhythm,
filler, repetition, and vocabulary. It returns a draft unchanged only after a
complete review finds no justified improvements.

**Fix what it finds.** Formulaic vocabulary, "not just X but Y" constructions,
em dashes, curly quotes, and ellipses get corrected when they turn up in editable
prose. Numeric ranges, dialogue dashes, protected technical material, and direct
quotations are left as they are.

**Preserve meaning and its force.** Facts, attribution, uncertainty, emphasis,
direct quotations, and protected technical material remain intact. A vague claim
is not disposable filler, and removing a phrase such as "sin duda alguna" can
change the writer's certainty even when the underlying information stays.

**Keep the edit concise.** Rhythm changes use existing material. The result stays
the same length or shorter, with minimal growth allowed only to avoid ambiguity,
preserve meaning, or state a supplied fact precisely. Optional improvements do not generate approval questions;
the default deliverable is the edited text without an explanation of each change.

For example:

> **Before.** Many experts believe this approach may potentially improve retention.
>
> **After.** Many experts believe this approach may improve retention.

The attribution and uncertainty remain. The skill also includes Spanish guidance
for filler, repeated connectives, register shifts, and translated sentence patterns.

**Trigger it** with `/humanize` in Claude Code, by naming it in Claude Desktop, or by
just asking for text that sounds less like a machine wrote it.

**A ChatGPT package** lives in [`humanize/chatgpt/`](humanize/chatgpt/): the same
skill, same text, same name and version. The release gate fails if the two files
ever differ.

---

## narrative-review

Narrative Review reads a short story, novel, screenplay, synopsis, scene, or
interactive route and reports how well it delivers what it promises. It diagnoses,
and on request it applies the corrections it found; it does not copyedit.

**Judges the story on its own terms.** The expectations come from the author's
stated intent, from what the opening and tone promise, and from the conventions
of the genre. No template is imposed: a contemplative story is not marked down
for lacking a confrontation, and a tragedy is not a flaw because it ends badly.
A lens table picks the structural model that clarifies the work, from three acts
to kishōtenketsu to branching routes.

**Verifies before it labels.** Each finding is located in the text, with chapter,
scene, or a short quotation. It is then checked against an alternative explanation
such as an unreliable narrator, an ellipsis, or a clue planted earlier. A table of
twenty-four devices, from deus ex machina to head hopping, states what makes
each one a problem and what to rule out first. Priority is kept separate from
confidence, and a story may pass with no corrections.

**Reports what to fix and in what order.** The report opens with a verdict and
the strengths to preserve. Findings follow by priority, each with evidence,
mechanism, and the smallest intervention that addresses the cause. A revision
plan closes it, ordered by dependency: architecture first, then characters and
information, then scenes and language.

**Applies fixes without rewriting the author.** Ask for it and pick the findings.
The skill edits only the passages those findings cite, matches the voice of the
lines around each insertion, and returns the full text with a change log per
finding. It then reviews the new version to confirm what was resolved and that
the strengths it flagged are still there. When `humanize` is installed, the
inserted lines pass through it with the rest of the story protected.

**Trigger it** with `/narrative-review` in Claude Code, by naming it in Claude
Desktop, or by asking for a story critique, a beta read, or "revisa mi cuento".

**A ChatGPT package** lives in [`narrative-review/chatgpt/`](narrative-review/chatgpt/),
identical to the skill, as with `humanize`.

---

## video-script

Video Script takes a narration, short story, treatment, or research dossier and
turns it into a script that can be recorded, visualized, edited, and checked.
Pointed at an existing script, shot list, storyboard, or cut plan, it reviews the
work against the same standard and, on request, applies the corrections it found.

**Adapts the experience, not the sentences.** The method starts with an
extraction reading and a one-sentence statement of what the audience should feel
and question, then a thesis, a motor, a point of view, and a sequence map in which
every sequence changes something. Interiority becomes behavior, image, sound, or
a voiceover that adds rather than describes. Every change to canon is recorded.

**Audio first, timing honest.** Existing audio fixes duration; nothing else does.
Without it, spoken material is estimated at a stated rate, labeled as an estimate,
and given a margin. No shot or asset gets a duration before the audio question is
settled.

**Reviews what it can read.** The skill works from text and still images and says
so: a cut is reviewed through a transcript, a timeline export, frames, or the
user's viewing notes, and a pass with no evidence in the material is reported as
not assessable. Seven passes run in order, from continuous experience to
accessibility, and a stage table states what a treatment, a script, or an animatic
allows to judge. Twenty-one frequent artifacts each come with a diagnostic test and
a correction target.

**Delivers a production master script.** The output is one document that works as
performance script and production dossier: production metadata, record-ready
spoken material per scene, music design, a scene-by-scene audio and visual plan,
consolidated requirements, and canon verification. A project's own production
instructions govern the naming scheme, segment limits, caption rules, and delivery
specifications; without them the skill's defaults apply and are labeled as
proposals. The full template is in the skill.

**Trigger it** with `/video-script` in Claude Code, by naming it in Claude
Desktop, or by asking to adapt a story for video, write a production script, or
"revisa el guion del episodio".

**A ChatGPT package** lives in [`video-script/chatgpt/`](video-script/chatgpt/),
identical to the skill, as with `humanize`.

---

## short-clip

Short Clip takes an idea, a meme, a phrase, an anecdote, or a reference image and
turns it into a vertical clip of about ten seconds for TikTok, Instagram Reels, or
YouTube Shorts. What comes back is what the generation tools consume: a prompt
for the reference image and a prompt that animates it with its dialogue and
sound. Post copy is added when a platform is named.

**Something has to happen.** The first question is whether the material is a
phrase or a story. A phrase is a feeling with a caption: it produces recognition
and nothing to wait for. A story has a character, an interaction, a change, and a
consequence. A phrase gets converted before anything is written, or reported as
better served by a still. Setup and turn must fit in one sentence; if they need
two, the clip needs more seconds than it has.

**Picks the structure by the effect.** An anecdote, a perspective-shift joke, a
visual gag, an everyday problem, a pursuit, a scare, or a reflection each gets its
own architecture and a control question. When later information can turn an
ordinary situation into something absurd or unsettling, the frame shift is the
default: it holds the strongest change ten seconds can carry.

**Designs the turn to survive a rewatch.** It separates the first reading from
the hidden truth, the facts compatible with both, and the visible consequence.
The hook is a promise the ending pays. The clip ends after the strongest reaction
and leaves something for the viewer to complete, which is also what gives the
comments a reason to exist.

**Writes prompts the tools can hold.** The image prompt fixes an invariant list
(identity, hands, objects, wardrobe, text, environment) and the animation prompt
repeats it. One central relationship, legible on a phone in a glance. Every
segment of the animation changes something the viewer sees; a camera drift over
a still frame does not count. Voice and image never say the same thing.

**Trigger it** with `/short-clip` in Claude Code, by naming it in Claude Desktop,
or by asking for a reel, a short, or "anima esta imagen".

**A ChatGPT package** lives in [`short-clip/chatgpt/`](short-clip/chatgpt/),
identical to the skill, as with `humanize`.

---

## story-writer

Story Writer takes one idea, or a dossier with characters, world, and ending
already decided, and writes the story. What the user supplies is canon and enters
the text without being contradicted; what the user leaves open is decided and
declared. The story comes back in Markdown, in the user's language, followed by
a short sheet of the decisions behind it.

**Builds before it writes.** Ten steps in order: promise, engine, five
milestones, a compatible model, cause-and-effect chains, a private table of who
knows what, scenes with change, rhythm, an ending audit, and breaking the
template only for a reason. A model table by main need, with a control question
per row, keeps a contemplative story from getting a confrontation forced on it.

**Dialogue to a professional standard.** Distinct voices, subtext, conflict in
every exchange, verbal economy, rhythm. Lines are anchored in physical action,
`dijo` is the base tag, and nobody explains what both already know. Spanish
dialogue uses the em dash with its tag cases spelled out; that dash is dialogue
punctuation, and `humanize` leaves it alone.

**Reviews itself, and verifies the reviewer.** A self-audit runs first. Then
`narrative-review` reads the story and each finding is checked against the text:
the real ones are corrected with the smallest change; the false positives are
rejected with a reason. Nothing is changed to please the reviewer. `humanize`
runs last, with the dialogue protected.

**Length follows the premise.** Two to ten thousand words by default, no hard
ceiling; longer when asked, and parts proposed only when the causal chain needs
more than one delivery.

**Trigger it** with `/story-writer` in Claude Code, by naming it in Claude
Desktop, or by asking for a story from an idea or saying "escribe un cuento sobre".

**A ChatGPT package** lives in [`story-writer/chatgpt/`](story-writer/chatgpt/),
identical to the skill, as with `humanize`.

---

## premortem

Premortem takes a plan that exists and can still change, puts it in a future
where it has already failed, and works backwards: what happened, which of it
matters, and what the plan does about it now. The object can be a launch, a
migration, an investment, a policy, a clinical program, a hire, or a career
move; the procedure is the same. What comes back is a complete report, or,
when there is a team, the kit to run the session and then the report built from
the team's notes.

**Analyzes with a fixed sequence.** A plan sheet with its assumptions and the
base rates the plan needs. A failure scenario in the past tense with no cause
built in. Cause generation with outsider prompts before any category sweep, then
risks written as cause, event, and impact, and a six-criterion prioritization
that orders without pretending to measure. Every treatment passes one test:
what, who, when, how it is verified, and what happens if it is not done. "Be
careful" and "coordinate better" do not make it into the report.

**Asks about not acting too.** The second barrel runs the mirror scenario, in
which the plan was shelved or diluted and the outcome was also bad, so that a
long list of failure modes does not reward caution by default.

**Keeps the user's causes first.** Causes the user or the team already wrote
enter unchanged and ahead of the skill's own, which are labeled. Whoever speaks
first sets the limits of what everyone else thinks of, so in facilitation mode
the skill produces no causes until the team's notes arrive.

**Universal, with probes per field.** Software gets the longest list (adoption,
technical debt, data quality, cutover and rollback, go/no-go, observability),
and engineering, strategy, public policy, health, and personal decisions each
get their own. Probes run after free generation, never instead of it, and a
plan from a field not listed runs the method unchanged. Where the plan needs
FMEA, HAZOP, threat modeling, or a clinical or security review, the report
names the handoff; the premortem produces hypotheses, not verified controls.

**Trigger it** with `/premortem` in Claude Code, by naming it in Claude
Desktop, or by asking what could make a plan fail or saying "haz un premortem
de este plan".

**A ChatGPT package** lives in [`premortem/chatgpt/`](premortem/chatgpt/),
identical to the skill, as with `humanize`.

---

## Installation

Each skill directory includes a `.zip` beside its `SKILL.md`. The archive contains
the skill folder at its root, as the Claude uploader expects. Upload it without
unpacking it.

### Claude Desktop and claude.ai

**1. Turn on code execution.** It is required to access the Skills section and run
skills. On Free, Pro and Max, use **Settings >
Capabilities > Code execution and file creation**. On Team and Enterprise, an owner
must enable both code execution and Skills in organization settings.

**2. Download the package.** Grab
[`humanize/humanize.zip`](https://github.com/BolivarTech/claude-skills/raw/main/humanize/humanize.zip)
from this repository. Do not unzip it.

**3. Upload it.** Open **[Customize > Skills](https://claude.ai/customize/skills)**, click
**Add**, and pick the file. The uploader takes `.zip` only.

**4. Toggle it on** in that same list.

Claude decides when to reach for it, or you say so outright: *"use the humanize skill on
this draft."*

Skills are available on Free, Pro, Max, Team and Enterprise. Anything you upload stays
private to your own account.

### ChatGPT

Upload
[`humanize/chatgpt/humanize-chatgpt.zip`](https://github.com/BolivarTech/claude-skills/raw/main/humanize/chatgpt/humanize-chatgpt.zip)
to ChatGPT. The archive holds the same `humanize/SKILL.md` layout and the same
text as the Claude package.

### Claude Code CLI

To install a skill, copy its folder to the location for your intended scope:

| Scope | Path | Available in |
|-------|------|--------------|
| Personal | `~/.claude/skills/<name>/SKILL.md` | every project on your machine |
| Project | `.claude/skills/<name>/SKILL.md` | that one repository, and it can be committed for the team |

**Personal install.** Clone and copy:

```bash
git clone https://github.com/BolivarTech/claude-skills.git
cp -r claude-skills/humanize ~/.claude/skills/
```

Or unpack the ZIP into the same location; it already contains the skill folder:

```bash
unzip humanize.zip -d ~/.claude/skills/
```

On Windows without a `unzip` binary, PowerShell does it:

```powershell
Expand-Archive humanize.zip -DestinationPath "$env:USERPROFILE\.claude\skills"
```

**Project install.** Copy the folder into the repository and commit it so everyone
who clones the project gets the skill:

```bash
mkdir -p .claude/skills
cp -r /path/to/claude-skills/humanize .claude/skills/
git add .claude/skills/humanize
```

**Check the installation.** Run `/skills` to list available skills. Invoke this one
with `/humanize`, or let Claude match your request to its description.

Claude Code watches these directories. Adding a skill to an existing
`~/.claude/skills/` makes it available in the current session without a restart.
Restart when creating that top-level folder for the first time: Claude Code was
not watching it before it existed.

Personal and project skills can share a name; the personal one takes precedence.
To uninstall a skill, delete its directory.

---

## Repository layout

```
.
├── humanize/
│   ├── SKILL.md          the skill
│   ├── CHANGELOG.md      what changed, per version
│   ├── humanize.zip      contains humanize/SKILL.md for upload to Claude
│   └── chatgpt/
│       ├── SKILL.md              the same skill, for ChatGPT
│       └── humanize-chatgpt.zip  the same layout, for upload to ChatGPT
├── narrative-review/
│   ├── SKILL.md
│   ├── CHANGELOG.md
│   ├── narrative-review.zip
│   └── chatgpt/
│       ├── SKILL.md
│       └── narrative-review-chatgpt.zip
├── video-script/
│   ├── SKILL.md
│   ├── CHANGELOG.md
│   ├── video-script.zip
│   └── chatgpt/
│       ├── SKILL.md
│       └── video-script-chatgpt.zip
├── short-clip/
│   ├── SKILL.md
│   ├── CHANGELOG.md
│   ├── short-clip.zip
│   └── chatgpt/
│       ├── SKILL.md
│       └── short-clip-chatgpt.zip
├── story-writer/
│   ├── SKILL.md
│   ├── CHANGELOG.md
│   ├── story-writer.zip
│   └── chatgpt/
│       ├── SKILL.md
│       └── story-writer-chatgpt.zip
├── premortem/
│   ├── SKILL.md
│   ├── CHANGELOG.md
│   ├── premortem.zip
│   └── chatgpt/
│       ├── SKILL.md
│       └── premortem-chatgpt.zip
├── scripts/
│   ├── validate_skills.py       release gate, run before every tag
│   ├── test_validate_skills.py  validator regression tests
│   ├── prose_metrics.py         shape metrics of a text before and after an edit
│   └── test_prose_metrics.py    metrics tests
├── LICENSE               MIT
├── LICENSE-APACHE        Apache-2.0
└── README.md
```

One directory per skill, named after the skill. Nothing skill-specific sits at the root.

`scripts/validate_skills.py` checks that the source and ZIP are byte-identical,
for the skill and for any variant nested under it, and that a variant carries the
skill's text unchanged.
It also checks the six allowed frontmatter keys, non-empty names and descriptions,
the archive's root folder, and version agreement between the frontmatter, README
table, and changelog. Run `python scripts/validate_skills.py --check-installed`
to also compare personal copies under `~/.claude/skills/` with the source.

Each check reports `PASS`, `FAIL`, `CANNOT_TEST` or `OUT_OF_SCOPE`, distinguishing
unavailable checks from successful ones. Whether the description triggers the
skill remains `OUT_OF_SCOPE`; that requires a live session.

Run validator regression tests with `python -m unittest discover -s scripts`.
The maintenance scripts require Python and PyYAML; the skill itself has no runtime
dependencies.

---

## Adding a skill

Create `./<name>/SKILL.md` with YAML frontmatter carrying `name` and `description`:

```yaml
---
name: my-skill
description: >-
  What the skill does, and the phrases that should trigger it.
---
```

Claude reads the description on every turn to decide whether to load the skill.
Describe what it does and the words users would use to request it. The instructions
below the frontmatter load only when the skill is selected, so a longer body does
not add context to unrelated turns.

Run `python scripts/validate_skills.py`. It discovers every `<name>/SKILL.md` in
the repository automatically. A release requires an exit code of zero.

---

## Requirements

| Component | Required | Notes |
|-----------|----------|-------|
| Claude Desktop or claude.ai | Either one | Needs code execution enabled; upload the `.zip` under Customize > Skills |
| Claude Code CLI | Either one | Skills load from `~/.claude/skills/` or a project's `.claude/skills/` |
| Runtime dependencies | **None** | Plain markdown, no build step, nothing to compile |

---

## Versioning

Skills here version independently, so a release names the skill it belongs to. The tag
for the current version is `humanize-v4.2.2`. Creating a tag and publishing a
[GitHub release](https://github.com/BolivarTech/claude-skills/releases) are separate
steps from updating the source and ZIP in this repository.

Semantic versioning, read for a document rather than for code:

| Bump | Means |
|------|-------|
| MAJOR | The skill produces materially different output on the same input, or guidance people relied on is gone |
| MINOR | New rules or sections, with everything that worked before still working |
| PATCH | Typos, wording, clarification. Behavior is unchanged |

**To check your installed version**, read the frontmatter in `SKILL.md` or ask
Claude which version it is running:

```yaml
metadata:
  version: 4.2.2
```

The file retains its version even after months in Claude Desktop. Compare it with the
[releases page](https://github.com/BolivarTech/claude-skills/releases). Watch the
repository if you would rather be told than have to look.

Installed skills do not update automatically. Upload the new ZIP or copy the
folder again to update.

---

## License

Dual licensed under [MIT](LICENSE) OR [Apache-2.0](LICENSE-APACHE), at your option.
