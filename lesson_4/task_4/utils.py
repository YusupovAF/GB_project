'''
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
'''

from requests import get, utils
import datetime

def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    response_content = response.content.decode(encoding=encodings)
    if currency.upper() in response_content:
        text_after_currency = response_content[(response_content.find(currency.upper()) + len(currency)):]
        rate_text = text_after_currency[text_after_currency.find('<Value>') + 7:text_after_currency.find('</Value>')]
        rate_date = response_content[response_content.find('Date="') + 6:70]
        rate_date_dt = datetime.datetime.strptime (rate_date, '%d.%m.%Y')
        return float(rate_text.replace(',', '.')), f"{rate_date_dt.date():%Y-%m-%d}"
    else:
        return None

if __name__ == "__main__":
    print('Происходит что-то лишнее')