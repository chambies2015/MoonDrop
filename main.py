import asyncio
import discord
import requests
import bot_token

client = discord.Client(intents=discord.Intents.all())

WEATHER_EMOTES = {
    "clear sky": "☀️",
    "few clouds": "⛅️",
    "scattered clouds": "☁️",
    "broken clouds": "☁️",
    "shower rain": "🌧️",
    "rain": "🌧️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
    "overcast": "☁",
    "overcast clouds": "☁",
    "light snow": "❄"
}


@client.event
async def on_message(message):
    if message.content.startswith("!weather"):

        location = message.content[9:]
        api_key = bot_token.open_weather_token

        if location.isnumeric() and len(location) == 5:
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?zip={location},us&appid={api_key}"

        else:
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

        weather_data = requests.get(weather_url).json()

        if 'message' in weather_data:
            if weather_data['message'] == 'city not found':
                sent_message = await message.channel.send("Invalid location. Please enter a valid 5-digit US zip code or city name.")
                await asyncio.sleep(10)
                await message.delete()
                await sent_message.delete()
                return
        temp = weather_data["main"]["temp"]
        temp_fahrenheit = (temp - 273.15) * 9 / 5 + 32
        description = weather_data["weather"][0]["description"]
        emote = WEATHER_EMOTES.get(description, "🌦️")
        embed = discord.Embed(title="Weather Information", color=0x00ff00)
        embed.add_field(name="Location", value=location)
        embed.add_field(name="Description", value=f"{emote} {description}")
        embed.add_field(name="Temperature (F)", value=f"{temp_fahrenheit:.2f}")
        embed.set_footer(text="This message will be deleted in 10 seconds.")
        sent_message = await message.channel.send(embed=embed)
        await asyncio.sleep(10)
        await message.delete()
        await sent_message.delete()


client.run(bot_token.bot_token)
