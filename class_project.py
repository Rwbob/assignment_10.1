

import requests, json

key="a20c50fd7da5e71c2e6673f2aca5b279"
host="http://api.openweathermap.org/data/2.5/weather?"

# Welcome message.
print('\nWelcome to Python Weather Services!')

def zip_funct():
   #zip code funtion for when user wantes to search by zip code 
    u_zip=input('Enter a U.S. valid Zip Code: ') 
    print('\nConnecting...')
    full_url=f'{host}q={u_zip},us&appid={key}&units=imperial' #the full url address for the request module using zip code
    returned=requests.get(full_url) #returns a response object   
    data=returned.json() #nested dictionary that contains data values to be printed from the response object

    if data["cod"] != "404": 
        #Checks for successful connection
        print(f"Connected to weather services for zip code: {u_zip}")
        print_funct(data)
    else:
        print_funct(data) #if 404 is found, runs print function to check for "key error" that will run the except code in the try block located in main()

    search=input("Would you like to search again? type 'y' for Yes or 'n' for No: ").lower()
    if search == 'y' or search == 'yes':
        main()
    if search == 'n' or search == 'no':
        print('Good bye! Thank you for using Python weather services')
        exit()


def city_funct():
    #City funtion for when user wantes to search by city 
    u_city=input('Enter city name: ').title() 
    print('\nConnecting...')
    full_url=f'{host}q={u_city}&appid={key}&units=imperial' # the full url address for the request module using city
    returned=requests.get(full_url) #returns a response object  
    data=returned.json() #nested dictionary that contains data values to be printed from the response object

    if data["cod"] != "404": 
        #Checks for successful connection
        print(f"\nConnected to {u_city} weather services! ")
        print_funct(data)
    else:
        print_funct(data) #if 404 is found, runs print function to check for "key error" that will run the except code in the try block located in main()
    
    search=input("Would you like to search again? type 'y' for Yes or 'n' for No: ").lower()
    if search == 'y' or search == 'yes':
        main()
    if search == 'n' or search == 'no':
        print('Good bye! Thank you for using Python weather services')
        exit()
    

def print_funct(data):
    #takes information stored in data varible and stores them in specific varibles that will be printed
    description = data['weather'][0]['description']
    print(f'\tDescription: {description.title()}')

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

    
# Main function
def main():
    # Prompts user to search by city or zip code, checks input and runs appropriate function
    # sets conditional for user inputs, errors if user input is not city or zip
    # errors if city not found
    while True:
        user_selection = input("If you would like to search by city please, type 'city'"
        " if you perfer to search by zip code type 'zip': ").lower()
        if user_selection == 'city':
            try:
                print('\nSearching by city name...')
                city_funct()
            except KeyError:
                print("\n---Error---\nConnention aborted, city not found. Please try again!\n")
                city_funct()
        elif user_selection == 'zip':
            try:
                print('\nSearching by zip code...')
                zip_funct()
            except KeyError:
                print("\n---Error---\nConnention aborted, zip code not found. Please try again!\n")
                zip_funct()
        else: 
            print("\nERROR! Search option is unavailable please search by 'city' or ' zip'.\n")        
main()
