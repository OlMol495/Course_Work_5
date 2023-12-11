from typing import Any
import psycopg2
import requests
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#from src.config import URL_HH_EMP, URL_HH_VAC
from pathlib import Path

URL_HH_EMP = 'https://api.hh.ru/employers/'
URL_HH_VAC = 'https://api.hh.ru/vacancies?employer_id='
JSON_HH_EMP = Path(Path(__file__).parent, 'cache_json', 'cache_hh_emp.json')
JSON_HH_VAC = Path(Path(__file__).parent, 'cache_json', 'cache_hh_vac.json')


def api_request_vacancy(company_id):
    """Запрос вакансий с сайта HH и формирование списка вакансий."""
    params = {
       'per_page': 100,
       'only_with_vacancies': True
   }
    url = URL_HH_VAC + str(company_id)
    vacancies_list = []
    response = requests.get(url, params=params)
    if response.status_code == 200:
        vacancies = response.json()
        for vacancy in vacancies['items']:
            if vacancy['salary'] is not None:
                hh_vacancies = {
                    'vacancy_name': vacancy['name'],
                    'salary_from': vacancy['salary']['from'],
                    'requirement': vacancy['snippet']['requirement'],
                    'employer_id': int(company_id)
                }
                vacancies_list.append(hh_vacancies)
        return vacancies_list

def api_request_employer(company_id):
    """Запрос данных о работодателе с сайта НН"""
    params = {
        'employer_id': company_id,
        'only_with_vacancies': True
    }
    url = URL_HH_EMP + str(company_id)
    response = requests.get(url, params=params)
    if response.status_code == 200:
        company_info = response.json()
        hh_company = {
            "employer_id": int(company_id),
            "company_name": company_info['name'],
            "open_vacancies": company_info['open_vacancies'],
            "company_url": company_info['site_url'],
            "about_company": company_info['alternate_url']
        }
        return hh_company


def create_database() -> None:
    """Создание базы данных и таблиц по работодателям и вакансиям"""

    conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='5758', port='5432')
    conn.autocommit = True
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute("""DROP DATABASE IF EXISTS Course_Work_5""")
    cur.close()
    conn.close()

    conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='5758', port='5432')
    conn.autocommit = True
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute("""CREATE DATABASE Course_Work_5""")

    cur.close()
    conn.close()

    conn = psycopg2.connect(database='Course_Work_5', host='localhost', user='postgres', password='5758', port='5432')
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers(
                employer_id INTEGER PRIMARY KEY,
                company_name VARCHAR(250) NOT NULL,
                open_vacancies INTEGER,
                company_url TEXT,
                about_company TEXT
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies(
                vacancy_id SERIAL PRIMARY KEY,
                vacancy_name VARCHAR(250) NOT NULL,
                salary_from INTEGER,
                requirement TEXT,
                employer_id INTEGER REFERENCES employers(employer_id)
            )
        """)

    conn.commit()
    conn.close()



def save_data_to_database(employers_ids: list, database_name: str, params: dict) -> None:
    """Заполняет таблицы данными о работодателях и вакансиях с сайта НН"""

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        for employer_id in employers_ids:
            employer_data = api_request_employer(employer_id)
            cur.execute(
                """
                INSERT INTO employers(employer_id, company_name, open_vacancies, company_url, about_company)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING employer_id
                """,
                (employer_data['employer_id'], employer_data['company_name'], employer_data['open_vacancies'],
                 employer_data['company_url'], employer_data['about_company'])
            )

        for employer_id in employers_ids:
            vacancy_data = api_request_vacancy(employer_id)
            for vacancy in vacancy_data:
                cur.execute(
                    """
                    INSERT INTO vacancies(vacancy_name, salary_from, requirement, employer_id)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (vacancy['vacancy_name'], vacancy['salary_from'], vacancy['requirement'],
                     vacancy['employer_id'])
                )
    conn.commit()
    conn.close()
