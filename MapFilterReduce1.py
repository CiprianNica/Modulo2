from functools import reduce

lista = [1, 2, 3, 4]

sumaTodos = reduce(lambda x, y: x+y, lista)

l = lista[:] # creo una sublista
l.insert(0,0) # añado un elem mas, neutro para la suma

sumaDobles = reduce(lambda x, y: x+y*2, l)
