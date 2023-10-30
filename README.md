# lab6_ds2500
Problem 4 (Calling API Functions)

Get yourself an API key from api.openweathermap.org and look into the “One Call API 3.0”. You get 1,000 free calls a day with your API key. Read through the documentation for the the current weather data at: https://openweathermap.org/current

Write a function that, given a latitude and longitude, returns a dictionary representing the current weather data at that location, in imperial units. 

Here are the specs:
Function name: get_weather_json
Parameters: lat (float), longitude (float), api key (string)
Returns: a dictionary of dictionaries, matching the JSON data described at the link above
