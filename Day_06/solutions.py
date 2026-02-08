# Day 6 参考答案
# 可以直接运行此文件查看效果

# =========================================================
# 练习 1 & 2: 学生类
# =========================================================
print("--- 练习 1 & 2 ---")
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def say_hi(self):
        print(f"大家好，我是 {self.name}")
        
    def check_pass(self):
        return self.score >= 60

# 测试使用
s1 = Student("Tony", 59)
s2 = Student("Alice", 90)

s1.say_hi()
if s1.check_pass():
    print(f"{s1.name} 及格了")
else:
    print(f"{s1.name} 不及格")

s2.say_hi()
if s2.check_pass():
    print(f"{s2.name} 及格了")
else:
    print(f"{s2.name} 不及格")


# =========================================================
# 练习 3: 计数器类
# =========================================================
print("\n--- 练习 3 ---")
class Counter:
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1
        
    def reset(self):
        self.count = 0
        
    def get_value(self):
        return self.count

# 测试使用
c = Counter()
c.increment()
c.increment()
print(f"当前计数: {c.get_value()}") # 2
c.reset()
print(f"重置后: {c.get_value()}") # 0


# =========================================================
# 挑战题: 电子宠物
# =========================================================
print("\n--- 挑战题 ---")
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0 # 0是不饿
    
    def eat(self):
        self.hunger = max(0, self.hunger - 2)
        print(f"{self.name}: Yummy! (饥饿度: {self.hunger})")
        
    def walk(self):
        self.hunger += 1
        print(f"{self.name}: Running... (饥饿度: {self.hunger})")
        
    def is_starving(self):
        return self.hunger >= 8

# 测试流程
my_pet = Pet("旺财")
# 疯狂散步
for _ in range(9):
    my_pet.walk()
    if my_pet.is_starving():
        print("警告: 宠物快饿死了！")

# 赶紧喂食
my_pet.eat()
my_pet.eat()
