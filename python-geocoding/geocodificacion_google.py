import pandas as pd
import requests
from config import API_KEY

def obtener_direccion_google(lat, lon):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={API_KEY}&language=es"
    try:
        response = requests.get(url).json()
        if response['status'] == 'OK' and len(response['results']) > 0:
            return response['results'][0]['formatted_address']
        return "No encontrada"
    except Exception as e:
        return f"Error: {e}"

def main():
    df = pd.read_csv("direcciones.csv")
    df["direccion_google"] = df.apply(lambda fila: obtener_direccion_google(fila["latitud"], fila["longitud"]), axis=1)
    df.to_csv("direcciones_con_google.csv", index=False)
    print("Geocodificación completada.")

if __name__ == "__main__":
    main()
