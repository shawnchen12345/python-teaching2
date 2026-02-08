# Day 3 课后作业 - Python 函数入门
# 本作业基于 lecture.md 课后作业部分
# 完成所有题目后，运行此文件测试你的答案

# ===========================================================
# 作业 1: 判断素数 (综合运用: 函数定义 + 返回值 + 循环)
# ===========================================================
# 题目:
# 定义函数 is_prime(n)，判断 n 是否为素数
# - 素数定义: 大于1的自然数，只能被1和自己整除
# - 如果是素数返回 True，否则返回 False
#
# 提示:
# - 2 是最小的素数
# - 可以用 for 循环从 2 到 n-1 检查是否有因数
# - 如果 n % i == 0，说明 n 能被 i 整除，不是素数

def is_prime(n):
    # 请在这里写代码
    if n<=1:
        return('不是素数')
        
    for x in range(2,n-1):
        if n%x==0:
            return '不是素数'
    return '是素数'
        
          

print("=" * 50)
print("作业 1 测试: 判断素数")
print("=" * 50)
# 取消下面的注释来测试
print(f"is_prime(2) = {is_prime(2)}")    # True
print(f"is_prime(7) = {is_prime(7)}")    # True
print(f"is_prime(10) = {is_prime(10)}")  # False
print(f"is_prime(1) = {is_prime(1)}")    # False


# ===========================================================
# 作业 2: 计算圆面积 (默认参数)
# ===========================================================
# 题目:
# 定义函数 circle_area(r, pi=3.14)
# - r: 圆的半径
# - pi: 圆周率，默认值 3.14
# - 返回圆的面积 (公式: π × r²)

def circle_area(r, pi=3.14):
    # 请在这里写代码
    pass


print("\n" + "=" * 50)
print("作业 2 测试: 圆面积")
print("=" * 50)
# 取消下面的注释来测试
# print(f"circle_area(5) = {circle_area(5)}")           # 78.5
# print(f"circle_area(5, 3.14159) = {circle_area(5, 3.14159)}")  # 更精确


# ===========================================================
# 作业 3: 秒数转时间 (多返回值 / 字符串格式化)
# ===========================================================
# 题目:
# 定义函数 seconds_to_time(total_seconds)
# - 将秒数转换为 "时:分:秒" 格式的字符串
# - 例如: 3665秒 → "1:1:5"
#
# 提示:
# - 1小时 = 3600秒
# - 1分钟 = 60秒
# - 用 // (整除) 和 % (取余) 运算符
#   hours = total_seconds // 3600
#   remaining = total_seconds % 3600
#   minutes = remaining // 60
#   seconds = remaining % 60

def seconds_to_time(total_seconds):
    # 请在这里写代码
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return f'{hours}:{minutes}:{seconds}'

print("\n" + "=" * 50)
print("作业 3 测试: 秒数转时间")
print("=" * 50)

print(f"seconds_to_time(3665) = {seconds_to_time(3665)}")  # 1:1:5
print(f"seconds_to_time(7322) = {seconds_to_time(7322)}")  # 2:2:2
print(f"seconds_to_time(60) = {seconds_to_time(60)}")      # 0:1:0


# ===========================================================
# 作业 4: 猜数字游戏 (函数化重构)
# ===========================================================
# 题目:
# 用函数的方式重构"猜数字游戏"，要求定义以下函数:
#
# 1. generate_secret() - 生成1-100的随机数并返回
# 2. get_guess() - 获取用户输入并返回整数
# 3. check_guess(guess, secret) - 比较猜测和答案
#    - 猜对返回 0
#    - 猜小了返回 -1
#    - 猜大了返回 1
# 4. play_game() - 主游戏函数，组合上面的函数实现完整游戏

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
        return 1
    elif guess<secret:
        return -1
    else:
        return 0

def play_game():
    # 请在这里写代码
    generate_secret()
    get_guess()
    check_guess(guess, secret)
    while check_guess(guess, secret)!=0:
        get_guess()
        check_guess(guess, secret)
    if check_guess(guess, secret)==0:
    break

    


print("\n" + "=" * 50)
print("作业 4: 猜数字游戏")
print("=" * 50)
# 取消下面的注释来运行游戏
# play_game()


# ===========================================================
# [挑战题] 递归计算斐波那契数列
# ===========================================================
# 题目:
# 斐波那契数列: 1, 1, 2, 3, 5, 8, 13, 21, ...
# 规律: F(n) = F(n-1) + F(n-2)，其中 F(1)=1, F(2)=1
#
# 定义函数 fibonacci(n)，用递归计算第 n 个斐波那契数
#
# 提示:
# - 终止条件: if n <= 2: return 1
# - 递归调用: return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    # 请在这里写代码
    if n <= 2: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


print("\n" + "=" * 50)
print("挑战题: 斐波那契数列")
print("=" * 50)
# 取消下面的注释来测试
print(f"fibonacci(1) = {fibonacci(1)}")   # 1
print(f"fibonacci(5) = {fibonacci(5)}")   # 5
print(f"fibonacci(10) = {fibonacci(10)}") # 55



