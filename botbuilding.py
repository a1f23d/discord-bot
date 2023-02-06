import discord
import random


TOKEN = #XXXXX oops, probably don't want the bot token floating around
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
    #take message as parameter
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})') #logging everything on server


    if message.author == client.user:
        return

    if message.channel.name == 'bot-testing':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hi {username}!')
            return
    elif user_message.lower() == 'bye':
        await message.channel.send(f'Until we meet again, {username}!')
        return
    elif user_message.lower() == "!random":
        response = f'Your random number is: {random.randrange(10000)}'
        await message.channel.send(response)
        return

    if user_message.lower() == '!anywhere':
        await message.channel.send('Usage here is ill advised')
        return


client.run(TOKEN)
