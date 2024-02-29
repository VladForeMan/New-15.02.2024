import requests

host = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest'
url = f'{host}/currencies.json'
response = requests.get(url)
cur_list = {}
if response.ok:
    cur_list = response.json()
else:
    print(f'{response.status_code=}')

print(list(cur_list.keys()))

cur_from = input("Введите то что хотите взять в обмен или то что сверху написано (eur, usd, jpy): ")
cur_to = input("Введите на то что вы хотите обменять или то что сверху написано (eur, usd, jpy): ")
amount = float(input("Введите количество "))

url = f'{host}/currencies/{cur_from}/{cur_to}.json'
response = requests.get(url)

if response.ok:
    as_json = response.json()
    print(as_json)
    print(f'{amount} {cur_from.upper()} = {round(amount * as_json[cur_to], 2)} {cur_to.upper()}')
else:
    print(f'{response.status_code=}')