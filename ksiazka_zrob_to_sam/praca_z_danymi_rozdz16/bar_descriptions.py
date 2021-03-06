import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_labe_rotation=45, show_legend=False)
chart.force_uri_protocol = 'http'
chart.title = 'Projekty Pythona'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 33084, 'label': 'Opis projektu httpie'},
    {'value': 30413, 'label': 'Opis projektu django'},
    {'value': 31787, 'label': 'Opis projektu flask'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')