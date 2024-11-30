from google_maps_api import GoogleMapsAPI
from hotel_info import HotelInfo
from telegram_bot import TelegramBot
from hotel_formatter import HotelFormatter

if __name__ == "__main__":
    api_key = "AIzaSyAnJsdwZB-3w0cf3semjoveDphyPMG7x6o" # API key for Google Maps
    telegram_token = "7570149338:AAHmQUYGwz7bbBmUXYFF0X7v_VeuORua7kA" # Telegram bot token
    chat_id = "-1002149787433" # Telegram chat ID

    api = GoogleMapsAPI(api_key)  # Initialize Google Maps API with the provided API key
    hotel_service = HotelInfo(api) # Create a HotelInfo instance to fetch hotel data
    telegram_bot = TelegramBot(telegram_token) # Initialize TelegramBot with the token

    hotel_name = input("Enter the name of the hotel: ") # Prompt to enter the name of a hotel
    hotel_info = hotel_service.fetch_hotel_info(hotel_name) # Fetch detailed information about the hotel

    if hotel_info:
        formatted_text = HotelFormatter.format_hotel_info(hotel_info) # Format the hotel information for readability
        print(f"Hotel information: \n{formatted_text}") # Print the formatted hotel information to the console

        if hotel_info['photo_url']:
            telegram_bot.send_photo_and_text(chat_id, hotel_info['photo_url'], formatted_text) # Check if the hotel has a photo URL and send the photo along with the formatted text to Telegram
    else:
        print("Failed to retrieve hotel information.") 
