from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Izlash đ",callback_data='izlash')
        ],
        [
            InlineKeyboardButton(text="Guruh qo'shish â", callback_data='add_group')
        ],
        [
            InlineKeyboardButton(text="Usernamedan id olish đ", callback_data="username_to_id")
        ]
    ]
)

home_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Orqaga âŠī¸",callback_data='back_home')
        ]
    ]
)