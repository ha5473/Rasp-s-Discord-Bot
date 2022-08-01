import discord
import youtube_dl
from discord.ext import commands

client = discord.Client()

bot = commands.Bot(command_prefix="!") # 접두사를 !로 지정

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) # 봇이 실행되면 콘솔창에 표시

@client.event
async def on_message(message):
    if message.author == client.user: # 봇 자신이 보내는 메세지는 무시
        return

    if message.content.startswith('!청소'): # 만약 !청소라는 채팅이 올라오면
        channel_R = message.channel
        channel_C = client.get_channel(int('638663265291075584'))
        amount_str = message.content[4:]

        if channel_R == channel_C:
            if len(amount_str):
                try:
                    amount = int(message.content[4:]) + 1
                except: # 에러 핸들러
                    await channel_R.send('\'!청소\' 또는 \'!청소 메시지수\'로 입력하세요.')
                    return
                await channel_R.purge(limit=amount)
            else:
                await channel_R.purge(limit=201)

client.run(os.environ['token'])
