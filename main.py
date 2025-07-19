from bot import Bot
from flask import Flask
import os
import threading

# Start your bot
app = Bot()

# Fake web server for Render
web = Flask(__name__)

@web.route('/')
def home():
    return "✅ Bot is running on Render"

# Function to run Flask
def run_flask():
    port = int(os.environ.get("PORT", 5000))
    web.run(host="0.0.0.0", port=port)

# Function to run your bot
def run_bot():
    app.run()

# Run both Flask + Bot in parallel threads
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    threading.Thread(target=run_bot).start()
