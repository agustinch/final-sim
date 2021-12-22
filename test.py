import random 
from Soporte.Utils import truncate, crearDataFrame, generarExcel


def ListaAleatoriaNativa(n, inferior, superior, s=None):
    if superior == 1:
        superior = 1.00001
    if s != 0:
        random.seed(s)
    #La funcion aleatoria se parametriza con el rango [0, 1.00001] para generar numeros aleatorios menores o iguales a uno
    #por algunos decimales, que luego son truncados mediante la funcion
    numbers_array = list([truncate(random.uniform(inferior,superior), 4) for i in range(n)])
    return list(filter(lambda x : x == 1, numbers_array))


print(ListaAleatoriaNativa(1000000, 0, 1))