# Day 4 演示脚本 - 面向对象编程 (OOP)
# 配合 lecture.md 使用，按章节顺序演示

import random

print("=" * 60)
print("Day 4: 面向对象编程 (OOP) 演示脚本")
print("=" * 60)

# ===========================================================
# 第一章：为什么需要面向对象？
# ===========================================================

print("\n" + "=" * 50)
print("第一章：为什么需要 OOP？")
print("=" * 50)

# 1.1 传统字典方式（面条式代码）
print("\n--- 1.1 传统方式（字典 + 函数）---")
student1 = {"name": "小明", "age": 16, "score": 85}
student2 = {"name": "小红", "age": 15, "score": 92}

def show_info(student):
    print(f"{student['name']}, {student['age']}岁, 成绩{student['score']}分")

def add_score(student, points):
    student['score'] += points
    print(f"{student['name']}加了{points}分，现在是{student['score']}分")

show_info(student1)
add_score(student1, 10)

# 1.2 面向对象方式
print("\n--- 1.2 面向对象方式（类）---")

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def show_info(self):
        print(f"{self.name}, {self.age}岁, 成绩{self.score}分")
    
    def add_score(self, points):
        self.score += points
        print(f"{self.name}加了{points}分，现在是{self.score}分")

xiaoming = Student("小明", 16, 85)
xiaoming.show_info()
xiaoming.add_score(10)

# 1.3 第一个简单的类
print("\n--- 1.3 第一个简单的类 Dog ---")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name}说：汪汪！")
    
    def info(self):
        print(f"我是{self.name}，今年{self.age}岁")

dog1 = Dog("旺财", 3)
dog2 = Dog("小黑", 5)

print(f"dog1.name = {dog1.name}")
print(f"dog2.age = {dog2.age}")
dog1.bark()
dog2.bark()
dog1.info()


# ===========================================================
# 第二章：深入理解属性与方法
# ===========================================================

print("\n" + "=" * 50)
print("第二章：属性与方法")
print("=" * 50)

# 2.1 类属性 vs 实例属性
print("\n--- 2.1 类属性 vs 实例属性 ---")

class Cat:
    # 类属性：所有猫共享
    species = "猫科动物"
    count = 0
    
    def __init__(self, name, color):
        # 实例属性：每只猫不同
        self.name = name
        self.color = color
        Cat.count += 1  # 类属性+1

cat1 = Cat("咪咪", "白色")
cat2 = Cat("花花", "橘色")
cat3 = Cat("小黑", "黑色")

print(f"cat1.species = {cat1.species}")
print(f"cat2.species = {cat2.species}")
print(f"Cat.species = {Cat.species}")
print(f"一共创建了 {Cat.count} 只猫")

# 2.2 银行账户示例
print("\n--- 2.2 银行账户示例 ---")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"存入{amount}元，余额{self.balance}元")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足！")
        elif amount <= 0:
            print("取款金额必须大于0")
        else:
            self.balance -= amount
            print(f"取出{amount}元，余额{self.balance}元")
    
    def show_balance(self):
        print(f"{self.owner}的账户余额：{self.balance}元")

acc = BankAccount("张三", 1000)
acc.show_balance()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)  # 余额不足


# ===========================================================
# 第三章：封装
# ===========================================================

print("\n" + "=" * 50)
print("第三章：封装")
print("=" * 50)

# 3.1 私有属性
print("\n--- 3.1 私有属性 ---")

class Person:
    def __init__(self, name, age, secret):
        self.name = name        # 公开
        self._age = age         # "内部使用"（约定）
        self.__secret = secret  # "私有"

p = Person("小明", 18, "我喜欢小红")

print(f"p.name = {p.name}")           # 可以访问
print(f"p._age = {p._age}")           # 可以访问（但不建议）
# print(p.__secret)                   # 会报错！
print(f"p._Person__secret = {p._Person__secret}")  # 技术上可以，但千万别这样做

