from unittest import TestCase

import printer

class AnswerTestCase(TestCase):
    def test_printer(self):
        self.assertEqual(printer.solution([2, 1, 3, 2], 2), 1)
        self.assertEqual(printer.solution([1, 1, 9, 1, 1, 1], 0), 5)
