import requests

try:
    # Request ISS position
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()

    # Extract fields
    timestamp = data['timestamp']
    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']

    url = f"https://script.google.com/macros/s/AKfycbxinoyKQzRelTlVp3U7hhJx2vrQoCwuOi1T9WAmjNVCGaiJQBDwtBmvyjBR52Qa-LeZ6g/exec?Longitude={longitude}&Latitude={latitude}"

    response = requests.get(url, timeout=10)
    print("Status:", response.status_code)
    print("Response:", response.text)
    print(f"Saved: {timestamp}, {longitude}, {latitude}")

    response.close()
except Exception as e:
    print(f"Error: {e}")

