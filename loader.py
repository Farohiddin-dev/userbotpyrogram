from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import Database
from data import config
from pyrogram import Client

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
app = Client("iztopar", api_id=config.API_ID, api_hash=config.API_HASH,)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db='data/userbot.db')
