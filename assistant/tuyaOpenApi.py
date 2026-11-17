import time
import os
from dotenv import load_dotenv
from tuya_connector import TuyaOpenAPI


load_dotenv()

ACCESS_ID = os.getenv("TUYA_ACCESS_ID")
ACCESS_KEY = os.getenv("TUYA_ACCESS_KEY")
API_ENDPOINT = os.getenv("TUYA_API_ENDPOINT")
DEVICE_ID = os.getenv("TUYA_DEVICE_ID")

openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Включаем розетку (если в отладке был код 'switch', замените 'switch_1' на 'switch')
print("Включаю...")
openapi.post(
    f"/v1.0/iot-03/devices/{DEVICE_ID}/commands",
    {"commands": [{"code": "switch_1", "value": True}]},
)

time.sleep(3)

# Выключаем розетку
print("Выключаю...")
openapi.post(
    f"/v1.0/iot-03/devices/{DEVICE_ID}/commands",
    {"commands": [{"code": "switch_1", "value": False}]},
)