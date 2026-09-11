#!/usr/bin/env python3
"""Deterministic shape metrics for a prose sample, before and after an edit.

The 30-row key measures whether each rule fired. It does not measure the
overall shape of the text: whether sentences got longer, whether the short
ones vanished, whether a phrase repeats. Those are cheap to compute exactly
and identical on every run, so they belong in a script, not in a judgement.

Metrics per text:
    words, sentences, mean / median / stdev / min / max sentence length,
    sentences of 3-8 words, under 3, over 30, function-word ratio, repeated
    3-grams (types, occurrences, the most frequent).

The function-word list covers Spanish and English so a mixed sample is not
undercounted. Sentence splitting is a heuristic: a terminator followed by
whitespace and a capital, an opening mark or a dash. Decimals ("3.000") and
abbreviations before a digit ("p. 471") do not split.

Complexity is O(n) in the number of words for every metric.

Usage::

    python scripts/prose_metrics.py source.txt            # one text
    python scripts/prose_metrics.py source.txt edited.txt # both, with deltas
"""

from __future__ import annotations

import re
import statistics
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

SHORT_MIN, SHORT_MAX = 3, 8
LONG_MIN = 31
TOP_TRIGRAMS = 5

FUNCTION_WORDS = frozenset("""
de la el en y a los las del que un una por con se su sus al lo como para es son o
no más pero ya sin sobre este esta esto ese esa eso estos estas esos esas entre
cuando muy hasta desde también ni si le les me mi nos sí ha han era fue está están
ser hay todo toda todos todas cada otro otra otros otras tan tanto así e u aunque
porque donde quien quienes cual cuales mismo misma uno hacia ante bajo tras durante
mediante según contra cuyo cuya cuyos cuyas aquí allí ahora después antes entonces
mientras algo alguno alguna algunos algunas nada nadie ninguno ninguna usted él
ella ellos ellas nosotros yo tú te qué cómo cuál puede pueden podría podrían debe
deben sea sean había hubo nuestro nuestra nuestros nuestras propio propia además
luego pues aun aún mucho mucha muchos muchas poco poca pocos pocas menos casi solo
sólo bien mal siempre nunca jamás
the a an and or but of to in on at by for with from as is are was were be been
being it its this that these those he she they them his her their we our you your
i my me not no so if than then there here which who whom whose what when where
while into over under again further once all any both each few more most other
some such only own same too very can will just should would could may might must
do does did have has had
""".split())

_WORD = re.compile(r"[a-záéíóúñüA-ZÁÉÍÓÚÑÜ]+")
# A dash opens a sentence only when an opening mark or a capital follows it;
# "? — preguntó" is the closing dash of a dialogue line, not a new sentence.
_OPENER = r"[\"“¿¡A-ZÁÉÍÓÚÑ]"
_SPLIT = re.compile(rf"(?<=[.!?…])\s+(?={_OPENER}|—\s?{_OPENER})")


def split_sentences(text: str) -> list[str]:
    """Split prose into sentences by terminator + space + opening character.

    Args:
        text: Running prose. Line breaks are treated as spaces.

    Returns:
        Non-empty sentence strings in order.
    """
    flat = re.sub(r"\s+", " ", text).strip()
    if not flat:
        return []
    return [part.strip() for part in _SPLIT.split(flat) if part.strip()]


def words_of(text: str) -> list[str]:
    """Lower-cased alphabetic tokens of the text, accents included."""
    return [w.lower() for w in _WORD.findall(text)]


