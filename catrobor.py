import discord
import asyncpraw
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

reddit = asyncpraw.Reddit(
    client_id="nGQzQXyc_3kHlbnkjzzrqg",
    client_secret="xgX_u44ASzPO9G0CC5J6tFHRGTJuLA",
    user_agent="windows:cat-bot:v1 (by /u/covfefe55)",
)

subs = [
    "OneOrangeBraincell",
    "Catswithjobs",
    "Catloaf",
    "WhatsWrongWithYourCat",
    "teefies",
    "CatsOnKeyboards",
    "blurrypicturesofcats",
]

submissions = []

async def getSubmissions(n):
    for sub in subs:
        subreddit = await reddit.subreddit(sub)
        async for submission in subreddit.hot(limit=n):
            if submission.is_reddit_media_domain and submission.url.startswith("https://i"):
                submissions.append(submission.url)
            else:
                continue
        print(len(submissions))


async def randomPost():
    if len(submissions) == 0:
        await getSubmissions(20)
    post = random.choice(submissions)
    submissions.remove(post)
    return post


@client.event
async def on_ready():
    print("Getting submissions...")
    await getSubmissions(20)
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('/cat'):
            await message.channel.send(await randomPost())

client.run(
    "MTA0MDk0NTgzODg4Njc2MDQ5OA.GtrAl6.zwgBPv1eupg_pjadSsG55EGp5k_z_3FHcmKFIk"
    )

