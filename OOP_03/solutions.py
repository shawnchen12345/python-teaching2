# ===================================================================
# OOP 第3课：继承与多态 —— 参考答案
# ===================================================================
import random
import math
from abc import ABC, abstractmethod


# ===================================================================
# 练习 1: 动物王国
# ===================================================================
print("=== 练习 1: 动物王国 ===")

class Animal:
    def __init__(self, name, age, sound="..."):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        print(f"{self.name} 说: {self.sound}")

    def info(self):
        print(f"我是{self.name}, 今年{self.age}岁")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "汪汪汪")
        self.breed = breed

    def speak(self):
        print(f"{self.name}(品种:{self.breed}): 汪汪汪！🐕")

    def fetch(self, item):
        print(f"{self.name} 捡起了 {item}")


class Cat(Animal):
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age, "喵喵~")
        self.indoor = indoor

    def speak(self):
        location = "室内" if self.indoor else "室外"
        print(f"{self.name}({location}猫): 喵喵~ 🐱")

    def scratch(self):
        print(f"{self.name} 在磨爪子")


class Parrot(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "啾啾")
        self.vocabulary = ["你好", "再见"]  # 默认会说两句

    def speak(self):
        word = random.choice(self.vocabulary)
        print(f"{self.name}: {word}！🦜")

    def learn(self, word):
        self.vocabulary.append(word)
        print(f"{self.name} 学会了说 \"{word}\"！")


# 创建动物
animals = [
    Dog("旺财", 3, "金毛"),
    Cat("咪咪", 2),
    Cat("汤姆", 4, indoor=False),
    Parrot("波利", 5),
]

# 鹦鹉学句子
animals[-1].learn("Python真好玩")
animals[-1].learn("你好世界")

# 多态演示：所有动物都能 speak，但行为不同
print("所有动物说话:")
for animal in animals:
    animal.speak()

print()
# 只有 Dog 能 fetch
animals[0].fetch("飞盘")
# 只有 Cat 能 scratch
animals[1].scratch()


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 2: 员工薪资系统
# ===================================================================
print("=== 练习 2: 员工薪资系统 ===")

class Employee:
    def __init__(self, name, base_salary=0):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

    def __str__(self):
        return f"{self.name} - 月薪: ¥{self.calculate_pay():,.0f}"


class SalaryEmployee(Employee):
    """月薪制员工"""
    def __init__(self, name, salary):
        super().__init__(name, salary)


class HourlyEmployee(Employee):
    """时薪制员工"""
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name, 0)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(Employee):
    """底薪+提成"""
    def __init__(self, name, base_salary, sales_amount, commission_rate):
        super().__init__(name, base_salary)
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def calculate_pay(self):
        return self.base_salary + self.sales_amount * self.commission_rate


class Manager(SalaryEmployee):
    """经理 = 月薪 + 管理奖金"""
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        return super().calculate_pay() + self.bonus


# 创建员工
employees = [
    SalaryEmployee("张三", 10000),
    HourlyEmployee("李四", 160, 80),            # 160小时 × 80元/小时
    CommissionEmployee("王五", 5000, 50000, 0.1),# 底薪5000 + 5万销售额 × 10%
    Manager("赵六", 15000, 5000),                # 月薪15000 + 奖金5000
]

total_payroll = 0
print("工资单:")
for emp in employees:
    print(f"  {emp}")
    total_payroll += emp.calculate_pay()

print(f"\n工资总额: ¥{total_payroll:,.0f}")


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 3: 图形面积计算器
# ===================================================================
print("=== 练习 3: 图形面积计算器 ===")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"{self.__class__.__name__}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return self.describe()


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    """正方形是特殊的长方形"""
    def __init__(self, side):
        super().__init__(side, side)  # 宽 = 高 = 边长


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        # 检查三角形合法性
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("无法构成三角形！")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # 海伦公式
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# 创建图形
shapes = [
    Rectangle(10, 5),
    Square(7),
    Circle(5),
    Triangle(3, 4, 5),
    Circle(3),
    Rectangle(8, 8),
]

# 打印所有信息
print("所有图形:")
for s in shapes:
    print(f"  {s}")

# 按面积排序
shapes.sort()
print("\n按面积从小到大排序:")
for i, s in enumerate(shapes, 1):
    print(f"  {i}. {s}")

# 最大的图形
biggest = max(shapes)
print(f"\n面积最大: {biggest}")


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 4: 交通工具模拟器
# ===================================================================
print("=== 练习 4: 交通工具模拟器 ===")

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, amount):
        self.current_speed = min(self.current_speed + amount, self.max_speed)
        print(f"  {self.name} 加速到 {self.current_speed} km/h")

    def brake(self, amount):
        self.current_speed = max(self.current_speed - amount, 0)
        print(f"  {self.name} 减速到 {self.current_speed} km/h")

    def __str__(self):
        return f"{self.name}: {self.current_speed}/{self.max_speed} km/h"


class Car(Vehicle):
    def __init__(self, name, max_speed, fuel=100):
        super().__init__(name, max_speed)
        self.fuel = fuel

    def accelerate(self, amount):
        fuel_cost = (amount / 10) * 5
        if self.fuel <= 0:
            print(f"  {self.name} 没油了！🛢️")
            return
        self.fuel = max(0, self.fuel - fuel_cost)
        super().accelerate(amount)
        print(f"    油量: {self.fuel:.0f}%")


class ElectricCar(Car):
    def __init__(self, name, max_speed, battery=100):
        super().__init__(name, max_speed, fuel=0)  # 不用油
        self.battery = battery

    def accelerate(self, amount):
        battery_cost = (amount / 10) * 3
        if self.battery <= 0:
            print(f"  {self.name} 没电了！🔋")
            return
        self.battery = max(0, self.battery - battery_cost)
        # 直接调用 Vehicle 的 accelerate，跳过 Car 的燃油逻辑
        Vehicle.accelerate(self, amount)
        print(f"    电量: {self.battery:.0f}%")

    def charge(self):
        self.battery = 100
        print(f"  {self.name} 充电完成！电量: 100% ⚡")


