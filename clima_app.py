import requests
import streamlit as st

# Configuración de la API
API_KEY = "29c134056183f4e1334546ac7c20972c"  # Reemplaza con tu propia API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# Funciones de lógica
def obtener_clima(ciudad):
    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",  # Cambiar a 'imperial' para Fahrenheit
        "lang": "es",  # Opcional: Traduce la descripción del clima al español
    }

    respuesta = requests.get(BASE_URL, params=params)

    if respuesta.status_code == 200:
        return respuesta.json()
    return None


# Interfaz de usuario (Streamlit)
st.title("Aplicación de Pronóstico del Clima")

# Campo de entrada para la ciudad
ciudad = st.text_input("Ingresa el nombre de la ciudad:")

# Botón de acción
if st.button("Obtener Clima"):
    if ciudad:
        clima = obtener_clima(ciudad)

        if clima:
            # Mostrar información del clima
            st.success(f"Clima en {clima['name']}:")  # Usa el nombre oficial de la API
            st.write(f"**Temperatura:** {clima['main']['temp']} °C")
            st.write(f"**Condición:** {clima['weather'][0]['description']}")
            st.write(f"**Humedad:** {clima['main']['humidity']}%")
            st.write(f"**Viento:** {clima['wind']['speed']} m/s")
        else:
            st.error("Ciudad no encontrada, verifica el nombre.")
    else:
        st.warning("Por favor, ingresa un nombre de ciudad.")
