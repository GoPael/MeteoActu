import streamlit as st
import requests

def get_weather_data(city, api_key):
    """Récupère les données météorologiques de l'API OpenWeatherMap."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city},FR&appid={api_key}&units=metric&lang=fr"
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(data):
    """Affiche les données météorologiques dans l'application Streamlit."""
    if data["cod"] != 200:
        st.error("Impossible de récupérer les données météorologiques. Veuillez vérifier le nom de la ville.")
        return

    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    st.write(f"**{city}**")
    st.write(f"**Température :** {temp} °C")
    st.write(f"**Humidité :** {humidity} %")
    st.write(f"**Vitesse du vent :** {wind_speed} m/s")
    st.write(f"**Description :** {description.capitalize()}")

# Configuration de base de l'application Streamlit
st.title("Application Météo pour les Villes Françaises")

# Saisie utilisateur pour la ville
city_input = st.text_input("Entrez le nom d'une ville française :")

# Bouton pour déclencher la récupération des données météorologiques
if st.button("Obtenir les conditions météorologiques"):
    if not city_input:
        st.error("Veuillez entrer le nom d'une ville.")
    else:
        # Utilisez votre clé API personnelle d'OpenWeatherMap ici
        api_key ="75539700c717617792340109ccbe6e09"
        weather_data = get_weather_data(city_input, api_key)
        display_weather_data(weather_data)
