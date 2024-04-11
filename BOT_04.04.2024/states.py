from aiogram.fsm.state import StatesGroup, State

class MachStates(StatesGroup):
    first_number = State()
    second_number = State()
