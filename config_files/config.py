#!/usr/bin/env python3.10.5
import os
import sys
import json
import random

from loguru import logger
from aiogram import types

from dataclasses import dataclass

def _get_OWMapi_key() -> str:
    owm_key = os.getenv("OWM_API_KEY")
    if owm_key is None:
        logger.critical("OWM key is None")
        return sys.exit()
    return owm_key

def get_telegram_api_key()-> str:
    token = os.getenv("TELEGRAM_API_KEY")
    if token is None: 
        logger.critical("Telegram api key is None")
        return sys.exit()
    return token
    
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + _get_OWMapi_key() + "&lang=ru&"
    "units=metric"
)

@dataclass(frozen=True, slots = True)
class Coordinates():
    latitube: float
    longitube: float


def get_answer_command(text: str) -> str:
    try:
        with open("config_files/answer.json", "r", encoding="utf-8") as file:
            answer_list = json.load(file)
    except FileNotFoundError:
        logger.error("File not found")
        raise sys.exit()

    for intent, value in answer_list["command"].items():
        for exepel in answer_list["command"][intent]["answer"]:
            if intent == text:
                return random.choice(value["answer"])
    return "This command not found"
   





