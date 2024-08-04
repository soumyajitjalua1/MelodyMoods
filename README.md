# MelodyMoods

## Overview

The Weather-Based Music Recommendation System is a Flask-based web application that provides users with music recommendations based on the current weather conditions of a specified city. The app integrates weather data from the OpenWeather API and music data from the Spotify API. Users can also get recommendations based on a selected singer, which enhances their listening experience by tailoring song choices to both the weather and their personal tastes.

## Features

- **Weather-Based Song Recommendations**: Get music suggestions that match the current weather conditions in your city.
- **Best Songs by Singer**: Find top songs by your favorite singers.
- **Recommended Songs**: Discover related songs based on the singer you selected.
- **YouTube Integration**: Listen to the songs directly on Spotify or watch the music videos on YouTube.
- **Dynamic Background**: The background image changes according to the current weather (sunny, rainy, cloudy, snowy).

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **APIs**: OpenWeather API, Spotify API, YouTube Data API
- **Deployment**: AWS

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/weather-based-music-system.git
    cd weather-based-music-system
    ```

2. **Set up the virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables**:
   Create a `.env` file in the root directory and add your API keys:
    ```env
    SPOTIFY_CLIENT_ID=your_spotify_client_id
    SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
    OPENWEATHER_API_KEY=your_openweather_api_key
    YOUTUBE_API_KEY=your_youtube_api_key
    SECRET_KEY=your_secret_key
    ```

5. **Run the Flask application**:
    ```bash
    flask run
    ```

6. **Visit the app in your browser**:
   Open `http://127.0.0.1:5000/` in your browser to start using the app.

## Usage

1. **Enter City Name**: On the main page, enter the name of your city to get the current weather.
2. **Enter Singer's Name**: Optionally, you can enter the name of a singer to get their best songs.
3. **Get Recommendations**: Click the "Get Recommendations" button to see the weather-based song list, the best songs by the singer, and recommended songs.
4. **Listen/Watch Songs**: Click on the links to listen on Spotify or watch on YouTube.

## Project Structure
weather-based-music-system/
│
├── app.py # Main application script
├── .env # Environment variables
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── static/
│ ├── styles.css # Custom CSS
│ └── images/ # Background images for different weather conditions
├── templates/
│ ├── index.html # Homepage template
│ └── recommendations.html # Recommendations page template
└── .gitignore # Git ignore file


## API References

- **[OpenWeather API](https://openweathermap.org/api)**: Provides the current weather data.
- **[Spotify API](https://developer.spotify.com/documentation/web-api/)**: Retrieves song data and provides Spotify links.
- **[YouTube Data API](https://developers.google.com/youtube/v3)**: Fetches YouTube video IDs for the songs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request. Contributions, issues, and feature requests are welcome!

## Contact

For any questions or feedback, feel free to reach out at Soumyajitjalua@gmail.com.

