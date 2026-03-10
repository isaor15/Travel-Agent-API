import requests

trip = []

def usermenu():
    while True: 
        
        usermenu = input("Welcome to the Bella Vista Travel Agency! Let's set up your plan! Enter the corresponding number to begin\n" \
        "1. Find you dream destination\n " 
        "2. Add a country to your trip\n "
        "3. Show trips\n " \
        "4. Calculate budget\n " \
        "5. Save your travel plan\n" \
        "6. Exit\n")
        
        if usermenu == "1":
            country_vis()

        elif usermenu == "2":
            addtrip()

        elif usermenu == "3":
            seetrip()

        elif usermenu == "4":
            calcbudg()

        elif usermenu == "5":
            saveplan()

        elif usermenu == "6":
            print("Thank you for visiting Bella Vista Travel Agency! Come back next time for your dream vacation!")

        else:
            print("Oh no! That's not an option!")

def country_vis():
        
        country = input("What country have you been dying to visit?: ").title()
        url = f"https://restcountries.com/v3.1/name/{country}"
        response = requests.get(url)


        if response.status_code == 200:

            data = response.json()[0]

            languages = ",".join(data["languages"].values())
            currencies = ",".join(data["currencies"].keys())
            timezones = ",".join(data["timezones"])

            print("Ahh, I've found it. What a great country!")
            print(f"Here's some useful information about {country}")

            #you gotta know this stuff
            print("This beautiful country's capital is:", data["capital"][0])
            print("This country's official name is", data["name"]["official"])
            print("The region this country is in the", data["region"])
            print("Around", data["population"], "people live here!")
            print("If you wanna buy anything, you'd use", currencies)
            print("You better start learning", languages, "!")
            print("I sure hope you don't get jet-lagged. here the time zone is", timezones)
        else:
            print("Oh no! We couldn't find that country :/")

def addtrip():
     country = input("What country are you adding to your trip?: ")
     days = int(input("How many days will you be visiting?: "))
     getthere = input("What date will you be arrving at? (DD/MM/YYYY format): ")
     mustknow = input("Are there any notes or special requirements we must know about? (Click ENTER if none): ")
     if mustknow == "":
          mustknow = "No notes or special requiremens"

def seetrip():
     pass

def calcbudg():
     pass

def saveplan():
     pass


usermenu()