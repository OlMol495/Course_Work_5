from pathlib import Path
from configparser import ConfigParser


URL_HH = 'https://api.hh.ru/vacancies'
JSON_HH = Path(Path(__file__).parent, 'cache_json', 'cache_hh.json')

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read parser
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        db = dict(params)

    return db