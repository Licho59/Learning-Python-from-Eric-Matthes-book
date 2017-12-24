import json
from pygal.maps.world import World, COUNTRIES
from pygal.style import LightColorizedStyle, RotateStyle
import country_codes
from country_codes import get_country_code

filename = 'C:\\Users\\Leszek\Documents\\python_scripts\\python_tutorial\\ksiazka_zrob_to_sam\\rozdz_16_pob_danych\\population_data.json'
with open(filename) as f:
    pop_data = json.load(f) # load() konwertuje dane na format możliwy do użycia w Pythonie

# Utworzenie słownika danych dotyczących populacji.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population
noncode_countries = country_codes.noncode
print(noncode_countries)
        
# Podzielenie panstw na trzy grupy według liczebności populacji.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000: cc_pops_1[cc] = pop
    elif pop < 1000000000: cc_pops_2[cc] = pop
    else: cc_pops_3[cc] = pop

# Wyświetlenie liczby panstw w każdej z trzech grup.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'Populacja na świecie w 2010 roku (dane dla poszczególnych panstw)'
wm.add('0 - 10 mln', cc_pops_1)
wm.add('10 mln - 1 mld', cc_pops_2)
wm.add('> 1 mld', cc_pops_3)

wm.render_to_file('world_population.svg') 
        