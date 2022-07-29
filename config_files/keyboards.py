#!/usr/bin/env python3.10.5
from aiogram import types

def locate_btn() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton("Узнать погоду🌤", request_location=True)
    return keyboard.add(btn)

def command_btn() -> types.InlineKeyboardMarkup:
    command_btn = types.InlineKeyboardMarkup()
    lacate_btn = types.InlineKeyboardButton(text = "Передать локацию🗺️", callback_data="/locate_me")
    help_btn = types.InlineKeyboardButton(text = "Помощь❓", callback_data= "/help")
    return command_btn.add(lacate_btn,help_btn)