# Course_Work_5
#Программа для парсинга из заранее определенного списка компаний и их открытых вакансий на сайте HeadHunter.ru

#Данные заносятся в базу SQL

#Внимание: до начала работы с программой надо зарегистрироваться на postgres

#До запуска программы надо заполнить файл database.ini: 
user=<ваш юзернейм>(в большинстве случаев по умолчанию <postgres>)
password=<ваш пароль при регистрации в postgres>
port=<по умолчанию <5432>, но если работаете в macOS, то он будет другим>
#Установите зависимости из файла requirements.txt с помощью команды pip install -r requirements.txt
Если работаете в окружении Poetry, то зависимости находятся в файле pyproject.toml

##Программа запускается из файла main.py

###При запуске программы происходит запрос с сайта НН по компаниям Яндекс, Россельхозбанк, Сбер, ВТБ,
2Гис, Альфабанк, Газпромбанк, Лукойл, Яндекс Еда, Автоваз и их открытым вакансиям
создается база в sql и две таблицы
Дальнейшая работа происходит с базой
###Пользователь может выбрать несколько опций по выводу данных из таблиц 
и также осуществить поиск вакансий по ключевому слову
###Программа прекращает работу при введении слова "стоп" или "stop"
