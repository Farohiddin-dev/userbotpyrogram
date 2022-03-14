from aiogram.types import ChatType
from loader import dp, app
from aiogram import types


# @dp.message_handler(chat_type=ChatType.SUPERGROUP)
# async def get_msg_id(msg: types.Message):
#     print('working')
#     chat_id = msg.chat.id
#     msg_id = msg.reply_to_message.message_id
#     await msg.answer('Deleting...')
#     await app.send_message(chat_id, 'Deleting')
#     for x in reversed(range(30000, msg_id+1)):
#         try:
#             await app.delete_messages(-1001139797433, x)
#         except Exception as e:
#             print(e)