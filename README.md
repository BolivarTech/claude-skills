# Claude Skills — A Skill Collection for Claude Desktop and Claude Code

[![Claude](https://img.shields.io/badge/Claude-skills-blueviolet.svg)](https://support.claude.com/en/articles/12512176-what-are-skills)
[![Runtime](https://img.shields.io/badge/runtime-none-success.svg)](#requirements)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](#skills)
[![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](#license)

Skills for Claude, one directory each. Claude Desktop and claude.ai install them from a
zip. Claude Code reads them straight off disk.

A skill is a markdown file that Claude reads when the work calls for it. It holds the
instructions you would otherwise retype every session, and it stays out of the context
window until something in the conversation matches its description. A long skill costs
nothing on the turns that never need it.

---

## Skills

| Skill | Version | What it does |
|-------|---------|--------------|
| [`humanize`](humanize/) | [2.0.0](humanize/CHANGELOG.md) | Rewrites prose so it reads as written by a person, and says why each thing it removes reads as machine-made |

---

## humanize

Generated prose has a signature, and little of it is subtle once you know where to look.
Some of it is vocabulary: delve, leverage, robust, seamless. Some of it is punctuation
nobody can actually type, the em-dash above all, which sits on no standard keyboard and
turns up constantly anyway. The rest is structure. Sentences that all land between twelve
and twenty words, paragraphs that all open on the thesis and close on a tidy landing.
And claims hedged at one steady rate, whether the writer knows the answer cold or is
guessing.

The skill names each tell and, more usefully, says why it is one.

**A fidelity boundary.** The pass is editorial, never semantic. Rhythm, word choice and
voice are fair game. A number, a date, a version, a flag or a path is not, and neither is
the strength of a claim, because a hedge and a guarantee say different things. Code
blocks, function signatures and error messages come out untouched. That boundary is what
makes the skill safe to run over a README or a changelog rather than only over a cover
letter.

**Tells with the reasoning attached.** Take the em-dash. It is not banned because some
list says so. It is banned because it appears on no standard keyboard, so a person
writing at speed reaches for a comma or a period, while the training corpus is thick with
copy-edited prose where an editor put them everywhere. Once you know that, you also know
the repair: rewrite the sentence. Swapping in an en-dash reads just as machine-made, and
it is the same tell in a cheaper costume.

**A stopping rule.** Push the levers to their limit and you get a second artificial
register, with a fragment in every paragraph and a contraction forced into every clause.
Aggressively informal AI is still AI. The skill says where to stop and how to tell you
have gone past it.

A real example, from the pass that produced part of this file:

> **Before.** In today's fast-paced world, understanding a large codebase is a
> significant challenge. Graphify is a comprehensive, robust solution that seamlessly
> transforms any repository into a queryable knowledge graph.
>
> **After.** Graphify turns a repository into a queryable knowledge graph you can ask
> questions of.

The blacklist is English. The levers are not, and a separate section covers what changes
in another language, with the Spanish tells worked out: *es importante destacar*, *cabe
mencionar*, the gerund that closes every other sentence, and the drift between tú and
usted that no English checklist would ever catch.

**Trigger it** with `/humanize` in Claude Code, by naming it in Claude Desktop, or by
just asking for text that sounds less like a machine wrote it.

---

## Installation

Every skill directory ships a `.zip` next to its `SKILL.md`. The archive holds the skill
folder at its root, which is the layout the Claude uploader expects, so it installs
without unpacking anything by hand.

### Claude Desktop and claude.ai

**1. Turn on code execution.** Skills will not run without it, and the Skills section
stays out of reach until it is on. On Free, Pro and Max it lives under **Settings >
Capabilities > Code execution and file creation**. On Team and Enterprise an owner has to
enable it in organization settings, along with Skills itself.

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

A skill is a directory on disk, so installing one is copying a folder. Where you put it
decides who gets it:

| Scope | Path | Available in |
|-------|------|--------------|
| Personal | `~/.claude/skills/<name>/SKILL.md` | every project on your machine |
| Project | `.claude/skills/<name>/SKILL.md` | that one repository, and it can be committed for the team |

**Personal install.** Clone and copy:

```bash
git clone https://github.com/BolivarTech/claude-skills.git
cp -r claude-skills/humanize ~/.claude/skills/
```

Or unpack the zip, which lands in the same place because the archive already carries the
folder:

```bash
unzip humanize.zip -d ~/.claude/skills/
```

On Windows without a `unzip` binary, PowerShell does it:

```powershell
Expand-Archive humanize.zip -DestinationPath "$env:USERPROFILE\.claude\skills"
```

**Project install.** Put it under the repository instead and commit it, and everyone who
clones gets the skill:

```bash
mkdir -p .claude/skills
cp -r /path/to/claude-skills/humanize .claude/skills/
git add .claude/skills/humanize
```

**Check it landed.** Run `/skills` for the list. Then invoke it with `/humanize`, or say
what you want and let Claude match your request against the skill's description.

Claude Code watches those directories, so a skill dropped into a `~/.claude/skills/` that
already existed shows up in the session you are in, no restart. The one case that needs a
restart is creating that top-level folder for the first time, because Claude Code was not
watching a directory that did not exist.

A personal skill and a project skill with the same name are not an error, the personal
one just wins. And uninstalling is deleting the directory.

---

## Repository layout

```
.
├── humanize/
│   ├── SKILL.md          the skill
│   ├── CHANGELOG.md      what changed, per version
│   └── humanize.zip      the same directory, zipped for upload to Claude
├── LICENSE               MIT
├── LICENSE-APACHE        Apache-2.0
└── README.md
```

One directory per skill, named after the skill. Nothing skill-specific sits at the root.

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

The description is the only part Claude reads on every turn, so it decides whether the
skill ever fires. Write it as a trigger, not as a summary: say what the skill does and
name the words a user would actually type when they want it. The body below the
frontmatter holds the instructions and loads only once the skill has fired, which is why
it can afford to be long.

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
for the one in this repository is `humanize-v1.0.0`, and each tag has a
[GitHub release](https://github.com/BolivarTech/claude-skills/releases) carrying the
notes and the zip for that version.

Semantic versioning, read for a document rather than for code:

| Bump | Means |
|------|-------|
| MAJOR | The skill produces materially different output on the same input, or guidance people relied on is gone |
| MINOR | New rules or sections, with everything that worked before still working |
| PATCH | Typos, wording, clarification. Behavior is unchanged |

**To see what you have installed**, open the `SKILL.md` and read the version out of its
frontmatter, or just ask Claude which version of the skill it is running:

```yaml
metadata:
  version: 1.0.0
```

The version travels inside the file, so a copy you uploaded to Claude Desktop months ago
still says what it is. Compare it against the
[releases page](https://github.com/BolivarTech/claude-skills/releases). Watch the
repository if you would rather be told than have to look.

Nothing updates itself. An installed skill is a copy, so a new version means uploading
the new zip or copying the folder again.

---

## License

Dual licensed under [MIT](LICENSE) OR [Apache-2.0](LICENSE-APACHE), at your option.
