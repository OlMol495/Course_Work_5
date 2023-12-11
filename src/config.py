from configparser import ConfigParser
# from pathlib import Path
#
# URL_HH_EMP = 'https://api.hh.ru/employers/'
# URL_HH_VAC = 'https://api.hh.ru/vacancies?employer_id='
# JSON_HH_EMP = Path(Path(__file__).parent, 'cache_json', 'cache_hh_emp.json')
# JSON_HH_VAC = Path(Path(__file__).parent, 'cache_json', 'cache_hh_vac.json')


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read parser
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        db = dict(params)
    else:
        raise Exception("Некорректный файл database.ini")

    return db

