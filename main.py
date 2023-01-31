import asyncio
import sqlite3
import discord
from discord.ext import commands
import bot_token
import random

gambling_slots_odds = False
free_gambling = True
slots_buy_in = 20
blackjack_buy_in = 10
flip_buy_in = 10
gambling_channels = [809544965386272792]
slotWinAmount = 2000
gigaSlotWinAmount = 100000

full_slot_options = ["<:binoculars:939664762491514940>", "<a:cocka:939664777838469141>",
                     "<a:CopiumTime:939664788995321946>", "<:Corpa:939664800483508245>",
                     "<a:cvPaste:939664810927325215>", "<a:donkWalk:939664828044292136>",
                     "<:FeelsAyayaMan:939664828157546516>", "<a:donkRun:939664828174319757>",
                     "<:farnsU:939664828245631037>", "<:farnsWoah:939664828564373535>",
                     "<:oldge:939664911867478017>", "<:NotSure:939664911892611073>",
                     "<:pepeStepBro:939664911905198191>", "<:strongge:939664911984914433>",
                     "<a:susge:939664912056197150>", "<:peepoRage:939664912056205332>",
                     "<:suskayge:939664912454668318>", "<:WeirdPaper:939664912458854500>",
                     "<:PepeA:939664912521773076>", "<:scaredge:939664912580485140>",
                     "<a:JesusBeGolfin:939664912840531978>", "<a:nerdge:939664913180274739>",
                     "<a:libido:939664913444503583>", "<a:peepersD:939664913759100998>",
                     "<a:GlizzyL:939664913775853590>", "<a:smogeintherain:939664914346283070>",
                     "<a:PEPSICLE:939664914748940308>", "<:bidness:939965404158263328>",
                     "<a:cumDetected:940049736491216896>", "<:EZ:940367669201362954>",
                     "<a:BoneZone:940370338410270821>", "<a:hoSway:940387997512253440>",
                     "<a:angeryping:941579591863124039>", "<a:Anone:941579593003962458>",
                     "<:Docpa:941579593616326656>", "<a:marioRun:941579594308390983>",
                     "<a:peepoShy:941579594883022878>", "<a:ppHop:941579595184996372>",
                     "<:copege:941579595524759612>", "<a:hyperNodders:941579596313280582>",
                     "<:Hyukchiha:941579596313288744>", "<:lulWut:941579596334256158>",
                     "<:Madge:941579596392960030>", "<:POGGERS:941579596598505483>",
                     "<:Oldge:941579596778836038>", "<:pepeStop:941579596942442526>",
                     "<:Grumpge:941579597688995841>", "<:Okayge:941579598041329674>",
                     "<a:peepoPunch:941579598162984960>", "<a:sadJam:941579598196518923>",
                     "<:pogO:941579598381076520>", "<a:peepoWave:941579598481727538>",
                     "<a:peepoLeave:941579598506897448>",
                     "<a:YAPPERS:941579599165419581>", "<a:NOPERS:941579599383494656>",
                     "<a:cumTime:941579599995867186>", "<a:peepoArrive:941579600574681128>",
                     "<a:peepoT:941579600620830740>", "<a:vegetaraining:941579601031856128>",
                     "<a:borpaItalian:941579601048633345>", "<a:borpaTalk:941579601119952906>",
                     "<a:PepeHmm:941579601384198224>", "<a:BOOBIES:941579601719750676>",
                     "<a:dankHackermans:941579601820385291>", "<a:boomies:941579603682689024>",
                     "<:Gasm:945139193334616094>", "<:PotL:948628546086113361>",
                     "<:AYAYARRR:948635232905596938>", "<a:pepeJAM:952943523244703774>",
                     "<:cropping:953391943281414175>", "<:propain:955188992796684298>",
                     "<a:madgeClap:964640093107265536>", "<a:madgeLate:964640724270329886>",
                     "<a:peepoFine:964641588695425107>", "<a:monkaGIGAftRobertDowneyJr:969671522732109834>",
                     "<a:BorpaChatting:986743565675814952>", "<:smadgebusiness:994375165507010570>",
                     "<:peepoPonderingBeans:996964477780115486>", "<:Suswokege:1009206863423873094>",
                     "<a:borpaSpin:1015069879663067177>", "<:peepoPonderingPOB:1021167542712139846>",
                     "<:handshakge:1027413028234330192>", "<a:rasadgan:1031726958087782442>",
                     "<:kreto:1037818306884808777>", "<:Cereal:1040021766631870566>",
                     "<a:joel:1040449738509656094>", "<:looking:1040449739562418216>",
                     "<:ben:1043656813763100743>"]

