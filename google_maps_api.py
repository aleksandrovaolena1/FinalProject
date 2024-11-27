import requests

class GoogleMapsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/place"

    def search_hotel(self, hotel_name):
        search_url = f"{self.base_url}/textsearch/json?query={hotel_name}&key={self.api_key}"
        response = requests.get(search_url).json()
        if response['status'] == 'OK' and response.get('results'):
            return response['results'][0]
        else:
            print(f"No results found or error: {response.get('status')}")
            return None

    def get_hotel_details(self, place_id):
        details_url = f"{self.base_url}/details/json?place_id={place_id}&key={self.api_key}"
        response = requests.get(details_url).json()
        if response['status'] == 'OK':
            return response.get('result', {})
        else:
            print(f"Details error: {response.get('status')}")
            return None

    def get_photo_url(self, photo_reference):
        if photo_reference:
            return f"{self.base_url}/photo?maxwidth=400&photo_reference={photo_reference}&key={self.api_key}"
        return None
