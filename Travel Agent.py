import requests

def country_vis():
    country = input("What country would you like to visit?: ")
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        print("Ahh, I've found it. What a great country!")
        print(f"Here's some useful information about {country}")
        print("Capital:", data["capital"][0])
    else:
        print("Oh no! We couldn't find that country :/")

country_vis()