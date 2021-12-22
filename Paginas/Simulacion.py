import streamlit as st
import os
from Soporte.Controlador import Simulacion
from Soporte.Utils import probabilidadesAcumuladas, convertirPorcentajesADecimales, crearIntervalos, generarExcel, validarProbabilidades, valores_demanda
import pandas as pd



def LoadPage():
    st.title('Tienda de Souvenirs')
    st.markdown('Ingrese los parametros solicitados y luego presione "Iniciar Simulación".')
    # Parametros de la simulacion y visualizacion
    st.header('Parámetros de la simulación.')
    seed = st.number_input('Semilla para la generación de los número random', min_value=0, value=0)

    tiempo = st.number_input('Tiempo a simular (meses)', min_value=0, value=12)
    mostrar_desde_mes = st.number_input('Mes desde el cual se muestran las iteraciones', min_value=0, value=1, max_value=tiempo)
    cant_it_mostrar = tiempo + 1 if mostrar_desde_mes == 0 else (tiempo + 1 - mostrar_desde_mes)
    cant_it_mostrar = st.number_input('Cantidad de iteraciones a mostrar', min_value=0, max_value=(tiempo + 1) if mostrar_desde_mes == 0 else (tiempo + 1 - mostrar_desde_mes), value=cant_it_mostrar if cant_it_mostrar <= tiempo + 1 else tiempo , format='%d')
    st.header('Parámetros de costos y precio de venta')
    costo_docena = st.number_input('Costo promedio de la docena de souvenirs', min_value=0, value=45, format='%d')
    costo_inversion = st.number_input('Monto de la inversión inicial', min_value=0, value=8200, format='%d')
    total_cuotas_inversion = st.number_input('Cantidad de cuotas sin interés para el pago de la inversión', min_value=0, value=12, format='%d')
    precio_unid = st.number_input('Precio promedio de venta de los souvenirs por unidad', min_value=0, value=8, format='%d')

    st.header('Parámetros de compra de mercadería')
    stock_inicial = 0
    ## stock_inicial = st.number_input('Stock inicial', min_value=0, value=0, format='%d')
    min_compra = st.number_input('Cantidad mínima de docenas de souvenirs que se pueden comprar por mes', min_value=0, value=30, format='%d')
    max_compra = 40
    max_compra = st.number_input('Cantidad máxima de docenas de souvenirs que se pueden comprar por mes', min_value=min_compra, value= max_compra if min_compra < max_compra else min_compra + 20, format='%d' )
    
    # Parametros de tiempo de compra de ticket
    st.header('Probabilidades (%) de la demanda')
    dem_250 = st.number_input('Probabilidad de tener una demanda de 250 unidades (%):', min_value=0, max_value=100, value=30)
    dem_300 = st.number_input('Probabilidad de tener una demanda de 300 unidades (%):', min_value=0, max_value=100, value=5)
    dem_350 = st.number_input('Probabilidad de tener una demanda de 350 unidades (%):', min_value=0, max_value=100, value=20)
    dem_400 = st.number_input('Probabilidad de tener una demanda de 400 unidades (%):', min_value=0, max_value=100, value=15)
    dem_450 = st.number_input('Probabilidad de tener una demanda de 450 unidades (%):', min_value=0, max_value=100, value=10)
    dem_500 = st.number_input('Probabilidad de tener una demanda de 500 unidades (%):', min_value=0, max_value=100, value=10)
    dem_600 = st.number_input('Probabilidad de tener una demanda de 600 unidades (%):', min_value=0, max_value=100, value=5)
    dem_700 = st.number_input('Probabilidad de tener una demanda de 700 unidades (%):', min_value=0, max_value=100, value=5)


    prob = [dem_250,dem_300,dem_350,dem_400,dem_450,dem_500,dem_600,dem_700]

    prob_ok = validarProbabilidades(prob)

    simulacion_ok = st.button('Iniciar simulación')
    if prob_ok == False: 
        st.error("Verifique las probabilidades.")
    if simulacion_ok and prob_ok:

        prob_acum = probabilidadesAcumuladas(prob)
        prob_interv = crearIntervalos(prob)
        prob_demanda_data = {'Demanda': valores_demanda,
                    'Probabilidad (%)':  prob,
                    'Probabilidad': convertirPorcentajesADecimales(prob),
                    'Probabilidad acumuladas':prob_acum[1:],
                    'Intervalos': prob_interv
                    }
        df_prob = pd.DataFrame(prob_demanda_data, columns = ['Demanda', 'Probabilidad (%)','Probabilidad','Probabilidad acumuladas', 'Intervalos'])


        simulacion, promedio = Simulacion(seed,tiempo, stock_inicial, costo_docena, min_compra, max_compra, precio_unid, prob, mostrar_desde_mes, cant_it_mostrar, costo_inversion, total_cuotas_inversion)
    
        st.write('Probabilidades de la demanda')
        st.write(df_prob)
        st.write(simulacion)

        st.header('Resultados')
        st.write(f"Resultado neto mensual promedio para los primeros {tiempo} meses de funcionamiento de la tienda: ${promedio}")
        nombre = "resultado.xlsx"
        try:
            data ={"Simulacion":simulacion}
            generarExcel(data, nombre)

        except Exception as err:
            st.error("Ocurrió un error, recuerde cerrar el archivo Excel antes de simular. Error: " + str(err))


       
        
      
        

