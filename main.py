# Faust - The Discord Bot
# By Abdullah Mustafa
# Created November 11th, 2021

import datetime
import json
import os
import random
import sys
import time
from io import StringIO

import discord
import jokelist
import praw
import requests
import textblocks
import prayer
import wolframalpha
from googlesearch import search
from PIL import Image, ImageFilter
from server import keep_alive

client = discord.Client(intents=discord.Intents.default())

TEAL = discord.Colour.teal()
GREEN = discord.Colour.green()

insults = [
    "disgusting oaf",
    "beef-witted foot licker",
    "rump-fed filthy rogue",
    "puking pox-marked codpiece",
    "obscene earth-vexing lewdster",
    "pestilent decayed foot-licker",
    "pathetic excuse for a human being",
    "maple-syrup-bottle doing hippo",
]

meme_buttons = {
    "🍭",
    "📩",
    "❌",
}

adjectives = [
    "my Emperor",
    "my King",
    "Supreme Leader",
    "my Lord",
    "my Führer",
    "thy Sovereign",
    "my Overlord",
    "my liege",
]

scary_subs = ["LetsNotMeet", "NoSleep"]
scary_stories = []

oldsub = "memes"
all_subs = []
reddit = praw.Reddit(
    client_id="HXzLlgUpGmSB4qUGKsa9Vw",
    client_secret="gOLh7a8pdW8-kYKIMm4wPwjRMn9I9g",
    username="BlissfulBroccoli",
    password=os.environ["reddit_pass"],
    user_agent="Faust123",
    check_for_async=False,
)


def read():
    global badwords
    with open("badwords.json") as f:
        badwords = json.load(f)


def rewrite():
    global badwords
    with open("badwords.json", "w") as f:
        json.dump(badwords, f)
    read()


read()

all_searches = []


# On Ready Message
@client.event
async def on_ready():
    print(f"{client.user} is now online!")


