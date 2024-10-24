import json
from src.tools.error_manager import *


class ReplicasManager:
    hot_reload: bool = False
    replicas: dict = {}
    def __init__(self, replicas_file_path: str) -> None:
        self.replicas_file_path = replicas_file_path
        self.update_list()

    def update_list(self) -> None:
        try:
            self.replicas = json.load(open(self.replicas_file_path))
            logger.info('Файл с ответами загружен')
        except FileNotFoundError:
            logger.error('Не найден файл с ответами')
        except json.JSONDecodeError:
            logger.error('Неверный формат файла с ответами')
    def get_reply(self, key: str) -> str | None:
        if self.hot_reload:
            self.update_list()

        return self.replicas.get(key)