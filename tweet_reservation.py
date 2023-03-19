import os
import discord
import tweepy
import datetime
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} が接続しました。")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"Received message: {message.content}")  # ここにログ出力を追加
    print(f"{message.channel}: {message.author.name}: {message.content}")
    await bot.process_commands(message)

async def schedule_tweet(ctx, tweet_text, schedule_time):
    try:
        delay = (schedule_time - datetime.datetime.now()).total_seconds()
        print(f"Waiting for {delay} seconds")  # ここにログ出力を追加
        await asyncio.sleep(delay)
        print(f"Done waiting")  # ここにログ出力を追加
        twitter_api.update_status(status=tweet_text)
        print(f"ツイートが投稿されました: {tweet_text}")  # ログに投稿されたツイートの情報を表示
        await ctx.send(f"ツイートが投稿されました: {tweet_text}")
    except Exception as e:
        print(f"予約投稿中にエラーが発生しました: {e}")
        await ctx.send(f"予約投稿中にエラーが発生しました: {e}")

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(name='tweet')
async def tweet(ctx, timestamp, *tweet_text):
    tweet_text = ' '.join(tweet_text)
    schedule_time = datetime.datetime.strptime(timestamp, '%Y,%m,%d,%H,%M')
    print(f"Received tweet command: {tweet_text} at {schedule_time}")  # ここにログ出力を追加

    if datetime.datetime.now() < schedule_time:
        await ctx.send(f"予約投稿が完了しました: {schedule_time.strftime('%Y-%m-%d %H:%M')}にツイート予定です。")
        bot.loop.create_task(schedule_tweet(ctx, tweet_text, schedule_time))
    else:
        await ctx.send("指定された時刻が過去のものです。正しい時刻を指定してください。")

bot.run(DISCORD_BOT_TOKEN)
