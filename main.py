import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='!', case_insensitive=True)
day = "rpg daily"
weekly = "rpg weekly"
chop = "rpg chop", "rpg bowsaw", "rpg chainsaw", "rpg axe"
fish = "rpg fish", "rpg net", "rpg bigboat"
cds = "rpg cd", "rpg cooldown", "rpg cds", "rpg ready", "rpg rd"
lootbox = "rpg open"
profile = "rpg p", "rpg profile"
inv = "rpg i", "rpg inventory"
farm = "rpg farm", "rpg farm carrot", "rpg farm potato", "rpg farm bread"
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#small letter here
    if message.content.startswith('help'):
        await message.channel.send('> random-discord-bot avalible commands\n> now this dumb bot will reply most of the rpg commands that u typed\n> this bot still in development feel free to fork me lolol')
    if message.content.startswith(day):
        await message.channel.send('> bruh come claim free stuff')
    if message.content.startswith(cds):
        await message.channel.send('> lolol all in cd lmao')
    if message.content.startswith(weekly):
        await message.channel.send('> woo claim one week of free stuff')
    if message.content.startswith(lootbox):
        await message.channel.send('> no mob drops hehe')
    if message.content.startswith('rpg vote'):
        await message.channel.send('> bruh need to watch medal ads again')
    if message.content.startswith('rpg hunt'):
        await message.channel.send('> no mob drops bruh')
    if message.content.startswith('rpg adv'):
        await message.channel.send('> no lootbox bruh')
    if message.content.startswith('rpg duel'):
        await message.channel.send('> why duel to get xp just eat cookies')
    if message.content.startswith('rpg quest'):
        await message.channel.send('> hope u get cook stuff quest')
    if message.content.startswith(chop):
        await message.channel.send('> wah sed trees')
    if message.content.startswith(fish):
        await message.channel.send('> baked fish lol')
    if message.content.startswith('rpg horse race'):
        await message.channel.send('> your horse too slow cant win')
    if message.content.startswith('rpg arena'):
        await message.channel.send('> join!!!')
    if message.content.startswith(profile):
        await message.channel.send('> bruh why see profile')
    if message.content.startswith(inv):
        await message.channel.send('> keep looking inventory still the same')
    if message.content.startswith('rpg tr'):
        await message.channel.send('> directly type n will do')
    if message.content.startswith(farm):
        await message.channel.send('> no seed so sad')
    if message.content.startswith('rpg guild'):
        await message.channel.send('> upgrade fail')

client.run('put your token here')
