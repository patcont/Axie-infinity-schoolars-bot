import requests
import json
import sys
import os
from asyncio import events
from discord.ext import commands

#You can use many urls as you want, they are from the site axie.management,
#after you have entered your schoolars ronin wallets in their site for tracking.
url = "https://api.axie.management/v1/overview/ronin_wallet_0"

url_2 = "https://api.axie.management/v1/overview/ronin_wallet_1"

url_3 = "https://api.axie.management/v1/overview/ronin_wallet_2"

#url_n (n means an infinite number of wallets you cand add depending on how many schoolars you have)

#The code below was taken from the application "insomnia" which call the APIs of each wallet,
#as the site doesn't allow to scrap directly we need this software to extrac the information of the APIs of each wallet.

payload = ""
headers = {
   "authority": "api.axie.management",
   "accept": "application/json, text/plain, */*",
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
   "dnt": "1",
   "sec-gpc": "1",
   "origin": "https://axie.management",
   "sec-fetch-site": "same-site",
   "sec-fetch-mode": "cors",
   "sec-fetch-dest": "empty",
   "referer": "https://axie.management/",
   "accept-language": "en-US,en;q=0.9,es-CL;q=0.8,es;q=0.7",
   "if-none-match": "W/ea-N84iKYoma0y7hc44E6AxTSQRr6Q"
}

#every response is linked to their respective url, url is correlated to response, url_2 to response_2 and so on"
response = requests.request("GET", url, data=payload, headers=headers).text
response_2 = requests.request("GET", url_2, data=payload, headers=headers).text
response_3 = requests.request("GET", url_3, data=payload, headers=headers).text
#response_n (n means you cand add as many responses depending on how many schollars you have)


#This is the main function than when called by the bot is gives the information we need
def scraping(r):

 y = json.loads(r)

 x=(y["slp"]["average"])

 z=str(x)

 a=(y["slp"]["total"])

 b=str(a)

 hoy= str(y["slp"]["todaySoFar"])

 ayer= str(y["slp"]["yesterdaySLP"])


 if x==None:
  juas=":sweat_smile:" 
   
 elif x>150 or x==150:
    juas=":partying_face:"
 elif x>100 and x<150 or x==100:
    juas= ":smiley:"
 elif x<100:
    juas= ":sweat:"

    

 promedio = ("Llevas en total " + b + " " + "slp" + " " + "con un promedio diario de: " + z + juas +  ", "
+ "hoy hiciste " + hoy + " " + "y ayer " + " " + ayer + ".")

 return promedio

#commands for the bot in the discord server
client = commands.Bot(command_prefix = ".")


@client.event
async def on_ready():
   print('bot online')

@client.command()
async def actualizar(ctx):
  await ctx.send("Datos actualizados :blush:")
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
async def player_1(ctx):
   await ctx.send(scraping(response))
   os.execv(sys.executable, ['python'] + sys.argv)
   
@client.command()
async def player_2(ctx):
   await ctx.send(scraping(response_2))
   os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
async def player_3(ctx):
   await ctx.send(scraping(response_3)) 
   os.execv(sys.executable, ['python'] + sys.argv)

#you cand add as many @client.command depending on how many schoolars you have
# clent.command()
#async def player_n(ctx):
# await ctx.send(scraping(response_n)) 
 # os.execv(sys.executable, ['python'] + sys.argv) 

client.run('TOKEN')   