import psycopg2


class DBManager():
    """Подключается к БД PostgreSQL и выполняет различные запросы."""

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname='HeadhunterRU', **params)
        self.cur = self.conn.cursor()


    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        pass

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        pass

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        pass

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self, keyword, cur):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова."""
        cur.execute(f'''SELECT * FROM vacancies WHERE vacancy_name LIKE "%{keyword}%"''')
        result = cur.fetchall()
        return result

