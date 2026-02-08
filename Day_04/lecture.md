# Day 4: 面向对象编程 (OOP) —— 从"写代码"到"设计系统"

**课程时长**: 8 小时 (上午 4 小时 + 下午 4 小时)
**适用对象**: 已完成函数学习的初学者
**教学目标**: 理解面向对象思想，掌握类的定义、属性与方法、继承、多态等核心概念

---

# 🌅 上午课程 (4小时)

---

## 第一章：为什么需要面向对象？(1小时)

### 1.1 回顾：函数帮我们解决了什么问题？

昨天我们学习了函数，它帮我们：
- ✅ 消除重复代码
- ✅ 把复杂逻辑封装成"黑盒子"
- ✅ 提高代码可读性

**但是，仅有函数还不够……**

---

### 1.2 一个尴尬的场景

假设我们要写一个"学生管理系统"，用函数式思维会这样写：

```python
# 学生数据用字典存储
student1 = {"name": "小明", "age": 16, "score": 85}
student2 = {"name": "小红", "age": 15, "score": 92}

# 函数操作学生数据
def show_info(student):
    print(f"{student['name']}, {student['age']}岁, 成绩{student['score']}分")

def add_score(student, points):
    student['score'] += points
    print(f"{student['name']}加了{points}分，现在是{student['score']}分")
```

**问题来了**：
1. 数据（字典）和操作（函数）是**分离**的，容易乱
2. 如果有人写错 key 名（如 `student['scores']`），运行时才会报错
3. 如果我想给"老师"也做类似功能，要重复很多代码

---

### 1.3 面向对象的解决方案

面向对象编程 (Object-Oriented Programming, OOP) 的核心思想：
**把"数据"和"操作数据的方法"打包在一起，形成一个整体。**

```python
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

# 使用
xiaoming = Student("小明", 16, 85)
xiaoming.show_info()      # 小明, 16岁, 成绩85分
xiaoming.add_score(10)    # 小明加了10分，现在是95分
```

**优点**：
- ✅ 数据和方法捆绑在一起，不会散落
- ✅ 代码更符合人类思维（"学生.展示信息" 比 "展示信息(学生)" 更直观）
- ✅ 可以复用（等会儿学继承）

---

### 1.4 核心术语

| 术语 | 英文 | 解释 | 类比 |
|------|------|------|------|
| 类 (Class) | Class | 定义事物的"蓝图"或"模板" | 建筑图纸 |
| 对象 (Object) | Object / Instance | 根据蓝图创建的具体"产品" | 根据图纸建造的一栋楼 |
| 属性 (Attribute) | Attribute | 对象拥有的数据 | 楼的地址、层数、颜色 |
| 方法 (Method) | Method | 对象能执行的操作 | 楼的电梯、开门关门 |
| 实例化 (Instantiation) | Instantiate | 根据类创建对象的过程 | 按照图纸盖楼 |

**生活类比**：
- **类**：狗 (Dog) 是一个抽象概念
- **对象**：隔壁家的"旺财"是一个具体的狗

---

### 1.5 定义第一个类

**语法结构**：

```python
class 类名:
    def __init__(self, 参数1, 参数2, ...):
        self.属性1 = 参数1
        self.属性2 = 参数2
    
    def 方法名(self, 其他参数):
        # 方法体
        pass
```

**关键点**：
1. `class` 关键字定义类，类名习惯用**大驼峰命名法** (如 `Student`, `ElectricCar`)
2. `__init__` 是**构造方法**（双下划线开头和结尾），创建对象时自动调用
3. `self` 代表**当前对象本身**，必须是每个方法的第一个参数

---

### 1.6 实例化对象

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name}说：汪汪！")

# 实例化：类名() 就像调用函数一样
dog1 = Dog("旺财", 3)
dog2 = Dog("小黑", 5)

# 访问属性
print(dog1.name)  # 旺财
print(dog2.age)   # 5

