
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
import numpy as np

valores_demanda = [250,300,350,400,450,500,600,700]


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def generarExcel(dataframe, nombre_archivo):
    wb = Workbook(nombre_archivo)
    for nombre,df in dataframe.items():
        ws = wb.create_sheet(nombre)
        for r in dataframe_to_rows(df, index=False, header=True):
            ws.append(r)
    wb.save(nombre_archivo)


def roundUP(val):
    return val if val == int(val) else int(val)+1


def probabilidadesAcumuladas(prob):
    v = [0] * (len(prob) + 1)
    for i in range(len(prob)):
        v[i + 1] = truncate(v[i] + prob[i] / 100, 2)
    return v

def convertirPorcentajesADecimales(prob):
    v = [0] * (len(prob))
    for i in range(len(prob)):
        v[i] = truncate(prob[i] / 100, 2)
    return v

def crearIntervalos(prob):
    prob_acumuladas = probabilidadesAcumuladas(prob)
    intervalos = []
    for i in range(len(prob_acumuladas) - 1):
        intervalos.append(str(prob_acumuladas[i]) + " - " + str(prob_acumuladas[i + 1]))
    return intervalos



def validarProbabilidades(vector):
    prob = 0
    for i in range (len(vector)):
        prob+= vector[i]
    if prob == 100:
      return True
    return False

def crearDataFrame(datos):
    
    col = ["Tiempo (meses)",
        "RND Demanda",
        "Demanda",
        "Venta",
        "Stock remanente",
        "Compra (unidades)",
        "Compra (docenas)",
        "Costo Compra",
        "Ganancia venta",
        "Cuota nro",
        "Cuota inversion",
        "Ganancia Total", 
        "Ganancia Acumulada",
         "Promedio"]

    df = pd.DataFrame(np.array(datos), columns=col)
    return df

