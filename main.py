import time
import requests
import os
from dotenv import load_dotenv
import json
import socket
# Tối ưu hóa ghi file
def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write('[\n')
        file.write(',\n'.join(data))
        file.write('\n]')
        file.close()

# Định nghĩa hàm get_config
def get_config(url, social_type, file_path):
    params = {'social_type': social_type}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        result = response.json()
        formatted_results = [json.dumps(item, indent=2) for item in result['data']['results']]
        write_file(file_path, formatted_results)
    else:
        print(f"API request failed with status code: {response.status_code}")

if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("API_GET_CONFIG")
    facebook = os.getenv("FACEBOOK")
    tiktok = os.getenv("TIKTOK")
    youtube = os.getenv("YOUTUBE")
    path_host = os.getenv("path_host")

    file_path_facebook = os.getenv("path_file_facebook")
    file_path_tiktok = os.getenv("path_file_tiktok")
    file_path_youtube =  os.getenv("path_file_youtube")
    server = os.getenv("ADDRESS_SERVER")
    port = os.getenv("PORT")
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = server
        client_socket.connect((host, int(port)))
        try:
            message = client_socket.recv(1024)
            if message is not None or message != '':
                message = message.decode()
                if int(message) == 0:
                        get_config(url, facebook, file_path_facebook)
                        time.sleep(3)
                if int(message) == 1:
                        get_config(url, tiktok, file_path_tiktok)
                        time.sleep(3)
                if int(message) == 2:
                        get_config(url, youtube, file_path_youtube)
                        time.sleep(3)
        except Exception as e:
            print(f"Lỗi: {e}")
            continue
