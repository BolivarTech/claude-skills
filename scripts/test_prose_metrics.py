"""Tests for the prose shape metrics: splitting, counting, ratios, report."""

import unittest

from prose_metrics import ProseMetrics, Report, split_sentences, words_of


class SentenceSplittingTests(unittest.TestCase):
    def test_splits_on_terminator_followed_by_capital(self):
        self.assertEqual(split_sentences("Uno va. Dos viene. ¿Tres? ¡Cuatro!"),
                         ["Uno va.", "Dos viene.", "¿Tres?", "¡Cuatro!"])

    def test_decimal_and_abbreviation_before_digit_do_not_split(self):
        self.assertEqual(len(split_sentences("Dejó 3.000 muertos, p. 471 de la edición.")), 1)

    def test_dialogue_dash_and_quote_open_a_sentence(self):
        parts = split_sentences('Ella habló. — ¿Cuándo? — preguntó él. "Nunca", dijo.')
        self.assertEqual(parts[1], "— ¿Cuándo? — preguntó él.")
        self.assertEqual(parts[2], '"Nunca", dijo.')

    def test_line_breaks_count_as_spaces(self):
        self.assertEqual(split_sentences("Uno.\n\nDos.\nTres."), ["Uno.", "Dos.", "Tres."])

    def test_empty_and_whitespace_give_no_sentences(self):
        self.assertEqual(split_sentences(""), [])
        self.assertEqual(split_sentences("   \n "), [])


class WordTokenTests(unittest.TestCase):
    def test_accents_kept_and_lowercased(self):
        self.assertEqual(words_of("Úrsula Iguarán, ¡años!"), ["úrsula", "iguarán", "años"])

    def test_digits_and_symbols_are_not_words(self):
        self.assertEqual(words_of("1928 ≈ 3.000 --"), [])


class MetricsTests(unittest.TestCase):
    TEXT = ("La novela es breve. Macondo muere. A lo largo del relato, a lo largo de "
            "los años, todo vuelve al mismo punto de partida sin que nadie lo note.")

    def test_counts_words_and_sentences(self):
        m = ProseMetrics.measure(self.TEXT)
        self.assertEqual(m.sentences, 3)
        self.assertEqual(m.words, 4 + 2 + 23)

    def test_length_bands(self):
        m = ProseMetrics.measure(self.TEXT)
        self.assertEqual((m.min_len, m.max_len), (2, 23))
        self.assertEqual(m.short, 1)        # "La novela es breve." = 4 words
        self.assertEqual(m.very_short, 1)   # "Macondo muere." = 2 words
        self.assertEqual(m.long, 0)

    def test_long_band_starts_at_31(self):
        thirty = " ".join(["palabra"] * 30) + "."
        thirty_one = " ".join(["palabra"] * 31) + "."
        self.assertEqual(ProseMetrics.measure(thirty).long, 0)
        self.assertEqual(ProseMetrics.measure(thirty_one).long, 1)

    def test_repeated_trigrams_counted_with_top_list(self):
        m = ProseMetrics.measure(self.TEXT)
        self.assertEqual(m.trigram_types, 1)          # "a lo largo" x2
        self.assertEqual(m.trigram_occurrences, 2)
        self.assertEqual(m.top_trigrams, (("a lo largo", 2),))

    def test_function_word_ratio(self):
        m = ProseMetrics.measure("el de la casa")   # 3 of 4
        self.assertAlmostEqual(m.function_ratio, 0.75)

    def test_single_sentence_has_zero_stdev(self):
        self.assertEqual(ProseMetrics.measure("Solo una.").stdev_len, 0.0)

    def test_text_without_words_is_an_error(self):
        with self.assertRaises(ValueError):
            ProseMetrics.measure("1928 --- ≈")


class ReportTests(unittest.TestCase):
    def test_single_report_lists_every_row_and_top_trigrams(self):
        out = Report(ProseMetrics.measure(MetricsTests.TEXT)).render()
        self.assertIn("mean length", out)
        self.assertIn('top 3-grams: "a lo largo" x2', out)
        self.assertNotIn("delta", out)

    def test_paired_report_shows_signed_deltas(self):
        before = ProseMetrics.measure("Alfa beta gamma. Delta zeta eta.")
        after = ProseMetrics.measure("Alfa beta gamma delta zeta eta.")
        out = Report(before, after).render()
        self.assertIn("delta", out)
        self.assertRegex(out, r"sentences\s+2\s+1\s+-1")
        self.assertRegex(out, r"mean length\s+3\.0\s+6\.0\s+\+3\.0")
        self.assertRegex(out, r"function words\s+0\.0%\s+0\.0%\s+\+0\.0 pp")

    def test_top_trigrams_say_none_when_nothing_repeats(self):
        out = Report(ProseMetrics.measure("Nada se repite aquí.")).render()
        self.assertIn("top 3-grams: none", out)


if __name__ == "__main__":
    unittest.main()
