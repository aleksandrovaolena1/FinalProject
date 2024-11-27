import requests

class HotelInfo:
    def __init__(self, api):
        self.api = api

    def fetch_hotel_info(self, hotel_name):
        hotel = self.api.search_hotel(hotel_name)
        if not hotel:
            return None

        name = hotel.get('name')
        address = hotel.get('formatted_address')
        place_id = hotel.get('place_id')
        photo_reference = hotel['photos'][0]['photo_reference'] if 'photos' in hotel else None
        photo_url = self.api.get_photo_url(photo_reference)

        details = self.api.get_hotel_details(place_id)
        if details:
            description = details.get('editorial_summary', {}).get('overview', 'No description available.')
            reviews = details.get('reviews', [])
            review_texts = [review['text'] for review in reviews[:3]]

            return {
                "name": name,
                "address": address,
                "photo_url": photo_url,
                "description": description,
                "reviews": review_texts
            }
        return None
