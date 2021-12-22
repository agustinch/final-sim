from Soporte.Utils import roundUP, truncate, crearDataFrame, probabilidadesAcumuladas, valores_demanda
import pandas as pd
import random 
import os

def calcularDemanda(prob, nro_aleatorio):
    len_lista = len(prob)
    indice = 0
    for i in range(len_lista - 1):
        if nro_aleatorio >= prob[i] and nro_aleatorio < prob[i + 1]:
            indice = i
            break
    return valores_demanda[indice] 

def calcularVentas(demanda, stock):
    if(demanda>stock):
        return stock
    return demanda


## Se calcula en docenas
def calcularCompra(demanda, min, max):
    demanda_docena = roundUP(demanda / 12)
    if(demanda_docena < min):
        return min
    if(demanda_docena > max):
        return max
    return demanda_docena


def Simulacion(seed, tiempo, stock_inicial, costo_docena, min_compra, max_compra, precio_unid, v_prob_demanda, mostrar_desde_mes, cant_it_mostrar, costo_inversion,total_cuotas_inversion):
    if(seed > 0):
        random.seed(seed)
    demanda_prob_acum = probabilidadesAcumuladas(v_prob_demanda)
    stock = stock_inicial
    ganancia_acum = 0
    iteraciones = [] # Iteraciones a mostrar
    prev_fila = []
    promedio = 0
    nro_cuota = 1
    valor_cuota = round(costo_inversion / total_cuotas_inversion,2)
    for i in range(tiempo + 1):
        if(i == 0):
            it_datos = [i, 0, 0, 0, stock_inicial,0,0,0,0,0,0,0,0,0]
        else:
            # Generar número aleatorio
            random_dem = truncate(random.random(), 4)

            # Calcula la demanda en base al número random obtenido
            cant_demanda = calcularDemanda(demanda_prob_acum, random_dem)

            # Recupera la demanda del mes anterior
            demanda_mes_anterior = prev_fila[2] # En Unidades

            # Calcula la compra a realizar en base al min y max permitido y la demanda del mes anterior
            compra_realizada_docenas = calcularCompra(demanda_mes_anterior,min_compra,max_compra)

            # Convierte la cantidad a comprar obtenida en docenas en unidades
            compra_realizada_unidades = compra_realizada_docenas * 12

            # Calcula la cantidad vendida en base a la demanda y el stock remanente más las unidades compradas ese mes

            # Unidades Disponible
            unidades_disponibles = stock + compra_realizada_unidades

            cant_venta = calcularVentas(cant_demanda, unidades_disponibles)

            # Calcula el stock remanente del mes actual
            stock = unidades_disponibles - cant_venta

            #Calcula el costo de la compra realizada
            costo_compra = costo_docena * compra_realizada_docenas

            #Calcula la ganancia de la venta
            ganancia_ventas = precio_unid * cant_venta
            
            # Contabiliza la cuota de la inversión realizada si corresponde
            cuota_inversion = 0 
            nro_cuota_actual = nro_cuota
            if(nro_cuota_actual <= total_cuotas_inversion and nro_cuota_actual > 0):
                cuota_inversion = valor_cuota
                # Se establece el nro de la siguiente cuota
                nro_cuota = nro_cuota + 1 if nro_cuota < total_cuotas_inversion else 0
            
            # Calcula la ganancia total del mes
            ganancia_total = round(ganancia_ventas - costo_compra - cuota_inversion,2)

            # Re calcula la ganancia acumulada
            ganancia_acum = round(ganancia_acum + ganancia_total,2)

            # Re calcula el promedio de la ganancia por mes
            promedio = round(ganancia_acum / i,2)

            it_datos = [str(i),random_dem, cant_demanda, cant_venta, stock,compra_realizada_unidades, compra_realizada_docenas, costo_compra,ganancia_ventas,nro_cuota_actual,cuota_inversion,ganancia_total, ganancia_acum, promedio]     
            
        # Se guarda la fila actual para ser usada en la siguiente iteración
        prev_fila = it_datos
        
        # Si corresponde se guarda la fila para ser mostrada
        if (i) >= mostrar_desde_mes and (i) - mostrar_desde_mes < cant_it_mostrar :
            iteraciones.append(it_datos)
        elif i == tiempo:
            iteraciones.append(it_datos)

    return crearDataFrame(iteraciones), promedio

