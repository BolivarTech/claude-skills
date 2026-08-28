# Claude Skills — A Skill Collection for Claude Code

[![Claude Code](https://img.shields.io/badge/Claude%20Code-skills-blueviolet.svg)](https://docs.claude.com/en/docs/claude-code/skills)
[![Runtime](https://img.shields.io/badge/runtime-none-success.svg)](#requirements)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](#skills)
[![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](#license)

Skills for Claude Code, one directory each.

A skill is a markdown file that Claude reads when the work calls for it. It holds the
instructions you would otherwise retype every session, and it stays out of the context
window until something in the conversation matches its description. A long skill costs
nothing on the turns that never need it.

There is no build step and nothing to install alongside it. Copy a directory into
`~/.claude/skills/` and it works on the next session.

---

## Skills

| Skill | What it does |
|-------|--------------|
| [`humanize`](humanize/) | Rewrites prose so it reads as written by a person, and says why each thing it removes reads as machine-made |

---

## humanize

Generated prose has a signature, and little of it is subtle once you know where to look.
Some of it is vocabulary: delve, leverage, robust, seamless. Some of it is punctuation
nobody can actually type, the em-dash above all, which sits on no standard keyboard and
turns up constantly anyway. The rest is structure. Sentences that all land between twelve
and twenty words. Paragraphs that all open on the thesis and close on a tidy landing.
Claims hedged at one steady rate whether the writer knows the answer cold or is guessing.

The skill names each tell and, more usefully, says why it is one. Three parts carry most
of the weight.

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

**Trigger it** with `/humanize`, or just ask for text that sounds less like a machine
wrote it.

---

## Installation

```bash
git clone https://github.com/BolivarTech/claude-skills.git
cp -r claude-skills/humanize ~/.claude/skills/
```

Claude Code picks the skill up on the next session. To confirm it landed, type `/` and
look for it in the list.

Each skill directory also carries a `.skill` file. That is the same directory zipped, for
handing one skill to someone who does not want the whole repository.

---

## Repository layout

```
.
├── humanize/
│   ├── SKILL.md          the skill
│   └── humanize.skill    the same directory, packaged
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
| Claude Code | Yes | Skills load from `~/.claude/skills/` |
| Runtime dependencies | **None** | Plain markdown, no build step, nothing to compile |

---

## License

Dual licensed under [MIT](LICENSE) OR [Apache-2.0](LICENSE-APACHE), at your option.
