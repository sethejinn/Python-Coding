import requests

API_KEY = "TU_API_KEY"  # Consigue una API Key en https://openweathermap.org/api
URL_BASE = "http://api.openweathermap.org/data/2.5/weather"
def obtener_clima(ciudad):
    params = {"q": ciudad, "appid": API_KEY, "units": "metric", "lang": "es"}
    respuesta = requests.get(URL_BASE, params=params)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        print(f"El clima en {ciudad} es: {descripcion}, con {temp}°C.")
    else:
        print("No se pudo obtener el clima. Revisa la ciudad o la API Key.")
if __name__ == "__main__":
    ciudad = input("Introduce el nombre de la ciudad: ")
    obtener_clima(ciudad)
