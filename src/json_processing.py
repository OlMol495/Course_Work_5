import json
from config import JSON_HH


class JsonProcessingHH():
    """Обработка json с сайта НН."""
    path = JSON_HH
    @classmethod
    def save_json(cls, data) -> None:
        """Сохранение json с сайта в файл."""
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls) -> None:
        """Чтение json."""
        with open(cls.path, 'r', encoding='utf-8') as file:
            return json.load(file)
