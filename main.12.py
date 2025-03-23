import requests
import csv
from cringe import get_table, get_rows

# Запрос к странице Wikipedia с информацией о кодах валют ISO 4217
r = requests.get('https://en.wikipedia.org/wiki/ISO_4217')

# Получение таблицы с данными о валютах
table = get_table(r)

# Извлечение строк из таблицы
rows = get_rows(table)

# Запись данных в CSV-файл
with open("data.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    # Заголовки столбцов
    writer.writerow(['Code', 'Nume', "currency"])
    # Запись строк данных
    writer.writerows(rows)
