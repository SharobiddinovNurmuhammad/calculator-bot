from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboards = {
    'CE': 'ce', 'C': 'c', '🔙': 'back', '➗': '/',
    '7':'7', '8': '8', '9': '9', '✖️': '*',
    '4': '4', '5': '5', '6': '6', '➖': '-',
    '1': '1', '2' : '2', '3' : '3', '➕' : '+',
    '+/-': 'plms', '0': '0', ',': ',', '🟰': 'result'
}

calcMenu = InlineKeyboardMarkup(row_width=4)

for i, k, in keyboards.items():
    buttons = InlineKeyboardButton(text=i, callback_data=k)
    calcMenu.insert(buttons)



