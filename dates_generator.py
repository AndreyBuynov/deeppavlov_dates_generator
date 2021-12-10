from datetime import date
import random
from num2words import num2words

months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

def ch_aux(word):
    word = num2words(word, lang='ru', to='ordinal')
    if word.split()[-1] == 'третий':
        return word[:-2] + 'ьего'
    else:
        return word[:-2] + 'ого'

def dates_generator(cnt: int, start_date=None, end_date=None):
    if start_date:
        start_date = start_date.toordinal()
    else:
        start_date = date.today().replace(day=1, month=1, year=1980).toordinal()
        
    if end_date:
        end_date = end_date.toordinal()
    else:
        end_date = date.today().toordinal()
        
    result = []
    
    for i in range(cnt):
        random_day = date.fromordinal(random.randint(start_date, end_date))
        year = random_day.strftime("%Y")
        month = random_day.strftime("%m")
        day = random_day.strftime("%d")
        result.append(ch_aux(day) + ' ' + months.get(str(month)) + ' ' + ch_aux(year) + ' года')
        
    return result
