import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

from states import MachStates
from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7082820861:AAGGd2Rpln7OBKqfWXmfChdS7F29mm5OxIk")
dp = Dispatcher()

from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder

@dp.message(Command("menu"))
async def cmd_help(message: types.Message):
    await message.answer(
        "/start - menu\n"
        "/roll - Рандомное число 1 до 100\n"
        "/test - тест команд\n"
        "/mach - калькулятор"

    )

@dp.message(Command("start"))
async def cmd_buttons(messege: types.Message, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='/start'))
    builder.add(types.KeyboardButton(text='/menu'))
    builder.row(types.KeyboardButton(text='/roll'))
    builder.add(types.KeyboardButton(text='/test'))
    builder.add(types.KeyboardButton(text='/mach'))
    builder.row(types.KeyboardButton(text='menu_stop'))

    for i in range(10):
        button = types.KeyboardButton(text=f'{i + 1}')
        if not i:
            builder.row(button)
        else:
            builder.add(button)



    keyboard_markup = builder.as_markup(
        resize_keyboard=True

    )
    await messege.answer('Кнопки додано', reply_markup=keyboard_markup)



@dp.message(Command("mach"))
async def cmd_mach(message: types.Message, state: FSMContext ):
    await message.answer('Введіть перше число: ')
    await state.set_state(MachStates.first_number)


@dp.message(MachStates.first_number)
async def get_first_number(message: types.Message, state: FSMContext):
    await message.answer(f'Ви вели {message.text}')
    await state.update_data(num_1=message.text)
    await message.answer('Введіть друге число: ')
    await state.set_state(MachStates.second_number)

@dp.message(MachStates.second_number)
async def get_second_number(message: types.Message, state: FSMContext):
    await message.answer(f'Ви вели {message.text}')
    data = await state.get_data()
    num_1 = int(data['num_1'])
    num_2 = int(message.text)
    await message.answer(f'{num_1} + {num_2} = {num_1 + num_2}')
    await state.clear()

@dp.message(F.text.in_(("menu_stop")))
async def onclick_button_1(message: types.Message, state: FSMContext ):
    await message.answer(f'Ви натиснули кнопку {message.text}',
                         reply_markup=types.ReplyKeyboardRemove())

# @dp.message(F.text == "1")
# async def onclick_button_1(message: types.Message, state: FSMContext ):
#     await message.answer('Ви натиснули кнопку 1')

@dp.message(Command("roll"))
async def cmd_roll(message: types.Message, command: CommandObject):
    max_value = 100
    if command.args and command.args[0].isdigit():
        max_value = min(int(command.args[0]), 50)

    random_number = random.randint(1, max_value)
    await message.answer(f"Випадкове число від 1 до {max_value}: {random_number}")

@dp.message(Command("test"))
async def cmd_test(message: types.Message, command: CommandObject):
    if command.args is not None:
      args = command.args.split()
      await message.answer(f'Параметри команди ({len(args)}): {args}')
    else:
      await message.answer("Команда без параметрів")



@dp.message()
async def get_message(message: types.Message):
    print(f'{message.from_user.full_name} (id: {message.from_user.id}): {message.text}')
    await message.answer('Повідомлення Отримано!')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())