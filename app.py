from aiogram import executor

from loader import dp
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import utils.run_local_server


async def on_startup(dispatcher):

    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)

    # import utils.run_local_server


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
