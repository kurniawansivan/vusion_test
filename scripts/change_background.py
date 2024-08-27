import requests
import os

# Mengambil API Key, storeId, dan deviceId dari environment variables (GitHub Secrets)
api_key = os.getenv('VUSION_API_KEY')  # API Key dari secrets
storeId = os.getenv('VUSION_STORE_ID')  # storeId dari secrets
deviceId = os.getenv('VUSION_DEVICE_ID')  # deviceId dari secrets

# Endpoint POST untuk mengganti background di device
url = f"https://eu-api.vusionrail.com/v1/stores/{storeId}/devices/{deviceId}/background"

# Header untuk autentikasi menggunakan Ocp-Apim-Subscription-Key
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

# Data yang akan dikirim untuk mengganti background (menggunakan template DONE dan konten DONE.jpg)
data = {
    "template": "DONE",
    "content": {
        "image": "DONE.jpg",
        "aisle": "acid",
        "section": "shampoo"
    }
}

# Mengirim POST request ke API untuk mengganti background
try:
    response = requests.post(url, headers=headers, json=data, timeout=10)
    
    # Mengecek status response
    if response.status_code == 200:
        print(f"Background berhasil diganti dengan template DONE dan konten DONE.jpg.")
        print(f"Response Data: {response.json()}")
    else:
        print(f"Gagal mengganti background. Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Terjadi error: {e}")
