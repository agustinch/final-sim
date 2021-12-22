import streamlit as st
import pandas as pd
from Soporte.Utils import valores_demanda

def LoadPage():
    st.title("Examen final Simulación")
    st.markdown("Agustín Chiavassa - Legajo 76255")

    st.header("Ejercicio 10: Tienda souvenirs.")
    st.write("Una empresa desea invertir en una pequeña tienda de souvenirs. Requiere de una inversión " + 
    "inicial de $ 8200 para comprar los bienes de uso necesarios para su funcionamiento y que " +
"pagara con tarjeta naranja en 12 cuotas sin interés durante los meses 1 al 12. " +
"La mercadería será comprada mensualmente a un promedio de $45 la docena en cantidades " +
"de 30 a 50 docenas mensuales, dependiendo de la demanda del mes anterior (compra la " +
"misma cantidad del mes anterior, como mínimo 30 y como máximo 50 docenas). " + 
"Tiene una demanda aleatoria y según las investigaciones realizadas, puede asumir los " +
"siguientes valores aleatorios:")
    probabilidades = pd.DataFrame({"Unidades Demandadas x Mes": valores_demanda, "Probabilidad de presentación": [0.30, 0.05,0.20,0.15,0.10, 0.10, 0.10,0.10]},columns=["Unidades Demandadas x Mes","Probabilidad de presentación"])
    st.table(probabilidades)

    st.header("Parámetros configurables")
    
    
    st.subheader('Parametros de simulación.')
    st.write("🔵 Semilla para la generación de los número random")
    st.write("🔵 Tiempo a simular (meses)")
    st.write("🔵 Mes desde el cual se muestran las iteraciones")
    st.write("🔵 Cantidad de iteraciones a mostrar")

    st.subheader("Parámetros de costos y precio de venta")
    st.write("🔵 Costo promedio de la docena de souvenirs")
    st.write("🔵 Monto de la inversión inicial")
    st.write("🔵 Cantidad de cuotas sin interés para el pago de la inversión")
    st.write("🔵 Precio promedio de venta de los souvenirs por unidad")



    st.subheader("Parametros de compra de mercadería")
    st.write("🔵 Cantidad mínima de docenas de souvenirs que se pueden comprar por mes")
    st.write("🔵 Cantidad máxima de docenas de souvenirs que se pueden comprar por mes")
    
    st.subheader("Probabilidades de la demanda")
    st.write("🔵 Se pueden configurar las probabilidades para los siguientes valores de demanda en unidades: " + ", ".join(str(d) for d in valores_demanda))



