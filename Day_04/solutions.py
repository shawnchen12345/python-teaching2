# Day 4 参考答案
# 可以直接运行此文件查看效果
import math

# =========================================================
# 练习 1: 定义简单的函数
# =========================================================
print("--- 练习 1 ---")
def say_hi(name, msg="你好"):
    print(f"{msg}, {name}")

# 测试
say_hi("Tony")
say_hi("Alice", "Welcome")

# =========================================================
# 练习 2: 计算圆的面积
# =========================================================
print("\n--- 练习 2 ---")
def circle_area(radius):
    return math.pi * radius * radius

# 测试
r = 5
print(f"半径{r}的圆面积是: {circle_area(r):.2f}")

# =========================================================
# 练习 3: 找最大值
# =========================================================
print("\n--- 练习 3 ---")
def find_max(num_list):
    if not num_list: return None
    max_val = num_list[0]
    for num in num_list:
        if num > max_val:
            max_val = num
    return max_val

# 测试
nums = [10, 5, 99, 2, 45]
max_num = find_max(nums)
print(f"列表 {nums} 中最大值是: {max_num}")

# =========================================================
# 练习 4: 剪刀石头布
# =========================================================
print("\n--- 练习 4 ---")
def check_win(player, computer):
    if player == computer:
        return "平局"
    elif (player == "r" and computer == "s") or \
         (player == "s" and computer == "p") or \
         (player == "p" and computer == "r"):
        return "玩家胜"
    else:
        return "电脑胜"

# 测试
print("Player: r, Computer: s ->", check_win("r", "s"))
print("Player: s, Computer: r ->", check_win("s", "r"))

# =========================================================
# 挑战题: 质数判断
# =========================================================
print("\n--- 挑战题 ---")
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 测试
print("7是质数吗?", is_prime(7))
print("10是质数吗?", is_prime(10))
