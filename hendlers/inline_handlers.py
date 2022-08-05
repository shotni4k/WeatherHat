#!/usr/bin/env python3.10.5
from create_bot import dp
from aiogram import types,Dispatcher
from config_files.config import get_answer_command
from keybards.keyboards import locate_btn,send_menu

@dp.callback_query_handler(lambda c: c.data == '/help')
async def _help_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer(get_answer_command(text= callback_query.data))

@dp.callback_query_handler(lambda c: c.data == 'complaint')
async def _complaint_button(callback_query: types.CallbackQuery):
     await callback_query.message.answer("Опишите вашу проблему")

@dp.callback_query_handler(lambda c: c.data == '/menu')
async def _menu_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Меню:",reply_markup = send_menu())

@dp.callback_query_handler(lambda c: c.data == '/locate_me')
async def _locate_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer(get_answer_command(text= callback_query.data), reply_markup=locate_btn())

def register_inline_hendlers(dp: Dispatcher) -> dp:
    dp.register_callback_query_handler(_help_button)
    dp.register_callback_query_handler(_complaint_button)
    #dp.register_callback_query_handler(_menu_button)
    dp.register_callback_query_handler(_locate_button)
    return dp