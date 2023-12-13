import psycopg2


class DBManager():
    """Подключается к БД PostgreSQL и выполняет различные запросы."""

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname='cw', **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        self.cur.execute(
            """SELECT company_name, open_vacancies FROM employers""")

        result = self.cur.fetchall()
        return result

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        self.cur.execute(
            """
            SELECT company_name, vacancy_name, salary_from, vacancy_url
            FROM vacancies
            JOIN employers USING (employer_id)
            ORDER BY employers.company_name DESC            
            """
        )
        result = self.cur.fetchall()
        return result

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""

        self.cur.execute(
            """
            SELECT AVG(salary_from) AS avg_salary FROM vacancies
            """
        )
        result = self.cur.fetchall()
        return result

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        self.cur.execute(
            """
            SELECT * FROM vacancies
            WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)
            """
        )
        result = self.cur.fetchall()
        return result

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова."""
        self.cur.execute(f'''SELECT * FROM vacancies 
                            WHERE vacancy_name LIKE '%{keyword}%' ''')
        result = self.cur.fetchall()
        return result
