import requests

def get_all_timezones(): #procedural abstraction
    url = "https://timeapi.io/api/TimeZone/AvailableTimeZones"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    return response.json() #list of all time zones


def get_city_time(timezone): #procedural abstraction & parameter
    url = f"https://timeapi.io/api/Time/current/zone?timeZone={timezone}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json() #result


all_timezones = get_all_timezones() #function call


timezone = input("Enter ANY valid time zone (example: America/New_York): ") #input

if timezone not in all_timezones: #conditional
    print("Invalid time zone.")
else:
    time_data = get_city_time(timezone) #function call

if time_data is None:
    print("Error retrieving time.")
else:
    print("\nTime Zone:", time_data["timeZone"])
    print("Current Time:", f'{time_data["hour"]}:{time_data["minute"]}')
    print("Date:", f'{time_data["month"]}/{time_data["day"]}/{time_data["year"]}')