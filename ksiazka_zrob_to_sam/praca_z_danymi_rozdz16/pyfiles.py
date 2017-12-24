import os
def gen_py():
    for i in os.listdir(): # ista plików w bieżącym katalogu
        if i.endswith('.py'): 
            yield i
            print(i)

m = gen_py() # wywołanie funkcji zawierającej instrukcję yield zwraca obiekt generatora, który obsługuje protokół iteratora.
next(m) # komenda dla iteratora
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)