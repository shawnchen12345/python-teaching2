# Day 3 实战练习 & 答案
import time
import random

# ---------------------------------------------------------
# 练习 1: 参数与返回值
# 定义函数 get_grade(score)，根据分数返回 'A', 'B', 'C', 'D'
# 并在外面调用测试
# ---------------------------------------------------------
print("--- 练习 1 ---")
# 在这里写代码:




# ---------------------------------------------------------
# 练习 2: 倒计时器
# 定义函数 countdown(seconds)
# 每隔一秒打印剩余时间，最后打印 "Time's up!"
# 提示: time.sleep(1)
# ---------------------------------------------------------
print("\n--- 练习 2 ---")
# 在这里写代码:




# ---------------------------------------------------------
# [挑战题] 随机密码生成器
# 定义函数 generate_password(length)
# 密码包含大写字母、小写字母、数字
# 提示: 
# import string
# chars = string.ascii_letters + string.digits
# random.choice(chars)
# ---------------------------------------------------------
print("\n--- 挑战题 ---")
# 在这里写代码:





# =========================================================
# ======================== 参考答案 ========================
# =========================================================

# --- 练习 1 ---
# def get_grade(score):
#     if score >= 90: return 'A'
#     elif score >= 80: return 'B'
#     elif score >= 60: return 'C'
#     else: return 'D'
# print(get_grade(85))

# --- 练习 2 ---
# def countdown(n):
#     for i in range(n, 0, -1):
#         print(f"{i}...")
#         time.sleep(1)
#     print("Time's up!")
# countdown(3)

# --- 挑战题 ---
# import string
# def generate_password(length=8):
#     chars = string.ascii_letters + string.digits # 所有字母和数字
#     pwd = ""
#     for _ in range(length):
#         pwd += random.choice(chars)
#     return pwd
# 
# print(f"生成的密码: {generate_password(12)}")
