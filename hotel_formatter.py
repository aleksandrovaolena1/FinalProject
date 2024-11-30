class HotelFormatter:
    
    @staticmethod
    def format_hotel_info(hotel_info):  # Formats hotel information into a readable string with emojis for better visual presentation
        
        review_text = (
            f"⭐ {hotel_info['reviews'][0]}"  # Format the first review with a star icon
            if hotel_info['reviews'] 
            else "No reviews available."
        )
        
        return f""" 
🏨 {hotel_info['name']}

📍 Location: {hotel_info['address']}

📝 Description: {hotel_info['description']}

🛎️ Guest Review: {review_text}
""" 
