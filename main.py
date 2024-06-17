import disnake

from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, test_guilds='this id your discord server')


@bot.event
async def on_ready():
    print('Bot is ready!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.slash_command()
async def ping(interaction):
    await interaction.response.send_message('Pong!')

bot.run('this your token ')