reduced_slot_options = ["<a:cumDetected:940049736491216896>", "<:EZ:940367669201362954>",
                        "<a:BoneZone:940370338410270821>", "<a:hoSway:940387997512253440>",
                        "<a:marioRun:941579594308390983>",
                        "<a:peepoShy:941579594883022878>", "<a:ppHop:941579595184996372>",
                        "<:copege:941579595524759612>", "<:lulWut:941579596334256158>",
                        "<:Madge:941579596392960030>", "<:POGGERS:941579596598505483>",
                        "<:Okayge:941579598041329674>",
                        "<:pogO:941579598381076520>", "<a:peepoWave:941579598481727538>",
                        "<a:YAPPERS:941579599165419581>", "<a:NOPERS:941579599383494656>",
                        "<a:peepoT:941579600620830740>", "<a:vegetaraining:941579601031856128>",
                        "<a:BOOBIES:941579601719750676>", "<a:boomies:941579603682689024>",
                        "<:Gasm:945139193334616094>", "<:PotL:948628546086113361>",
                        "<:AYAYARRR:948635232905596938>", "<a:monkaGIGAftRobertDowneyJr:969671522732109834>",
                        "<:peepoPonderingBeans:996964477780115486>", "<a:borpaSpin:1015069879663067177>",
                        "<:handshakge:1027413028234330192>", "<a:rasadgan:1031726958087782442>",
                        "<:kreto:1037818306884808777>", "<:Cereal:1040021766631870566>",
                        "<a:joel:1040449738509656094>", "<:ben:1043656813763100743>"]

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    conn = sqlite3.connect("MoonDropCasino.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS ChipTracker (id INTEGER PRIMARY KEY, chips INTEGER)"
    )
    conn.commit()
    conn.close()


