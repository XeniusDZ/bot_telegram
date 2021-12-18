import unittest

import bot


class MyTestCase(unittest.TestCase):
    def test_question(self):
        data = bot.question("youtube")
        self.assertEqual("image" in data, True)
        data = bot.question("should not find an answer")
        self.assertEqual("image" in data, False)


if __name__ == '__main__':
    unittest.main()
