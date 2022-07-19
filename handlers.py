from aiogram.types import Message
from random import randint

from main import bot, dp
from config import chat_id, check_text, answer_text

@dp.message_handler()
async def send_messege(message: Message):
    text = message.text
    for alina in check_text:
        if alina in text.lower():
            answer = answer_text[randint(0, len(answer_text)-1)]
            await message.answer(text=answer)
