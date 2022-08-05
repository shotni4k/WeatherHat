#!/usr/bin/env python3.10.5
from create_bot import dp
from config_files.config import get_answer_command
from keybards.keyboards import command_btn,locate_btn,send_menu
from aiogram import types, Dispatcher
from loguru import logger 


@dp.message_handler(commands = ['start'])
async def _send_welcome(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}")
    await message.answer(get_answer_command(text=message.text),reply_markup = command_btn())

@dp.message_handler(commands = ['menu'])
async def _create_menu(message: types.Message):
    await message.answer(text = "Meню", reply_markup=send_menu())

@dp.message_handler(commands=['help'])
async def _help_command(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}")
    await message.answer(get_answer_command(text = message.text))

@dp.message_handler(commands=['locate_me'])
async def _locate_command(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}")
    await message.answer(get_answer_command(text=message.text), reply_markup=locate_btn())


def register_command(dp: Dispatcher) -> dp:
    dp.register_message_handler(_send_welcome)
    dp.register_message_handler(_create_menu)
    dp.register_message_handler(_help_command)
    dp.register_message_handler(_locate_command)
    return dp