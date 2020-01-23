###Imports
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from calcTime import calculateCsTime,calculateCsTimeSeconds
load_dotenv()

#from timers import timerToCs

###Constants
client = commands.Bot(command_prefix = '!')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

###Utilities

#List of the possible cs times
def switchCsTime(argument):
    switcher = {
        1: [22,10],
        2: [23,10],
        3: [0,30]
    }
    return switcher.get(argument, "Invalid cs time")
#List of the members in the cs team
CS_TEAM = []

#ON_READY bot
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
async def cs(ctx, nCsTime: int):
    strCalculated = calculateCsTime(switchCsTime(nCsTime))
    csString = f"{strCalculated[0]} hours, {strCalculated[1]} minutes, {strCalculated[2]} seconds left to COUNTER STRIKE HOUR NUMBER {nCsTime}"
    await ctx.send(csString)

#!cs_assemble (cshournumber) starts the timer for a certain cs time that will be played
@client.command()
async def cs_assemble(ctx, csHourNumber: int):
    #iniciar timer tendo em conta CS_TIMES[cs_hournumber-1]
    #de alguma forma quando o timer terminar o bot vai entrar na sala de onde foi chamado (FORÇAR A ESTAR NUMA SALA PARA ELE DEPOIS ENTRAR - REJEITAR SE NÃO ESTIVER NUMA SALA)
    #fazer mention à equipa se a lista tiver membros adicionados quando é feito o assemble e depois quando chegar a hora
    calculatedTimeSeconds = calculateCsTimeSeconds(switchCsTime(csHourNumber))

    await ctx.send

#!cs_add (user_y) adds a discord user to the cs team
@client.command()
async def cs_add(ctx, *members: discord.Member):
    for member in members:
        if member not in CS_TEAM:
            CS_TEAM.append(member)
            await ctx.send(f"{member.mention} convocado")
        else:
            await ctx.send("Esse já tá na equipa cralhes")
    

#!cs_remove (user_y) removes a discord user from the cs team
@client.command()
async def cs_remove(ctx, member: discord.Member):
    if member not in CS_TEAM:
        await ctx.send("Esse não tá na equipa")
    else: 
        CS_TEAM.remove(member)
        await ctx.send(f"{member.mention} fora da equipa")

#Mostra quem está atualmente na equipa
@client.command()
async def cs_team(ctx):
    CS_TEAM.sort
    team = "Convocatória atual: "
    teamLength = len(CS_TEAM)
    i=0
    if(teamLength < 1):
        await ctx.send("Não há ninguém pra hora do cs", file=discord.File('pepehands.png'))
    else:
        while i < teamLength:
            if(i<1):
                team+=f"{CS_TEAM[i].mention}"
            else: 
                team+=f", {CS_TEAM[i].mention}"
            i+= 1
        await ctx.send(team)
    

@client.command()
async def timertest(ctx):
    calculated_time = calculateCsTime(switch_cstime(1))
    print(calculated_time)
    timetest(calculated_time, True)
    await ctx.send("Timer")
    
client.run(TOKEN)