from loader import dp, app, db
from keyboards.inline.buttons import btn, home_menu
from aiogram.types import CallbackQuery, Message
from states.states import GroupForm
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text_contains="add_group")
async def add_gr_form(call: CallbackQuery):
    try:
        await call.message.delete()
    except:
        pass
    await call.message.answer("Menga guruh nomini yuboring")
    await GroupForm.username.set()


@dp.message_handler(state=GroupForm.username)
async def username(message: Message, state: FSMContext):
    txt = message.text
    try:
         txt2 = await app.get_chat(txt)
         await message.answer(txt2.type)
    except Exception as e:
        print(e)
    async with state.proxy() as data:
        data['username'] = txt.lower()
        try:
            db.add_group(data['username'])
            return await message.answer("Guruh muvaffaqiyatli qo'shildi\nYana guruh qo'shmoqchi"
                                        "bo'sangiz yuborishingiz mumkin", reply_markup=home_menu)
        except:
            return await message.answer("<b>Kechirasiz bu guruh bazada mavjud.</b>\n\n "
                                        "Boshqa guruh qo'shmoqchi bo'lsangiz "
                                        "guruh usernameni yuboring", reply_markup=home_menu)


@dp.callback_query_handler(text_contains="back_home",state=GroupForm.username)
async def add_gr_form(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(f"<b>Asosiy meyudasiz\nKerakli bo'limni tanlang</b>", reply_markup=btn)


@dp.message_handler(state=GroupForm.username)
async def username(message: Message, state: FSMContext):
    txt = message.text
    async with state.proxy() as data:
        data['username'] = txt.lower()
        try:
            db.add_group(data['username'])
            return await message.answer("Guruh muvaffaqiyatli qo'shildi\nYana guruh qo'shmoqchi"
                                        "bo'sangiz yuborishingiz mumkin", reply_markup=home_menu)
        except:
            return await message.answer("Kechirasiz bu guruh bazada mavjud.", reply_markup=home_menu)