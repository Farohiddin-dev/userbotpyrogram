from aiogram.dispatcher.filters.state import State, StatesGroup


class GroupForm(StatesGroup):
    username = State()
