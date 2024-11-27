from google_maps_api import GoogleMapsAPI
from hotel_info import HotelInfo
from telegram_bot import TelegramBot
from hotel_formatter import HotelFormatter

if __name__ == "__main__":
    api_key = "AIzaSyAnJsdwZB-3w0cf3semjoveDphyPMG7x6o"
    telegram_token = "7570149338:AAHmQUYGwz7bbBmUXYFF0X7v_VeuORua7kA"
    chat_id = "-1002149787433"

    api = GoogleMapsAPI(api_key)
    hotel_service = HotelInfo(api)
    telegram_bot = TelegramBot(telegram_token)

    hotel_name = input("Введите название отеля: ")
    hotel_info = hotel_service.fetch_hotel_info(hotel_name)

    if hotel_info:
        formatted_text = HotelFormatter.format_hotel_info(hotel_info)
        print(f"Информация об отеле: \n{formatted_text}")

        if hotel_info['photo_url']:
            telegram_bot.send_photo_and_text(chat_id, hotel_info['photo_url'], formatted_text)
    else:
        print("Не удалось получить информацию об отеле.")
