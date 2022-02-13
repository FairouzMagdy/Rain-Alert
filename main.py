import requests
import os
from twilio.rest import Client

lat = -13.445720
lon = -49.152618
APIkey = os.environ.get("OWM_API_KEY")
account_sid = "AC41709b817779f6d9a94c8893537e1a31"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": APIkey,
    "exclude": "daily,current,minutely",
    "units": "metric"
}
endpoint = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False
for hour_data in weather_slice:
    ID = hour_data["weather"][0]['id']
    if ID < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain, remember to bring an umbrella",
        from_="TwilioNumber",
        to="Any_Number"
    )
    print(message.status)