# 3.2 用方法保护属性
print("\n--- 3.2 用方法保护属性 ---")

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp
        self.__max_hp = hp
    
    def get_hp(self):
        return self.__hp
    
    def take_damage(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
        print(f"{self.name}受到{damage}点伤害，剩余HP: {self.__hp}/{self.__max_hp}")
    
    def heal(self, amount):
        self.__hp += amount
        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp
        print(f"{self.name}恢复{amount}点HP，当前HP: {self.__hp}/{self.__max_hp}")

player = Player("勇者", 100)
player.take_damage(30)
player.take_damage(80)  # 不会变成负数
player.heal(50)


# ===========================================================
# 第四章：继承
# ===========================================================

print("\n" + "=" * 50)
print("第四章：继承")
print("=" * 50)

# 4.1 基本继承
print("\n--- 4.1 基本继承 ---")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name}在吃东西")
    
    def sleep(self):
        print(f"{self.name}在睡觉")

class Dog2(Animal):
    def bark(self):
        print(f"{self.name}说：汪汪！")

class Cat2(Animal):
    def meow(self):
        print(f"{self.name}说：喵~")

dog = Dog2("旺财", 3)
dog.eat()    # 继承自 Animal
dog.sleep()  # 继承自 Animal
dog.bark()   # Dog2 自己的方法

# 4.2 super() 的使用
print("\n--- 4.2 super() 的使用 ---")

class Animal3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog3(Animal3):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类构造
        self.breed = breed           # 子类独有属性
    
    def info(self):
        print(f"{self.name}, {self.age}岁, 品种: {self.breed}")

shiba = Dog3("旺财", 3, "柴犬")
shiba.info()

# 4.3 方法重写
print("\n--- 4.3 方法重写 ---")

class Animal4:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name}发出声音")

class Dog4(Animal4):
    def speak(self):
        print(f"{self.name}说：汪汪！")

class Cat4(Animal4):
    def speak(self):
        print(f"{self.name}说：喵~")

class Duck(Animal4):
    def speak(self):
        print(f"{self.name}说：嘎嘎！")

animals = [Dog4("旺财"), Cat4("咪咪"), Duck("唐老鸭")]
for animal in animals:
    animal.speak()


# ===========================================================
# 第五章：多态
# ===========================================================

print("\n" + "=" * 50)
print("第五章：多态")
print("=" * 50)

# 5.1 形状计算器
print("\n--- 5.1 形状计算器（多态演示）---")

class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c

def print_shape_info(shape, name):
    print(f"{name}：面积={shape.area():.2f}, 周长={shape.perimeter():.2f}")

shapes = [
    (Rectangle(10, 5), "长方形(10x5)"),
    (Circle(7), "圆(r=7)"),
    (Triangle(3, 4, 5), "三角形(3,4,5)")
]

for shape, name in shapes:
    print_shape_info(shape, name)


# ===========================================================
# 第六章：特殊方法
# ===========================================================

print("\n" + "=" * 50)
print("第六章：特殊方法（魔法方法）")
print("=" * 50)

# 6.1 __str__ 方法
print("\n--- 6.1 __str__ 方法 ---")

class BookNoStr:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookWithStr:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"《{self.title}》 by {self.author}"

book1 = BookNoStr("Python入门", "张三")
book2 = BookWithStr("Python入门", "张三")

print(f"没有__str__: {book1}")
print(f"有__str__:   {book2}")

# 6.2 __eq__ 方法
print("\n--- 6.2 __eq__ 方法 ---")

class PointNoEq:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointWithEq:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = PointNoEq(3, 4)
p2 = PointNoEq(3, 4)
print(f"没有__eq__: p1 == p2 是 {p1 == p2}")

p3 = PointWithEq(3, 4)
p4 = PointWithEq(3, 4)
print(f"有__eq__:   p3 == p4 是 {p3 == p4}")

# 6.3 __add__ 方法
print("\n--- 6.3 __add__ 方法 ---")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v3}")


# ===========================================================
# 第七章：类的关系与设计模式
# ===========================================================

print("\n" + "=" * 50)
print("第七章：购物车系统示例")
print("=" * 50)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} (¥{self.price})"

class CartItem:
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity
    
    def total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity} = ¥{self.total()}"

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add(self, product, quantity=1):
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))
    
    def remove(self, product_name):
        self.items = [item for item in self.items 
                      if item.product.name != product_name]
    
    def total(self):
        return sum(item.total() for item in self.items)
    
    def show(self):
        print("=" * 30)
        print("🛒 购物车清单：")
        for item in self.items:
            print(f"  {item}")
        print("-" * 30)
        print(f"  总计: ¥{self.total()}")
        print("=" * 30)

