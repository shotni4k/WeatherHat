#!/usr/bin/env python3.10.5
from aiogram import Bot,Dispatcher
from config_files.config import get_telegram_api_key

bot = Bot(token= get_telegram_api_key())
dp = Dispatcher(bot)