@client.event
async def on_message(message):
    if message.author != client.user:
        global gambling_slots_odds
        global full_slot_options
        global reduced_slot_options
        global free_gambling
        global slots_buy_in
        global blackjack_buy_in

        conn = sqlite3.connect("MoonDropCasino.db")
        c = conn.cursor()
        c.execute("SELECT id FROM ChipTracker")
        sqlResults = c.fetchall()
        listOfMembers = []
        # check if user has an account in the casino database. If not, create one for them and give them starting chips.
        for member in sqlResults:
            listOfMembers.append(int(member[0]))
        memberID = message.author.id
        if memberID not in listOfMembers and message.channel.id in gambling_channels:
            c.execute(f"INSERT INTO ChipTracker (id, chips) VALUES ({message.author.id}, 5000)")
            conn.commit()

        # switching between max and reduced emotes in slots.
        if message.content.startswith("!max") and message.author.id == 179025046872784896:
            gambling_slots_odds = True
            embed = discord.Embed(title="Slots emotes increased to max!", color=0x00ff00)
            await message.channel.send(embed=embed)
        if message.content.startswith("!reduced") and message.author.id == 179025046872784896:
            gambling_slots_odds = False
            embed = discord.Embed(title="Slots emotes decreased!", color=0x00ff00)
            await message.channel.send(embed=embed)

        # slots command
        elif message.content.startswith("!slots") and message.channel.id in gambling_channels:
            userChips = getUserChips(message.author.id)

            if userChips < slots_buy_in:
                embed = discord.Embed(title="Not enough chips to use slots!", color=0x00ff00)
                await message.channel.send(embed=embed)
            else:

                if gambling_slots_odds is True:
                    slot_result = [random.choice(full_slot_options) for i in range(9)]
                else:
                    slot_result = [random.choice(reduced_slot_options) for i in range(9)]

                emote1 = slot_result[0]
                emote2 = slot_result[1]
                emote3 = slot_result[2]
                emote4 = slot_result[3]
                emote5 = slot_result[4]
                emote6 = slot_result[5]
                emote7 = slot_result[6]
                emote8 = slot_result[7]
                emote9 = slot_result[8]

                if emote1 == emote2 == emote3 or emote4 == emote5 == emote6 or emote7 == emote8 == emote9 \
                        or emote1 == emote4 == emote7 or emote2 == emote5 == emote8 or emote3 == emote6 == emote9 \
                        or emote1 == emote5 == emote9 or emote3 == emote5 == emote7:

                    embed = discord.Embed(title="Slot Machine Results: 🎉🎉 WINNER! 🎉🎉", color=0xf1c40f)
                    embed.add_field(name="Reel 1", value=emote1)
                    embed.add_field(name="Reel 2", value=emote2)
                    embed.add_field(name="Reel 3", value=emote3)
                    embed.add_field(name="", value='\n', inline=False)
                    embed.add_field(name="", value=emote4)
                    embed.add_field(name="", value=emote5)
                    embed.add_field(name="", value=emote6)
                    embed.add_field(name="", value='\n', inline=False)
                    embed.add_field(name="", value=emote7)
                    embed.add_field(name="", value=emote8)
                    embed.add_field(name="", value=emote9)
                    author = message.author.name
                    if gambling_slots_odds:
                        odds = (len(full_slot_options) ** 3) / 8
                        odds = round(odds, 0)
                    else:
                        odds = (len(reduced_slot_options) ** 3) / 8
                        odds = round(odds, 0)
                    embed.set_footer(text="Roller: " + author + "\nOdds of winning are: 1 in " + str(odds) + "\n"
                                                                                                             f"You won {str(slotWinAmount)} chips!")
                    await message.channel.send(embed=embed)
                    addChips(message.author.id, slotWinAmount)
                elif emote1 == emote2 == emote3 == emote4 == emote5 == emote6 == emote7 == emote8 == emote9:
                    embed = discord.Embed(title="Slot Machine Results: 🎉🎉 GIGA WINNER! 🎉🎉", color=0xe74c3c)
                    embed.description = "GIGA WINNER!"
                    embed.add_field(name="Reel 1", value=emote1)
                    embed.add_field(name="Reel 2", value=emote2)
                    embed.add_field(name="Reel 3", value=emote3)
                    embed.add_field(name="", value='\n', inline=False)
                    embed.add_field(name="", value=emote4)
                    embed.add_field(name="", value=emote5)
                    embed.add_field(name="", value=emote6)
                    embed.add_field(name="", value='\n', inline=False)
                    embed.add_field(name="", value=emote7)
                    embed.add_field(name="", value=emote8)
                    embed.add_field(name="", value=emote9)
                    author = message.author.name
                    if gambling_slots_odds:
                        odds = (len(full_slot_options) ** 3) / 8
                        odds = round(odds, 0)
                    else:
                        odds = (len(reduced_slot_options) ** 3) / 8
                        odds = round(odds, 0)
                    embed.set_footer(text="Roller: " + author + "\nOdds of winning are: 1 in " + str(odds) + "\n"
                                                                                                             f"You won {str(gigaSlotWinAmount)} chips!")
                    await message.channel.send(embed=embed)
                    addChips(message.author.id, gigaSlotWinAmount)
                else:
                    embed = discord.Embed(title="Slot Machine Results", color=0x3498db)
                    embed.add_field(name="Reel 1", value=emote1)
                    embed.add_field(name="Reel 2", value=emote2)
                    embed.add_field(name="Reel 3", value=emote3)
                    embed.add_field(name="", value='\n', inline=False)
                    embed.add_field(name="", value=emote4)
                    embed.add_field(name="", value=emote5)
                    embed.add_field(name="", value=emote6)
                    embed.add_field(name="", value='\n', inline=False)
                    embed.add_field(name="", value=emote7)
                    embed.add_field(name="", value=emote8)
                    embed.add_field(name="", value=emote9)
                    author = message.author.name
                    if gambling_slots_odds:
                        odds = (len(full_slot_options) ** 3) / 8
                        odds = round(odds, 0)
                    else:
                        odds = (len(reduced_slot_options) ** 3) / 8
                        odds = round(odds, 0)
                    embed.set_footer(text="Roller: " + author + "\nOdds of winning are: 1 in " + str(odds) + f"\nYou lost"
                                                                                                             f" {slots_buy_in} chips.")
                    subChips(message.author.id, slots_buy_in)
                    await message.channel.send(embed=embed)

        elif message.content.startswith("!commands") and message.channel.id in gambling_channels:
            await message.channel.send('!slots\n!blackjack\n!commands\n!balance\n!flip\n!buyins\n!leaderboard')

        elif message.content.startswith("!blackjack") and message.channel.id in gambling_channels:
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
                    embed = discord.Embed(title='You lose.', color=0x3498db)
                    embed.set_footer(text=f"You lost {blackjack_buy_in} chips.")
                    await message.channel.send(embed=embed)
                    subChips(message.author.id, blackjack_buy_in)
                else:
                    while dealer_score < 17:
                        dealer_hand.append(random.choice(cards))
                        dealer_score = calculate_hand(dealer_hand)

                    embed = discord.Embed(title=f"{message.author.name}'s Blackjack", color=0x3498db)
                    embed.add_field(name="Dealer\'s hand: ", value=f'{dealer_hand} ({dealer_score})')
                    await message.channel.send(embed=embed)

                    if dealer_score > 21:
                        embed = discord.Embed(title='Dealer busts! You win.', color=0x3498db)
                        embed.set_footer(text=f"You won {blackjack_buy_in * 2} chips.")
                        await message.channel.send(embed=embed)
                        addChips(message.author.id, blackjack_buy_in)
                    elif player_score > dealer_score:
                        embed = discord.Embed(title='You win!', color=0x3498db)
                        embed.set_footer(text=f"You won {blackjack_buy_in * 2} chips.")
                        await message.channel.send(embed=embed)
                        addChips(message.author.id, blackjack_buy_in)
                    elif player_score < dealer_score:
                        embed = discord.Embed(title='You lose.', color=0x3498db)
                        embed.set_footer(text=f"You lost {blackjack_buy_in} chips.")
                        await message.channel.send(embed=embed)
                        subChips(message.author.id, blackjack_buy_in)
                    else:
                        embed = discord.Embed(title='It\'s a push!', color=0x3498db)
                        await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title="Game already in progress, please wait your turn to play.", color=0x3498db)
                await message.channel.send(embed=embed)

        elif message.content.startswith("!flip") and message.channel.id in gambling_channels:
            coin = [0, 1]
            flippedCoin = random.choice(coin)
            if flippedCoin == 0:
                embed = discord.Embed(title="You won the flip!", color=0x00ff00)
                embed.set_footer(text=f"You won {flip_buy_in * 2} chips.")
                await message.channel.send(embed=embed)
                addChips(message.author.id, flip_buy_in)
            else:
                embed = discord.Embed(title="You lost the flip!", color=0x00ff00)
                embed.set_footer(text=f"You lost {flip_buy_in} chips.")
                await message.channel.send(embed=embed)
                subChips(message.author.id, flip_buy_in)

        elif message.content.startswith("!balance") and message.channel.id in gambling_channels:
            userBalance = getUserChips(message.author.id)
            embed = discord.Embed(title=f"Your chip balance is: {userBalance} chips.", color=0x00ff00)
            await message.channel.send(embed=embed)

        elif message.content.startswith("!buyins") and message.channel.id in gambling_channels:
            embed = discord.Embed(title=currentBuyIns(), color=0x3498db)
            await message.channel.send(embed=embed)

        elif message.content.startswith("!leaderboard") and message.channel.id in gambling_channels:
            conn = sqlite3.connect("MoonDropCasino.db")
            c = conn.cursor()
            c.execute("SELECT id, chips FROM ChipTracker order by chips desc")
            queryResult = c.fetchall()
            embed = discord.Embed(title="Current Leaderboard:", color=0xf1c40f)
            rank = 1
            for result in queryResult:
                user = await client.fetch_user(result[0])
                embed.add_field(name=f"#{str(rank)}: {user}", value=f"{result[1]}")
                embed.add_field(name="", value='\n', inline=False)
                rank += 1
            await message.channel.send(embed=embed)

            conn.close()

            # Code to get all emotes in the respective server where !emotes is used.

        # You will need to change the slot_options variable for each discord it's used in.
        # elif message.content.startswith("!emotes"):
        #     print(f'Logged in as {client.user}')
        #     for guild in client.guilds:
        #         print(f'{guild.name} has {len(guild.emojis)} emotes.')
        #         for emoji in guild.emojis:
        #             print(f'{emoji.name}: {emoji.id}')

        conn.close()


