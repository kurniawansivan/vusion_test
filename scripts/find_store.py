import requests
import os

# Mengambil API Key dan storeId dari environment variables (GitHub Secrets)
api_key = os.getenv('VUSION_API_KEY')  # API Key dari secrets
storeId = os.getenv('VUSION_STORE_ID')  # storeId dari secrets

# Endpoint GET untuk mencari store berdasarkan ID
url = f"https://api-eu.vusion.io/vusion-cloud/v1/stores/{storeId}"

# Header untuk autentikasi menggunakan Ocp-Apim-Subscription-Key
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

# Mengirim GET request ke API untuk mencari store
try:
    response = requests.get(url, headers=headers, timeout=5)
    
    # Mengecek status response
    if response.status_code == 200:
        store_data = response.json()  # Mengambil data store dari response JSON
        print(f"Store ditemukan: {store_data}")
    else:
        print(f"Gagal mencari store. Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Terjadi error: {e}")
