# Day 1 练习参考答案
# 对应 Day_01/exercises.py 中的习题
import random

# =========================================================
# 练习 1: 高级计算器
# =========================================================
print("--- 练习 1: 高级计算器 ---")
try:
    n1 = float(input("数字1: "))
    n2 = float(input("数字2: "))
    op = input("运算符(+, -, *, /): ")
    
    if op == '+':
        print(f"结果: {n1 + n2}")
    elif op == '-':
        print(f"结果: {n1 - n2}")
    elif op == '*':
        print(f"结果: {n1 * n2}")
    elif op == '/':
        if n2 == 0:
            print("错误: 不能除以0")
        else:
            print(f"结果: {n1 / n2}")
    else:
        print("无效运算符")
except ValueError:
    print("输入错误：请输入有效的数字")

print("\n" + "="*30 + "\n")

# =========================================================
# 练习 2: 猜数字 (While循环)
# =========================================================
print("--- 练习 2: 猜数字 ---")
target = random.randint(1, 100)
count = 0
print("我已经想好了一个 1-100 的数字。")

while True:
    try:
        guess_str = input("猜个数字 (输入 q 退出): ")
        if guess_str.lower() == 'q':
            print(f"放弃了？答案是 {target}")
            break
            
        guess = int(guess_str)
        count += 1
        
        if guess > target:
            print("大了")
        elif guess < target:
            print("小了")
        else:
            print(f"恭喜！对了！你猜了 {count} 次")
            break
    except ValueError:
        print("请输入整数！")

print("\n" + "="*30 + "\n")

# =========================================================
# 练习 3: 数组处理大神
# =========================================================
print("--- 练习 3: 数组处理大神 ---")
try:
    num_str = input("请输入一组数字 (用空格隔开): ")
    # 处理空输入的情况
    if not num_str.strip():
        print("未输入任何数字")
    else:
        nums = [int(x) for x in num_str.split()]
        print(f"原始数组: {nums}")

        # 1. 反向
        print(f"反向数组: {nums[::-1]}")

        # 2. 平均值
        if len(nums) > 0:
            avg = sum(nums) / len(nums)
            print(f"平均值: {avg:.2f}")
        else:
            print("数组为空，无法计算平均值")

        # 3. 奇偶统计
        odds = 0
        evens = 0
        for n in nums:
            if n % 2 == 0: evens += 1
            else: odds += 1
        print(f"奇数: {odds} 个, 偶数: {evens} 个")

        # [附加题] 质数统计
        primes = 0
        for n in nums:
            if n < 2: continue
            is_prime = True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime: primes += 1
        print(f"质数: {primes} 个")
except ValueError:
    print("输入错误：请确保输入的都是整数，并用空格隔开")

print("\n" + "="*30 + "\n")

# =========================================================
# [挑战题] 剪刀石头布
# =========================================================
print("--- 挑战题: 剪刀石头布 (三局两胜) ---")
p_score = 0
c_score = 0
options = ["石头", "剪刀", "布"]

print("游戏开始！谁先赢2局谁获胜。")

while p_score < 2 and c_score < 2:
    # 0=石头, 1=剪刀, 2=布
    # 赢的逻辑: (0胜1), (1胜2), (2胜0) -> 即 (玩家-电脑)==-1 或 2
    
    try:
        c_choice = random.randint(0, 2)
        p_input_str = input("请出拳 (0=石头, 1=剪刀, 2=布): ")
        if p_input_str not in ['0', '1', '2']:
            print("请输入 0, 1, 或 2")
            continue
            
        p_input = int(p_input_str)
        
        print(f"电脑出了: {options[c_choice]}, 你出了: {options[p_input]}")
        
        if p_input == c_choice:
            print("平局")
        elif (p_input == 0 and c_choice == 1) or \
             (p_input == 1 and c_choice == 2) or \
             (p_input == 2 and c_choice == 0):
            print("你赢了这一局！")
            p_score += 1
        else:
            print("电脑赢了这一局！")
            c_score += 1
            
        print(f"当前比分 - 玩家 {p_score} : {c_score} 电脑\n")
    except ValueError:
        print("输入无效！")

if p_score > c_score:
    print("=== 最终胜利者：玩家！ ===")
else:
    print("=== 最终胜利者：电脑！ ===")
