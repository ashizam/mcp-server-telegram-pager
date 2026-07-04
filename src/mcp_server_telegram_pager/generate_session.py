import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("=======================================")
print(" Telegram Session Generator")
print("=======================================\n")
print("1. Go to https://my.telegram.org/apps and log in.")
print("2. Copy your App api_id and App api_hash.\n")

api_id = input("Enter your API_ID: ").strip()
api_hash = input("Enter your API_HASH: ").strip()

print("\nConnecting to Telegram... (You will receive a login code on your Telegram app)")

# Create an in-memory string session
with TelegramClient(StringSession(), int(api_id), api_hash) as client:
    print("\n✅ Authentication Successful!")
    print("\n=======================================")
    print(" YOUR SESSION STRING (KEEP THIS SECRET)")
    print("=======================================\n")
    print(client.session.save())
    print("\n=======================================")
    print("Copy the long string above. You will need it for your MCP config.")
