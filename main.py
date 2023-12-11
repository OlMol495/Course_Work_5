from src.config import config
from src.utils import create_database, save_data_to_database


def main():
    employers_ids = [
        1740,  # Яндекс
        58320,  # Россельхозбанк
        3529,  # Сбер
        4181,  # ВТБ
        64174,  # 2Гис
        80,  # АльфаБанк
        39305,  # Газпромбанк
        907345,  # Лукойл
        10343488,  # Яндекс Еда
        193400  # АВТОВАЗ
    ]

    params = {'host': 'localhost', 'user': 'postgres', 'password': '5758'}
    create_database()
    save_data_to_database(employers_ids,'Course_work_5', params)




if __name__ == '__main__':
    main()