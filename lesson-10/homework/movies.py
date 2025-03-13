import requests
import random

def get_genres(bearer_token):
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    genres = response.json().get("genres", [])
    return {genre["name"].lower(): genre["id"] for genre in genres}

def get_movies_by_genre(bearer_token, genre_id):
    url = "https://api.themoviedb.org/3/discover/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    params = {
        "with_genres": genre_id,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": 1
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json().get("results", [])

def recommend_movie(bearer_token):
    genres = get_genres(bearer_token)
    print("Available genres:", ", ".join(genres.keys()))
    
    user_genre = input("Enter a movie genre: ").strip().lower()
    
    if user_genre in genres:
        genre_id = genres[user_genre]
        movies = get_movies_by_genre(bearer_token, genre_id)
        if movies:
            random_movie = random.choice(movies)
            print("\nRecommended Movie: ", random_movie['title'])
            print("Release Date: ", random_movie['release_date'])
            print("Rating: ", random_movie['vote_average'])
            print("Overview: ", random_movie['overview'])
        else:
            print("No movies found for this genre.")
    else:
        print("Invalid genre. Please try again.")

if __name__ == "__main__":
    BEARER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2NDQwN2U1ZTQyMTc1Y2ZiOGMwYTNmMWVkYmY0ZmY5MyIsIm5iZiI6MTc0MTg1ODE0MS42OCwic3ViIjoiNjdkMmE1NWQzMjVlNjJiM2QxNjA5YTk2Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.Yre8dcvGaLw-_IlsFJd1Xp1Xjk7aPpeXTLa686eO5eI"  # Replace with your actual TMDb Bearer Token
    recommend_movie(BEARER_TOKEN)
