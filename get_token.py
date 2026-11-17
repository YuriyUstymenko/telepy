import logging
import os
from dotenv import load_dotenv
from miio.integrations.vacuum.roborock.vacuum import RoborockVacuum

logging.basicConfig(level=logging.INFO)


ROOM_RED = 15 # ?
ROOM_BLUE = 16
ROOM_ORANGE = 17 # 

def main():
    print("Подключение к пылесосу напрямую...")
    try:
        # Инициализируем пылесос
        vacuum = RoborockVacuum(ip=os.getenv("ROBOROCK_DEVICE_IP"), token=os.getenv("ROBOROCK_DEVICE_TOKEN"))
        
        # Получаем текущее состояние
        # status = vacuum.status()
        # pprint.pprint(status.__dict__) 

        

        # привіт, я тут
        vacuum.send("find_me")


        # Или для просмотра вложенных деталей:
        # print(status.clean_details)
        # print("\n=== СТАТУС УСТРОЙСТВА ===")
        # print(f"Заряд батареи: {status.battery}%")
        # print(f"Режим работы: {status.state}")

        # Пример запуска уборки (раскомментируйте, чтобы запустить)
        # vacuum.start()
        # vacuum.send("app_start")
        # Поставить на паузу
        # vacuum.send("app_pause")
        # Вернуть на док-станцию (зарядку)
        # vacuum.send("app_charge")

        
        # Коды мощности (fan_power)
        # 101 — Quiet (Тихий)
        # 102 — Balanced (Сбалансированный / Стандартный)
        # 103 — Turbo (Турбо)104 — Max (Максимальный)
        # 105 — Max+ / Усиленный (доступен не на всех прошивках)        
        # vacuum.send("set_custom_mode", [104])

        # vacuum.send("app_segment_clean", [16])
        # vacuum.send("app_segment_clean", [17])


        # status_data = vacuum.send("get_status")
        # print(status_data)


    except Exception as e:
        print(f"Ошибка управления устройством: {e}")

if __name__ == "__main__":
    load_dotenv()
    main()