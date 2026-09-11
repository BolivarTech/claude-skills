# Claude Skills — A Skill Collection for Claude Desktop and Claude Code

[![Claude](https://img.shields.io/badge/Claude-skills-blueviolet.svg)](https://support.claude.com/en/articles/12512176-what-are-skills)
[![Runtime](https://img.shields.io/badge/runtime-none-success.svg)](#requirements)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](#skills)
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
| [`humanize`](humanize/) | [3.0.0](humanize/CHANGELOG.md) | Rewrites existing prose for a natural voice while preserving meaning and limiting unnecessary changes |

---

## humanize

Humanize edits existing drafts to improve naturalness, clarity, and rhythm while
preserving the writer's voice. It does not draft from notes or add new content.

**Review every draft.** The skill checks meaning, voice, structure, rhythm,
filler, repetition, and vocabulary. It returns a draft unchanged only after a
complete review finds no justified improvements.

**Edit in context.** Familiar words, parallel constructions, and punctuation are
signals to inspect, not automatic defects. Appropriate typography, formal
language, and useful technical vocabulary stay.

**Preserve meaning and its force.** Facts, attribution, uncertainty, emphasis,
direct quotations, and protected technical material remain intact. A vague claim
is not disposable filler, and removing a phrase such as "sin duda alguna" can
change the writer's certainty even when the underlying information stays.

**Keep the edit concise.** Rhythm changes use existing material. The result stays
the same length or shorter, with minimal growth allowed only to avoid ambiguity
or preserve meaning. Optional improvements do not generate approval questions;
the default deliverable is the edited text without an explanation of each change.

For example:

> **Before.** Many experts believe this approach may potentially improve retention.
>
> **After.** Many experts believe this approach may improve retention.

The attribution and uncertainty remain. The skill also includes Spanish guidance
for filler, repeated connectives, register shifts, and translated sentence patterns.

**Trigger it** with `/humanize` in Claude Code, by naming it in Claude Desktop, or by
just asking for text that sounds less like a machine wrote it.

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
│   └── humanize.zip      contains humanize/SKILL.md for upload to Claude
├── scripts/
│   ├── validate_skills.py       release gate, run before every tag
│   └── test_validate_skills.py  validator regression tests
├── LICENSE               MIT
├── LICENSE-APACHE        Apache-2.0
└── README.md
```

One directory per skill, named after the skill. Nothing skill-specific sits at the root.

`scripts/validate_skills.py` checks that the source and ZIP are byte-identical.
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
for the current version is `humanize-v3.0.0`. Creating a tag and publishing a
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
  version: 3.0.0
```

The file retains its version even after months in Claude Desktop. Compare it with the
[releases page](https://github.com/BolivarTech/claude-skills/releases). Watch the
repository if you would rather be told than have to look.

Installed skills do not update automatically. Upload the new ZIP or copy the
folder again to update.

---

## License

Dual licensed under [MIT](LICENSE) OR [Apache-2.0](LICENSE-APACHE), at your option.
