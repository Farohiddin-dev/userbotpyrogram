from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, app
from keyboards.inline.buttons import btn


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"<b>Men bilan muloqot qilish uchun\ntugmalardan foydalaning</b>", reply_markup=btn)
    await app.send_message('me', message.text)


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"<b>Men bilan muloqot qilish uchun\ntugmalardan foydalaning</b>", reply_markup=btn)
