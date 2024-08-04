import os
import random
import requests
from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import time

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
))

def get_weather(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {}

def get_weather_based_songs(condition):
    queries = [f"{condition} mood", f"{condition} songs", f"{condition} playlist"]
    query = random.choice(queries)  # Randomly pick a query for more variety
    try:
        results = sp.search(q=query, type='track', limit=6)
        return [
            {
                'name': track['name'],
                # 'artists': ', '.join([artist['name'] for artist in track['artists']])
                'artists': [artist['name'] for artist in track['artists']],  # Ensure proper formatting
                'spotify_link': f"https://open.spotify.com/track/{track['id']}",
                'youtube_id': get_youtube_id(track['name'])
            }
            for track in results['tracks']['items']
        ]
    except Exception as e:
        print(f"Error fetching weather-based songs: {e}")
        return []

def get_best_songs_by_singer(singer):
    try:
        results = sp.search(q='artist:' + singer, type='track', limit=6)
        return [
            {
                'name': track['name'],
                # 'artists': ', '.join([artist['name'] for artist in track['artists']]), 
                'artists': [artist['name'] for artist in track['artists']] ,# Ensure proper formatting
                'spotify_link': f"https://open.spotify.com/track/{track['id']}",
                'youtube_id': get_youtube_id(track['name'])
            }
            for track in results['tracks']['items']
        ]
    except Exception as e:
        print(f"Error fetching best songs by singer: {e}")
        return []

def get_recommended_songs(singer):
    query = f"{singer} related"
    try:
        results = sp.search(q=query, type='track', limit=6)
        return [
            {
                'name': track['name'],
                # 'artists': ', '.join([artist['name'] for artist in track['artists']])
                'artists': [artist['name'] for artist in track['artists']],  # Ensure proper formatting
                'spotify_link': f"https://open.spotify.com/track/{track['id']}",
                'youtube_id': get_youtube_id(track['name'])
            }
            for track in results['tracks']['items']
        ]
    except Exception as e:
        print(f"Error fetching recommended songs: {e}")
        return []

def get_youtube_id(song_name):
    try:
        query = f"{song_name} official"
        response = requests.get(
            f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={os.getenv('YOUTUBE_API_KEY')}"
        )
        results = response.json()
        if 'items' in results and results['items']:
            video_id = results['items'][0]['id']['videoId']
            print(f"Video ID: {video_id}")  # Debugging line
            return video_id
        else:
            print(f"No YouTube video found for {song_name}")
            return None
    except Exception as e:
        print(f"Error in get_youtube_id: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    city = request.form.get('city')
    singer = request.form.get('singer')
    
    # Fetch weather data
    weather_data = get_weather(city)
    if not weather_data:
        return render_template('error.html', message="Unable to fetch weather data.")
    
    weather_info = {
        'city': weather_data.get('name', 'Unknown'),
        'temperature': weather_data['main'].get('temp', 'N/A'),
        'condition': weather_data['weather'][0].get('description', 'N/A')
    }

    weather_based_songs = get_weather_based_songs(weather_info['condition'])
    best_songs = get_best_songs_by_singer(singer)
    recommended_songs = get_recommended_songs(singer)
    
    return render_template(
        'recommendations.html',
        weather_info=weather_info,
        weather_based_songs=weather_based_songs,
        best_songs=best_songs,
        recommended_songs=recommended_songs,
        singer=singer
    )

if __name__ == '__main__':
    app.run(debug=True)
