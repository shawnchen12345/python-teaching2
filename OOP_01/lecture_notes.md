# OOP 第1课：类与对象入门

**课程时长**: 约 2 小时  
**前置知识**: 变量、数据类型、函数、列表/字典  
**教学目标**: 理解面向对象的核心思想，掌握类的定义、对象的创建、`__init__` 构造方法、实例属性和实例方法。

---

## 第一部分：为什么需要面向对象？(20 分钟)

### 1.1 从"面条代码"到"有组织的代码"

我们之前学的所有内容——变量、if/else、循环、函数——都属于**面向过程**编程 (Procedural Programming)。

**面向过程** = 做菜的步骤：先洗菜 → 切菜 → 开火 → 炒菜 → 装盘

它的问题是什么？当程序变大时：
- 数据和函数是**分离**的，容易混乱
- 代码**复用**困难，到处复制粘贴
- **维护**噩梦，改一个地方到处出问题

### 1.2 万物皆对象

看看真实世界：
- 一辆 **汽车** → 有颜色、品牌、速度(属性)，能加速、刹车、转弯(行为)
- 一个 **学生** → 有姓名、年龄、成绩(属性)，能学习、考试、交作业(行为)
- 一只 **猫** → 有品种、体重、颜色(属性)，能吃饭、睡觉、喵喵叫(行为)

**面向对象 = 把数据(属性)和操作数据的函数(方法)打包在一起**

### 1.3 类 vs 对象——模具与产品

| 概念 | 类比 | 编程中 |
|------|------|--------|
| **类 (Class)** | 建筑图纸 / 月饼模具 | 模板，定义了属性和方法 |
| **对象 (Object/Instance)** | 盖好的房子 / 做出的月饼 | 根据模板创建的具体东西 |

**一个类可以创建无数个对象**，就像一个模具可以做出无数个月饼。

```
类: 学生
├── 属性: 姓名, 年龄, 成绩
├── 方法: 学习(), 考试()
│
├── 对象1: 小明, 18岁, 95分
├── 对象2: 小红, 17岁, 88分
└── 对象3: 小刚, 19岁, 72分
```

### 1.4 面向过程 vs 面向对象 —— 代码对比

**面向过程版本**（用字典 + 函数）：
```python
# 数据
student1 = {"name": "小明", "age": 18, "score": 95}
student2 = {"name": "小红", "age": 17, "score": 88}

# 函数（和数据分离）
def introduce(student):
    print(f"我叫{student['name']}，今年{student['age']}岁")

def study(student, subject):
    print(f"{student['name']}正在学习{subject}")

introduce(student1)  # 每次都要传 student 进去
study(student1, "数学")
```

**面向对象版本**：
```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")
    
    def study(self, subject):
        print(f"{self.name}正在学习{subject}")

s1 = Student("小明", 18, 95)
s1.introduce()        # 数据和行为绑定在一起！
s1.study("数学")
```

数据和行为**住在同一个房子里**，不再分居。

---

## 第二部分：定义你的第一个类 (30 分钟)

### 2.1 类的基本语法

```python
class 类名:
    """文档字符串（可选，描述这个类的作用）"""
    
    def __init__(self, 参数1, 参数2):
        """构造方法：创建对象时自动调用"""
        self.属性1 = 参数1
        self.属性2 = 参数2
    
    def 方法名(self, 其他参数):
        """实例方法：操作对象的行为"""
        # 用 self.属性 来访问自己的数据
        pass
```

**命名规范**：
- **类名**用**大驼峰** (PascalCase)：`Student`, `BankAccount`, `GameCharacter`
- **方法名/属性名**用**蛇形** (snake_case)：`get_score`, `max_health`

### 2.2 `__init__` —— 构造方法

`__init__` 是一个**魔术方法** (Magic Method / Dunder Method)，双下划线开头结尾。

它在你"创建对象"的时候自动执行——就是"出生仪式"。

```python
class Cat:
    def __init__(self, name, breed):
        print(f"一只叫 {name} 的猫诞生了！")
        self.name = name       # 把参数存到对象身上
        self.breed = breed
        self.energy = 100      # 默认值，不需要传参

# 创建对象（自动调用 __init__）
my_cat = Cat("咪咪", "橘猫")
# 输出: 一只叫 咪咪 的猫诞生了！
```

### 2.3 `self` 是什么？

`self` 是**当前对象自己**的引用。

**类比**: 你在写自我介绍时用"我"这个字。对于 Python 的类，"我"就是 `self`。

```python
class Dog:
    def __init__(self, name):
        self.name = name  # self.name = "当前这只狗的名字"

    def bark(self):
        # self 就是调用这个方法的那个对象
        print(f"{self.name}: 汪汪汪！")

dog1 = Dog("旺财")
dog2 = Dog("大黄")

dog1.bark()  # self = dog1, 输出: 旺财: 汪汪汪！
dog2.bark()  # self = dog2, 输出: 大黄: 汪汪汪！
```

**注意**：
- `self` 是**约定俗成**的名字，技术上你写 `this` 也行，但**千万别这么做**
- 调用方法时**不需要**传 self，Python 自动传

### 2.4 实例属性 vs 参数

```python
class Phone:
    def __init__(self, brand, price):
        # 实例属性 = self.xxx
        self.brand = brand     # 来自参数
        self.price = price     # 来自参数
        self.battery = 100     # 默认值（不依赖参数）
        self.is_on = False     # 默认关机
```

每个 Phone 对象都有**独立**的属性，互不影响。

---

## 第三部分：给对象添加行为——实例方法 (30 分钟)

