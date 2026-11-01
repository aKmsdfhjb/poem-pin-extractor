import unittest

from main import pin_extractor


class PinExtractorTests(unittest.TestCase):
    def test_diagonal_word_lengths(self):
        poems = ["The sky is blue\nBirds fly high\nNature is quite beautiful"]
        self.assertEqual(pin_extractor(poems), ["335"])

    def test_missing_word_uses_zero(self):
        self.assertEqual(pin_extractor(["One\nTwo words\nThree"]), ["120"])

    def test_empty_entry(self):
        self.assertEqual(pin_extractor([""]), ["0"])


if __name__ == "__main__":
    unittest.main()
