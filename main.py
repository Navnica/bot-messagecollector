import asyncio
from src.tools.error_manager import *
from aiogram import Bot, Dispatcher
from src.bot.routers import routers
from src.tools.settings_manager import SettingsManager

settings_manager: SettingsManager = SettingsManager()

token: str = settings_manager.get_settings_for_field('token')

dispatcher: Dispatcher = Dispatcher()
[dispatcher.include_router(router) for router in routers]


async def main():
    try:
        await dispatcher.start_polling(Bot(token=token))
    except Exception as error:
        logger.error(error)


if __name__ == '__main__':
    if not settings_manager.check_settings(silent=False):
        logger.error('Невозможно загрузить файл настроек.')
        exit()
    asyncio.run(main())
