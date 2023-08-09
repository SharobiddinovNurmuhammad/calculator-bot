import logging

from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import calcMenu
from functions import calculator

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        text="Assalomu alaykum Calculator botga xush kelibsiz!"
    )

@dp.message_handler(commands='calculator')
async def send_welcome(message: types.Message):
    await message.answer(
        text="0", reply_markup=calcMenu
    )

@dp.callback_query_handler()
async def on_calculator(call: types.CallbackQuery):
    text = call.message.text
    value = call.data
    data = await calculator(
      value=value, text=text  
    )
    if data==False:
        await call.message.edit_text(text='0', reply_markup=calcMenu)
        await call.answer(cache_time=0)
    else:
        await call.message.edit_text(text=data, reply_markup=calcMenu)
        await call.answer(cache_time=0)

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)