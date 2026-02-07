# Day 3 课堂练习

import time
import random

# ---------------------------------------------------------
# 练习 1: if 条件判断
# 题目: 判断闰年
# 规则: 能被4整除且不能被100整除，或能被400整除
# ---------------------------------------------------------
print("--- 练习 1: 判断闰年 ---")
year = 2024





# ---------------------------------------------------------
# 练习 2: for 循环
# 题目: 打印九九乘法表 (右上三角形)
# 预期输出:
# 1x1=1
# 1x2=2  2x2=4
# 1x3=3  2x3=6  3x3=9
# ...
# ---------------------------------------------------------
print("\n--- 练习 2: 九九乘法表 ---")
# 在这里写代码:




# ---------------------------------------------------------
# 练习 3: 函数设计
# 题目: 温度转换器
# 定义函数 convert_temp(value, unit="C")
# - 如果 unit="C", 转为华氏度 (F = C * 9/5 + 32)
# - 如果 unit="F", 转为摄氏度 (C = (F - 32) * 5/9)
# - 返回转换后的值
# ---------------------------------------------------------
print("\n--- 练习 3: 温度转换 ---")
# 在这里写代码:




# 测试:
# print(convert_temp(0, "C"))    # 应输出 32.0
# print(convert_temp(32, "F"))   # 应输出 0.0

# ---------------------------------------------------------
# 练习 4: while 循环
# 题目: 猜数字游戏
# 1. 生成1-100的随机数
# 2. 用户输入猜测 (用 input() 或直接给值测试)
# 3. 如果猜对，打印 "恭喜！" 并退出
# 4. 如果没猜对，提示"太大"或"太小"
# ---------------------------------------------------------
print("\n--- 练习 4: 猜数字 ---")
# 在这里写代码:




# ---------------------------------------------------------
# 练习 5: 判断质数
# 定义函数 is_prime(n)
# 质数: 只能被1和自己整除的数 (2, 3, 5, 7, 11...)
# 提示: 用 for 循环从 2 到 n-1，检查是否有能整除的数
# ---------------------------------------------------------
print("\n--- 练习 5: 判断质数 ---")
# 在这里写代码:




# 测试:
# print(is_prime(7))   # True
# print(is_prime(10))  # False
# print(is_prime(13))  # True

# ---------------------------------------------------------
# 练习 6: *args 可变参数
# 定义函数 find_max(*nums)
# 返回所有参数中的最大值
# 不允许使用内置 max() 函数
# ---------------------------------------------------------
print("\n--- 练习 6: 找最大值 ---")
# 在这里写代码:




# 测试:
# print(find_max(3, 7, 2, 9, 5))  # 9
# print(find_max(100, 50))        # 100

# ---------------------------------------------------------
# [挑战题] 随机密码生成器
# 定义函数 generate_password(length=8, use_special=False)
# - 密码包含大小写字母、数字
# - 如果 use_special=True，还要包含特殊字符 (!@#$%^&*)
# 提示: 
# import string
# chars = string.ascii_letters + string.digits
# random.choice(chars)
# ---------------------------------------------------------
print("\n--- 挑战题: 密码生成器 ---")
# 在这里写代码:




# 测试:
# print(generate_password(12))           # 例如: Kx7pQm2Lv9As
# print(generate_password(10, True))     # 例如: K!7pQ@2Lv9


# =========================================================
# ======================== 参考答案 ========================
# =========================================================

# --- 练习 1 ---
# is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# print(f"{year} 是闰年" if is_leap else f"{year} 不是闰年")

# --- 练习 2 ---
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}x{i}={i*j}", end="\t")
#     print()  # 换行

# --- 练习 3 ---
# def convert_temp(value, unit="C"):
#     if unit == "C":
#         return value * 9/5 + 32
#     elif unit == "F":
#         return (value - 32) * 5/9
#     else:
#         return "未知单位"

# --- 练习 4 ---
# secret = random.randint(1, 100)
# while True:
#     guess = int(input("猜一个数字 (1-100): "))
#     if guess == secret:
#         print("恭喜！猜对了！")
#         break
#     elif guess < secret:
#         print("太小了")
#     else:
#         print("太大了")

# --- 练习 5 ---
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# --- 练习 6 ---
# def find_max(*nums):
#     if not nums:
#         return None
#     max_val = nums[0]
#     for n in nums:
#         if n > max_val:
#             max_val = n
#     return max_val

# --- 挑战题 ---
# import string
# def generate_password(length=8, use_special=False):
#     chars = string.ascii_letters + string.digits
#     if use_special:
#         chars += "!@#$%^&*"
#     
#     password = ""
#     for _ in range(length):
#         password += random.choice(chars)
#     return password
