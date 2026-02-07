# Day 4 实战练习 & 答案

# ---------------------------------------------------------
# 练习 1: 简单的类
# 定义一个 Car 类
# 属性: brand (品牌), speed (速度, 初始0)
# 方法: accelerate(amount) 加速, brake() 刹车归零
# ---------------------------------------------------------
print("--- 练习 1 ---")
# 在这里写代码:




# ---------------------------------------------------------
# 练习 2: 继承
# 定义一个 ElectricCar (电动车) 继承自 Car
# 新增属性: battery (电池, 0-100)
# 重写 accelerate: 如果 battery > 0 才能加速，且消耗 10 电量
# ---------------------------------------------------------
print("\n--- 练习 2 ---")
# 在这里写代码:




# ---------------------------------------------------------
# [挑战题] 模拟战斗 loop
# 创建一个 Hero 和一个 Monster
# 循环让他们互相攻击，每次攻击后打印双方血量
# 直到一方 HP <= 0，打印胜利者
# ---------------------------------------------------------
print("\n--- 挑战题 ---")
# class Character...
# 在这里写代码:





# =========================================================
# ======================== 参考答案 ========================
# =========================================================

# --- 练习 1 & 2 ---
# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#         self.speed = 0
#     def accelerate(self, amount):
#         self.speed += amount
#         print(f"{self.brand} speed: {self.speed}")
#     def brake(self):
#         self.speed = 0
#         print(f"{self.brand} stopped.")

# class ElectricCar(Car):
#     def __init__(self, brand):
#         super().__init__(brand)
#         self.battery = 100
#     def accelerate(self, amount):
#         if self.battery >= 10:
#             self.speed += amount
#             self.battery -= 10
#             print(f"{self.brand} speed: {self.speed}, Battery: {self.battery}%")
#         else:
#             print("没电了！")

# --- 挑战题 ---
# class Fighter:
#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#     def attack(self, other):
#         other.hp -= self.atk
#         print(f"{self.name} attacks {other.name}, remaining HP: {other.hp}")

# h = Fighter("Hero", 100, 15)
# m = Fighter("Boss", 200, 8)

# while h.hp > 0 and m.hp > 0:
#     h.attack(m)
#     if m.hp <= 0:
#         print("Hero Wins!")
#         break
#     m.attack(h)
#     if h.hp <= 0:
#         print("Monster Wins!")
#         break
