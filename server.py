from aiogram import Bot, Dispatcher, executor, types
from config_files.config import get_telegram_api_key, locate_btn,Coordinates,get_answer_command
from loguru import logger
from weather import get_weather


bot = Bot(token = get_telegram_api_key())
dp = Dispatcher(bot)
# dd
logger.add("log/INFO.log",colorize=True, format="{time} {level} {message}", level="INFO")



@dp.message_handler(commands = ['start','help'])
async def send_welcome(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}")
    await message.answer(get_answer_command(message))


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}\n lat&long = {message.location}")
    await message.answer(get_weather(Coordinates(latitube = message.location.latitude,longitube = message.location.longitude)), reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['locate_me'])
async def cmd_locate_me(message: types.Message):
    reply = get_answer_command(message)
    logger.info(f"\n user-id {message.from_user.id} \n user-name - {message.from_user.full_name}\n text - {message.text}")
    await message.answer(reply, reply_markup=locate_btn())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)