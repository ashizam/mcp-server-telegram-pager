# Telegram Pager MCP Server

A specialized [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that allows AI coding assistants (like Cursor, Cline, or Claude Desktop) to send direct messages via your personal Telegram account.

**Security First:** This server exposes exactly *one* tool (`send_telegram_message`). It is intentionally designed as a "Telegram Pager", meaning the AI cannot read your chat history, delete messages, or view your contacts.

## Prerequisites

To use this, you need a Telegram API ID and Hash.
1. Log in to [my.telegram.org/apps](https://my.telegram.org/apps).
2. Create an application (if you haven't already).
3. Copy your `App api_id` and `App api_hash`.

## Installation & Setup

1. **Clone the repository and install dependencies:**
   ```bash
   git clone https://github.com/ashizam/mcp-server-telegram-pager.git
   cd mcp-server-telegram-pager
   pip install -e .
   ```

2. **Generate your Session String:**
   Because Telegram requires 2FA (a login code sent to your app), you must generate an authentication session string locally first.
   ```bash
   python -m mcp_server_telegram_pager.generate_session
   ```
   *Follow the prompts to enter your API ID, Hash, and Login Code. Copy the long session string it outputs!*

## Configuring your MCP Client

Add the following to your IDE's MCP configuration file (e.g., in Cursor or Claude Desktop):

```json
{
  "mcpServers": {
    "telegram-pager": {
      "command": "mcp-server-telegram-pager",
      "env": {
        "TELEGRAM_API_ID": "YOUR_API_ID_HERE",
        "TELEGRAM_API_HASH": "YOUR_API_HASH_HERE",
        "TELEGRAM_SESSION": "YOUR_LONG_SESSION_STRING_HERE"
      }
    }
  }
}
```

## How to Test
Once configured, you can ask your AI assistant:
> "Send a Telegram message to username 'jakethesnake' saying 'The build finished successfully!'"

*(Note: Do not include the `@` symbol in the username).*
