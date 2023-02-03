import praw
import discord
import time

intents = discord.Intents.default()
intents.members = True

discord_client = discord.Client(intents=intents)

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='I-amExtremely-')

discord_client = discord.Client()


@discord_client.event
async def on_ready():
    print(f'Logged in as {discord_client.user}')
    while True:
        subreddit = reddit.subreddit('okbuddyretard')
        hot_posts = subreddit.hot(limit=1)
        for post in hot_posts:
            message = f"Hot post from r/okbuddyretard: {post.title}\n{post.url}"
            channel = discord_client.get_channel(channel_id)
            await channel.send(message)
        time.sleep(10800)

discord_client.run(
    '')