# 调用方法
dog1.bark()  # 旺财说：汪汪！
dog2.bark()  # 小黑说：汪汪！
```

**📝 随堂练习 1**: 
1. 定义一个 `Cat` 类，包含属性 `name` 和 `color`
2. 添加方法 `meow()` 打印 "xxx说：喵~"
3. 创建两只猫并调用它们的方法

---

## 第二章：深入理解属性与方法 (1小时)

### 2.1 self 到底是什么？

`self` 是 Python 的约定俗成的名字，代表**调用该方法的对象本身**。

```python
class Student:
    def __init__(self, name):
        # self.name 是对象的属性
        # name 是传入的参数
        self.name = name  # 把参数赋值给对象的属性
    
    def greet(self):
        # 这里的 self 就是调用 greet() 的那个对象
        print(f"大家好，我是{self.name}")

s1 = Student("小明")
s2 = Student("小红")

s1.greet()  # self 指向 s1，输出：大家好，我是小明
s2.greet()  # self 指向 s2，输出：大家好，我是小红
```

**易错点**：调用方法时不需要传 self，Python 自动帮你传！

```python
s1.greet()        # ✅ 正确
s1.greet(s1)      # ❌ 错误：多传了一个参数
Student.greet(s1) # ✅ 也可以这样调用（但不常用）
```

---

### 2.2 属性的两种类型

**① 实例属性 (Instance Attribute)**
- 每个对象独有的数据
- 在 `__init__` 中用 `self.xxx = ...` 定义
- 不同对象的值可以不同

**② 类属性 (Class Attribute)**
- 所有对象**共享**的数据
- 直接在类中定义，不在方法里
- 修改类属性会影响所有对象

```python
class Dog:
    # 类属性：所有狗共享
    species = "犬科动物"
    count = 0  # 记录创建了多少只狗
    
    def __init__(self, name):
        # 实例属性：每只狗不同
        self.name = name
        Dog.count += 1  # 每创建一只狗，计数+1

# 测试
d1 = Dog("旺财")
d2 = Dog("小黑")

print(d1.species)  # 犬科动物
print(d2.species)  # 犬科动物
print(Dog.species) # 犬科动物
print(Dog.count)   # 2

print(d1.name)  # 旺财
print(d2.name)  # 小黑
```

---

### 2.3 方法中修改属性

方法可以读取和修改对象的属性：

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.balance += amount
            print(f"存入{amount}元，余额{self.balance}元")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        """取款"""
        if amount > self.balance:
            print("余额不足！")
        elif amount <= 0:
            print("取款金额必须大于0")
        else:
            self.balance -= amount
            print(f"取出{amount}元，余额{self.balance}元")
    
    def show_balance(self):
        """查询余额"""
        print(f"{self.owner}的账户余额：{self.balance}元")

# 测试
acc = BankAccount("张三", 1000)
acc.show_balance()   # 张三的账户余额：1000元
acc.deposit(500)     # 存入500元，余额1500元
acc.withdraw(200)    # 取出200元，余额1300元
acc.withdraw(2000)   # 余额不足！
```

---

### 2.4 方法返回值

方法也可以有返回值，和普通函数一样：

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """返回面积"""
        return self.width * self.height
    
    def perimeter(self):
        """返回周长"""
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print(f"面积: {rect.area()}")      # 面积: 50
print(f"周长: {rect.perimeter()}")  # 周长: 30
```

**📝 随堂练习 2**: 
1. 定义一个 `Counter` 类
2. 包含属性 `count`（初始值为 0）
3. 包含方法 `increment()` 使 count 加 1
4. 包含方法 `decrement()` 使 count 减 1
5. 包含方法 `get_count()` 返回当前值
6. 创建一个计数器，调用几次加减后，打印结果

---

## 第三章：封装 —— 保护你的数据 (1小时)

### 3.1 什么是封装？

**封装 (Encapsulation)** 是 OOP 的三大特性之一（另外两个是继承和多态）。

核心思想：**隐藏内部细节，只暴露必要的接口。**

**生活类比**：
- 电视遥控器：你只需要知道"按音量+"就能调大声音，不需要知道内部电路是怎么工作的
- 汽车：你只需要踩油门就能加速，不需要知道发动机怎么燃烧汽油

---

### 3.2 为什么需要封装？

看看不封装会出什么问题：

```python
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp  # 血量

p = Player("勇者", 100)

# 问题1：外部可以随意修改属性
p.hp = -999  # 血量变成负数？这不合理！

