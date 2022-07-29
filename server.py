#!/usr/bin/env python3.10.5
from loguru import logger
from weather import get_weather
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from config_files.keyboards import locate_btn,command_btn
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from config_files.config import get_telegram_api_key,Coordinates,get_answer_command


memory_storage = MemoryStorage()


bot = Bot(token = get_telegram_api_key())
dp = Dispatcher(bot, storage= memory_storage)
logger.add("log/INFO.log",colorize=True, format="{time} {level} {message}", level="INFO")

@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}")
    await message.answer(get_answer_command(text=message.text),reply_markup = command_btn())

@dp.message_handler(commands=['help'])
async def help_answer(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}")
    await message.answer(get_answer_command(text = message.text))

@dp.callback_query_handler(lambda c: c.data == '/help')
async def handle_help_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer(get_answer_command(text= callback_query.data))

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}\n lat&long = {message.location}")
    await message.answer(get_weather(Coordinates(latitube = message.location.latitude,longitube = message.location.longitude)), reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['locate_me'])
async def cmd_locate_me(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}")
    await message.answer(get_answer_command(text=message.text), reply_markup=locate_btn())

@dp.callback_query_handler(lambda c: c.data == '/locate_me')
async def handle_help_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer(get_answer_command(text= callback_query.data), reply_markup=locate_btn())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)