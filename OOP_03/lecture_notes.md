# OOP 第3课：继承与多态

**课程时长**: 约 2 小时  
**前置知识**: OOP 第1-2课（类、对象、封装、property、魔术方法）  
**教学目标**: 掌握继承的核心概念，理解方法重写与 `super()`，理解多态思想，了解抽象类。

---

## 第一部分：继承——代码复用的艺术 (30 分钟)

### 1.1 什么是继承？

**生活类比**: 
- 你继承了父母的基因（某些特征自动拥有）
- 但你也有自己独特的特征（可以扩展）
- 你甚至可以改变遗传来的特征（方法重写）

**编程中**: 子类自动获得父类的所有属性和方法，还可以扩展和修改。

```
        Animal (父类/基类/超类)
        ├── name, age
        ├── eat(), sleep()
        │
        ├── Dog (子类/派生类)
        │   ├── 继承: name, age, eat(), sleep()
        │   └── 新增: breed, bark(), fetch()
        │
        └── Cat (子类/派生类)
            ├── 继承: name, age, eat(), sleep()
            └── 新增: indoor, purr(), scratch()
```

### 1.2 基本语法

```python
class Animal:
    """父类 (基类)"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self, food):
        print(f"{self.name} 正在吃 {food}")
    
    def sleep(self):
        print(f"{self.name} 正在睡觉 💤")
    
    def __str__(self):
        return f"{self.name} ({self.age}岁)"


class Dog(Animal):
    """子类：在括号里写父类名"""
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类的 __init__
        self.breed = breed           # Dog 特有的属性
    
    def bark(self):                  # Dog 特有的方法
        print(f"{self.name}: 汪汪汪！🐕")
    
    def fetch(self, item):
        print(f"{self.name} 捡回了 {item}")


class Cat(Animal):
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)
        self.indoor = indoor
    
    def purr(self):
        print(f"{self.name}: 呼噜呼噜~ 🐱")
    
    def scratch(self, target):
        print(f"{self.name} 挠了 {target}！")


# 使用
dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2)

# 继承来的方法
dog.eat("骨头")     # 旺财 正在吃 骨头 (来自 Animal)
dog.sleep()         # 旺财 正在睡觉 💤 (来自 Animal)
print(dog)          # 旺财 (3岁) (来自 Animal 的 __str__)

# 自己的方法
dog.bark()          # 旺财: 汪汪汪！🐕
dog.fetch("飞盘")    # 旺财 捡回了 飞盘

cat.eat("小鱼")      # 咪咪 正在吃 小鱼
cat.purr()           # 咪咪: 呼噜呼噜~

# dog.purr()  ❌ Dog 没有 purr 方法
# cat.bark()  ❌ Cat 没有 bark 方法
```

### 1.3 `super()` ——调用父类

`super()` 用来调用**父类的方法**，最常用在 `__init__` 中。

```python
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
        self.speed = 0

class ElectricCar(Vehicle):
    def __init__(self, brand, max_speed, battery_capacity):
        super().__init__(brand, max_speed)  # 先让父类做初始化
        self.battery = battery_capacity      # 再做自己的初始化
        self.charge = 100  # 百分比
```

**为什么用 `super()` 而不是直接写父类名？**
```python
# 不推荐（但能工作）：
# Vehicle.__init__(self, brand, max_speed)

# 推荐（特别是多继承时更安全）：
# super().__init__(brand, max_speed)
```

### 1.4 `isinstance()` 和 `issubclass()`

```python
dog = Dog("旺财", 3, "金毛")

print(isinstance(dog, Dog))     # True  (旺财是Dog)
print(isinstance(dog, Animal))  # True  (旺财也是Animal!)
print(isinstance(dog, Cat))     # False (旺财不是Cat)

print(issubclass(Dog, Animal))  # True  (Dog是Animal的子类)
print(issubclass(Cat, Animal))  # True  (Cat是Animal的子类)
print(issubclass(Dog, Cat))     # False (Dog不是Cat的子类)
```

---

## 第二部分：方法重写 (Override) (25 分钟)

### 2.1 什么是方法重写？

子类可以**重新定义**父类的方法，改变其行为。

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} 发出了声音")
    
    def __str__(self):
        return f"Animal: {self.name}"


class Dog(Animal):
    def speak(self):
        """重写父类的 speak 方法"""
        print(f"{self.name}: 汪汪！🐕")
    
    def __str__(self):
        return f"🐕 {self.name}"


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 喵喵！🐱")
    
    def __str__(self):
        return f"🐱 {self.name}"


class Duck(Animal):
    def speak(self):
        print(f"{self.name}: 嘎嘎！🦆")