# 问题2：外部可以设置不合法的值
p.hp = "很多血"  # 把数字变成字符串？
```

---

### 3.3 "私有"属性的约定

Python 没有真正的私有，但有**命名约定**：

| 命名方式 | 含义 | 能否外部访问 |
|---------|------|------------|
| `self.name` | 公开属性 | ✅ 可以 |
| `self._name` | "内部使用"（约定，不强制） | ✅ 可以，但不建议 |
| `self.__name` | "私有"属性 | ❌ 不能直接访问 |

```python
class Person:
    def __init__(self, name, age, secret):
        self.name = name        # 公开
        self._age = age         # "内部使用"
        self.__secret = secret  # "私有"

p = Person("小明", 18, "我喜欢小红")

print(p.name)       # 小明 ✅
print(p._age)       # 18 ✅ (能访问，但IDE会警告)
print(p.__secret)   # ❌ 报错！AttributeError
```

**原理**：Python 把 `__secret` 重命名为 `_Person__secret`（名字改写，Name Mangling）。虽然技术上还是能访问，但不建议这样做。

---

### 3.4 使用方法保护属性

正确的做法是：用方法来控制属性的读写。

```python
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp  # 私有属性
    
    def get_hp(self):
        """获取血量"""
        return self.__hp
    
    def take_damage(self, damage):
        """受到伤害"""
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0  # 血量不能为负
        print(f"{self.name}受到{damage}点伤害，剩余HP: {self.__hp}")
    
    def heal(self, amount):
        """恢复血量"""
        self.__hp += amount
        if self.__hp > 100:
            self.__hp = 100  # 血量有上限
        print(f"{self.name}恢复{amount}点HP，当前HP: {self.__hp}")

# 测试
p = Player("勇者", 100)
p.take_damage(30)   # 勇者受到30点伤害，剩余HP: 70
p.take_damage(80)   # 勇者受到80点伤害，剩余HP: 0 (不会变成负数)
p.heal(50)          # 勇者恢复50点HP，当前HP: 50
```

---

### 3.5 @property 装饰器 (选讲)

Python 提供了更优雅的方式：用 `@property` 把方法伪装成属性。

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        """获取半径"""
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        """设置半径"""
        if value <= 0:
            raise ValueError("半径必须大于0")
        self.__radius = value
    
    @property
    def area(self):
        """面积（只读）"""
        return 3.14 * self.__radius ** 2

# 使用：看起来像访问属性，实际上调用了方法
c = Circle(5)
print(c.radius)    # 5 (调用 getter)
print(c.area)      # 78.5 (调用 getter)

c.radius = 10      # (调用 setter)
print(c.radius)    # 10

c.radius = -5      # 报错！ValueError: 半径必须大于0
```

**📝 随堂练习 3**: 
1. 定义一个 `Student` 类
2. 包含私有属性 `__score`（0-100之间）
3. 添加方法 `get_score()` 返回成绩
4. 添加方法 `set_score(score)` 设置成绩，要求必须在 0-100 之间，否则打印错误信息

---

## 第四章：继承 —— 代码复用的艺术 (1小时)

### 4.1 什么是继承？

**继承 (Inheritance)** 让一个类可以"继承"另一个类的属性和方法，从而实现代码复用。

**生活类比**：
- 你**继承**了父母的基因（属性）
- 你**学会**了父母教给你的本领（方法）
- 你还可以**发展**出自己独特的特长（新方法/重写方法）

---

### 4.2 继承的语法

```python
class 父类:
    # 父类的属性和方法
    pass

class 子类(父类):  # 括号里写父类名
    # 子类继承了父类的所有内容
    # 还可以添加新的属性和方法
    pass
```

**示例**：动物 → 狗

```python
# 父类 (基类、超类)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name}在吃东西")
    
    def sleep(self):
        print(f"{self.name}在睡觉")

# 子类 (派生类)
class Dog(Animal):
    def bark(self):
        print(f"{self.name}说：汪汪！")

# 测试
dog = Dog("旺财", 3)
dog.eat()   # 继承自 Animal
dog.sleep() # 继承自 Animal
dog.bark()  # Dog 自己的方法
```

---

### 4.3 子类的构造方法与 super()

如果子类需要额外的属性，必须先调用父类的 `__init__`：

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        # 调用父类的构造方法
        super().__init__(name, age)
        # 添加子类独有的属性
        self.breed = breed
    
    def info(self):
        print(f"{self.name}, {self.age}岁, 品种: {self.breed}")

