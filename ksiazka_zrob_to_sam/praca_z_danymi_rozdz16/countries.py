from pygal.maps.world import COUNTRIES
i = 1
for country_code in sorted(COUNTRIES.keys()):
    print(str(i) +'. ' + country_code + ' - ' + COUNTRIES[country_code])
    i += 1