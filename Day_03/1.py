import random

def generate_secret():
    # 请在这里写代码
    return random.randint(1,100)

def get_guess():
    # 请在这里写代码
    return int(input('请输入猜测值'))

def check_guess(guess, secret):
    # 请在这里写代码
    if guess>secret:
        print('太大')
        return 1
        
    elif guess<secret:
        print('太小')
        return -1
    else:
        print('恭喜')
        return 0

def play_game():
    # 请在这里写代码
    secret=generate_secret()
    guess=get_guess()
    result=-1
    while result!=0:
        guess=get_guess()
        result=check_guess(guess, secret)
        if result==0:
            break

play_game()   