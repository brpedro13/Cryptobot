import discord
from requests import Request, Session
import json

intents = discord.Intents.default()
intents.message_content = True
DCTOKEN = "MTEyNzM1NTkyMTkxNjUxNDQ0NQ.G6OMjX.OUiGHyModOso7UPhTSNlI03lXMnDGhEuXKEhSU"

url =  "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

parameters = {
    'slug':'bitcoin,ethereum,monero',
    'convert':'USD'
}

headers = {
    'Accepts' : 'application/json',
    'X-CMC_PRO_API_KEY' : 'a9a476de-82aa-4861-9540-2063bb7037cf'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)

client = discord.Client(intents=intents)

def calculate_value(quantity, value):
    return round(quantity * value, 2)

# Get cryptocoins value from CoinMarketCap.com
bitcoin = (json.loads(response.text))['data']['1']['quote']['USD']['price']
bitcoin = round(bitcoin, 2)
ethereum = (json.loads(response.text))['data']['1027']['quote']['USD']['price']
ethereum = round(ethereum, 2)
monero = (json.loads(response.text))['data']['328']['quote']['USD']['price']
monero = round(monero, 2)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/.help"):
        help_message = """
        Hello! I'm a bot capable of listing the prices of the following cryptocurrencies:
        
        Bitcoin: `/.bitcoin`
        Ethereum: `/.ethereum`
        Monero: `/.monero`
        
        To get the price of a cryptocurrency, type the corresponding command.
        To calculate a value for a specific quantity, use: `/.value <cryptocurrency> <quantity>`
        Example: `/.value bitcoin 0.1` (to calculate the value of 0.1 Bitcoin)
        """
        await message.channel.send(help_message)

    # Print cryptocoin prices

    if message.content.startswith("/.bitcoin"):
        await message.channel.send(f"Bitcoin price right now: {bitcoin}$")
    if message.content.startswith("/.ethereum"):
        await message.channel.send(f"ethereum price right now: {ethereum}$")       
    if message.content.startswith("/.monero"):
        await message.channel.send(f"monero price right now: {monero}$")
    
      # Print fractioned cryptocoin prices
    if message.content.startswith("/.value"):
        _, cryptocurrency, quantity = message.content.split()
        try:
            quantity = float(quantity)
        except ValueError:
            await message.channel.send("You entered an invalid quantity. Please try again with a numeric value.")
            return
        
        if cryptocurrency not in ["bitcoin", "ethereum", "monero"]:
            await message.channel.send("You entered an incorrect cryptocurrency. Please try again using: Bitcoin, Ethereum, or Monero.")
            return
        
        if cryptocurrency == "bitcoin":
            price = bitcoin
        elif cryptocurrency == "ethereum":
            price = ethereum
        elif cryptocurrency == "monero":
            price = monero
        
        calculated_value = calculate_value(quantity, price)
        await message.channel.send(f"The value of {quantity} {cryptocurrency.capitalize()} is: {calculated_value}$")

client.run(DCTOKEN)