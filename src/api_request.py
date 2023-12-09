import os
from config import URL_HH
import requests
from src.json_processing import JsonProcessingHH

class APIRequestHH():
    """Запросы с сайта НН."""
    def __init__(self, keyword=str, page=0, area=113):
        self.url = URL_HH
        self.parameter = {
            'text': keyword,
            'page': page,
            'area': area,
            'only_with_salary': True
        }

    def api_request(self):
        """Запрос с сайта HH и загрузка в json файл."""
        response = requests.get(self.url, params=self.parameter)
        print(response.status_code)
        JsonProcessingHH.save_json(response.json()['items'])