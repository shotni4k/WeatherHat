#!/usr/bin/env python3.10.5
from aiogram.utils import executor
from create_bot import dp
from hendlers import inline_handlers,other_hendlers,command_hendlers

command_hendlers.register_command(dp)
other_hendlers.register_other_handlers(dp)
inline_handlers.register_inline_hendlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)