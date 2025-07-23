import os
import asyncio
import threading
from flask import Flask
from bot import Bot

# Create Flask app for Render/uptime monitoring
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "✅ Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ bot is live."

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

# Run Flask in background
threading.Thread(target=run_flask).start()

# Your async main
async def main():
    app = Bot()
    await app.start()
    await asyncio.Event().wait()  # Keep the bot running forever

# Safe async run
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        print(f"[!] RuntimeError: {e}")
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
