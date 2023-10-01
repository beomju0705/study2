# 가위바위보 게임 업그레이드
# 이전에 만든 가위바위보 게임을 총 게임횟수와 승리횟수를
# 게임을 다시 실행해도 유지되도록 수정하세요.
import random

def play():
    user = int(input("1. 가위, 2. 바위, 3. 보를 입력하세요 : "))
    com = random.randrange(1,4)
    win = 0

    print()

    if user == 1:
        if com ==2:
            print("패배")
        elif com == 3:
            print("승리")

    if user == 2:
        if com ==1:
            print("승리")
            win += 1
        elif com == 3:
            print("패배")

    if user == 3:
        if com ==1:
            print("패배")
        elif com == 2:
            print("승리")
            win += 1



def write_game():


def read_game():


while True:
    play()

