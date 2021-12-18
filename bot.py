import http_client
from aiogram import Bot, Dispatcher, types
import json

"""M3O_API_TOKEN is the secret token used to connect to the m3o.com API."""
M3O_API_TOKEN = "NmVkOThiYTctY2Y0Ni00NjljLTg1ODEtNGJiN2ZiZDM3OTM4"

"""TELEGRAM_API_TOKEN is the secret token used to connect to the Telegram bot API."""
TELEGRAM_API_TOKEN = "5067771273:AAH0Oh9-LouEUWZzvUmIJNc5LbGdEEKhp5o"

"""creates the telegram bot aiogram instance."""
dp = Dispatcher(Bot(token=TELEGRAM_API_TOKEN))



def question(query):
    """
    question sends a request to the m3o API to get answers for the query question.
    :param query:
    :return: returns the api response.
    """
    response = http_client.post("https://api.m3o.com/v1/answer/Question", {'query': query}, M3O_API_TOKEN)

    return json.loads(response.replace('\\', ''))


"""start executed when user starts conversation with the bot."""
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hey, I'm Aladin Bot! Message me anything and I will try to answer it.\nmade by @yanis_b.")


"""help is executed when user asks the bot for help."""
@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.reply("If you find any problems or bugs with the bot contact @yanis_b.")


"""author is executed asks for the bot author name."""
@dp.message_handler(commands=['yanis', 'author'])
async def yanis(message: types.Message):
    await message.reply("Yanis Boudiaf is a 19 years old software engineer still learning who made the Aladin "
                        "telegram bot.")



@dp.message_handler()
async def answer(message: types.Message):
    """
    :param message: message that we input
    :return: answer process all messages sent as questions and reply with the answer.
    """
    response = question(message.text)
    if "image" in response:
        await message.answer_photo(response["image"], response["answer"])
    else:
        await message.answer(response["answer"].replace("xf0x9fx98x9e", "!"))
