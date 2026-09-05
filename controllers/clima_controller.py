import requests

def obtener_clima(ciudad="Lima", api_key = "992907bc503ed64b72750961b1dc4dc3"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        clima = {
            "ciudad": ciudad,
            "temperatura": data["main"]["temp"],
            "descripcion": data["weather"][0]["description"],
            "humedad": data["main"]["humidity"],
        }
        return clima
    except Exception as e:
        return {"error":str(e)}