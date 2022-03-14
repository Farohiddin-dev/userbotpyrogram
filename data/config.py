from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot tokeni
ADMINS = env.list("ADMINS")  # Adminlar
API_ID = env.int("API_ID")  # API ID https://my.telegram.org/auth?to=apps  << shu yerdan olinadi
API_HASH = env.str("API_HASH")  # api hash https://my.telegram.org/auth?to=apps << shu yerdan olinadi
IP = env.str("ip")  # localhost deb yozlgan .envda

