import requests

class GoogleMapsAPI:
    def __init__(self, api_key):
        # Initializes the GoogleMapsAPI object with the provided API key
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/place"  # Base URL for the Google Maps Places API

    def search_hotel(self, hotel_name):
        # Sends a request to the Google Maps API to search for hotels based on the given name
        search_url = f"{self.base_url}/textsearch/json?query={hotel_name}&key={self.api_key}"
        response = requests.get(search_url).json()
        # Checks if the response was successful and returns the first result
        if response['status'] == 'OK' and response.get('results'):
            return response['results'][0]
        else:
            print(f"No results found or error: {response.get('status')}")
            return None

    def get_hotel_details(self, place_id):  # Constructs the URL for a text search request to find hotels by name
        details_url = f"{self.base_url}/details/json?place_id={place_id}&key={self.api_key}"
        response = requests.get(details_url).json()  # Sends the GET request and parses the JSON response
        if response['status'] == 'OK': # Checks if the response status is 'OK' and if there are any results
            return response.get('result', {})  # Returns the first result from the search
        else:
            print(f"Details error: {response.get('status')}") # Prints an error message if no results are found or there is an issue with the response
            return None

    def get_photo_url(self, photo_reference): # Constructs the URL to retrieve a photo using its reference
        if photo_reference:
            return f"{self.base_url}/photo?maxwidth=400&photo_reference={photo_reference}&key={self.api_key}"
        return None   # Returns None if the photo reference is not provided
