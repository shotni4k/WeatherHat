#!/usr/bin/env python3.10.5
from aiogram import types

def locate_btn() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton("Узнать погоду🌤", request_location=True)
    return keyboard.add(btn)

def command_btn() -> types.InlineKeyboardMarkup:
    command_btn = types.InlineKeyboardMarkup(row_width=2)
    lacate_btn = types.InlineKeyboardButton(text = "Передать локацию🗺️", callback_data="/locate_me")
    help_btn = types.InlineKeyboardButton(text = "Помощь❓", callback_data= "/help")
    menu = types.InlineKeyboardButton(text = "Меню🗒", callback_data = "/menu",)
    return command_btn.add(lacate_btn,help_btn, menu)

def send_menu()-> types.InlineKeyboardMarkup:
    menu_btn = types.InlineKeyboardMarkup(row_width=1)
    complaint = types.InlineKeyboardButton(text= "Жалоба😡", callback_data="complaint")
    support = types.InlineKeyboardButton(text= "Поддержать проект💶", callback_data="support")
    subscriptions = types.InlineKeyboardButton(text = "Меню подписок✅", callback_data="subscriptions")
    return menu_btn.add(complaint,support,subscriptions)