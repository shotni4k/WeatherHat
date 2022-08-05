#!/usr/bin/env python3.10.5
from create_bot import dp 
from aiogram import types, Dispatcher
from config_files.data import Coordinates
from weather import get_weather
from loguru import logger



@dp.message_handler(content_types=['location'])
async def _handle_location(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}\n lat&long = {message.location}")
    await message.answer(get_weather(Coordinates(latitube = message.location.latitude,longitube = message.location.longitude)), reply_markup=types.ReplyKeyboardRemove())


def register_other_handlers(dp: Dispatcher):
    return dp.register_message_handler(_handle_location)