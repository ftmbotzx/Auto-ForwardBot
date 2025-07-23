import os
import asyncio
import threading
from flask import Flask
from pyrogram.idle import idle
from bot import Bot  # make sure Bot is a subclass of pyrogram.Client

# Flask server for keeping the app alive on Render
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "✅ Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ bot is live."

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

# Start Flask in a background thread
threading.Thread(target=run_flask).start()

# Async bot runner
async def start_bot():
    app = Bot()  # Your Bot class must subclass pyrogram.Client
    await app.start()
    print("🤖 Bot started.")
    await idle()  # Keeps the bot running
    await app.stop()
    print("❌ Bot stopped.")

# Run bot (use current event loop or fallback)
if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except RuntimeError as e:
        # Handle "event loop already running" error (optional fallback)
        print(f"[!] RuntimeError caught: {e}")
        loop = asyncio.get_event_loop()
        loop.create_task(start_bot())
        loop.run_forever()
