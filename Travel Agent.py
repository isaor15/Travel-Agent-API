import requests

trip = []

def usermenu():

    while True: 
        
        usermenu = input("Welcome to the Bella Vista Travel Agency! Let's set up your plan! Enter the corresponding number to begin: \n" \
        "1. Find your dream destination\n" 
        "2. Add a country to your trip\n"
        "3. Show trips\n"
        "4. Calculate budget\n"
        "5. Save your travel plan\n"
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
            break

        else:
            print("Oh no! That's not an option!")

def country_vis():
        
        country = input("What country have you been dying to visit?: ").title()
        url = f"https://restcountries.com/v3.1/name/{country}"
        response = requests.get(url)


        if response.status_code == 200:

            data = response.json()[0]

            languages = ", ".join(data["languages"].values())
            currencies = ", ".join(data["currencies"].keys())
            timezones = ", ".join(data["timezones"])

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

    tripinfo = ({
        "Country": country,
        "Days": days,
        "Arrival": getthere,
        "Notes/requirements": mustknow
    })

    trip.append(tripinfo)

    
    print(f"{country} has been added to your trip. How exciting!")
    print(country, "Amount of days:", days, "Arrival", getthere, "Notes:", mustknow)

def seetrip():

    if len(trip) == 0:
        print("No countries added to your trip yet!")   

    else:
        print("Your Travel Plan:")
        for place in trip:
            print(place["Country"], "-", place["Days"], "days")
            print("Arrival:", place["Arrival"])
            print("Notes/requirements: ", place["Notes/requirements"])

def calcbudg():

    if len(trip) == 0:
        print("There is no trip to calculate a budget for:(")

    else:
        alldays = 0

        for place in trip:
            alldays = alldays + place["Days"]
        
        hotel = alldays * 100
        transport = len(trip) * 70
        agentfee = 40

        total = hotel + transport + agentfee

        print("Here is your estimated budget for your dream destination!:")
        print("Your beautiful hotel would be: ", hotel)
        print("Transportation would be: ", transport)
        print("The agency fee would be: ", agentfee)
        print("You're only $", total, "away from your dream trip!")

def saveplan():

    if len(trip) == 0:
        print("Oh no! There isn't a trip to save!")
        return

    client = input("Traveler, what is your name?: ")

    with open ("travelplan.txt", "w") as file:
        file.write("---Bella Vista Travel Agency---\n")
        file.write("Client: " + client + "\n")

        for place in trip:
            country = place["Country"]
            days = place["Days"]
            arrival = place["Arrival"]
            notes = place["Notes/requirements"]

            file.write("Destination: " + country + "\n")
            file.write("Duration of stay: " + str(days) + "\n") 
            file.write("Arrival date: " + arrival + "\n")
            file.write("Notes/requirements: " + notes + "\n")

    print("Your travel plan is ready and saved! Bon voyage!")
usermenu()