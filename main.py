import os
import requests
from app_config import UserInfo


user = UserInfo()

api_key = os.getenv(user.get_api())

base_url = 'http://api.weatherapi.com/v1'

response = requests.get(f'{base_url}/current.json?q=Plovdiv&key={user.get_api()}')
if response.ok:
    print(response.json())

else:
    print(f'Error: {response.status_code}')
