import requests
url = "http://127.0.0.1:8000/productos"

# Hacer la solicitud GET
response = requests.get(url)

# Verificar el código de respuesta
print(response.status_code, "-- respuesta:", response.text)