### 3.1 定义和调用实例方法

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance  # 余额
    
    def deposit(self, amount):
        """存钱"""
        if amount > 0:
            self.balance += amount
            print(f"存入 {amount} 元，余额: {self.balance} 元")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        """取钱"""
        if amount > self.balance:
            print(f"余额不足！当前余额: {self.balance} 元")
        elif amount <= 0:
            print("取款金额必须大于0")
        else:
            self.balance -= amount
            print(f"取出 {amount} 元，余额: {self.balance} 元")
    
    def show_balance(self):
        """查询余额"""
        print(f"{self.owner}的账户余额: {self.balance} 元")

# 使用
acc = BankAccount("小明", 1000)
acc.show_balance()   # 小明的账户余额: 1000 元
acc.deposit(500)     # 存入 500 元，余额: 1500 元
acc.withdraw(200)    # 取出 200 元，余额: 1300 元
acc.withdraw(2000)   # 余额不足！当前余额: 1300 元
```

### 3.2 方法之间互相调用

方法内部可以用 `self.其他方法()` 调用：

```python
class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.is_alive = True
    
    def take_damage(self, damage):
        """受到伤害"""
        self.hp -= damage
        print(f"{self.name} 受到 {damage} 点伤害, 剩余 HP: {self.hp}")
        self._check_alive()   # 调用自己的另一个方法
    
    def _check_alive(self):
        """检查是否存活（方法名前加_表示"内部使用"）"""
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.name} 已阵亡！")
    
    def heal(self, amount):
        """回血"""
        if not self.is_alive:
            print(f"{self.name} 已经阵亡，无法治疗")
            return
        self.hp += amount
        if self.hp > 100:
            self.hp = 100  # 不超过最大生命值
        print(f"{self.name} 恢复了 {amount} HP, 当前 HP: {self.hp}")

hero = Player("勇者")
hero.take_damage(30)   # 勇者 受到 30 点伤害, 剩余 HP: 70
hero.heal(15)          # 勇者 恢复了 15 HP, 当前 HP: 85
hero.take_damage(100)  # 勇者 受到 100 点伤害, 剩余 HP: 0 → 勇者 已阵亡！
hero.heal(50)          # 勇者 已经阵亡，无法治疗
```

### 3.3 `__str__` 方法——让 print 更好看

当你 `print(对象)` 时，默认输出是一段看不懂的内存地址。

```python
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        """定义 print(对象) 时显示什么"""
        return f"《{self.title}》 作者: {self.author}, 定价: {self.price}元"

b = Book("三体", "刘慈欣", 59.9)
print(b)  # 《三体》 作者: 刘慈欣, 定价: 59.9元
# 如果没有 __str__，输出类似: <__main__.Book object at 0x7f3b3c4d5e60>
```

---

## 第四部分：对象之间的交互 (20 分钟)

### 4.1 对象可以作为另一个对象的属性

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"引擎启动！{self.horsepower}马力轰鸣！")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # engine 是另一个对象！
        self.speed = 0
    
    def start(self):
        print(f"{self.brand} 准备出发...")
        self.engine.start()   # 调用 engine 对象的方法
    
    def accelerate(self, amount):
        self.speed += amount
        print(f"当前速度: {self.speed} km/h")

v8 = Engine(450)
my_car = Car("特斯拉", v8)
my_car.start()
# 特斯拉 准备出发...
# 引擎启动！450马力轰鸣！
```

### 4.2 对象可以放在列表/字典里

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return f"{self.name}: {self.score}分"

# 创建一个班级（学生对象的列表）
classroom = [
    Student("小明", 95),
    Student("小红", 88),
    Student("小刚", 72),
    Student("小美", 91),
]

# 找出最高分
best = max(classroom, key=lambda s: s.score)
print(f"最高分: {best}")  # 最高分: 小明: 95分

# 及格的同学
passed = [s for s in classroom if s.score >= 80]
print("80分以上:")
for s in passed:
    print(f"  {s}")

# 按分数排序
classroom.sort(key=lambda s: s.score, reverse=True)
print("\n排名:")
for i, s in enumerate(classroom, 1):
    print(f"  第{i}名: {s}")
```

---

## 第五部分：重点总结与常见错误 (10 分钟)

### 5.1 本节核心概念

| 概念 | 说明 |
|------|------|
| `class` | 定义类（模板） |
| `对象 = 类名()` | 创建对象（实例化） |
| `__init__` | 构造方法，创建对象时自动调用 |
| `self` | 当前对象自身的引用 |
| `self.xxx` | 实例属性，每个对象独立一份 |
| 实例方法 | 定义在类中的函数，第一个参数是 self |
| `__str__` | 控制 print(对象) 的输出 |

### 5.2 新手常见错误

```python
# ❌ 错误1：忘记 self
class Wrong:
    def __init__(self, name):
        name = name  # 这只是局部变量，没有绑定到对象上！
        # ✅ 应该: self.name = name

# ❌ 错误2：方法忘记写 self 参数
class Wrong:
    def greet():  # 少了 self!
        print("Hello")
# w = Wrong()
# w.greet()  # TypeError!

# ❌ 错误3：__init__ 拼成 __int__ 或 _init_ 或 init
class Wrong:
    def _init_(self, name):  # 少了一个下划线！
        self.name = name  # 这个方法不会被自动调用

# ❌ 错误4：在类外部用 self
# self 只能在类的方法内部使用！
```

---

## 知识地图

```
OOP 第1课
│
├── 为什么需要 OOP
│   ├── 面向过程 vs 面向对象
│   └── 类 vs 对象 (图纸 vs 产品)
│
├── 定义类
│   ├── class 语法
│   ├── __init__ 构造方法
│   ├── self 的含义
│   └── 实例属性
│
├── 实例方法
│   ├── 定义和调用
│   ├── 方法内调用方法
│   └── __str__ 方法
│
└── 对象交互
    ├── 对象作为属性
    └── 对象放在容器中
```