dog = Dog("旺财", 3, "柴犬")
dog.info()  # 旺财, 3岁, 品种: 柴犬
```

**为什么要用 super()**？
- 保证父类的初始化逻辑被执行
- 如果你忘了调用，父类的属性就不会被创建

---

### 4.4 方法重写 (Override)

子类可以**重写**父类的方法，提供自己的实现：

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name}发出声音")

class Dog(Animal):
    def speak(self):  # 重写父类方法
        print(f"{self.name}说：汪汪！")

class Cat(Animal):
    def speak(self):  # 重写父类方法
        print(f"{self.name}说：喵~")

# 测试
animals = [Dog("旺财"), Cat("咪咪")]
for animal in animals:
    animal.speak()

# 输出：
# 旺财说：汪汪！
# 咪咪说：喵~
```

---

### 4.5 继承的好处

```python
# 游戏角色示例
class Character:
    """所有角色的基类"""
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    
    def is_alive(self):
        return self.hp > 0
    
    def attack(self, target):
        target.hp -= self.atk
        print(f"{self.name}攻击{target.name}，造成{self.atk}点伤害")

class Warrior(Character):
    """战士：血厚攻高"""
    def __init__(self, name):
        super().__init__(name, hp=150, atk=20)
    
    def shield_bash(self, target):
        """特殊技能：盾击"""
        damage = self.atk + 10
        target.hp -= damage
        print(f"{self.name}使用盾击，对{target.name}造成{damage}点伤害！")

class Mage(Character):
    """法师：血脆但有魔法"""
    def __init__(self, name):
        super().__init__(name, hp=80, atk=15)
        self.mp = 100
    
    def fireball(self, target):
        """特殊技能：火球术"""
        if self.mp >= 20:
            self.mp -= 20
            damage = 50
            target.hp -= damage
            print(f"{self.name}释放火球术，对{target.name}造成{damage}点伤害！")
        else:
            print(f"{self.name}魔力不足！")
```

**📝 随堂练习 4**: 
1. 定义一个 `Vehicle` 类（交通工具）
   - 属性：`brand`, `speed`
   - 方法：`start()` 打印 "启动"
2. 定义子类 `Car`，添加属性 `wheels=4`，重写 `start()` 打印 "汽车启动"
3. 定义子类 `Motorcycle`，添加属性 `wheels=2`，重写 `start()` 打印 "摩托车启动"

---

# 🌆 下午课程 (4小时)

---

## 第五章：多态 —— 同一接口，不同行为 (1小时)

### 5.1 什么是多态？

**多态 (Polymorphism)** = 同一个方法名，在不同对象上有不同的行为。

前面的例子其实已经展示了多态：
```python
dog.speak()  # 汪汪
cat.speak()  # 喵~
```

虽然都是调用 `speak()` 方法，但不同动物叫的声音不一样。

---

### 5.2 多态的威力

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪"

class Cat(Animal):
    def speak(self):
        return "喵~"

class Duck(Animal):
    def speak(self):
        return "嘎嘎"

# 多态的应用：同一个函数处理不同类型的对象
def animal_concert(animals):
    for animal in animals:
        print(animal.speak())

# 不管传入什么动物，这个函数都能工作！
animals = [Dog(), Cat(), Duck(), Dog()]
animal_concert(animals)
# 输出：汪汪、喵~、嘎嘎、汪汪
```

**好处**：
- 代码更灵活，不需要写 `if isinstance(animal, Dog)` 这种判断
- 新增动物种类时，主程序不需要修改

---

### 5.3 鸭子类型 (Duck Typing)

Python 的多态特别灵活，不强制要求继承关系：

> "如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子。"

```python
class Robot:
    def speak(self):
        return "嘟嘟嘟"

# Robot 没有继承 Animal，但它也有 speak() 方法
# 所以也可以参加"动物音乐会"！
robot = Robot()
print(robot.speak())  # 嘟嘟嘟
```

---

### 5.4 实战：形状计算器

```python
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

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
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # 海伦公式
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c

# 多态的应用
def print_shape_info(shape):
    print(f"面积: {shape.area():.2f}")
    print(f"周长: {shape.perimeter():.2f}")

shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print_shape_info(shape)
    print("-" * 20)
