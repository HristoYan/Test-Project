# import logging
import os
from loguru import logger
import requests
from app_config import UserInfo

# logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
# logger = logging.getLogger(__name__)


user = UserInfo()

api_key = os.getenv(user.get_api())

base_url = 'http://api.weatherapi.com/v1'

logger.info('Making a get request to the API')
response = requests.get(f'{base_url}/current.json?q=Plovdiv&key={user.get_api()}1')
if response.ok:
    print(response.json())

else:
    if response.status_code == 403:
        logger.error(f'Check your API key: {response.status_code}')
    print(f'Error: {response.status_code}')
