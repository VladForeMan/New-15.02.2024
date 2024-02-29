import requests

full_names = {
    "eur": "Євро",
    "usd": "Долар США",
    "jpy": "Японська єна",
    "gbp": "Фунт стерлінгів",
    "chf": "Швейцарський франк",
    "cad": "Канадський долар",
    "aud": "Австралійський долар",
    "nzd": "Новозеландський долар",
    "sek": "Шведська крона",
    "nok": "Норвезька крона",
    "dkk": "Данська крона",
    "rub": "Російський рубль",
    "cny": "Китайський юань",
    "inr": "Індійська рупія",
    "brl": "Бразильський реал",
    "mxn": "Мексиканський песо",
    "zar": "Південноафриканський ранд",
    "try": "Турецька ліра",
}

host = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest'
url = f'{host}/currencies.json'
response = requests.get(url)
cur_list = {}
if response.ok:
    cur_list = response.json()
else:
    print(f'{response.status_code=}')

while True:
    cur_from = input("Введіть код валюти, яку хочете обміняти (наприклад, eur usd jpy gbp chf cad aud nzd sek nok dkk rub cny brl mxn zar try ): ").lower()
    if cur_from not in cur_list:
        print("Невідома валюта.")
        continue
    break

while True:
    cur_to = input("Введіть код валюти, на яку хочете обміняти (наприклад, eur usd jpy gbp chf cad aud nzd sek nok dkk rub cny brl mxn zar try): ").lower()
    if cur_to not in cur_list:
        print("Невідома валюта.")
        continue
    break

amount = float(input("Введіть суму для обміну: "))

url = f'{host}/currencies/{cur_from}/{cur_to}.json'
response = requests.get(url)

if response.ok:
    as_json = response.json()

    amount_to = round(amount * as_json[cur_to], 2)

    print(f"{amount} {full_names[cur_from].upper()} = {amount_to} {full_names[cur_to].upper()}")
else:
    print(f'{response.status_code=}')