```

**📝 随堂练习 5**: 
1. 创建一个基类 `Employee`（员工），包含方法 `get_salary()` 返回 0
2. 创建子类 `FullTimeEmployee`（全职），`get_salary()` 返回固定月薪
3. 创建子类 `PartTimeEmployee`（兼职），`get_salary()` 返回 时薪 × 工时
4. 编写函数 `total_salary(employees)` 计算一组员工的总薪资

---

## 第六章：特殊方法 (魔法方法) (1小时)

### 6.1 什么是特殊方法？

Python 中以双下划线开头和结尾的方法叫**特殊方法**（Magic Methods / Dunder Methods）。

它们让你的类可以与 Python 的内置功能协同工作。

---

### 6.2 常用特殊方法

| 方法 | 作用 | 触发方式 |
|------|------|---------|
| `__init__` | 构造方法 | `obj = Class()` |
| `__str__` | 字符串表示 | `print(obj)` 或 `str(obj)` |
| `__repr__` | 开发者表示 | 在交互式环境直接输入 `obj` |
| `__len__` | 长度 | `len(obj)` |
| `__eq__` | 等于比较 | `obj1 == obj2` |
| `__lt__` | 小于比较 | `obj1 < obj2` |
| `__add__` | 加法 | `obj1 + obj2` |

---

### 6.3 __str__ 方法

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s = Student("小明", 90)
print(s)  # <__main__.Student object at 0x...>  不友好！
```

添加 `__str__` 后：

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return f"Student({self.name}, {self.score}分)"

s = Student("小明", 90)
print(s)  # Student(小明, 90分)  好多了！
```

---

### 6.4 __eq__ 方法

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)  # False！因为是两个不同的对象
```

添加 `__eq__` 后：

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)  # True！
```

---

### 6.5 __add__ 方法

```python
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
v3 = v1 + v2  # 会调用 v1.__add__(v2)
print(v3)  # Vector(4, 6)
```

**📝 随堂练习 6**: 
1. 定义一个 `Book` 类，属性：`title`, `author`, `price`
2. 实现 `__str__` 方法，返回 "《书名》 - 作者 - ¥价格"
3. 实现 `__eq__` 方法，当书名和作者都相同时返回 True

---

## 第七章：类的关系与设计模式初探 (1小时)

### 7.1 类与类之间的关系

**① 继承关系 (is-a)**
"A 是一种 B"

```python
class Dog(Animal):  # Dog is an Animal
    pass
```

**② 组合关系 (has-a)**
"A 拥有 B"

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # Car has an Engine

class Engine:
    def start(self):
        print("引擎启动")
```

**③ 关联关系 (uses-a)**
"A 使用 B"

```python
class Teacher:
    def teach(self, student):  # Teacher uses Student
        print(f"教 {student.name}")
```

---

### 7.2 组合 vs 继承

**场景**：设计一个"游戏角色"系统

**方案1：继承**
```python
class FlyingWarrior(Warrior, FlyingAbility):  # 多继承，可能变复杂
    pass
```

**方案2：组合（更推荐）**
```python
class Character:
    def __init__(self, name):
        self.name = name
        self.abilities = []
    
    def add_ability(self, ability):
        self.abilities.append(ability)

class FlyAbility:
    def use(self):
        print("飞上天空")

# 使用
c = Character("超人")
c.add_ability(FlyAbility())
```

**原则**：优先使用组合而非继承（更灵活）

---

### 7.3 实战：简易购物车系统

```python
class Product:
    """商品类"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} (¥{self.price})"

class CartItem:
    """购物车项目（商品 + 数量）"""
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity
    
    def total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity} = ¥{self.total()}"

class ShoppingCart:
    """购物车"""
    def __init__(self):
        self.items = []
    
    def add(self, product, quantity=1):
        # 检查商品是否已在购物车中
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                return
        # 不存在则新增
        self.items.append(CartItem(product, quantity))
    
    def remove(self, product_name):
        self.items = [item for item in self.items 
                      if item.product.name != product_name]
    
    def total(self):
        return sum(item.total() for item in self.items)
    
    def show(self):
        print("=" * 30)
        print("购物车清单：")
        for item in self.items:
            print(f"  {item}")
        print("-" * 30)
        print(f"  总计: ¥{self.total()}")
        print("=" * 30)

# 测试
apple = Product("苹果", 5)
milk = Product("牛奶", 8)
bread = Product("面包", 12)

cart = ShoppingCart()
cart.add(apple, 3)
cart.add(milk, 2)
cart.add(bread)
cart.show()
```