# 测试购物车
apple = Product("苹果", 5)
milk = Product("牛奶", 8)
bread = Product("面包", 12)

cart = ShoppingCart()
cart.add(apple, 3)
cart.add(milk, 2)
cart.add(bread)
cart.add(apple, 2)  # 再加2个苹果
cart.show()


# ===========================================================
# 第八章：综合实战 - RPG 战斗系统
# ===========================================================

print("\n" + "=" * 50)
print("第八章：RPG 战斗系统")
print("=" * 50)

class Role:
    """角色基类"""
    def __init__(self, name, hp, atk):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
    
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"  💔 {self.name} 受到 {damage} 点伤害，"
              f"剩余HP: {self.hp}/{self.max_hp}")
    
    def attack(self, target):
        print(f"⚔️ 【{self.name}】普通攻击 → {target.name}")
        target.take_damage(self.atk)

class Warrior(Role):
    """战士：血厚，可以重击"""
    def __init__(self, name):
        super().__init__(name, hp=150, atk=25)
    
    def heavy_strike(self, target):
        damage = int(self.atk * 1.5)
        print(f"💪 【{self.name}】使用重击 → {target.name}")
        target.take_damage(damage)

class Mage(Role):
    """法师：有魔法"""
    def __init__(self, name):
        super().__init__(name, hp=80, atk=15)
        self.mp = 100
    
    def fireball(self, target):
        if self.mp >= 20:
            self.mp -= 20
            print(f"🔥 【{self.name}】释放火球术 → {target.name}（MP: {self.mp}）")
            target.take_damage(50)
        else:
            print(f"【{self.name}】魔力不足，使用普通攻击")
            self.attack(target)

class Healer(Role):
    """治疗师：能加血"""
    def __init__(self, name):
        super().__init__(name, hp=100, atk=10)
        self.mp = 80
    
    def heal(self, target):
        if self.mp >= 15:
            self.mp -= 15
            heal_amount = 30
            target.hp = min(target.hp + heal_amount, target.max_hp)
            print(f"💚 【{self.name}】治疗 → {target.name}，恢复 {heal_amount} HP "
                  f"(HP: {target.hp}/{target.max_hp})")
        else:
            print(f"【{self.name}】魔力不足，无法治疗")

def battle_demo():
    print("\n" + "=" * 40)
    print("⚔️  迷你RPG战斗演示  ⚔️")
    print("=" * 40)
    
    warrior = Warrior("勇者")
    mage = Mage("魔法师")
    healer = Healer("光明牧师")
    boss = Role("史莱姆王", hp=250, atk=20)
    
    team = [warrior, mage, healer]
    
    round_num = 1
    while any(m.is_alive() for m in team) and boss.is_alive():
        print(f"\n{'─'*40}")
        print(f"📍 第 {round_num} 回合")
        print(f"{'─'*40}")
        
        # 我方行动
        for member in team:
            if not member.is_alive():
                continue
            
            if not boss.is_alive():
                break
            
            if isinstance(member, Warrior):
                if random.random() > 0.5:
                    member.heavy_strike(boss)
                else:
                    member.attack(boss)
            elif isinstance(member, Mage):
                member.fireball(boss)
            elif isinstance(member, Healer):
                # 优先治疗血量最低的队友
                injured = [m for m in team if m.is_alive() and m.hp < m.max_hp * 0.6]
                if injured:
                    target = min(injured, key=lambda m: m.hp)
                    member.heal(target)
                else:
                    member.attack(boss)
        
        if not boss.is_alive():
            break
        
        # 敌方行动
        alive_team = [m for m in team if m.is_alive()]
        if alive_team:
            target = random.choice(alive_team)
            boss.attack(target)
        
        round_num += 1
        
        if round_num > 20:  # 防止死循环
            print("战斗超时！")
            break
    
    print("\n" + "=" * 40)
    if boss.is_alive():
        print("💀 队伍全灭，挑战失败...")
    else:
        print("🎉 胜利！击败了史莱姆王！")
    print("=" * 40)

# 运行战斗演示
battle_demo()


print("\n" + "=" * 60)
print("Day 4 演示脚本结束")
print("=" * 60)
