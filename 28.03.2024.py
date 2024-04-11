import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7082820861:AAGGd2Rpln7OBKqfWXmfChdS7F29mm5OxIk")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_help(message: types.Message):
    await message.answer(
        "/start - запуск бота\n"
        "/roll - Рандомное число 1 до 100\n"
        "/test - тест команд"

    )
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