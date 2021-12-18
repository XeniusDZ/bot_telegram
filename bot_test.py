import unittest

import bot


class MyTestCase(unittest.TestCase):
    #testing if we get an image in answer if we give a question that has a picture and one which doesn't
    def test_question(self):
        data = bot.question("youtube")
        self.assertEqual("image" in data, True)
        data = bot.question("should not find an answer")
        self.assertEqual("image" in data, False)


if __name__ == '__main__':
    unittest.main()
