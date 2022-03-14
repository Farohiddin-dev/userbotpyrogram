from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ChatType
from loader import dp, app


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")


@dp.message_handler(commands='clear')
async def clear_gr(message: types.message):
    await message.answer("O'chirilmoqda....")
    for x in reversed(range(35000, 49792)):
        try:
            await app.delete_messages(-1001139797433, x)
        except Exception as e:
            print(e)


@dp.message_handler(chat_type=ChatType.SUPERGROUP, text_contains='del')
async def get_msg_id(msg: types.Message):
    print('working')
    chat_id = msg.chat.id
    msg_id = msg.reply_to_message.message_id
    # await msg.answer('Deleting...')
    # for mm in app.search_messages(chat_id=chat_id, filter='photo'):
    #     try:
    #         await app.delete_messages(chat_id=chat_id, message_ids=mm.message_id)
    #     except:
    #         pass
    # await app.send_message(chat_id, 'Deleting')
    for x in reversed(range(30000, msg_id+1)):
        try:
            await app.delete_messages(-1001139797433, x)
        except Exception as e:
            print(e)