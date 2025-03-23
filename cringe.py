from bs4 import BeautifulSoup

# Функция для получения таблицы из HTML-страницы
def get_table(page):
    # Поиск таблицы с классом "wikitable" и извлечение всех строк
    table = BeautifulSoup(page.text, 'html.parser').find("table", class_="wikitable").find_all("tr")
    return table

# Функция для извлечения данных из строк таблицы
def get_rows(table):
    rows = []
    for i in table:
        # Поиск всех ячеек в строке
        row = i.find_all('td')
        # Проверка, что строка содержит достаточно ячеек
        if len(row) >= 4:
            # Извлечение кода валюты, названия и валюты
            code = row[0].text.strip()
            nume = row[1].text.strip()
            currency = row[3].text.strip()
            # Добавление строки в список
            rows.append([code, nume, currency])
    return rows
