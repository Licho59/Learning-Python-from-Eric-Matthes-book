from pygal.maps.world import COUNTRIES

#noncode = COUNTRIES.copy()
def get_country_code(country_name):
    '''Zwraca stosowany przez Pygal dwuznakowy kod panstwa przypisany danemu panstwu.'''
    #global noncode
    for code, name in COUNTRIES.items():
        if name == country_name:
            #del noncode[code]
            return code
    # Jeżeli panstwo nie zostało znalezione, wartością zwrotną będzie None.   
    return None
#print(noncode, len(noncode))