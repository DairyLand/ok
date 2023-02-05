import discord
import praw
import random

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

async def post_hot_post(subreddit, channel):
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         username='YOUR_REDDIT_USERNAME',
                         password='YOUR_REDDIT_PASSWORD',
                         user_agent='YOUR_APP_NAME')
    hot_post = reddit.subreddit(subreddit).hot(limit=1)
    for post in hot_post:
        message = post.title + '\n' + post.url
        await channel.send(message)

async def post_random_post(subreddit, channel):
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         username='YOUR_REDDIT_USERNAME',
                         password='YOUR_REDDIT_PASSWORD',
                         user_agent='YOUR_APP_NAME')
    posts = reddit.subreddit(subreddit).hot(limit=100)
    post = random.choice(list(posts))
    message = post.title + '\n' + post.url
    await channel.send(message)

@client.event
async def on_message(message):
    if message.content == '!okaybuddyreatard':
        channel = message.channel
        await post_hot_post('okaybuddyreatard', channel)
    if message.content == '!dogelore':
        channel = message.channel
        await post_hot_post('dogelore', channel)
    if message.content == '!altdogelore':
        channel = message.channel
        await post_hot_post('altdogelore', channel)
    if message.content == '^meme':
        channel = message.channel
        subreddits = ['okaybuddyreatard', 'dogelore', 'altdogelore']
        subreddit = random.choice(subreddits)
        await post_random_post(subreddit, channel)

client.run('YOUR_BOT_TOKEN')
