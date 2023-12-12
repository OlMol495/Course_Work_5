from src.config import config
from src.utils import create_database, save_data_to_database
from src.dbmanager import DBManager


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

    print("В базе представлена информация по открытым вакансиям компаний Яндекс, Россельхозбанк, Сбер, ВТБ,"
          "2Гис, Альфабанк, Газпромбанк, Лукойл, Яндекс Еда, Автоваз")

    params = {'host': 'localhost', 'user': 'postgres', 'password': '5758', 'port': '5432'}
    create_database()
    save_data_to_database(employers_ids,'Course_work_5', params)
    dbmanager = DBManager()

    while True:

        extra = input(
            "Для дополнительной сортировки:"
            "Введите 1, чтобы получить количество вакансий по каждой компании\n"
            "Введите 2, чтобы получить список всех компаний с их вакансиями, зарплатой и ссылкой на вакансию\n "
            "Введите 3, чтобы получить среднюю зарплату по всем вакансиям из базы\n"
            "Введите 4, чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "Введите 5, чтобы получить список вакансий по ключевому слову из их названия\n"
            "Введите Стоп, чтобы завершить работу\n"
        )

        if extra.lower() in ('стоп', 'stop'):
            print('Спасибо, что воспользовались нашей программой.\n'
                  ' До свидания!')
            break
        elif extra == '1':
            print(f'{dbmanager.get_companies_and_vacancies_count()}\n')

        elif extra == '2':
            print(f'{dbmanager.get_all_vacancies()}\n')

        elif extra == '3':
            print(f'{dbmanager.get_avg_salary()}\n')

        elif extra == '4':
            print(f'{dbmanager.get_vacancies_with_higher_salary()}\n')

        elif extra == '5':
            keyword = input('Введите слово для поиска вакансий: \n')
            print(f'{dbmanager.get_vacancies_with_keyword(keyword)}\n')

        else:
            print('Неверный ввод. Повторите')
            

if __name__ == '__main__':
    main()