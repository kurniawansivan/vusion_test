import requests
import os

# Mengambil API Key dan storeId dari environment variables (GitHub Secrets)
api_key = os.getenv('VUSION_API_KEY')  # API Key dari secrets
storeId = os.getenv('VUSION_STORE_ID')  # storeId dari secrets

# Endpoint POST untuk melakukan ping ke labels di store
url = f"https://api-eu.vusion.io/vusion-cloud/v1/stores/{storeId}/labels/ping"

# Header untuk autentikasi menggunakan API Key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Body request (ping biasanya tidak membutuhkan body, jadi bisa dikosongkan)
data = {}

# Mengirim POST request ke API untuk melakukan ping
try:
    response = requests.post(url, headers=headers, json=data, timeout=5)
    
    # Mengecek status response
    if response.status_code == 200:
        print(f"Ping berhasil ke store {storeId}.")
        print(f"Response Data: {response.json()}")
    else:
        print(f"Gagal melakukan ping. Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Terjadi error: {e}")
