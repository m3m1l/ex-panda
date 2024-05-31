"""
Wersja beta 0.1
Developed by Email Zelman
"""

import keyboard

abbrv_dict = {
    'txt' : 'put your text here',
    'txt2' : 'put your text here.',
    'txt3' : 'put your text there!'
}


print('=========================Loading abbreviation list...====================\n\n')


for (abbrv, target) in abbrv_dict.items():
    keyboard.add_abbreviation(abbrv, target)
    print('abbrv :', abbrv, 'target :', target)


print('\n\n=========================Loading finished====================')


keyboard.wait()
