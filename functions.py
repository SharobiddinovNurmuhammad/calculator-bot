
def on_eval(text: str) -> str:
    try:
        result = eval(text)
        return result
    except:
        return False

def num_writer(value: str, text: str) -> str:
    if text == '0':
        text = value
    else:
        text += value
    return text

def sim_writer(value: str, text: str) -> str:
    if text[-1] in ['/', '*', '+', '-', ',']:
        pass
    elif text == '0':
        pass
    else: 
        text += value
    return text
        
def cal_writer(value: str, text: str) -> str:
    if value == 'ce' or value == 'c':
        text = '0'
    elif value == 'back':
        if text == '0':
            pass
        elif len(text) == 1:
            text = '0'
        else:
            new_text = ''
            for i in range(len(text)-1):
                new_text += text[i]
            text = new_text 
    elif value == ',':
        if text[-1] in ['/', '*', '+', '-']:
            pass
        else:
            text += value
    elif value == 'plms':
        text = '-' + text
    return text

async def calculator(value: str, text: str) -> str:
    if value == 'result':
        return on_eval(text)
    if value in ['/', '*', '+', '-']:
        return sim_writer(value, text)
    elif value in ['ce', 'c', 'back', ',', 'plms']:
        return cal_writer(value, text)
    elif int(value) in range(10):
        return num_writer(value, text)