class Bicycle(Vehicle):
    def __init__(self, name, max_speed=40):
        super().__init__(name, max_speed)
        self.rider_stamina = 100

    def accelerate(self, amount):
        stamina_cost = (amount / 10) * 10
        if self.rider_stamina <= 0:
            print(f"  {self.name} 骑手太累了，无法加速！😫")
            return
        self.rider_stamina = max(0, self.rider_stamina - stamina_cost)
        super().accelerate(amount)
        print(f"    体力: {self.rider_stamina:.0f}%")

    def rest(self):
        self.rider_stamina = min(100, self.rider_stamina + 50)
        print(f"  {self.name} 骑手休息中... 体力: {self.rider_stamina:.0f}%")


# 模拟旅程
print("🚗 燃油车:")
car = Car("丰田", 180)
car.accelerate(60)
car.accelerate(60)
car.accelerate(60)
car.brake(40)

print("\n⚡ 电动车:")
ev = ElectricCar("特斯拉", 200)
ev.accelerate(80)
ev.accelerate(80)
ev.accelerate(60)  # 可能没电了
ev.charge()
ev.accelerate(60)

print("\n🚲 自行车:")
bike = Bicycle("捷安特")
bike.accelerate(20)
bike.accelerate(20)
bike.accelerate(20)  # 可能体力不足了
bike.rest()
bike.accelerate(10)


print("\n" + "=" * 50 + "\n")


# ===================================================================
# [挑战题] 练习 5: RPG 战斗系统
# ===================================================================
print("=== 挑战题: RPG 战斗系统 ===")

class Character(ABC):
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.is_alive = True

    def attack(self, target):
        damage = max(1, self.attack_power - target.defense)
        print(f"  ⚔️ {self.name} 攻击 {target.name}，造成 {damage} 点伤害！")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            self.is_alive = False
            print(f"  💀 {self.name} 被击败了！")
        else:
            print(f"    {self.name} 剩余 HP: {self.hp}/{self.max_hp}")

    @abstractmethod
    def special_skill(self, target):
        pass

    def __str__(self):
        status = "❤️" if self.is_alive else "💀"
        return f"{status} {self.name} [HP: {self.hp}/{self.max_hp}]"


class Warrior(Character):
    """战士：高攻高防"""
    def __init__(self, name):
        super().__init__(name, hp=120, attack_power=25, defense=15)

    def special_skill(self, target):
        damage = int(self.attack_power * 1.5)  # 1.5倍攻击，无视防御
        print(f"  🗡️ {self.name} 使用【猛击】，造成 {damage} 点伤害！")
        target.take_damage(damage)


class Mage(Character):
    """法师：高攻低防，有法力"""
    def __init__(self, name):
        super().__init__(name, hp=80, attack_power=30, defense=5)
        self.mana = 50

    def special_skill(self, target):
        mana_cost = 20
        if self.mana < mana_cost:
            print(f"  ❌ {self.name} 法力不足！(当前: {self.mana})")
            return
        self.mana -= mana_cost
        damage = self.attack_power * 2
        print(f"  🔥 {self.name} 使用【火球术】(法力-{mana_cost})，造成 {damage} 点伤害！")
        target.take_damage(damage)


class Healer(Character):
    """治疗师：能给自己回血"""
    def __init__(self, name):
        super().__init__(name, hp=90, attack_power=15, defense=10)

    def special_skill(self, target):
        """target 参数在这里不用，治疗师治疗自己"""
        heal_amount = 30
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + heal_amount)
        actual_heal = self.hp - old_hp
        print(f"  💚 {self.name} 使用【治疗术】，恢复 {actual_heal} HP！"
              f"(HP: {self.hp}/{self.max_hp})")


# ===== 战斗模拟 =====
def battle(team_a, team_b):
    """回合制战斗"""
    print("=" * 40)
    print("⚔️  战斗开始！ ⚔️")
    print(f"  队伍A: {', '.join(c.name for c in team_a)}")
    print(f"  队伍B: {', '.join(c.name for c in team_b)}")
    print("=" * 40)

    round_num = 0
    while True:
        # 检查是否有一队全灭
        alive_a = [c for c in team_a if c.is_alive]
        alive_b = [c for c in team_b if c.is_alive]

        if not alive_a:
            print("\n🏆 队伍B 获胜！")
            break
        if not alive_b:
            print("\n🏆 队伍A 获胜！")
            break

        round_num += 1
        print(f"\n--- 第 {round_num} 回合 ---")

        # 队伍A行动
        for char in alive_a:
            alive_b = [c for c in team_b if c.is_alive]
            if not alive_b:
                break
            target = random.choice(alive_b)

            # 30% 概率使用特殊技能
            if random.random() < 0.3:
                char.special_skill(target)
            else:
                char.attack(target)

        # 队伍B行动
        for char in [c for c in team_b if c.is_alive]:
            alive_a = [c for c in team_a if c.is_alive]
            if not alive_a:
                break
            target = random.choice(alive_a)

            if random.random() < 0.3:
                char.special_skill(target)
            else:
                char.attack(target)

        # 显示状态
        print("\n  状态:")
        for c in team_a + team_b:
            print(f"    {c}")

    print("\n战斗结束！")


# 创建角色
team_heroes = [Warrior("关羽"), Mage("诸葛亮"), Healer("华佗")]
team_villains = [Warrior("吕布"), Mage("司马懿")]

battle(team_heroes, team_villains)
