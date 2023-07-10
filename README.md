# Discord Cryptocurrency Price Bot

This is a simple Discord bot that provides the ability to fetch and display the prices of popular cryptocurrencies such as Bitcoin, Ethereum, and Monero. It utilizes the CoinMarketCap API to retrieve the latest cryptocurrency prices in USD.

## Features

- Fetch and display the current prices of Bitcoin, Ethereum, and Monero.
- Calculate the value of a specific quantity of a cryptocurrency.

## Setup

To set up the bot locally, follow these steps:

1. Clone this repository to your local machine.
2. Obtain a Discord bot token and CoinMarketCap API key.
3. Replace the placeholder values for `DCTOKEN` and `cmckey` in the code with your Discord bot token and CoinMarketCap API key, respectively.

## Usage

- Use the command `/.bitcoin` to fetch and display the current price of Bitcoin.
- Use the command `/.ethereum` to fetch and display the current price of Ethereum.
- Use the command `/.monero` to fetch and display the current price of Monero.
- Use the command `/.value <cryptocurrency> <quantity>` to calculate the value of a specific quantity of a cryptocurrency. For example, `/.value bitcoin 0.1` will calculate the value of 0.1 Bitcoin.

