import requests

# Wykonanie wywołania API i zachowanie otrzymanych odpowiedzi.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Kod stanu:', r.status_code)

# Umieszczenie odpowiedzi API w zmiennej.
response_dict = r.json() # konwersja danych z formatu json do postaci słownika Pythona
print("Calkowita liczba repozytoriow:", response_dict['total_count']) #'total_count' to jeden z 3 kluczy ww słownika

# Przetworzenie informacji o repozytoriach.
repo_dicts = response_dict['items']
print('Liczba zwroconych repozytoriow:', len(repo_dicts))
print('\nWybrane informacje o kazdym repozytorium:')
for repo_dict in repo_dicts:
    try:
        print('Nazwa:', repo_dict['name'])
        print('Wlasciciel:', repo_dict['owner']['login'])
        print('Gwiazdki:', repo_dict['stargazers_count'])
        print('Repozytorium:', repo_dict['html_url'])
        print('Uaktualnione:', repo_dict['updated_at'])
        print('Opis:', repo_dict['description'])
    except UnicodeEncodeError:
        print('<<<Jakis problem z opisem?>>>'.upper())

