import requests
from telegram import Bot
import asyncio

TELEGRAM_BOT_TOKEN = "7527280210:AAHf-QmkgnfDevyLDJnr0SWEjRvJSgClFcA"
CHAT_ID = "162479128"

def fetch_crypto_rates():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    return response.json()

def fetch_uah_rates():
    url = "https://api.exchangerate-api.com/v4/latest/UAH"
    response = requests.get(url)
    data = response.json()
    return {
        "UAH/USD": data["rates"]["USD"],
        "UAH/EUR": data["rates"]["EUR"]
    }

async def send_to_telegram(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    crypto_rates = fetch_crypto_rates()
    uah_rates = fetch_uah_rates()

    message = "📈 **Rates Update**:\n\n"
    message += f"💰 Bitcoin (BTC): ${crypto_rates['bitcoin']['usd']}\n"
    message += f"💎 Ethereum (ETH): ${crypto_rates['ethereum']['usd']}\n"
    message += f"🌟 Solana (SOL): ${crypto_rates['solana']['usd']}\n\n"
    message += f"💵 UAH/USD: {uah_rates['UAH/USD']}\n"
    message += f"💶 UAH/EUR: {uah_rates['UAH/EUR']}"

    asyncio.run(send_to_telegram(message))

if __name__ == "__main__":
    main()
