import requests

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
spliting = response.text.split('</Valute>')

date = response.headers['Date']
char_code = [i[(i.find('<CharCode>') + len('<CharCode>')): i.find('</CharCode>')] for i in spliting]
nominal = [i[(i.find('<Nominal>') + len('<Nominal>')): i.find('</Nominal>')] for i in spliting]
naming = [i[(i.find('<Name>') + len('<Name>')): i.find('</Name>')] for i in spliting]
value = [i[(i.find('<Value>') + len('<Value>')): i.find('</Value>')].replace(',', '.') for i in spliting]


def currency_rates(code):
    try:
        index = char_code.index(code)
    except ValueError:
        return None
    return f'As for {date} {naming[index]} is {float(value[index]) / float(nominal[index])} rub'


if __name__ == '__main__':
    print(f'List of currency codes{char_code}')
    answer = (input(f'Select currency code: '))
    print(currency_rates(answer))
