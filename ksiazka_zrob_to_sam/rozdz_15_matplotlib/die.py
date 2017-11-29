from random import randint

class Die():
    '''Klasa przedstawiająca pojedynczą kość do gry.'''

    def __init__(self, num_sides=6):
        '''Przyjęto założenie, że kość do gry jest sześcianem.'''
        self.num_sides = num_sides

    def roll(self):
        '''Zwrot wartości z zakresu od 1 do liczby ścianek kości.'''
        return randint(1, self.num_sides)