a = Animal("动物")
d = Dog("旺财")
c = Cat("咪咪")

a.speak()  # 动物 发出了声音 (父类版本)
d.speak()  # 旺财: 汪汪！🐕 (Dog 重写版本)
c.speak()  # 咪咪: 喵喵！🐱 (Cat 重写版本)
```

### 2.2 用 `super()` 扩展而非替换

有时候你不想完全替换父类的方法，而是在其基础上**添加功能**。

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} 正在工作")
    
    def get_info(self):
        return f"姓名: {self.name}, 基本工资: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)      # 父类负责 name, salary
        self.department = department
        self.team = []
    
    def work(self):
        super().work()                      # 先调用父类的 work
        print(f"  (正在管理 {self.department} 部门)")  # 再加自己的
    
    def add_member(self, employee):
        self.team.append(employee)
        print(f"  {employee.name} 加入了 {self.department}")
    
    def get_info(self):
        base_info = super().get_info()       # 获取父类的信息
        return f"{base_info}, 部门: {self.department}, 团队人数: {len(self.team)}"


e = Employee("小红", 8000)
m = Manager("张总", 20000, "技术部")

e.work()
# 小红 正在工作

m.work()
# 张总 正在工作            (来自 super().work())
#   (正在管理 技术部 部门)   (Manager 自己添加的)

m.add_member(e)
print(m.get_info())
# 姓名: 张总, 基本工资: 20000, 部门: 技术部, 团队人数: 1
```

### 2.3 方法解析顺序 (MRO)

Python 按照一定顺序查找方法（从子类到父类）：

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(B):
    pass  # 没有定义 greet

c = C()
c.greet()  # Hello from B  (C没有 → 找B → 找到了！)

# 查看 MRO
print(C.__mro__)
# (<class 'C'>, <class 'B'>, <class 'A'>, <class 'object'>)
# 搜索顺序: C → B → A → object
```

---

## 第三部分：多态——同一方法，不同表现 (25 分钟)

### 3.1 什么是多态？

多态 = **同一个方法名，不同对象有不同的实现**

**类比**: "说话"这个动作：
- 人类 → 说普通话
- 狗 → 汪汪叫
- 猫 → 喵喵叫

它们都在"说话"，但方式不同。

### 3.2 多态实战

```python
class Shape:
    def area(self):
        return 0
    
    def describe(self):
        return f"{self.__class__.__name__}: 面积 = {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


# 多态的威力：统一处理不同类型
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(8, 6),
    Rectangle(3, 3),
    Circle(2.5),
]

# 同一个方法调用，不同的结果（多态！）
print("所有图形:")
for shape in shapes:
    print(f"  {shape.describe()}")

# 计算总面积（不需要知道具体是什么图形）
total_area = sum(s.area() for s in shapes)
print(f"\n总面积: {total_area:.2f}")
```

### 3.3 鸭子类型 (Duck Typing)

> "如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子。"

Python 不在乎对象的**类型**，只在乎它**能做什么**。

```python
class Duck:
    def quack(self):
        print("嘎嘎嘎！")
    
    def walk(self):
        print("摇摇摆摆走路")

class Person:
    def quack(self):
        print("我在模仿鸭子叫：嘎嘎嘎！")
    
    def walk(self):
        print("正常走路")

class RubberDuck:
    def quack(self):
        print("吱吱吱！（塑料鸭叫声）")
    
    def walk(self):
        print("（不会走路，在水上漂）")

def test_duck(duck):
    """这个函数不关心传入的是什么类型"""
    duck.quack()
    duck.walk()

# Person 和 RubberDuck 都不是 Duck 的子类
# 但它们都有 quack() 和 walk() 方法，所以可以用！
for thing in [Duck(), Person(), RubberDuck()]:
    test_duck(thing)
    print()
```

**Python 哲学**: 不需要继承同一个父类，只要有相同的方法就能一起使用。

### 3.4 多态在内置类型中的体现

你其实已经一直在用多态了：

```python
# len() 对不同类型的行为不同
print(len("Hello"))    # 5 (字符数)
print(len([1, 2, 3]))  # 3 (元素数)
print(len({"a": 1}))   # 1 (键值对数)

# + 对不同类型的行为不同
print(1 + 2)           # 3 (数字相加)
print("Hello" + " World")  # Hello World (字符串拼接)
print([1, 2] + [3, 4])     # [1, 2, 3, 4] (列表合并)

# for 循环对不同类型的遍历行为不同
# 字符串：逐字符
# 列表：逐元素
# 字典：逐键
```

---

## 第四部分：抽象类——定义规范 (20 分钟)

### 4.1 问题引入

如果你定义一个 `Shape` 基类，但忘记在子类中实现 `area` 方法怎么办？

```python
class Shape:
    def area(self):
        return 0  # 这个默认值没有意义