@dataclass(frozen=True)
class ProseMetrics:
    """Shape metrics of one prose sample.

    Build with :meth:`measure`; every field is derived from the text once.
    """

    words: int
    sentences: int
    mean_len: float
    median_len: float
    stdev_len: float
    min_len: int
    max_len: int
    short: int
    very_short: int
    long: int
    function_ratio: float
    trigram_types: int
    trigram_occurrences: int
    top_trigrams: tuple[tuple[str, int], ...]

    @classmethod
    def measure(cls, text: str) -> "ProseMetrics":
        """Compute every metric for ``text``.

        Args:
            text: The prose to measure. Markdown tables and headings are
                counted as they are; strip them first if they should not be.

        Returns:
            A populated :class:`ProseMetrics`.

        Raises:
            ValueError: if the text contains no words.
        """
        tokens = words_of(text)
        if not tokens:
            raise ValueError("text contains no words")
        lengths = [n for n in (len(words_of(s)) for s in split_sentences(text)) if n > 0]
        trigrams = Counter(zip(tokens, tokens[1:], tokens[2:]))
        repeated = {k: v for k, v in trigrams.items() if v > 1}
        top = sorted(repeated.items(), key=lambda kv: (-kv[1], kv[0]))[:TOP_TRIGRAMS]
        return cls(
            words=len(tokens),
            sentences=len(lengths),
            mean_len=float(statistics.mean(lengths)),
            median_len=float(statistics.median(lengths)),
            stdev_len=statistics.pstdev(lengths) if len(lengths) > 1 else 0.0,
            min_len=min(lengths),
            max_len=max(lengths),
            short=sum(SHORT_MIN <= n <= SHORT_MAX for n in lengths),
            very_short=sum(n < SHORT_MIN for n in lengths),
            long=sum(n >= LONG_MIN for n in lengths),
            function_ratio=sum(t in FUNCTION_WORDS for t in tokens) / len(tokens),
            trigram_types=len(repeated),
            trigram_occurrences=sum(repeated.values()),
            top_trigrams=tuple((" ".join(k), v) for k, v in top),
        )

    def rows(self) -> list[tuple[str, str]]:
        """Label / value pairs for a report, in display order."""
        return [
            ("words", f"{self.words}"),
            ("sentences", f"{self.sentences}"),
            ("mean length", f"{self.mean_len:.1f}"),
            ("median length", f"{self.median_len:.0f}"),
            ("stdev length", f"{self.stdev_len:.1f}"),
            ("min / max", f"{self.min_len} / {self.max_len}"),
            (f"{SHORT_MIN}-{SHORT_MAX} words", f"{self.short}"),
            (f"< {SHORT_MIN} words", f"{self.very_short}"),
            (f">= {LONG_MIN} words", f"{self.long}"),
            ("function words", f"{100 * self.function_ratio:.1f}%"),
            ("repeated 3-grams", f"{self.trigram_types} types / {self.trigram_occurrences} hits"),
        ]


class Report:
    """Render one or two :class:`ProseMetrics` as an aligned text table."""

    def __init__(self, before: ProseMetrics, after: ProseMetrics | None = None):
        self.before = before
        self.after = after

    def render(self) -> str:
        """Return the table; with two samples, a third column shows the delta."""
        left = self.before.rows()
        lines = []
        if self.after is None:
            width = max(len(k) for k, _ in left)
            lines += [f"{k:<{width}}  {v}" for k, v in left]
            lines.append(self._top("top 3-grams", self.before))
            return "\n".join(lines)
        right = self.after.rows()
        width = max(len(k) for k, _ in left)
        w_left = max(len(v) for _, v in left)
        w_right = max(len(v) for _, v in right)
        lines.append(f"{'':<{width}}  {'before':<{w_left}}  {'after':<{w_right}}  delta")
        for (k, a), (_, b) in zip(left, right):
            lines.append(f"{k:<{width}}  {a:<{w_left}}  {b:<{w_right}}  {self._delta(k)}")
        lines.append(self._top("top 3-grams before", self.before))
        lines.append(self._top("top 3-grams after", self.after))
        return "\n".join(lines)

    _NUMERIC = {
        "words": "words", "sentences": "sentences", "mean length": "mean_len",
        "median length": "median_len", "stdev length": "stdev_len",
        f"{SHORT_MIN}-{SHORT_MAX} words": "short", f"< {SHORT_MIN} words": "very_short",
        f">= {LONG_MIN} words": "long", "function words": "function_ratio",
        "repeated 3-grams": "trigram_occurrences",
    }

    def _delta(self, label: str) -> str:
        field = self._NUMERIC.get(label)
        if field is None or self.after is None:
            return ""
        a, b = getattr(self.before, field), getattr(self.after, field)
        d = b - a
        if field == "function_ratio":
            return f"{100 * d:+.1f} pp"
        return f"{d:+.1f}" if isinstance(d, float) else f"{d:+d}"

    @staticmethod
    def _top(label: str, m: ProseMetrics) -> str:
        items = ", ".join(f'"{g}" x{n}' for g, n in m.top_trigrams) or "none"
        return f"{label}: {items}"


def main(argv: list[str]) -> int:
    """CLI entry: one or two text files, table on stdout.

    Returns:
        0 on success, 2 on usage or unreadable input.
    """
    if len(argv) not in (2, 3):
        print(__doc__.split("Usage::")[1].strip(), file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # accents survive a Windows console
    try:
        texts = [Path(p).read_text(encoding="utf-8") for p in argv[1:]]
        metrics = [ProseMetrics.measure(t) for t in texts]
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(Report(*metrics).render())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
