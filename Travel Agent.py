import requests

def country_vis():
    country = input("What country would you like to visit?: ").upper()
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        print("Ahh, I've found it. What a great country!")
        print(f"Here's some useful information about {country}")
        #you gotta know this stuff
        print("This beautiful country's capital is:", data["capital"][0])
        print("This country's official name is", data["name"]["official"])
        print("The region this country is in the", data["region"])
        print("Around", data["population"], "people live here!")
        print("If you wanna buy anything, you'd use", data["currency"])
        print("You better start learning", data["languages"],"!")
        print("I sure hope you don't get jet-lagged. here the time zone is", data["timezones"])
    else:
        print("Oh no! We couldn't find that country :/")

country_vis()