import unittest
import bot
from unittest.mock import MagicMock

class MyTestCase(unittest.TestCase):
    """testing if we get an image in answer if we give a question that has a picture and one which doesn't"""
    def test_question(self):
        """
        :return: if we find image in data or not
        """
        data = bot.question("youtube")
        self.assertEqual("image" in data, True)
        data = bot.question("should not find an answer")
        self.assertEqual("image" in data, False)
async def async_magic():
    """
    testing async functions
    """
    pass


MagicMock.__await__ = lambda x: async_magic().__await__()

"""
took test code from https://stackoverflow.com/questions/23033939/how-to-test-python-3-4-asyncio-code
"""
class MyTestCase2(unittest.IsolatedAsyncioTestCase):
    """ testing every bot function"""
    async def test_start(self):
        """
        :return: function test_start works properly
        """
        message = MagicMock()
        await bot.start(message=message)
        message.reply.assert_called_with("Hey, I'm Aladin Bot! Message me anything and I will try to answer it.\nmade by @yanis_b.")

    async def test_start_false(self):
        """
        :return: function test_start doesn't work properly
        """
        message = MagicMock()
        await bot.start(message=message)
        not message.reply("Test for start")

    async def test_help_cmd(self):
        """
        :return: function help_cmd works properly
        """
        message = MagicMock()
        await bot.help_cmd(message=message)
        not message.reply.assert_called_with("If you find any problems or bugs with the bot contact @yanis_b.")

    async def test_help_cmd_false(self):
        """
        :return: function help_cmd doesn't work properly
        """
        message = MagicMock()
        await bot.help_cmd(message=message)
        not message.reply("test for help_cmd")

    async def test_yanis(self):
        """
        :return: function yanis works properly
        """
        message = MagicMock()
        await bot.yanis(message=message)
        message.reply.assert_called_with("Yanis Boudiaf is a 19 years old software engineer still learning who made the Aladin "
                        "telegram bot.")
    async def test_yanis_false(self):
        """
        :return: fuction yanis doesn't work properly
        """
        message = MagicMock()
        await bot.yanis(message=message)
        not message.reply("Test for yanis")

if __name__ == '__main__':
    unittest.main()
