
from functools import reduce


lista = [1, 3, -1, 15, 9, 10]

listaDoble = map(lambda x: x*x, lista)
listaPares = filter(lambda x: x%2 == 0, lista)

sumaTodos = reduce(lambda x, y: x+y, lista)

suma100 = reduce(lambda x, y: x+y, range(101))