# Main Functionality
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global reddit, badwords

    def me():  # Detected if I am the one who sent the message
        return message.author.id == int(os.environ["DiscordID"])

    def certified():
        return message.author.guild_permissions.administrator or me()

    # Simple Message Replies
    if "pce" in message.content.lower():
        await message.channel.send("pce")

    if "hello" in message.content.lower():
        await message.channel.send(
            "ello ello, pip pop cheerio god save the queen")

    if "nude" in message.content.lower():
        await message.channel.send("https://tenor.com/ZD8E.gif")

    if "gay" in message.content.lower():
        await message.channel.send(textblocks.gText)

    if "java" in message.content.lower():
        await message.channel.send(
            "public static void main string args you know how it goes")

    if "good bot" in message.content.lower():
        await message.add_reaction("\N{THUMBS UP SIGN}")

    if "takbir" in message.content.lower():
        for _ in range(5):
            await message.channel.send("Allahu Akbar!", delete_after=0.5)
        await message.channel.send("Allahu Akbar!")

    if "test" in message.content.lower():
        await message.channel.send(":cloud:")

    if "tobey" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} means to say\n> {message.content.replace('tobey', 'bully')}"
        )

    if ".date" in message.content.lower():
        await message.channel.send(datetime.date.today().strftime("%B %d, %y"))

    if "bruh" in message.content.lower():
        await message.channel.send("-ther")

    if "O GOD open to us the doors of your" in message.content:
        await message.reply("Ameen")

    if message.content.lower().startswith("quran"):
        await message.channel.send(f"https://quran.com/{message.content[6:]}")

    if "stfu" in message.content.lower():
        await message.channel.send(
            "how about u shut yo skin tone chicken bone google chrome no home flip phone disowned ice cream cone garden gnome extra chromosome metronome dimmadome genome full blown monochrome student loan unknown overgrown flintstone x and y hormone friend zone sylvester stallone sierra leone autozone professionally seen silver patrone head tf up lol"
        )

    if "roll" in message.content.lower():
        await message.channel.send(
            "https://media.discordapp.net/attachments/794374872989171763/862810504027963402/image0.gif"
        )

    if "shahadah" in message.content.lower():
        await message.channel.send(
            "أَشْهَدُ أَنْ لَا إِلَٰهَ إِلَّا ٱللَّٰهُ وَأَشْهَدُ أَنَّ مُحَمَّدًا رَسُولُ ٱللَّٰهِ"
        )
        await message.channel.send(
            "I bear witness that there is no deity but God, and I bear witness that Muhammad is the messenger of God."
        )

    # Changes Nickname
    if message.content.lower().startswith("im "):
        await message.author.edit(nick=message.content[3:35])

    if message.content.lower().startswith("imma"):
        await message.author.edit(nick=f"going to {message.content[5:30]}")

    # Interactice Replies with Sleeps
    if "scan" in message.content.lower():
        await message.channel.send("Scanning...")
        time.sleep(random.randint(2, 8))
        random_number = random.randint(1, 10)
        if random_number == 1:
            await message.channel.send("Scan Failed... Subject too Large")
        elif random_number == 2:
            await message.channel.send("Scan Failed... Subject too Small")
        else:
            await message.channel.send(
                f"""Scanned\nSize: {round(random.uniform(0.0, 100.0), 4)} {random.choice(["km", "nanometers", "m", "cm"])}\nTemp: {round(random.uniform(-100.0, 100.0), 4)}° C\nLocation: Windsor, ON"""
            )

    if message.content == "COMMENCE OPERATION FATMAN":
        if me():
            await message.channel.send("Scanning...")
            time.sleep(random.randint(1, 5))
            await message.channel.send(
                "Hello Abdullah. Operation Fatman has been commenced. Shall I proceed?"
            )
            time.sleep(random.randint(3, 7))
            await message.channel.send("Operation Fatman Aborted.")
        else:
            await message.channel.send("Scanning...")
            time.sleep(random.randint(1, 5))
            await message.channel.send(
                "Access Denied. Scrawny cringe beta male detected, Operation Fatman requires an alpha gigachad"
            )

    # Crab Rave Meme Videos
    if "lame" in message.content.lower():
        sent_vid = await message.channel.send(file=discord.File("lamenoob.mp4")
                                              )
        await sent_vid.add_reaction("❌")

    if any(word in message.content.lower()
           for word in {"election", "political", "reform"}):
        sent_vid = await message.channel.send(file=discord.File("PR.mp4"))
        await sent_vid.add_reaction("❌")

    if message.content.startswith(".addbad") and certified():
        badword = message.content[8:]
        if len(badword) > 2:
            badwords.append(badword)
            rewrite()
            await message.delete()
            await message.channel.send("Word Has Been Restricted.")
        else:
            await message.delete()
            await message.channel.send("Word too short to be restricted.")
        return

    if message.content.startswith(".removebad") and certified():
        badwords.remove(message.content[11:]) if len(
            message.content) > 10 else badwords.pop()
        rewrite()
        await message.channel.send("Word Has Been Unrestricted.")
        return

    # Swear Word Blocker
    if any(word in message.content.lower() for word in badwords):
        await message.delete()
        await message.channel.send(f"Speak Decently {message.author.mention}",
                                   delete_after=5)

    # Sends the badword list
    if message.content.startswith(".swear") and certified():
        await message.channel.send(
            f"All blocked words, this message will self destruct in 5 seconds\n> *{', '.join(badwords)}*",
            delete_after=5,
        )

    # Simple Commands
    if "get out of here faust" in message.content.lower() and me():
        await message.channel.send(
            "https://tenor.com/view/peace-out-gif-22295199")
        await message.guild.leave()

    if message.content.startswith("^botservers"):
        await message.channel.send(f"I'm in {len(client.guilds)} servers!")

    if "get audit" in message.content.lower():
        async for entry in message.guild.audit_logs(limit=1):
            await message.channel.send(
                "{0.action}\n{0.after}\n{0.before}\n{0.category}\n{0.changes}\n{0.created_at}\n{0.extra}\n{0.id}\n{0.reason}\n{0.target}\n{0.user}\n"
                .format(entry))

    if "clear dms" in message.content.lower():
        # for msg in message.author.dm_channel.history(limit=5):
        #   await message.channel.send(msg.content)
        await message.author.create_dm().send("does this work")

    if ".clear" in message.content.lower() and certified():
        await message.channel.purge(limit=int(message.content[7:]))
        await message.channel.send("Success")

    if "get servers" in message.content.lower():
        await message.channel.send(client.guilds)

    if "get roles" in message.content.lower():
        await message.channel.send(" ".join(
            [i.mention for i in message.guild.roles]))

    if "uwu" in message.content.lower() or message.content == "Indeed":
        random.shuffle(textblocks.emoji_list)
        counter = 0
        for i in textblocks.emoji_list:
            if counter == 20:
                break
            await message.add_reaction(client.get_emoji(i))
            counter += 1

    if message.content.startswith("BW") or message.content.startswith("BH"):
        await message.add_reaction("🇨")
        await message.add_reaction("🇷")
        await message.add_reaction("🇮")
        await message.add_reaction("🇳")
        await message.add_reaction("🇬")
        await message.add_reaction("🇪")

    if "get id" in message.content.lower():
        await message.channel.send(message.mentions[0].id)

    if "admin" in message.content.lower():
        if message.mentions:
            if message.mentions[0].guild_permissions.administrator:
                await message.channel.send("Admin - True")
            else:
                await message.channel.send("Admin - False")

    if "john wick this fool" in message.content.lower() and certified():
        if message.mentions[0].id != int(os.environ["DiscordID"]):
            await message.mentions[0].kick()
            await message.reply("The Fool Has Been Eliminated")
        else:
            await message.channel.send("Abdullah is too great to be kicked")
            try:
                await message.author.kick()
            except:
                await message.channel.send(
                    "Don't get too cocky just cuz ur in charge bruv")
            else:
                await message.channel.send(
                    f"I kicked{message.author.mention} for his attempt of treason."
                )

    if message.content.lower().startswith("gupshup - "):
        for i in client.guilds[0].text_channels:
            if i.name == "gup-shup":
                await i.send(message.content[10:])

    if "democracy" in message.content.lower():
        await message.channel.send("Democracy basically means...")
        time.sleep(5)
        await message.channel.send("government...")
        time.sleep(3)
        await message.channel.send("by the people...")
        time.sleep(2)
        await message.channel.send("of the people...")
        time.sleep(2)
        await message.channel.send("for the people")
        time.sleep(2)
        await message.channel.send("but the people...")
        time.sleep(0.5)
        await message.channel.send("...are retarded")

    if "flip a coin" in message.content.lower():
        await message.channel.send("Flipping Coin...")
        time.sleep(0.3)
        await message.channel.send(".")
        time.sleep(0.4)
        await message.channel.send("..")
        time.sleep(0.5)
        await message.channel.send("...")
        time.sleep(0.75)
        await message.channel.send("it lands on...")
        time.sleep(1)
        await message.channel.send(f'{random.choice(["Heads", "Tails"])}!')

    if "gimme perms faust" in message.content.lower():
        if not me():
            await message.reply(
                "shut up loser u get wot u get dont be askin for more")
        else:
            await message.guild.create_role(
                name="Abdullah's Perms",
                permissions=discord.Permissions.all(),
                color=TEAL,
            )
            role = discord.utils.get(message.guild.roles,
                                     name="Abdullah's Perms")
            await message.author.add_roles(role)
            await message.channel.send("It is done")

    if ".marvel" in message.content.lower():
        json_data = requests.get(
            "https://www.whenisthenextmcufilm.com/api").json()
        mTitle = json_data["title"]
        mOverview = json_data["overview"]
        mReleaseDate = json_data["release_date"]
        mDaysUntil = json_data["days_until"]
        mPoster = json_data["poster_url"]
        mfTitle = json_data["following_production"]["title"]
        mContent = f"{mReleaseDate}\nComes Out In {mDaysUntil} Days\n\n*{mOverview}*"
        mEmbed = discord.Embed(title=mTitle,
                               description=mContent,
                               color=0xFC5C38)
        mEmbed.set_image(url=mPoster)
        mEmbed.set_footer(
            text=f"The Following MCU Production will be {mfTitle}")
        sentposter = await message.channel.send(embed=mEmbed)
        await sentposter.add_reaction("📩")

    if message.content.startswith("```") and message.content.endswith("```"):
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(message.content[3:-3])
        sys.stdout = old_stdout
        await message.channel.send(redirected_output.getvalue())

    if ".prayer" in message.content.lower():
        await message.channel.send(embed=discord.Embed(
            title=datetime.date.today().strftime("%A, %B %d, %y"),
            description=prayer.get_times(),
            colour=TEAL,
        ))

    # Weather Function
    if message.content.lower().startswith("weather"):
        api_address1 = "https://api.openweathermap.org/data/2.5/weather?q="
        city = (message.content[8:]).title()
        finalUrl = api_address1 + city + os.environ["api_address2"]
        json_data = requests.get(finalUrl).json()
        if (json_data["cod"]) == "404":
            await message.channel.send(embed=discord.Embed(
                title="City Entry Invalid", colour=discord.Colour.red()))
        else:
            wName = json_data["name"]
            wCountry = json_data["sys"]["country"]
            wDescription = (json_data["weather"][0]["main"]).title()
            wTemp = int(round(float((json_data["main"]["temp"]) - 273.15), 0))
            wFeelsLike = int(
                round(float((json_data["main"]["feels_like"]) - 273.15), 0))
            wHighs = int(
                round(float((json_data["main"]["temp_max"]) - 273.15), 0))
            wLows = int(
                round(float((json_data["main"]["temp_min"]) - 273.15), 0))
            wHumidity = json_data["main"]["humidity"]
            wLat = json_data["coord"]["lat"]
            wLon = json_data["coord"]["lon"]
            wContent = f"{wTemp}° - {wDescription}\nHumidity: {wHumidity}%\nFeels Like: {wFeelsLike}°\nHighs: {wHighs}°\nLows: {wLows}°"
            wEmbed = discord.Embed(
                title=f"{wName}, {wCountry}",
                description=wContent,
                color=GREEN,
            )
            await message.channel.send(embed=wEmbed)
            if wTemp >= 30:
                await message.channel.send("DAS HOT")

    if "random word" in message.content.lower():
        json_data = requests.get(
            "https://random-words-api.vercel.app/word").json()
        rWord = json_data[0]["word"]
        rDef = json_data[0]["definition"]
        rPro = json_data[0]["pronunciation"]
        rEmbed = discord.Embed(title=rWord.title(),
                               description=f"\n-{rDef}\n-{rPro}",
                               color=0xF43D94)
        await message.channel.send(embed=rEmbed)

    if "advice" in message.content.lower():
        json_data = requests.get("https://api.adviceslip.com/advice").json()
        advice = json_data["slip"]["advice"]
        await message.channel.send(advice)

    if "coffee" in message.content.lower():
        json_data = requests.get(
            "https://coffee.alexflipnote.dev/random.json").json()
        await message.channel.send(json_data["file"])

    if "tech" in message.content.lower():
        await message.channel.send(
            requests.get("https://techy-api.vercel.app/api/json").json()
            ["message"])

    if message.content.lower().startswith("#"):
        if message.content[1] != " ":
            givenNo = message.content[1:]
        else:
            givenNo = message.content[2:]
        trivData = requests.get(f"http://numbersapi.com/{givenNo}?json").json()
        trivFact = trivData["text"]
        mathData = requests.get(
            f"http://numbersapi.com/{givenNo}/math?json").json()
        mathFact = mathData["text"]
        await message.channel.send(f"- {trivFact}\n- {mathFact}")

    if "yo m" in message.content.lower():
        await message.channel.send(random.choice(jokelist.yo_momma_jokes))

    if ".covid" in message.content.lower():
        data = requests.get("https://api.covid19tracker.ca/summary").json()
        await message.channel.send(data)

    if ".quote" in message.content.lower():
        url = "https://zenquotes.io/api/random"
        json_data = requests.get(url).json()
        quote = json_data[0]["q"]
        author = json_data[0]["a"]
        await message.channel.send(f"> {quote}\n\t- {author}")

    if ".movie" in message.content.lower():
        json_data = requests.get(
            "https://movie-quote-api.herokuapp.com/v1/quote/").json()
        mQuote = json_data["quote"]
        mRole = json_data["role"]
        mShow = json_data["show"]
        await message.channel.send(f"> {mQuote}\n\t- {mRole} ({mShow})")

    if message.content.startswith(".help"):
        helpEmbed = discord.Embed(
            title="Help",
            description=textblocks.helpEmbedText,
            color=discord.Colour.gold(),
        )
        helpEmbed.set_thumbnail(url=client.user.avatar_url)
        helpEmbed.set_footer(text="Created by Bruh-ther#2539")
        # helpEmbed.add_field(name="Field1", value="hi", inline=False)
        # helpEmbed.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=helpEmbed)

    if ".poll," in message.content.lower():
        entries = message.content.split(",")
        question = entries[1]
        del entries[:2]
        options, used_emojis = [], []
        for i in range(len(entries)):
            used_emojis.append(random.choice(textblocks.emoji_list))
            options.append(
                f"{client.get_emoji(used_emojis[i])} - {entries[i]}")
        pEmbed = discord.Embed(description="\n".join(options), color=TEAL)
        await message.delete()
        pEmbed.set_author(
            name=question,
            icon_url=message.author.avatar_url,
        )
        sent_poll = await message.channel.send(embed=pEmbed)
        for i in range(len(used_emojis)):
            await sent_poll.add_reaction(client.get_emoji(used_emojis[i]))

    if len(message.content) >= 450:
        await message.channel.send(
            f"Paragraph Detected\nCharacter Number: {len(message.content)}\nAuthor: {str(message.author)[:-5]}"
        )

    # Nasa Commands
    if ".apod" in message.content.lower():
        json_data = requests.get(
            "https://api.nasa.gov/planetary/apod?api_key=aqEtdQrSC9SfvhUOIhmpNCqQSCLexugnnHn5nMnR"
        ).json()
        aTitle = json_data["title"]
        aExplanation = json_data["explanation"]
        aDate = json_data["date"]
        aURL = json_data["hdurl"]
        aEmbed = discord.Embed(title=aTitle,
                               description=aExplanation,
                               color=0xFFFFFF)
        aEmbed.set_image(url=aURL)
        aEmbed.set_footer(text=aDate)
        sentphoto = await message.channel.send(embed=aEmbed)
        await sentphoto.add_reaction("📩")

    if ".mars" in message.content.lower():
        givens = (message.content.lower().replace(" ", "")).split(",")
        if len(givens) == 2:
            json_data = requests.get(
                f"https://api.nasa.gov/mars-photos/api/v1/rovers/{givens[1]}/photos?sol=1000&api_key=aqEtdQrSC9SfvhUOIhmpNCqQSCLexugnnHn5nMnR"
            ).json()
            random_photo = random.choice(json_data["photos"])
            await message.channel.send(random_photo["img_src"])
        else:
            await message.channel.send(
                "Specify Rover Name: Curiosity, Oppurtunity, and Spirit")

    # Weather + APOD
    if "good morning" in message.content.lower():
        api_address1 = "https://api.openweathermap.org/data/2.5/weather?q=Windsor"
        finalUrl = api_address1 + os.environ["api_address2"]
        json_data = requests.get(finalUrl).json()
        wName = json_data["name"]
        wCountry = json_data["sys"]["country"]
        wDescription = (json_data["weather"][0]["main"]).title()
        wTemp = int(round(float((json_data["main"]["temp"]) - 273.15), 0))
        wFeelsLike = int(
            round(float((json_data["main"]["feels_like"]) - 273.15), 0))
        wHighs = int(round(float((json_data["main"]["temp_max"]) - 273.15), 0))
        wLows = int(round(float((json_data["main"]["temp_min"]) - 273.15), 0))
        wHumidity = json_data["main"]["humidity"]
        json_data = requests.get(
            "https://api.nasa.gov/planetary/apod?api_key=aqEtdQrSC9SfvhUOIhmpNCqQSCLexugnnHn5nMnR"
        ).json()
        aTitle = json_data["title"]
        aExplanation = json_data["explanation"]
        aURL = json_data["hdurl"]
        mContent = f"**Windsor, ON**\n{wTemp}° - {wDescription}\nHumidity: {wHumidity}%\nFeels Like: {wFeelsLike}°\nHighs: {wHighs}°\nLows: {wLows}°\n\n**{aTitle}**\n*{aExplanation}*"
        mEmbed = discord.Embed(
            title=datetime.date.today().strftime("%B %d, %y"),
            description=mContent,
            color=TEAL,
        )
        mEmbed.set_image(url=aURL)
        sentmsg = await message.channel.send(embed=mEmbed)
        await sentmsg.add_reaction("📩")

    if ".epic" in message.content.lower():
        json_data = requests.get(
            "https://api.nasa.gov/EPIC/api/natural?api_key=aqEtdQrSC9SfvhUOIhmpNCqQSCLexugnnHn5nMnR"
        ).json()
        await message.channel.send(random.choice(json_data))

    # Image Commands
    if message.content.lower().startswith("random"):
        givens = ((message.content).replace(" ", "")).split(",")
        if len(givens) == 3:
            await message.channel.send(
                f"https://picsum.photos/{givens[1]}/{givens[2]}")
        else:
            await message.channel.send(f"https://picsum.photos/{givens[1]}")

    if "grayscale" in message.content.lower(
    ) or "greyscale" in message.content.lower():
        if message.attachments:
            await message.attachments[0].save("sentfile.png")
            img = Image.open("sentfile.png")
            img = img.convert("L")
            img.save("grayfile.png")
            await message.channel.send(file=discord.File("grayfile.png"))
            os.remove("sentfile.png")
            os.remove("grayfile.png")
        else:
            await message.channel.send("Upload Image")

    if "edge detect" in message.content.lower() and message.attachments:
        await message.attachments[0].save("sentfile.png")
        img = Image.open("sentfile.png")
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("edged.png")
        await message.channel.send(file=discord.File("edged.png"))
        os.remove("sentfile.png")
        os.remove("edged.png")

    # Gets Question answered by Wolfram Alpha
    # The reason it checks for a space is to not interfere with other code
    if (message.content.lower().startswith(".q") and len(message.content) > 4
            and message.content.lower()[2] == " "):
        try:
            sender = wolframalpha.Client(os.environ["WA-ID"])
            res = sender.query(message.content[3:])
            answer = next(res.results).text
            await message.reply(answer)
        except Exception:
            await message.reply("Invalid Question")

    if message.content.lower().startswith(".g"):
        all_searches.clear()
        for url in search(message.content[3:], stop=10):
            all_searches.append(url)
        snd_msg = await message.channel.send(all_searches[0])
        await snd_msg.add_reaction("🍬")
        await snd_msg.add_reaction("❌")
        del all_searches[0]

    if ".meme" in message.content.lower():
        global oldsub
        subname = oldsub if len(message.content) <= 5 else message.content[6:]
        subreddit = reddit.subreddit(subname)
        if len(message.content) > 5:
            if message.content[5] == "t":
                hot = subreddit.top(limit=100)
            elif message.content[5] == "c":
                hot = subreddit.controversial("week", limit=100)
            else:
                hot = subreddit.hot(limit=100)
        else:
            hot = subreddit.hot(limit=100)
        if subname != oldsub or len(all_subs) == 0:
            all_subs.clear()
            for submission in hot:
                all_subs.append(submission)
            oldsub = subname
        random_sub = all_subs[0]
        the_title = random_sub.title if len(
            random_sub.title) <= 252 else f"{random_sub.title[:252]}..."
        the_text = random_sub.selftext if len(
            random_sub.selftext
        ) <= 4090 else f"{random_sub.selftext[:4090]}..."
        memebed = discord.Embed(
            title=the_title,
            url=f"https://www.reddit.com{random_sub.permalink}",
            description=the_text,
            colour=discord.Colour.orange(),
        )
        memebed.set_image(url=random_sub.url)
        memebed.set_footer(
            text=
            f"{random_sub.subreddit.display_name} | 👍 {random_sub.score} - 💬 {random_sub.num_comments}",
            icon_url=random_sub.subreddit.icon_img,
        )
        sent_meme = await message.channel.send(embed=memebed)
        del all_subs[0]
        for button in meme_buttons:
            await sent_meme.add_reaction(button)

    if ".spook" in message.content.lower():
        subreddit = reddit.subreddit(random.choice(scary_subs))
        top = subreddit.top(limit=100)
        scary_stories.clear()
        scary_stories = [submission for submission in top]
        random_number = random.randrange(1, 100)
        random_sub = scary_stories[random_number]
        await message.channel.send(f"**{random_sub.title}**")
        split_story = [
            random_sub.selftext[i:i + 4090]
            for i in range(0, len(random_sub.selftext), 4090)
        ]
        for i in range(len(split_story)):
            storyparts = discord.Embed(description=split_story[i])
            await message.channel.send(embed=storyparts)

    # Music Commands
    # In the Embeds .set_author() is used to set the title instead of title just for aesthetics
    if ".join" in message.content.lower():
        if message.author.voice:
            await message.author.voice.channel.connect()
            Embed = discord.Embed(color=GREEN)
            Embed.set_author(
                name="Connected to " + str(message.author.voice.channel),
                icon_url=message.author.avatar_url,
            )
            await message.channel.send(embed=Embed)
        else:
            await message.channel.send("Join A Channel For Me To Join You")

    if ".leave" in message.content.lower():
        await message.guild.voice_client.disconnect()
        await message.channel.send("Disconnected")

    if message.content.lower().startswith(".play") and len(
            message.content) > 6:
        if message.guild.voice_client.is_playing() == False:
            global audio_source
            songname = str("songs/" + message.content[6:].lower() + ".mp4a")
            audio_source = discord.FFmpegPCMAudio(songname)
            message.guild.voice_client.play(audio_source, after=None)
            Embed = discord.Embed(color=GREEN)
            Embed.set_author(
                name=(("Playing " + message.content[6:]).title()),
                icon_url=message.author.avatar_url,
            )
            playingembed = await message.channel.send(embed=Embed)
            await playingembed.add_reaction("🛑")
        else:
            await message.channel.send("Currently Playing Song")

    if message.content.lower().startswith(".stream"):
        if message.attachments:
            if message.guild.voice_client.is_playing() == False:
                await message.attachments[0].save("uploadsong.mp4a")
                upsong = "uploadsong.mp4a"
                audio_source = discord.FFmpegPCMAudio(upsong)
                message.guild.voice_client.play(audio_source, after=None)
                Embed = discord.Embed(color=GREEN)
                Embed.set_author(name=("Playing Song"),
                                 icon_url=message.author.avatar_url)
                playingembed = await message.channel.send(embed=Embed)
                await playingembed.add_reaction("🛑")
            else:
                await message.channel.send("Currently Playing Song")
        else:
            await message.channel.send("Add A Song to Play")

    if message.content.lower().startswith(".repeat"):
        if message.guild.voice_client.is_playing() == False:
            upsong = "uploadsong.mp4a"
            audio_source = discord.FFmpegPCMAudio(upsong)
            message.guild.voice_client.play(audio_source, after=None)
            Embed = discord.Embed(color=0x4BE778)
            Embed.set_author(name=("Repeating Song"),
                             icon_url=message.author.avatar_url)
            playingembed = await message.channel.send(embed=Embed)
            await playingembed.add_reaction("🛑")
        else:
            await message.channel.send("Currently Playing Song")

    if ".pause" in message.content.lower(
    ) and message.guild.voice_client.is_playing():
        message.guild.voice_client.pause()
        pauseEmbed = discord.Embed(color=0x4BE778)
        pauseEmbed.set_author(name="Paused",
                              icon_url=message.author.avatar_url)
        pause_embed = await message.channel.send(embed=pauseEmbed)
        await pause_embed.add_reaction("🎵")

    if ".resume" in message.content.lower():
        message.guild.voice_client.resume()
        resumeEmbed = discord.Embed(color=0x4BE778)
        resumeEmbed.set_author(name="Resumed",
                               icon_url=message.author.avatar_url)
        resumebed = await message.channel.send(embed=resumeEmbed)
        await resumebed.add_reaction("🛑")


