import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Wykonanie wywołania API i zachowanie otrzymanych odpowiedzi.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Kod stanu:', r.status_code)

# Umieszczenie odpowiedzi API w zmiennej.
response_dict = r.json() # konwersja danych z formatu json do postaci słownika Pythona
print("Calkowita liczba repozytoriow:", response_dict['total_count']) #'total_count' to jeden z 3 kluczy ww słownika

# Przetworzenie informacji o repozytoriach.
repo_dicts = response_dict['items'] # lista repozytoriów
print('Liczba elementów:', len(repo_dicts))

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = 'http'
chart._title = 'Oznaczone największą liczbą gwiazdek projekty Pythona w serwisie GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos_1.svg')