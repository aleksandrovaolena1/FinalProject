import requests

class HotelInfo:  # A class to fetch detailed information about hotels using a provided API instance
    def __init__(self, api): # Initializes the HotelInfo object with an API instance
        self.api = api

    def fetch_hotel_info(self, hotel_name): # Fetches detailed information about a hotel based on its name
        hotel = self.api.search_hotel(hotel_name)  # Search for the hotel using the provided API instance
        if not hotel:
            return None # If no hotel is found, return None
        # Extract basic hotel information from the search results
        name = hotel.get('name')
        address = hotel.get('formatted_address')
        place_id = hotel.get('place_id')
        photo_reference = hotel['photos'][0]['photo_reference'] if 'photos' in hotel else None # Get the photo reference if available, otherwise set to None
        photo_url = self.api.get_photo_url(photo_reference)  # Generate a photo URL using the reference, if available
        # Retrieve detailed hotel information using the place_id
        details = self.api.get_hotel_details(place_id) # Get the hotel's description, or provide a default message if not available
        if details:
            description = details.get('editorial_summary', {}).get('overview', 'No description available.')
            reviews = details.get('reviews', []) # Retrieve the list of reviews (limit to the first three reviews)
            review_texts = [review['text'] for review in reviews[:1]]
            # Return the collected hotel data in a structured dictionary format
            return {
                "name": name,
                "address": address,
                "photo_url": photo_url, 
                "description": description,
                "reviews": review_texts 
            }
        return None