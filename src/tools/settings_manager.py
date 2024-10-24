from src.tools.error_manager import *
import json
from typing import Any


class SettingsManager:
    settings: dict[str, Any] | None = None
    settings_file: str = ''

    def __init__(self, settings_file: str = 'settings.json') -> None:
        self.settings_file = settings_file
        if not self.check_settings():
            exit()

    def check_settings(self, silent: bool = True) -> bool:
        try:
            if not silent:
                logger.info('Проверка файла настроек')
            json.load(open(self.settings_file))
            if not silent:
                logger.info('Файл настроек загружен')
            return True
        except FileNotFoundError:
            if not silent:
                logger.error(f'Не найден файл настроек {self.settings_file}')
            return False
        except json.decoder.JSONDecodeError:
            if not silent:
                logger.error(f'{self.settings_file} имеет неверный формат. Невозможно привести к JSON')
            return False

    def get_settings(self) -> dict[str, Any]:
        return json.load(open(self.settings_file))

    def get_settings_for_field(self, field: str) -> dict[str, Any] | str:
        try:
            return self.get_settings()[field]
        except KeyError:
            logger.error(f'Файл настроек {self.settings_file} не содержит поля {field}')
            exit()

    def update_settings(self, new_settings: dict[str, Any]) -> None:
        old_setting: dict[str, Any] = self.get_settings()
        old_setting.update(new_settings)
        json.dump(old_setting, open(self.settings_file, 'w'), indent=2)
