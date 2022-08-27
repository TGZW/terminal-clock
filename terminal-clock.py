from random import randint
import time
import os
from modules.newsheadlines import headlines, LENGTH
from modules.office import title_printer, theoffice

from format import format, bcolors

X = LENGTH+1
Y = 9

VERSION = "1.0.0"
ROWS = 3
SYMBOL = {
    "0": ' __ \n|  |\n|__|',
    "1": '    \n   |\n   |',
    "2": ' __ \n __|\n|__ ',
    "3": ' __ \n __|\n __|',
    "4": '    \n|__|\n   |',
    "5": ' __ \n|__ \n __|',
    "6": ' __ \n|__ \n|__|',
    "7": ' __ \n   |\n   |',
    "8": ' __ \n|__|\n|__|',
    "9": ' __ \n|__|\n   |',
    ":": ' \n.\n.'
}

def resize_window():
    try:
        os.system(f'mode con: cols={X} lines={Y}')
    except: pass

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear') 

def printer(digits):
    def digits_parser(digits): 
        return [''.join(dig.split('\n')[i] for dig in digits) for i in range(ROWS)]
    for row in digits_parser(digits): print(row)

def hour_parser():
    def hour(): return time.strftime("%H:%M:%S",time.localtime())
    return [SYMBOL[i] for i in hour()]

def telepromter(i,h):
    if len(h) < i+LENGTH:
        i = 0
        h = headlines()[:35]
    yield h[i:i+LENGTH]
    yield from telepromter(i+1,h)

heads = headlines()
# index_init = heads.find("|", randint(0,len(heads)))
# teleprom = telepromter(0,heads[index_init:])

def telepromt(heads):
    index = int(time.time()*5) % len(heads)
    return heads[index:index+LENGTH]

def main():
    clear_output()
    format("the terminal clock  v"+VERSION, bcolors.HEADER)
    printer(hour_parser())
    print()
    # print(next(teleprom))
    format(telepromt(heads), bcolors.WARNING)
    format(title_printer(theoffice), bcolors.BOLD)
    print(telepromt(theoffice[0]['script']))
    time.sleep(0.25)

if __name__ == '__main__':
    resize_window()
    while True:
        main()