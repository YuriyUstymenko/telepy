import json
import urllib.request
import urllib.error

def get_weather():
    # Строка запроса к бесплатному API Open-Meteo
    url = f"https://api.open-meteo.com/v1/forecast?latitude=50.43&longitude=30.45&current_weather=true"

    try:
        # Настройка заголовков, чтобы сервер не принял Python за спам-бота
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())

        current = data["current_weather"]
        temp = round(current["temperature"])
        wind = round(current["windspeed"])

        # ИСПРАВЛЕННЫЙ БЛОК ГРАММАТИКИ (проверка окончаний градусов)
        abs_temp = abs(temp)
        if abs_temp % 10 == 1 and abs_temp % 100 != 11:
            gradus_text = "градус"
        elif abs_temp % 10 in [2, 3, 4] and abs_temp % 100 not in [11, 12, 13, 14]:
            gradus_text = "градуса"
        else:
            gradus_text = "градусов"

        return f"Сейчас на улице примерно {temp} {gradus_text}. Скорость ветра {wind} метров в секунду."
        

    except urllib.error.URLError as e:
        print(f"[Ошибка сети]: Нет доступа к интернету или сайту. Детали: {e}")
        return "Мне не удалось подключиться к серверу погоды. Проверьте интернет соединение."
    except Exception as e:
        print(f"[Другая ошибка погоды]: {e}")
        return "Произошла ошибка при обработке данных погоды."
    
def get_weather_tomorrow():
    # Строка запроса к бесплатному API Open-Meteo
    url = f"https://api.open-meteo.com/v1/forecast?latitude=50.43&longitude=30.45&daily=temperature_2m_max,temperature_2m_min&timezone=auto&forecast_days=2"

    try:
        # Настройка заголовков, чтобы сервер не принял Python за спам-бота
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
        
        # Данные на завтра находятся под индексом 1 (индекс 0 — это сегодня)
        # Берем максимальную и минимальную температуру
        temp_max = round(data["daily"]["temperature_2m_max"][1])
        temp_min = round(data["daily"]["temperature_2m_min"][1])

        return f"Завтра ожидается от {temp_min} до {temp_max} градусов."        

    except urllib.error.URLError as e:
        print(f"[Ошибка сети]: Нет доступа к интернету или сайту. Детали: {e}")
        return "Мне не удалось подключиться к серверу погоды. Проверьте интернет соединение."
    except Exception as e:
        print(f"[Другая ошибка погоды]: {e}")
        return "Произошла ошибка при обработке данных погоды."    