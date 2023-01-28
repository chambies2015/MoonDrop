import asyncio
import discord
from discord.ext import commands
import requests
import bot_token
import random

# client = discord.Client(intents=discord.Intents.all())

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

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


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
                sent_message = await message.channel.send(
                    "Invalid location. Please enter a valid 5-digit US zip code or city name.")
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

    elif message.content.startswith("!slots") and message.channel.id == 1068400883316052008:

        slot_options = ["<:binoculars:939664762491514940>",
                        "<a:cocka:939664777838469141>",
                        "<a:CopiumTime:939664788995321946>",
                        "<:Corpa:939664800483508245>",
                        "<a:cvPaste:939664810927325215>",
                        "<a:donkWalk:939664828044292136>",
                        "<:FeelsAyayaMan:939664828157546516>",
                        "<a:donkRun:939664828174319757>",
                        "<:farnsU:939664828245631037>",
                        "<:farnsWoah:939664828564373535>",
                        "<:oldge:939664911867478017>",
                        "<:NotSure:939664911892611073>",
                        "<:pepeStepBro:939664911905198191>",
                        "<:strongge:939664911984914433>",
                        "<a:susge:939664912056197150>",
                        "<:peepoRage:939664912056205332>",
                        "<:suskayge:939664912454668318>",
                        "<:WeirdPaper:939664912458854500>",
                        "<:PepeA:939664912521773076>",
                        "<:scaredge:939664912580485140>",
                        "<a:JesusBeGolfin:939664912840531978>",
                        "<a:nerdge:939664913180274739>",
                        "<a:libido:939664913444503583>",
                        "<a:peepersD:939664913759100998>",
                        "<a:GlizzyL:939664913775853590>",
                        "<a:smogeintherain:939664914346283070>",
                        "<a:PEPSICLE:939664914748940308>",
                        "<:bidness:939965404158263328>",
                        "<a:cumDetected:940049736491216896>",
                        "<:EZ:940367669201362954>",
                        "<a:BoneZone:940370338410270821>",
                        "<a:hoSway:940387997512253440>",
                        "<a:angeryping:941579591863124039>",
                        "<a:Anone:941579593003962458>",
                        "<:Docpa:941579593616326656>",
                        "<a:marioRun:941579594308390983>",
                        "<a:peepoShy:941579594883022878>",
                        "<a:ppHop:941579595184996372>",
                        "<:copege:941579595524759612>",
                        "<a:hyperNodders:941579596313280582>",
                        "<:Hyukchiha:941579596313288744>",
                        "<:lulWut:941579596334256158>",
                        "<:Madge:941579596392960030>",
                        "<:POGGERS:941579596598505483>",
                        "<:Oldge:941579596778836038>",
                        "<:pepeStop:941579596942442526>",
                        "<:Grumpge:941579597688995841>",
                        "<:Okayge:941579598041329674>",
                        "<a:peepoPunch:941579598162984960>",
                        "<a:sadJam:941579598196518923>",
                        "<:pogO:941579598381076520>",
                        "<a:peepoWave:941579598481727538>",
                        "<a:peepoLeave:941579598506897448>",
                        "<a:YAPPERS:941579599165419581>",
                        "<a:NOPERS:941579599383494656>",
                        "<a:cumTime:941579599995867186>",
                        "<a:peepoArrive:941579600574681128>",
                        "<a:peepoT:941579600620830740>",
                        "<a:vegetaraining:941579601031856128>",
                        "<a:borpaItalian:941579601048633345>",
                        "<a:borpaTalk:941579601119952906>",
                        "<a:PepeHmm:941579601384198224>",
                        "<a:BOOBIES:941579601719750676>",
                        "<a:dankHackermans:941579601820385291>",
                        "<a:boomies:941579603682689024>",
                        "<:Gasm:945139193334616094>",
                        "<:PotL:948628546086113361>",
                        "<:AYAYARRR:948635232905596938>",
                        "<a:pepeJAM:952943523244703774>",
                        "<:cropping:953391943281414175>",
                        "<:propain:955188992796684298>",
                        "<a:madgeClap:964640093107265536>",
                        "<a:madgeLate:964640724270329886>",
                        "<a:peepoFine:964641588695425107>",
                        "<a:monkaGIGAftRobertDowneyJr:969671522732109834>",
                        "<a:BorpaChatting:986743565675814952>",
                        "<:smadgebusiness:994375165507010570>",
                        "<:peepoPonderingBeans:996964477780115486>",
                        "<:Suswokege:1009206863423873094>",
                        "<a:borpaSpin:1015069879663067177>",
                        "<:peepoPonderingPOB:1021167542712139846>",
                        "<:handshakge:1027413028234330192>",
                        "<a:rasadgan:1031726958087782442>",
                        "<:kreto:1037818306884808777>",
                        "<:Cereal:1040021766631870566>",
                        "<a:joel:1040449738509656094>",
                        "<:looking:1040449739562418216>",
                        "<:ben:1043656813763100743>"]
        slot_result = [random.choice(slot_options) for i in range(9)]

        emote1 = slot_result[0]
        emote2 = slot_result[1]
        emote3 = slot_result[2] + "\n"
        emote4 = slot_result[3]
        emote5 = slot_result[4]
        emote6 = slot_result[5] + "\n"
        emote7 = slot_result[6]
        emote8 = slot_result[7]
        emote9 = slot_result[8]

        if emote1 == emote2 == emote3 or emote4 == emote5 == emote6 or emote7 == emote8 == emote9 \
                or emote1 == emote4 == emote7 or emote2 == emote5 == emote8 or emote3 == emote6 == emote9 \
                or emote1 == emote5 == emote9 or emote3 == emote5 == emote7:

            embed = discord.Embed(title="Slot Machine Results: WINNER!", color=0xf1c40f)
            embed.add_field(name="Reel 1", value=emote1)
            embed.add_field(name="Reel 2", value=emote2)
            embed.add_field(name="Reel 3", value=emote3)
            embed.add_field(name="", value=emote4)
            embed.add_field(name="", value=emote5)
            embed.add_field(name="", value=emote6)
            embed.add_field(name="", value=emote7)
            embed.add_field(name="", value=emote8)
            embed.add_field(name="", value=emote9)
            author = message.author.name
            embed.set_footer(text=author)
            await message.channel.send(embed=embed)
            await message.channel.send("@everyone " + message.author.name + " has won slots!")
        elif emote1 == emote2 == emote3 == emote4 == emote5 == emote6 == emote7 == emote8 == emote9:
            embed = discord.Embed(title="Slot Machine Results: GIGA WINNER!!!!!!!!!!", color=0xe74c3c)
            embed.description = "GIGA WINNER!"
            embed.add_field(name="Reel 1", value=emote1)
            embed.add_field(name="Reel 2", value=emote2)
            embed.add_field(name="Reel 3", value=emote3)
            embed.add_field(name="", value=emote4)
            embed.add_field(name="", value=emote5)
            embed.add_field(name="", value=emote6)
            embed.add_field(name="", value=emote7)
            embed.add_field(name="", value=emote8)
            embed.add_field(name="", value=emote9)
            author = message.author.name
            embed.set_footer(text=author)
            await message.channel.send(embed=embed)
            await message.channel.send("@everyone " + message.author.name + " has won slots!")
        else:
            embed = discord.Embed(title="Slot Machine Results", color=0x3498db)
            embed.add_field(name="Reel 1", value=emote1)
            embed.add_field(name="Reel 2", value=emote2)
            embed.add_field(name="Reel 3", value=emote3)
            embed.add_field(name="", value=emote4)
            embed.add_field(name="", value=emote5)
            embed.add_field(name="", value=emote6)
            embed.add_field(name="", value=emote7)
            embed.add_field(name="", value=emote8)
            embed.add_field(name="", value=emote9)
            author = message.author.name
            odds = (len(slot_options) ** 3) / 9
            odds = round(odds, 0)
            embed.set_footer(text="Roller: " + author + "\nOdds of winning are: 1 in " + str(odds))
            sent_message = await message.channel.send(embed=embed)
            await asyncio.sleep(5)

    # Code to get all emotes in the respective server where !emotes is used.
    # You will need to change the slot_options variable for each discord it's used in.
    # elif message.content.startswith("!emotes"):
    #     print(f'Logged in as {client.user}')
    #     for guild in client.guilds:
    #         print(f'{guild.name} has {len(guild.emojis)} emotes.')
    #         for emoji in guild.emojis:
    #             print(f'{emoji.name}: {emoji.id}')

    elif message.content.startswith("!commands") and message.channel.id == 1068400883316052008:
        await message.channel.send('!slots\n!blackjack')

    elif message.content.startswith("!blackjack"):
        author = message.author

        def calculate_hand(hand):
            score = 0
            aces = 0
            for card in hand:
                if card in ['J', 'Q', 'K']:
                    score += 10
                elif card == 'A':
                    score += 11
                    aces += 1
                else:
                    score += int(card)

            while score > 21 and aces > 0:
                score -= 10
                aces -= 1
            return score

        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        player_hand = [random.choice(cards), random.choice(cards)]
        dealer_hand = [random.choice(cards), random.choice(cards)]

        player_score = calculate_hand(player_hand)
        dealer_score = calculate_hand(dealer_hand)

        embed = discord.Embed(title=f"{message.author.name}'s Blackjack", color=0x3498db)
        embed.add_field(name="Your hand: ", value=f'{player_hand} ({player_score}) ')
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=f"{message.author.name}'s Blackjack", color=0x3498db)
        embed.add_field(name="Dealer\'s hand: ", value=f'{dealer_hand[0]} ***')
        await message.channel.send(embed=embed)

        if message.author == author:
            while player_score < 21:
                response = await client.wait_for('message', check=lambda message: message.author == author)
                if response.content.lower() == 'hit':
                    player_hand.append(random.choice(cards))
                    player_score = calculate_hand(player_hand)
                    await message.channel.send(f'Your hand: {player_hand} ({player_score})')
                elif response.content.lower() == 'stand':
                    break
                else:
                    await message.channel.send('Invalid command. Please enter "hit" or "stand".')

            if player_score > 21:
                await message.channel.send('Bust! You lose.')
            else:
                while dealer_score < 17:
                    dealer_hand.append(random.choice(cards))
                    dealer_score = calculate_hand(dealer_hand)

                embed = discord.Embed(title=f"{message.author.name}'s Blackjack", color=0x3498db)
                embed.add_field(name="Dealer\'s hand: ", value=f'{dealer_hand} ({dealer_score})')
                await message.channel.send(embed=embed)

                if dealer_score > 21:
                    await message.channel.send('Dealer busts! You win.')
                elif player_score > dealer_score:
                    await message.channel.send('You win!')
                elif player_score < dealer_score:
                    await message.channel.send('You lose.')
                else:
                    await message.channel.send('It\'s a tie!')
        else:
            message.channel.send("Game already in progress, please wait your turn to play.")

    def calculate_hand(hand):
        score = 0
        aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                score += 10
            elif card == 'A':
                score += 11
                aces += 1
            else:
                score += int(card)

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1


client.run(bot_token.bot_token)
