# Day 1 实战练习 & 答案
import random

# ---------------------------------------------------------
# 练习 1: 高级计算器
# 让用户输入两个数字和一个运算符 (+, -, *, /)
# 根据运算符计算结果。如果除数为0，提示错误。
# ---------------------------------------------------------
print("--- 练习 1 ---")
# 在这里写代码:




# ---------------------------------------------------------
# 练习 2: 猜数字 (While循环)
# 随机生成 1-100 的数字。
# 用户不断猜，提示大了/小了，直到猜对。
# 猜对后打印尝试次数。
# ---------------------------------------------------------
print("\n--- 练习 2 ---")
# 在这里写代码:




# ---------------------------------------------------------
# [挑战题] 剪刀石头布 (三局两胜)
# 1. 电脑随机出 (可以用数字 0/1/2 代表)
# 2. 玩家输入 (Rock/Scissors/Paper) 或 对应数字
# 3. 记录 player_score 和 computer_score
# 4. 循环直到某方达到 2 分
# ---------------------------------------------------------
print("\n--- 挑战题 ---")
# 在这里写代码:





# ---------------------------------------------------------
# 练习 3: 数组处理大神 (列表与数学)
# 输入一组用空格隔开的任意数字 (例如: "1 2 3 4 5")
# 1. 输出这组数的反向数组
# 2. 计算平均值
# 3. 统计有多少个奇数，多少个偶数
# [附加题] 统计有多少个质数 (Prime Number)
# ---------------------------------------------------------
print("\n--- 练习 3 ---")
# 在这里写代码:





# =========================================================
# ======================== 参考答案 ========================
# =========================================================

# --- 练习 1 ---
# n1 = float(input("数字1: "))
# n2 = float(input("数字2: "))
# op = input("运算符(+, -, *, /): ")
# if op == '+': print(n1 + n2)
# elif op == '-': print(n1 - n2)
# elif op == '*': print(n1 * n2)
# elif op == '/':
#     if n2 == 0: print("不能除以0")
#     else: print(n1 / n2)
# else: print("无效运算符")

# --- 练习 2 ---
# target = random.randint(1, 100)
# count = 0
# while True:
#     guess = int(input("猜个数字: "))
#     count += 1
#     if guess > target: print("大了")
#     elif guess < target: print("小了")
#     else:
#         print(f"对了！你猜了 {count} 次")
#         break

# --- 挑战题 ---
# p_score = 0
# c_score = 0
# options = ["石头", "剪刀", "布"]
# 
# print("游戏开始！谁先赢2局谁获胜。")
# 
# while p_score < 2 and c_score < 2:
#     # 0=石头, 1=剪刀, 2=布
#     # 赢的逻辑: (0胜1), (1胜2), (2胜0) -> 即 (玩家-电脑)==-1 或 2
#     
#     c_choice = random.randint(0, 2)
#     p_input = int(input("请出拳 (0=石头, 1=剪刀, 2=布): "))
#     
#     print(f"电脑出了: {options[c_choice]}, 你出了: {options[p_input]}")
#     
#     if p_input == c_choice:
#         print("平局")
#     elif (p_input == 0 and c_choice == 1) or \
#          (p_input == 1 and c_choice == 2) or \
#          (p_input == 2 and c_choice == 0):
#         print("你赢了这一局！")
#         p_score += 1
#     else:
#         print("电脑赢了这一局！")
#         c_score += 1
#         
#     print(f"当前比分 - 玩家 {p_score} : {c_score} 电脑\n")
# 
# if p_score > c_score:
#     print("=== 最终胜利者：玩家！ ===")
# else:
#     print("=== 最终胜利者：电脑！ ===")

# --- 练习 3 ---
# num_str = input("请输入一组数字 (用空格隔开): ")
# nums = [int(x) for x in num_str.split()]
# 
# # 1. 反向
# print(f"反向数组: {nums[::-1]}")
# 
# # 2. 平均值
# avg = sum(nums) / len(nums)
# print(f"平均值: {avg:.2f}")
# 
# # 3. 奇偶统计
# odds = 0
# evens = 0
# for n in nums:
#     if n % 2 == 0: evens += 1
#     else: odds += 1
# print(f"奇数: {odds} 个, 偶数: {evens} 个")
# 
# # [附加题] 质数统计
# primes = 0
# for n in nums:
#     if n < 2: continue
#     is_prime = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime: primes += 1
# print(f"质数: {primes} 个")
