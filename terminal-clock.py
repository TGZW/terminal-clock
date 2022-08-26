import time
import os


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

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear') 

def printer(digits):
    def digits_parser(digits): 
        return [''.join(dig.split('\n')[i] for dig in digits) for i in range(ROWS)]
    for row in digits_parser(digits): print(row)

def hour_parser():
    def hour(): return time.strftime("%H:%M:%S",time.localtime())
    return [SYMBOL[i] for i in hour()]

def clock():
    clear_output()
    printer(hour_parser())
    time.sleep(1)

if __name__ == '__main__':
    while True:
        clock()