import requests

def download_rate(currency):
    try:
        url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/?format=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['rates'][0]['mid']
        else:
            print(f'Błąd podczas pobierania danych z API o {currency}')
            return None
    except:
        print('Brak połączenia z internetem')
    
def download_gold_rate():
    try:    
        url = "http://api.nbp.pl/api/cenyzlota/?format=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0]['cena']
        else:
            print('Błąd podczas pobierania danych z API o cenie złota')
            return None
    except:
        print('Brak połączenia z internetem')

#-------------------------------------------------------------------

if __name__ == "__main__":
    print()
    print('Rozpoczynam pobieranie danych...')

    usd = download_rate('usd')
    eur = download_rate('eur')
    chf = download_rate('chf')
    gbp = download_rate('gbp')
    jpy = download_rate('jpy')
    czk = download_rate('czk')
    dkk = download_rate('dkk')
    cny = download_rate('cny')
    gold = download_gold_rate()

    print()
    print('Aktualne kursy NBP:')
    print()

    if usd:
        print(f'PLN/USD: {usd}')
    if eur:
        print(f'PLN/EUR: {eur}')
    if chf:
        print(f'PLN/CHF: {chf}')
    if gbp:
        print(f'PLN/GBP: {gbp}')
    if jpy:
        print(f'PLN/JPY: {jpy}')
    if czk:
        print(f'PLN/CZK: {czk}')
    if dkk:
        print(f'PLN/DKK: {dkk}')
    if cny:
        print(f'PLN/CNY: {cny}')
    if gold:
        oz = float(gold)
        oz *= 31.1
        print(f'Cena 1g złota w NBP to: {gold} zł')
        print(f'Cena 1 oz to: {round(oz, 2)} zł')
        if gold < 250.0:
            print('Tanio! KUPUJ!')
    print()