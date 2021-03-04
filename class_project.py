# A python project that relies on user input and an API to generate weather information 
# by city, or zip code. Uses the request libary and json. 
# by: Robert Sivadon
# for: CIS245 Jordan Moline
# due: 03-06-2021

import requests, json

key="a20c50fd7da5e71c2e6673f2aca5b279"
host="http://api.openweathermap.org/data/2.5/weather?"

# Welcome message.
print('\nWelcome to Python Weather Services!')

def zip_funct():
   # zip code funtion for when user wantes to search by zip code 
    u_zip=input('Enter a valid zip code: ') 
    print('\nConnecting...')
    full_url=f'{host}q={u_zip}&appid={key}&units=imperial' #the full url address for the request module using zip code
    returned=requests.get(full_url) #returns a response object   
    data=returned.json() #nested dictionary that contains data values to be printed from the response object

    if data["cod"] != "404": 
        # Checks for successful connection
        print(f"Connected to weather services for zip code: {u_zip}.")
        print_funct(data)
        ask_to_continue()
    else:
        print_funct(data) # if 404 is found, runs print function to check for "key error" that will run the except block located in main()

def city_funct():
    # City funtion for when user wantes to search by city 
    u_city=input('Enter city name: ').title() 
    print('\nConnecting...')
    full_url=f'{host}q={u_city}&appid={key}&units=imperial' # the full url address for the request module using city
    returned=requests.get(full_url) # returns a response object  
    data=returned.json() # nested dictionary that contains data values to be printed from the response object

    if data["cod"] != "404": 
        # Checks for successful connection
        print(f"\nConnected to {u_city} weather services! ")
        print_funct(data)
        ask_to_continue()
    else:
        print_funct(data) # if 404 is found, runs print function to check for "key error" that will run the except block located in main()

def both_funct():
    # function for a more accurate search result
    u_both=input("\nEnter the city name first, followed by the 2-letter country code (example: US for United States), then the zip code; all seperated by a comma: ")
    print(u_both)
    print('\nConnecting...')
    full_url=f'{host}q={u_both}&appid={key}&units=imperial' # the full url address for the request module using city
    r=requests.get(full_url)
    data=r.json()

    if data["cod"] != "404": 
        # Checks for successful connection
        print(f"\nConnected to {u_both} weather services! ")
        print_funct(data)
        ask_to_continue()
    else:
        print_funct(data) # if 404 is found, runs print function to check for "key error" that will run the except block located in main()
     
def print_funct(data):
    # takes information stored in data varible and stores them in specific varibles that will be printed
    description = data['weather'][0]['description']
    print(f'\tDescription: {description.title()}')

    convert_clouds(data)

    temp = data['main']['temp']
    print(f'\tCurrent temprature: {temp} degree fahrenheit')
    
    temp_max = data['main']['temp_max']
    print(f'\tHigh: {temp_max} degree fahrenheit')

    temp_min = data['main']['temp_min']
    print(f'\tLow: {temp_min} degree fahrenheit')

    feels_like = data['main']['feels_like']
    print(f'\tFeels like: {feels_like} degree fahrenheit')

    humidity = data['main']['humidity']
    print(f'\tHumidity: {humidity}%')

    pressure = data['main']['pressure']
    print(f'\tPressure: {pressure} hPa')

    wind = data['wind']['speed']
    print(f'\tWind Speed: {wind} mph\n')

def ask_to_continue():
    # Asks user if they want to search again.
    while True:
        search=input("Would you like to search again? type 'y' for Yes or 'n' for No: ").lower()
        if search == 'y' or search == 'yes':
            main()
            break
        elif search == 'n' or search == 'no':
            print('\nGood bye! Thank you for using Python weather services!')
            exit()
        else:
            print("\nError! Not a valid option please try again.\n")

def convert_clouds(data):
    # Converts percentage of clould cover to descriptive value.
    if data['clouds']['all'] < 10: # 0 - 9%
        print(f"\tCloud Coverage: {data['clouds']['all']}%")
        print("\t\tDay: Sunny")
        print("\t\tNight: Clear")

    elif data['clouds']['all'] < 20: # 10 - 19%
        print(f"\tCloud Coverage: {data['clouds']['all']}%")
        print("\t\tDay: Sunny to Mostly Sunny")
        print("\t\tNight: Fair")

    elif data['clouds']['all'] < 30: # 20 - 29%
        print(f"\tCloud Coverage: {data['clouds']['all']}%")
        print("\t\tDay: Mostly Sunny")
        print("\t\tNight: Mostly Fair")

    elif data['clouds']['all'] < 60: # 30 - 59%
        print(f"\tCloud Coverage: {data['clouds']['all']}%")
        print("\t\tDay: Partly Sunny")
        print("\t\tNight: Partly Cloudy")

    elif data['clouds']['all'] < 90: # 60 - 89% 
        print(f"\tCloud Coverage: {data['clouds']['all']}%")
        print("\t\tDay: Mostly Cloudy")
        print("\t\tNight: Mostly Cloudy")

    elif data['clouds']['all'] >= 90: # 90 - 100% 
        print(f"\tCloud Coverage: {data['clouds']['all']}%")
        print("\t\tDay: Cloudy")
        print("\t\tNight: Cloudy")

# Main function
def main():
    # Prompts user to search by city or zip code, checks input and runs appropriate function
    # sets conditional for user inputs, errors if user input is not city or zip
    # errors if city not found
    while True:
        user_selection = input("If you would like to search by city please, type 'city'"
        " if you perfer to search by zip code type 'zip'"
        "\nfor a comprehensive search type 'both' : ").lower()
        if user_selection == 'city':
            print('\nSearching by city name...')
            try:
                city_funct()
            except KeyError:
                print("\n---Error---\nConnention aborted, city not found. Please try again.\n")
        elif user_selection == 'zip':
            print('\nSearching by zip code...')
            try:
                zip_funct()
            except KeyError:
                print("\n---Error---\nConnention aborted, zip code not found. Please try again.\n")
        elif user_selection == 'both':
            try:
                both_funct()
            except KeyError:
                print("\n---Error---\nConnention aborted, city or zip code not found. Please try again.\n")
        else: 
            print("\nERROR! Search option is unavailable please search by 'city' or ' zip'.\n")        
main()