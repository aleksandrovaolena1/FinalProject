# Final Project

Welcome to **Final Project**! This Python-based project aims to create an application that automates the search for hotel information using the Google Maps API and publishes the results to a Telegram channel. This solution will help quickly find detailed information about hotels, including photos and descriptions, addresses, and reviews, and share it with clients through a promotional Telegram channel.

## Features

### Hotel Search:
- Utilizes the Google Maps API to search for hotels by name.
- Returns detailed hotel information, including location, description, and user reviews.

### Detailed Hotel Information:
- Fetches comprehensive data about hotels, such as address, amenities, and ratings.
- Retrieves photos of the hotel to provide visual context.

### User Reviews Display:
- Extracts guest reviews and displays them alongside hotel details.
- If no reviews are available, shows a default message ("No reviews available").

### Telegram Integration:
- Sends formatted hotel information and photos directly to a promotional Telegram channel.
- Ensures easy sharing of hotel data with clients through an automated process.

### Formatted Output:
- Outputs hotel information in a well-structured, readable format with emojis for better visual appeal.
- Makes it easy for clients to quickly read and understand key hotel details.

### Interactive User Input:
- Prompts the user to enter the name of the hotel, allowing for quick and personalized searches.

## Project Structure

- **`main.py`**: The main entry point of the application. This file runs the core functionality of the project, where the Google Maps API is used to search for hotels and publish results to the Telegram channel.
- **`google_maps_api.py`**: Contains the `GoogleMapsAPI` class for interacting with the Google Maps API, allowing the search for hotels and retrieval of detailed information.
- **`hotel_info.py`**: Defines the `HotelInfo` class that handles the fetching of hotel data using the `GoogleMapsAPI` class.
- **`hotel_formatter.py`**: Includes the `HotelFormatter` class, which formats the hotel data into a readable and presentable format for output and sharing.
- **`telegram_bot.py`**: Contains the `TelegramBot` class, responsible for sending formatted hotel information and images to a specified Telegram channel.
- **`README.md`**: The documentation file that provides an overview of the project, its purpose, features, and instructions for setup and usage.

## 🛠️ Installation

Follow these steps to set up the project locally:

1. Clone the repo:
    ```bash
    git clone https://github.com/aleksandrovaolena1/FinalProject.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the project:
    ```bash
    python main.py
    ```

## 📈 Example

### Step 1: Run the Application
Run the `main.py` file:
```bash
python main.py
```
### Step 2: Input Example
Enter the name of the hotel when prompted:
Enter the name of the hotel: Hilton Garden Inn

### Step 3: Telegram Message
The application will send a formatted message to your Telegram channel with the hotel information, including photos and reviews:
![telegram](https://github.com/user-attachments/assets/9e9dea86-a2cf-477d-8b90-8f2e9c613597)






