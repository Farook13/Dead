import os
import sys
import glob
import importlib
import logging
import logging.config
import pytz
import asyncio
from pathlib import Path
from datetime import date, datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from aiohttp import web
from pyrogram import Client, idle
from pyromod import listen

from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from Script import script
from plugins import web_server
from bot import TheBlackBot
from util.keepalive import ping_server
from bot.clients import initialize_clients

# Environment-based PORT (default to 8080 if not set)
PORT = int(os.environ.get("PORT", 8080))

# Health check server
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running!')

def run_health_server():
    server = HTTPServer(('0.0.0.0', 8085), HealthCheckHandler)
    server.serve_forever()

Thread(target=run_health_server, daemon=True).start()

# Logging setup
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

# Plugin loading
ppath = "plugins/*.py"
files = glob.glob(ppath)
TheBlackBot.start()
loop = asyncio.get_event_loop()

LOG_STR = "Bot started successfully!"


async def start():
    print('\nInitalizing Your Bot')
    bot_info = await TheBlackBot.get_me()
    await initialize_clients()

    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("TheBlackXYZ => " + plugin_name)

    if ON_HEROKU:
        asyncio.create_task(ping_server())

    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()

    me = await TheBlackBot.get_me()
    temp.BOT = TheBlackBot
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name

    logging.info(LOG_STR)
    logging.info(script.LOGO)

    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")

    await TheBlackBot.send_message(
        chat_id=LOG_CHANNEL,
        text=script.RESTART_TXT.format(today, time)
    )

    app = web.AppRunner(await web_server())
    await app.setup()
    await web.TCPSite(app, "0.0.0.0", PORT).start()
    await idle()


if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye')