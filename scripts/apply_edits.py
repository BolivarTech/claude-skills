#!/usr/bin/env python3
"""Apply a batch of exact-string edits to a file, or apply none of them.

Written after a batch of hand-typed replacements aborted midway three times.
Each abort discarded the replacements that had already succeeded, because the
write happened at the end, and one of the losses was reported as applied. The
failure was deterministic every time: a string that does not match the file
will never match on a retry, so retrying was pure waste.

The fix is order. Every edit is checked against the file **before** any of them
is applied, so a bad edit costs a message instead of a lost batch, and every
edit is confirmed present afterwards, so "applied" is a fact rather than an
assumption.

Usage::

    from apply_edits import apply_edits
    apply_edits("humanize/SKILL.md", [
        ("old text", "new text", "what this fixes"),
    ])

Raises:
    EditError: a preflight or verification check failed. The file is untouched
        on a preflight failure.
"""

from __future__ import annotations

import pathlib
from typing import Iterable, Sequence

#: An edit is (old, new, label). The label names what the edit is for and is
#: what gets reported, so it should read as a claim you would defend.
Edit = tuple[str, str, str]


class EditError(RuntimeError):
    """A batch was rejected. Nothing was written unless the message says so."""


def apply_edits(path: str | pathlib.Path, edits: Sequence[Edit]) -> None:
    """Apply every edit, or none.

    Args:
        path: File to edit.
        edits: The batch. Each old string must appear exactly once.

    Raises:
        EditError: An old string is missing or ambiguous (nothing written), or
            a new string is absent after writing (file written, batch suspect).

    Example:
        >>> apply_edits("a.md", [("foo", "bar", "rename foo")])
    """
    p = pathlib.Path(path)
    text = p.read_text(encoding="utf-8")

    problems = []
    for old, _new, label in edits:
        n = text.count(old)
        if n != 1:
            problems.append(f"  {label}: found {n} times, need exactly 1")
    if problems:
        raise EditError(
            f"preflight failed for {len(problems)} of {len(edits)} edits, "
            f"nothing written:\n" + "\n".join(problems)
        )

    for old, new, _label in edits:
        text = text.replace(old, new, 1)
    p.write_text(text, encoding="utf-8")

    after = p.read_text(encoding="utf-8")
    missing = [label for _o, new, label in edits if new not in after]
    if missing:
        raise EditError(
            "file was written but these edits are not present: " + ", ".join(missing)
        )

    for _o, _n, label in edits:
        print(f"  applied  {label}")
    print(f"{len(edits)} edits applied and verified in {p}")


def require(path: str | pathlib.Path, markers: Iterable[tuple[str, str]]) -> int:
    """Report which expected markers are present in a file.

    Args:
        path: File to audit.
        markers: (needle, description) pairs that should each appear.

    Returns:
        Count of missing markers. Zero means the file carries them all.
    """
    text = pathlib.Path(path).read_text(encoding="utf-8")
    missing = 0
    for needle, desc in markers:
        ok = needle in text
        print(f"  {'OK     ' if ok else 'MISSING'}  {desc}")
        missing += not ok
    return missing
