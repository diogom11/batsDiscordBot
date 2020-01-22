import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from calcTime import calculate_cs_time
load_dotenv()

client = commands.Bot(command_prefix = '!')

#Constants
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CS_TIMES = [[22,10], [23,10], [0,30]]
CS_TEAM = []



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    game = discord.Game("with your momma")  
    await client.change_presence(status=discord.Status.do_not_disturb, activity=game)

#=========================================================================================
#================================ CS RELATED COMMAND EVENTS ==============================
#=========================================================================================


#!cs shows all the bot functions regarding counter strike -> PLACEHOLDER FOR NOW SHOWS TIME REMAINING FOR FIRST CS TIME
@client.command()
async def cs(ctx):
    await ctx.send(calculate_cs_time(CS_TIMES[0], 1))

#!cs_assemble (cshournumber) starts the timer for a certain cs time that will be played
@client.command()
async def cs_assemble(ctx, cs_hournumber: int):
    #iniciar timer tendo em conta CS_TIMES[cs_hournumber-1]
    #de alguma forma quando o timer terminar o bot vai entrar na sala de onde foi chamado (FORÇAR A ESTAR NUMA SALA PARA ELE DEPOIS ENTRAR - REJEITAR SE NÃO ESTIVER NUMA SALA)
    #fazer mention à equipa se a lista tiver membros adicionados quando é feito o assemble e depois quando chegar a hora 


#!cs_add (user_y) adds a discord user to the cs session
@client.command()
async def cs_add(ctx, member: discord.Member):
    CS_TEAM.append(member)
    #print(CS_TEAM)
    await ctx.send(member.mention)

client.run(TOKEN)