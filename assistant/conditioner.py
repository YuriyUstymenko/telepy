import requests
import json
import os
from dotenv import load_dotenv

# Конфигурация
URL = f"https://api.smartthings.com/v1/devices/{os.getenv('AIR_DEVICE_ID')}/commands"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('AIR_TOKEN')}",
    "Content-Type": "application/json"
}

def send_command(capability, command, arguments=[]):
    payload = [{
        "component": "main",
        "capability": capability,
        "command": command,
        "arguments": arguments
    }]
    response = requests.post(URL, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        print(f"Команда '{command}' успешно отправлена!")
    else:
        print(f"Ошибка {response.status_code}: {response.text}")

# --- ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ ---

# 1. Включить кондиционер
# send_command("switch", "on")

# 2. Выключить кондиционер
# send_command("switch", "off")

# 3. Установить температуру на 23 градуса
# send_command("thermostatCoolingSetpoint", "setCoolingSetpoint", [23.0])

# 4. Сменить режим (cool, heat, dry, wind, auto)
# send_command("airConditionerMode", "setAirConditionerMode", ["cool"])



# [
#     {
#         "component": "main",
#         "capability": "switch",
#         "command": "on",
#         "arguments": []
#     }
# ]