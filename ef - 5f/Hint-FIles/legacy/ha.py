import sys
import time
import os

def pause():
    os.system("pause>nul")

def tpw(text, speed=2):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(speed / 50)

def yn():
    while True:
        to = input("Y/N:")
        if to == "y" or to == "Y":
            break
        elif to == "n" or to == "N":
            quit
        else:
            tpw("잘못된 입력값입네다.\n\n")

def answer(a):
    to = input("번호 입력:")
    to = int(to)
    if to == a:
        tpw("정답.\n\n")
        pause()
    else:
        tpw("오답.\n\n")
        pause()
        quit