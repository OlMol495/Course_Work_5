from configparser import ConfigParser

URL_HH_EMP = 'https://api.hh.ru/employers/'
URL_HH_VAC = 'https://api.hh.ru/vacancies?employer_id='


def config(filename='src/database.ini', section='postgresql'):
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
