
from requests import get, utils
from decimal import Decimal

def currency_rates(char_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    server_date = response.headers['Set-Cookie'].split(',')[1]
    print(f'Дата сервера: {server_date}')

    content = response.content.decode(encoding=encodings)

    currency_dict = {}
    for n in content.split('</Value>'):  # Находим код валюты и её значение
        i = n.split('</CharCode>')[0][-3:]
        currency_dict[i] = n[-7:] if i.isalpha() else None # Создаем список с валютой и её стоимостью

    char_code = char_code.upper()
    if currency_dict.setdefault(char_code) == None:
        print('Неверный код валюты')
    else:                                 #Если ключ есть в списке выдаём значение валюты
        price = Decimal(currency_dict[char_code].replace(',', '.')).quantize(Decimal('0.01'))
        print(f'{char_code} = {price} руб.')

currency_rates(input('Введите валюту в формате (USD,usd):'))
