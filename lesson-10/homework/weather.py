import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat=41.3123363&lon=69.2787079&appid=98ec3c43b4c208986a8e5e02c5ca57a4&units=metric"

lon_lat = "http://api.openweathermap.org/geo/1.0/direct?q=Tashkent&limit=5&appid=98ec3c43b4c208986a8e5e02c5ca57a4"

def get_temperature():
    all_posts = requests.get(BASE_URL)
    temperature = all_posts.json()["main"]["temp"]
    humidity = all_posts.json()["main"]["humidity"]
    return f"In Tashkent we have {temperature} C. and {humidity} humidity"

if __name__ == '__main__':
    post = get_temperature()
    print(post)