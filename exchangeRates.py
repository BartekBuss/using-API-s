import requests

def download_rate(currency):
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'][0]['mid']
    else:
        print('Błąd podczas pobierania danych z API')
        return None
    
def gold_rate():
    url = "http://api.nbp.pl/api/cenyzlota/?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['cena']
    else:
        print('Błąd podczas pobierania danych z API')
        return None

#-------------------------------------------------------------------

if __name__ == "__main__":
    print("Aktualne kursy walut:")
    print()
    usd = download_rate('usd')
    eur = download_rate('eur')
    gold = gold_rate()

    if usd:
        print(f"PLN do USD to: {usd}")
        print()
    if eur:
        print(f"PLN do EUR to: {eur}")
        print()
    if gold:
        print(f"Cena 1g złota w NBP to: {gold}")
        print()