import requests
;0
valid_zones = [
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Asia/Shanghai"
] #list

def get_city_time(timezone, greeting_type="default"):#procedural abstraction & timezone and greeting_type are parameters
    url = f"https://timeapi.io/api/Time/current/zone?timeZone={timezone}"
    response = requests.get(url)

    if response.status_code != 200:
        return None, "Invalid time zone. Please try again."

    data = response.json()
    hour = data["hour"]

    if hour < 12:
        message = "Good morning!"
    elif hour < 18:
        message = "Good afternoon!"
    else:
        message = "Good evening!"
    #conditional

    if greeting_type == "friendly":
        message += " Hope you have a great day!" #uses second parameter to modify output

    return data, message #results/return values


print("Available Time Zones:")
for zone in valid_zones:
    print("-", zone) #loop/iteration

timezone = input("\nEnter a time zone from the list above: ") #input

time_data, greeting = get_city_time(timezone)#first function call

if time_data is None:
    print(greeting)
else:
    print("\nTime Zone:", time_data["timeZone"])
    print("Current Time:", f'{time_data["hour"]}:{time_data["minute"]}')
    print("Date:", f'{time_data["month"]}/{time_data["day"]}/{time_data["year"]}')
    print(greeting) #output  

# Second function call to show 2 function calls, 2 parameters, 2 results
timezone2 = "Europe/London"
time_data2, greeting2 = get_city_time(timezone2, greeting_type="friendly") #second function call

print("\n--- Second Time Zone Example ---")
print("Time Zone:", time_data2["timeZone"])
print("Current Time:", f'{time_data2["hour"]}:{time_data2["minute"]}')
print("Date:", f'{time_data2["month"]}/{time_data2["day"]}/{time_data2["year"]}')
print(greeting2) #output
