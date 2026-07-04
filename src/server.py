import os
import asyncio
from mcp.server.fastmcp import FastMCP
from telethon import TelegramClient
from telethon.sessions import StringSession

# Initialize the MCP server
# This creates a server that exposes ONLY the tools defined below.
mcp = FastMCP("Telegram Pager")

@mcp.tool()
async def send_telegram_message(username: str, message: str) -> str:
    """
    Send a direct message to a Telegram user.
    Do not use the @ symbol in the username (e.g. use 'jakethesnake', not '@jakethesnake').
    """
    api_id = os.environ.get("TELEGRAM_API_ID")
    api_hash = os.environ.get("TELEGRAM_API_HASH")
    session_str = os.environ.get("TELEGRAM_SESSION")

    if not all([api_id, api_hash, session_str]):
        return "Error: TELEGRAM_API_ID, TELEGRAM_API_HASH, and TELEGRAM_SESSION environment variables must be set."

    try:
        # Connect using the pre-authenticated session string
        client = TelegramClient(StringSession(session_str), int(api_id), api_hash)
        await client.connect()

        if not await client.is_user_authorized():
            await client.disconnect()
            return "Error: Session is invalid or expired. Please generate a new session string."

        # Send the message (this is the ONLY capability the AI has access to)
        await client.send_message(username, message)
        await client.disconnect()
        
        return f"Successfully sent message to {username}."

    except Exception as e:
        return f"Failed to send message: {str(e)}"

def main():
    """Entry point for the package console script."""
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
