# Final project for course 'Python for Developers'

The main goal to create a script that would:
- fetch rates for Bitcoin (BTC), Etherium (ETC) and Solana (SOL) 
- fetch rates for ukrainian hryvna UAH/USD and UAH/EUR
- send all fetched info to selected Telegram channel


### Setup environment
 - python -m venv venv
 - source venv/bin/activate
 - pip install requests python-telegram-bot

### Create telegram bot
1. Open Telegram and search for "BotFather."
2. Use /newbot to create a new bot and get the API token.
3. Go to created bot and write any message
4. Fetch CHAT_ID from https://api.telegram.org/bot<your_bot_token>/getUpdates
5. Past TELEGRAM_BOT_TOKEN and CHAT_ID in the .env