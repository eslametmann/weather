import requests

API_KEY = "1cf3f5c282c6e81aa6a0cfc229fc80b2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = "   weather : "+data["weather"][0]["main"]
    temp = "  temp : " + str(round(data["main"]["temp"] - 273.15))+"celsius"

    with open("  weather.json","a") as f:
        f.write(f"city : {city}")
        f.write(weather)
        f.write(temp)
        f.write("_________________")
        f.write("\n")
    print(weather)
    print(temp)
else:
    print("an error occured!")