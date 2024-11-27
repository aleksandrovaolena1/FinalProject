import requests

class HotelFormatter:
    
    @staticmethod
    def format_hotel_info(hotel_info):
        reviews_text = "\n".join(
            [f"- {review}" for review in hotel_info['reviews']] 
            if hotel_info['reviews'] 
            else ["No reviews available."]
        )
        return f"""
        🏨 {hotel_info['name']}

        📍 Location: {hotel_info['address']}

        🖍 Description: {hotel_info['description']}

        Guest Reviews:
        {reviews_text}
        """