def currentBuyIns():
    buyIns = f"Slots: {slots_buy_in} chips\n Blackjack: {blackjack_buy_in} chips\n Flip: {flip_buy_in} chips"
    return buyIns


def getUserChips(memberID):
    conn = sqlite3.connect("MoonDropCasino.db")
    c = conn.cursor()
    c.execute(f"SELECT chips FROM ChipTracker where id={memberID}")
    queryResult = c.fetchall()
    totalUserChips = []
    for result in queryResult:
        totalUserChips.append(int(result[0]))
    totalUserChips = totalUserChips[0]
    conn.close()
    return totalUserChips


def addChips(memberID, chipsToBeAdded):
    conn = sqlite3.connect("MoonDropCasino.db")
    c = conn.cursor()
    c.execute(f"SELECT chips FROM ChipTracker where id={memberID}")
    queryResult = c.fetchall()
    totalUserChips = []
    for result in queryResult:
        totalUserChips.append(int(result[0]))
    totalUserChips = totalUserChips[0]
    newChipTotal = totalUserChips + chipsToBeAdded
    c.execute(f"UPDATE ChipTracker SET chips={newChipTotal} where id={memberID}")
    conn.commit()
    conn.close()


def subChips(memberID, chipsToBeSubbed):
    conn = sqlite3.connect("MoonDropCasino.db")
    c = conn.cursor()
    c.execute(f"SELECT chips FROM ChipTracker where id={memberID}")
    queryResult = c.fetchall()
    totalUserChips = []
    for result in queryResult:
        totalUserChips.append(int(result[0]))
    totalUserChips = totalUserChips[0]
    newChipTotal = totalUserChips - chipsToBeSubbed
    c.execute(f"UPDATE ChipTracker SET chips={newChipTotal} where id={memberID}")
    conn.commit()
    conn.close()


client.run(bot_token.bot_token)
