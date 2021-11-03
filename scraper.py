import requests
import json
import sys
import os
from asyncio import events
from discord.ext import commands

url = "https://api.axie.management/v1/overview/schoolar_wallet"

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



response = requests.request("GET", url, data=payload, headers=headers)


y = json.loads(response.text)

x=(y["slp"]["average"])

z=str(x)

a=(y["slp"]["total"])

b=str(a)

hoy= str(y["slp"]["todaySoFar"])

ayer= str(y["slp"]["yesterdaySLP"])


def funt(i):

   if i==None:
    return ":sweat_smile:" 
   
   elif i>150 or i==150:
    return ":partying_face:"
   elif i>100 and i<150 or i==100:
    return ":smiley:"
   elif i<100:
    return ":sweat:"

    
juas=funt(x)


   


url_2 = "https://api.axie.management/v1/schoolar_wallet"

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
   "if-none-match": "W/^\^eb-pSrZ1yxEHS+mRQzXhui5c8fGjl8^^"
}

response_2 = requests.request("GET", url_2, data=payload, headers=headers)

y_2 = json.loads(response_2.text)

x_2=(y_2["slp"]["average"])

z_2=str(x_2)

a_2=(y_2["slp"]["total"])

b_2=str(a_2)

hoy_2= str(y_2["slp"]["todaySoFar"])

ayer_2= str(y_2["slp"]["yesterdaySLP"])



juas_2=funt(x_2)










url_3 = "https://api.axie.management/v1/overview/schoolar_wallet"

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
   "if-none-match": "W/^\^ea-3fFmFUsnQX2HyL194lEU3DmCdQ4^^"
}

response_3 = requests.request("GET", url_3, data=payload, headers=headers)

y_3 = json.loads(response_3.text)

x_3=(y_3["slp"]["average"])

z_3=str(x_3)

a_3=(y_3["slp"]["total"])

b_3=str(a_3)

hoy_3= str(y_3["slp"]["todaySoFar"])

ayer_3= str(y_3["slp"]["yesterdaySLP"])

juas_3=funt(x_3)

print(juas,juas_2,juas_3)

from asyncio import events
import discord
from discord.ext import commands
client = commands.Bot(command_prefix = ".")

promedio = ("Llevas en total " + b + " " + "slp" + " " + "con un promedio diario de: " + z + juas +  ", "
+ "hoy hiciste " + hoy + " " + "y ayer " + " " + ayer + ".")

promedio_2 = ("Llevas en total " + b_2 + " " + "slp" + " " + "con un promedio diario de: " + z_2 + juas_2 + ", "
+ "hoy hiciste " + hoy_2 + " " + "y ayer " + " " + ayer_2 + ".")

promedio_3 = ("Llevas en total " + b_3 + " " + "slp" + " " + "con un promedio diario de: " + z_3  +  juas_3 +  ", "
+ "hoy hiciste " + hoy_3 + " " + "y ayer " + " " + ayer_3 + ".")


@client.event
async def on_ready():
   print('bot online')

@client.command()
async def actualizar(ctx):
  await ctx.send("Datos actualizados :blush:")
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
async def player_1(ctx):
   await ctx.send(promedio)
   os.execv(sys.executable, ['python'] + sys.argv)
   
@client.command()
async def player_2(ctx):
   await ctx.send(promedio_2)
   os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
async def player_3(ctx):
   await ctx.send(promedio_3) 
   os.execv(sys.executable, ['python'] + sys.argv)

client.run('token')   