---

## 第八章：综合实战 —— 文字版 RPG 战斗系统 (1小时)

### 8.1 需求分析

设计一个迷你 RPG 战斗系统：
- 有多种角色（战士、法师、治疗师）
- 角色可以互相攻击
- 每个角色有独特的技能
- 战斗持续到一方全灭

### 8.2 完整代码

```python
import random

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
        print(f"  {self.name} 受到 {damage} 点伤害，剩余HP: {self.hp}/{self.max_hp}")
    
    def attack(self, target):
        print(f"【{self.name}】普通攻击 → {target.name}")
        target.take_damage(self.atk)

class Warrior(Role):
    """战士：血厚，可以格挡"""
    def __init__(self, name):
        super().__init__(name, hp=150, atk=25)
    
    def heavy_strike(self, target):
        """重击：造成1.5倍伤害"""
        damage = int(self.atk * 1.5)
        print(f"【{self.name}】使用重击 → {target.name}")
        target.take_damage(damage)

class Mage(Role):
    """法师：血少，但魔法伤害高"""
    def __init__(self, name):
        super().__init__(name, hp=80, atk=15)
        self.mp = 100
    
    def fireball(self, target):
        """火球术：消耗20MP，造成50点伤害"""
        if self.mp >= 20:
            self.mp -= 20
            print(f"【{self.name}】释放火球术 → {target.name}（MP剩余: {self.mp}）")
            target.take_damage(50)
        else:
            print(f"【{self.name}】魔力不足，使用普通攻击")
            self.attack(target)

class Healer(Role):
    """治疗师：攻击弱，但能加血"""
    def __init__(self, name):
        super().__init__(name, hp=100, atk=10)
        self.mp = 80
    
    def heal(self, target):
        """治疗：恢复30HP"""
        if self.mp >= 15:
            self.mp -= 15
            heal_amount = 30
            target.hp = min(target.hp + heal_amount, target.max_hp)
            print(f"【{self.name}】治疗 → {target.name}，恢复 {heal_amount} HP")
        else:
            print(f"【{self.name}】魔力不足，无法治疗")

# 战斗演示
def battle_demo():
    print("=" * 40)
    print("⚔️ 迷你RPG战斗演示 ⚔️")
    print("=" * 40)
    
    warrior = Warrior("勇者")
    mage = Mage("魔法师")
    boss = Role("史莱姆王", hp=200, atk=15)
    
    round_num = 1
    while warrior.is_alive() and boss.is_alive():
        print(f"\n--- 第 {round_num} 回合 ---")
        
        # 我方行动
        if random.random() > 0.5:
            warrior.heavy_strike(boss)
        else:
            warrior.attack(boss)
        
        if not boss.is_alive():
            break
        
        if mage.is_alive():
            mage.fireball(boss)
        
        if not boss.is_alive():
            break
        
        # 敌方行动
        target = random.choice([warrior, mage])
        if target.is_alive():
            boss.attack(target)
        
        round_num += 1
    
    print("\n" + "=" * 40)
    if boss.is_alive():
        print("💀 队伍全灭，挑战失败...")
    else:
        print("🎉 胜利！击败了史莱姆王！")
    print("=" * 40)

# 运行
battle_demo()
```

---

## 课程总结

| 核心概念 | 要点 |
|---------|------|
| 类与对象 | `class 类名:`, 类是模板，对象是实例 |
| __init__ | 构造方法，初始化对象属性 |
| self | 指代当前对象本身 |
| 封装 | 用私有属性 `__` 和方法保护数据 |
| 继承 | `class 子类(父类):`, 代码复用 |
| super() | 调用父类方法 |
| 多态 | 同一方法名，不同实现 |
| 特殊方法 | `__str__`, `__eq__`, `__add__` 等 |

---

## 课后作业

1. **图书管理系统**：设计 `Book` 和 `Library` 类，实现添加、删除、查找图书功能
2. **银行账户**：设计包含存款、取款、转账功能的账户类，注意余额验证
3. **动物园模拟**：设计动物基类和多种具体动物，实现"喂食"和"表演"功能
4. **扩展 RPG**：给战斗系统添加新职业（刺客：暴击），或新机制（闪避率）
