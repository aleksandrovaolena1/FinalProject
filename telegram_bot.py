import requests

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        

    def send_photo_and_text(self, chat_id, photo_url, text):
        max_caption_length = 1024
        if len(text) > max_caption_length:
            text = text[:max_caption_length]

        file_response = requests.get(photo_url)
        if file_response.status_code == 200:
            files = {'photo': ('photo.jpg', file_response.content)}
            url = f"{self.base_url}/sendPhoto"
            response = requests.post(url, data={'chat_id': chat_id, 'caption': text}, files=files)
            if response.status_code == 200:
                print("Photo and text successfully sent!")
            else:
                print(f"Error sending photo: {response.status_code}, {response.text}")
        else:
            print(f"Error loading photo: {file_response.status_code}")