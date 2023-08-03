import requests

def send_post_request():
    # Define the JSON data
    json_data = {
        "sensors": {
            "sensorData": [
                {
                    "info": "<sensor info>",
                    "data": "<new sensor data>"
                }
            ]
        }
    }

    # Replace '<your_key>' and '<your_board_key>' with your actual API key and board key
    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor0=1&info1=GPIO18"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)

    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO19"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)
    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO28"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)

    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO29"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)
    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO14"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)

    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO15"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)
    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO8"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)

    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO9"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)
    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO7"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)

    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO16"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)
    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO13"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)

    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO4"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)

    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO5"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)

    url = "https://consentiuminc.onrender.com/api/board/update/?key=3a41a18d4a83451da385f9ab2d69a5d2&boardkey=c47dacc93180e0d9&sensor1=1&info1=GPIO2"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=json_data, headers=headers)
        print("POST Request Status Code:", response.status_code)
        print("POST Request Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making POST request:", e)
if __name__ == '__main__':
    send_post_request()
