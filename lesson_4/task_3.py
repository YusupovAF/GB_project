'''
3. * (вместо 2) Доработать функцию currency_rates():
теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
какой тип данных лучше использовать в ответе функции?
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
        rate_date = response_content[response_content.find('Date="') + 6 : 70]
        rate_date_dt = datetime.datetime.strptime (rate_date, '%d.%m.%Y')
        return float(rate_text.replace(',', '.')), rate_date_dt.date()
    else:
        return None

if __name__ == "__main__":
    print(currency_rates('EuR'))