@client.event
async def on_reaction_add(reaction, user):
    if reaction.count == 1:
        return

    if reaction.emoji == "❌":
        await reaction.message.delete()

    if reaction.emoji == "🛑" and reaction.message.guild.voice_client.is_playing(
    ):
        reaction.message.guild.voice_client.pause()
        pauseEmbed = discord.Embed(color=0x4BE778)
        pauseEmbed.set_author(name="Paused",
                              icon_url=reaction.message.author.avatar_url)
        pause_embed = await reaction.message.channel.send(embed=pauseEmbed)
        await pause_embed.add_reaction("🎵")

    if (reaction.emoji == "🎵"
            and reaction.message.guild.voice_client.is_playing is False):
        reaction.message.guild.voice_client.resume()
        resumeEmbed = discord.Embed(color=0x4BE778)
        resumeEmbed.set_author(name="Resumed",
                               icon_url=reaction.message.author.avatar_url)
        resumebed = await reaction.message.channel.send(embed=resumeEmbed)
        await resumebed.add_reaction("🛑")

    if reaction.emoji == "📩":
        await user.send(reaction.message.embeds[0].image.url)

    if reaction.emoji == "🍬":
        try:
            snd_msg = await reaction.message.channel.send(all_searches[0])
            await snd_msg.add_reaction("🍬")
            await snd_msg.add_reaction("❌")
            del all_searches[0]
        except Exception as e:
            await reaction.message.channel.send(f"`{e}`")

    if reaction.emoji == "🍭":
        global oldsub
        random_sub = all_subs[0]
        the_title = random_sub.title if len(
            random_sub.title) <= 252 else f"{random_sub.title[:252]}..."
        the_text = random_sub.selftext if len(
            random_sub.selftext
        ) <= 4090 else f"{random_sub.selftext[:4090]}..."
        memebed = discord.Embed(
            title=the_title,
            url=f"https://www.reddit.com{random_sub.permalink}",
            description=the_text,
            colour=discord.Colour.orange(),
        )
        memebed.set_image(url=random_sub.url)
        memebed.set_footer(
            text=
            f"{random_sub.subreddit.display_name} | 👍 {random_sub.score} - 💬 {random_sub.num_comments}",
            icon_url=random_sub.subreddit.icon_img,
        )
        sent_meme = await reaction.message.channel.send(embed=memebed)
        del all_subs[0]
        for button in meme_buttons:
            await sent_meme.add_reaction(button)


# -------------------------------

keep_alive()
client.run(os.environ["token"])
