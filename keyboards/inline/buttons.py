from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Izlash 🔎",callback_data='izlash')
        ],
        [
            InlineKeyboardButton(text="Guruh qo'shish ➕", callback_data='add_group')
        ],
        [
            InlineKeyboardButton(text="Usernamedan id olish 🆔", callback_data="username_to_id")
        ]
    ]
)

home_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Orqaga ↩️",callback_data='back_home')
        ]
    ]
)