import requests

class TelegramBot:    # A class to interact with the Telegram Bot API for sending messages and photos
    def __init__(self, token): # Initializes the TelegramBot object with a bot token
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}" # Base URL for Telegram Bot API requests
        

    def send_photo_and_text(self, chat_id, photo_url, text): # Sends a photo and text to a specified Telegram chat
        max_caption_length = 1024 # The Telegram API limits captions to a maximum of 1024 characters
        if len(text) > max_caption_length: 
            text = text[:max_caption_length] # Сut off the text if it more than 1024 haracters

        file_response = requests.get(photo_url) # Fetch the photo content from the provided URL
        if file_response.status_code == 200: # Check if the photo was successfully retrieved
            files = {'photo': ('photo.jpg', file_response.content)}  # Prepare the photo as a file to send with the API request
            url = f"{self.base_url}/sendPhoto" # Endpoint for sending photos
            response = requests.post(url, data={'chat_id': chat_id, 'caption': text}, files=files)
            if response.status_code == 200: # Successfully sent the photo and text
                print("Photo and text successfully sent!")
            else:
                print(f"Error sending photo: {response.status_code}, {response.text}") # Handle errors from the Telegram API
        else:
            print(f"Error loading photo: {file_response.status_code}") # Handle errors when fetching the photo