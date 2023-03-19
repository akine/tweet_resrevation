import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import tweepy
import datetime

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"{bot.user} が接続しました。")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"{message.channel}: {message.author.name}: {message.content}")
    await bot.process_commands(message)

@bot.command(name='tweet')
async def tweet(ctx, timestamp, *tweet_text):
    tweet_text = ' '.join(tweet_text)
    schedule_time = datetime.datetime.strptime(timestamp, '%Y,%m,%d,%H,%M')

    if datetime.datetime.now() < schedule_time:
        twitter_api.update_status(status=tweet_text)
        await ctx.send(f"予約投稿が完了しました: {schedule_time.strftime('%Y-%m-%d %H:%M')}にツイート予定です。")
    else:
        await ctx.send("指定された時刻が過去のものです。正しい時刻を指定してください。")

bot.run(DISCORD_BOT_TOKEN)
