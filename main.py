import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='!', case_insensitive=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#small letter here
    if message.content.startswith('rpg daily'):
        await message.channel.send('bruh come claim free stuff')
    if message.content.startswith('rpg cd'):
        await message.channel.send('lolol all in cd lmao')
    if message.content.startswith('rpg weekly'):
        await message.channel.send('woo claim one week of free stuff')
    if message.content.startswith('rpg buy ed lb'):
        await message.channel.send('no mob drops hehe')
    if message.content.startswith('rpg vote'):
        await message.channel.send('bruh need to watch medal ads again')
    if message.content.startswith('rpg hunt'):
        await message.channel.send('no mob drops bruh')
    if message.content.startswith('rpg adv'):
        await message.channel.send('no lootbox bruh')
    if message.content.startswith('rpg duel'):
        await message.channel.send('why duel to get xp just eat cookies')
    if message.content.startswith('rpg quest'):
        await message.channel.send('hope u get cook stuff quest')
    if message.content.startswith('rpg chop'):
        await message.channel.send('wah sed trees')
    if message.content.startswith('rpg fish'):
        await message.channel.send('baked fish lol')
    if message.content.startswith('rpg horse race'):
        await message.channel.send('your horse too slow cant win')
    if message.content.startswith('rpg arena'):
        await message.channel.send('join!!!')
    if message.content.startswith('rpg p'):
        await message.channel.send('bruh why see profile')
    if message.content.startswith('rpg i'):
        await message.channel.send('keep looking inventory still the same')
    if message.content.startswith('rpg tr'):
        await message.channel.send('directly type n will do')
    if message.content.startswith('rpg farm'):
        await message.channel.send('no seed so sad')
    if message.content.startswith('rpg farm carrot'):
        await message.channel.send('fun')
    if message.content.startswith('rpg farm bread'):
        await message.channel.send('fun')
    if message.content.startswith('rpg farm potato'):
        await message.channel.send('fun')
    if message.content.startswith('rpg guild'):
        await message.channel.send('upgrade fail')

#caps here
    if message.content.startswith('Rpg daily'):
        await message.channel.send('bruh come claim free stuff')
    if message.content.startswith('Rpg cd'):
        await message.channel.send('lolol all in cd lmao')
    if message.content.startswith('Rpg weekly'):
        await message.channel.send('woo claim one week of free stuff')
    if message.content.startswith('Rpg buy ed lb'):
        await message.channel.send('no mob drops hehe')
    if message.content.startswith('Rpg vote'):
        await message.channel.send('bruh need to watch medal ads again')
    if message.content.startswith('Rpg hunt'):
        await message.channel.send('no mob drops bruh')
    if message.content.startswith('Rpg adv'):
        await message.channel.send('no lootbox bruh')
    if message.content.startswith('Rpg duel'):
        await message.channel.send('why duel to get xp just eat cookies')
    if message.content.startswith('Rpg quest'):
        await message.channel.send('hope u get cook stuff quest')
    if message.content.startswith('Rpg chop'):
        await message.channel.send('wah sed trees')
    if message.content.startswith('Rpg fish'):
        await message.channel.send('baked fish lol')
    if message.content.startswith('Rpg horse race'):
        await message.channel.send('your horse too slow cant win')
    if message.content.startswith('Rpg arena'):
        await message.channel.send('join!!!')
    if message.content.startswith('Rpg p'):
        await message.channel.send('bruh why see profile')
    if message.content.startswith('Rpg i'):
        await message.channel.send('keep looking inventory still the same')
    if message.content.startswith('Rpg tr'):
        await message.channel.send('directly type n will do')
    if message.content.startswith('Rpg farm'):
        await message.channel.send('no seed so sad')
    if message.content.startswith('Rpg farm carrot'):
        await message.channel.send('fun')
    if message.content.startswith('Rpg farm bread'):
        await message.channel.send('fun')
    if message.content.startswith('Rpg farm potato'):
        await message.channel.send('fun')
    if message.content.startswith('Rpg guild'):
        await message.channel.send('upgrade fail')
client.run('put your token here')