class Hexagon(Shape):
    def __init__(self, side):
        self.side = side
    # 忘记实现 area() 了！

h = Hexagon(5)
print(h.area())  # 0  ← 悄悄返回了错误结果，没有任何提醒！
```

### 4.2 抽象类和抽象方法

使用 `abc` 模块（Abstract Base Class）**强制**子类实现某些方法。

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """抽象基类：不能直接创建对象"""
    
    @abstractmethod
    def area(self):
        """子类必须实现这个方法"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """子类必须实现这个方法"""
        pass
    
    def describe(self):
        """普通方法：子类可以直接使用"""
        return f"{self.__class__.__name__}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"


# s = Shape()  # ❌ TypeError: 不能实例化抽象类！

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


# 如果子类没有实现所有抽象方法：
# class BadShape(Shape):
#     def area(self):
#         return 0
#     # 忘了实现 perimeter!
# b = BadShape()  # ❌ TypeError!

r = Rectangle(10, 5)
c = Circle(7)
print(r.describe())  # Rectangle: 面积=50.00, 周长=30.00
print(c.describe())  # Circle: 面积=153.94, 周长=43.98
```

### 4.3 抽象类的应用：支付接口

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """支付处理器接口"""
    
    @abstractmethod
    def pay(self, amount):
        pass
    
    @abstractmethod
    def refund(self, amount):
        pass
    
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")


class AliPay(PaymentProcessor):
    def __init__(self, account):
        self.account = account
    
    def pay(self, amount):
        self.log(f"支付宝支付 ¥{amount}")
        return True
    
    def refund(self, amount):
        self.log(f"支付宝退款 ¥{amount}")
        return True


class WeChatPay(PaymentProcessor):
    def __init__(self, openid):
        self.openid = openid
    
    def pay(self, amount):
        self.log(f"微信支付 ¥{amount}")
        return True
    
    def refund(self, amount):
        self.log(f"微信退款 ¥{amount}")
        return True


def process_order(processor, amount):
    """处理订单——不关心具体用什么支付方式"""
    print(f"订单金额: ¥{amount}")
    processor.pay(amount)

# 多态 + 抽象类
alipay = AliPay("user@alipay")
wechat = WeChatPay("wx_openid_123")

process_order(alipay, 99.9)   # 支付宝支付
process_order(wechat, 49.9)   # 微信支付
```

---

## 第五部分：多层继承和组合 (15 分钟)

### 5.1 多层继承

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} 在呼吸")

class Mammal(Animal):
    def feed_milk(self):
        print(f"{self.name} 在哺乳")

class Dog(Mammal):
    def bark(self):
        print(f"{self.name}: 汪！")

# Dog 拥有三层的所有方法
dog = Dog("旺财")
dog.breathe()     # 来自 Animal
dog.feed_milk()   # 来自 Mammal
dog.bark()        # 自己的
```

### 5.2 继承 vs 组合

**继承** = "A **是** B"（is-a 关系）
**组合** = "A **有** B"（has-a 关系）

```python
# ❌ 不好的继承（引擎不是汽车）
class Engine:
    def start(self): print("引擎启动")

class Car(Engine):  # Car IS-A Engine？不对！
    pass

# ✅ 正确的组合（汽车有引擎）
class Engine:
    def start(self): print("引擎启动")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine ✅
    
    def start(self):
        self.engine.start()
```

**经验法则**: 
- 能用**组合**解决的，优先用组合
- 只有真正的 "is-a" 关系才用继承

---

## 第六部分：重点总结 (5 分钟)

### 知识地图

```
OOP 第3课
│
├── 继承
│   ├── class 子类(父类)
│   ├── super().__init__()
│   ├── isinstance / issubclass
│   └── 多层继承
│
├── 方法重写
│   ├── 完全重写（替换）
│   ├── super() 扩展（增强）
│   └── MRO 方法解析顺序
│
├── 多态
│   ├── 同一方法，不同行为
│   ├── 鸭子类型
│   └── 内置多态示例
│
├── 抽象类
│   ├── ABC + @abstractmethod
│   ├── 强制子类实现
│   └── 接口设计
│
└── 继承 vs 组合
    ├── is-a → 继承
    └── has-a → 组合
```

### 设计原则

1. **单一职责**: 一个类只做一件事
2. **开闭原则**: 对扩展开放，对修改关闭（用继承添加新功能，不改旧代码）
3. **里氏替换**: 子类能替代父类使用（不应破坏父类的行为）
4. **组合优于继承**: 能用组合就别用继承
