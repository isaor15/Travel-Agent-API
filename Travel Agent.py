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
            print("This country's official name is:", data["name"]["official"])
            print("The country is in the region of:", data["region"], "and subregion of:", data["subregion"])
            print("Around", data["population"], "people live here!")
            print("Here's a useful tidbit to remember! This country's code is:", data["cca2"])
            print("If you wanna buy anything, you'd use", currencies)
            print("You better start learning", languages,"!")
            print("Here the time zone is", timezones, "I sure hope you don't get jet-lagged!")

            weatherlink = f"https://api.open-meteo.com/v1/forecast?latitude=45.4643&longitude=9.1895&hourly=temperature_2m" 
            weather = requests.get(weatherlink)

            if weather.status_code == 200:
                wdata = weather.json()

                temp = wdata["hourly"]["temperature_2m"][0]

            print("The weather here seems nice! Its currently:", temp, "C")
            
        else:
            print("Oh no! We couldn't find that country :/")

def addtrip():

    country = input("What country are you adding to your trip?: ")
    mustknow = input("Are there any notes or special requirements we must know about? (Click ENTER if none): ")
    if mustknow == "":
          mustknow = "No notes or special requirements"

    days = int(input("How many days will you be visiting?: "))
    if days <= 0:
        print("Oh no!. It seems you can't have negative days, they must be greater than 0! Are you trying to avoid paying?")
        return
    
    getthere = input("What date will you be arrving? (DD/MM/YYYY format): ")
    specdays = getthere.split("/")
    if len(specdays) != 3:
        print("We can't accept that date format:(")
        return
    
    day = int(specdays[0])
    month = int(specdays[1])
    year = int(specdays[2])

    if day < 1 or day > 31:
        print("This isn't a REAl day, silly! There are only 31 days in a month!")
        return
    
    if month < 1 or month > 12:
        print("Oops, it seems like that is an invalid month:/")
        return
    
    if year < 2026:
        print("Oh no! That date is in the past! Use another year.")
        return

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
        print("Your beautiful hotel would be: $", hotel)
        print("Transportation would be: $", transport)
        print("The agency fee would be: $", agentfee)
        print("You're only $", total, "away from your dream trip!")

def saveplan():

    if len(trip) == 0:
        print("Oh no! There isn't a trip to save!")
        return

    client = input("Traveler, what is your name?: ")

    with open ("travelplan.txt", "a") as file:
        file.write("---Bella Vista Travel Agency---\n")
        file.write("Client: " + client + "\n")

        for place in trip:
            country = place["Country"]
            days = place["Days"]
            arrival = place["Arrival"]
            notes = place["Notes/requirements"]

            file.write("Destination: " + country + "\n")
            file.write("Duration of stay (days): " + str(days) + "\n") 
            file.write("Arrival date: " + arrival + "\n")
            file.write("Notes/requirements: " + notes + "\n")

    print("Your travel plan is ready and saved! Bon voyage!")
usermenu()