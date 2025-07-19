import os
import asyncio
import threading
from flask import Flask
from bot import Bot  # assuming your bot.py has Bot class with async .run()

# Fake Flask server to bind port for Render
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "✅ Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ bot is live."

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

# Run Flask in a thread
threading.Thread(target=run_flask).start()

# Run your async bot on main thread (Render needs this)
async def main():
    app = Bot()  # Your bot class instance
    await app.run()  # This should be an async method

if __name__ == "__main__":
    asyncio.run(main())
