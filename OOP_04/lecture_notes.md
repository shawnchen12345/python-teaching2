# OOP 第4课：综合实战与设计模式

**课程时长**: 约 2 小时  
**前置知识**: OOP 第1-3课（类与对象、封装、继承、多态）  
**教学目标**: 综合运用所有 OOP 知识完成实战项目，了解常用设计模式，掌握 OOP 项目设计思维。

---

## 第一部分：OOP 知识体系回顾 (15 分钟)

### 1.1 四大特性总结

| 特性 | 含义 | 关键技术 |
|------|------|----------|
| **封装** | 隐藏内部实现细节 | `_`, `__`, `@property` |
| **继承** | 子类复用父类功能 | `class Dog(Animal)`, `super()` |
| **多态** | 同一接口，不同实现 | 方法重写、鸭子类型 |
| **抽象** | 定义接口规范 | `ABC`, `@abstractmethod` |

### 1.2 设计口诀

```
写代码之前先想：
1. 有哪些"东西"？→ 定义类
2. 每个东西有哪些"特征"？→ 定义属性
3. 每个东西能做哪些"动作"？→ 定义方法
4. 这些东西之间什么关系？→ 继承 or 组合
5. 有什么共同行为可以统一？→ 多态 + 抽象类
```

---

## 第二部分：常用设计模式入门 (30 分钟)

### 2.1 什么是设计模式？

设计模式 = 前人总结的"最佳实践"，解决特定问题的通用方案。

就像武术有招式一样，编程也有套路。

### 2.2 工厂模式 (Factory Pattern)

**问题**: 创建对象的过程很复杂，或者需要根据条件创建不同类型的对象。

**方案**: 用一个"工厂"来统一创建对象。

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}: 汪汪！"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: 喵喵！"

class Bird(Animal):
    def speak(self):
        return f"{self.name}: 啾啾！"


class AnimalFactory:
    """工厂类：根据类型创建动物"""
    
    _animal_types = {
        "dog": Dog,
        "cat": Cat,
        "bird": Bird,
    }
    
    @classmethod
    def create(cls, animal_type, name):
        animal_class = cls._animal_types.get(animal_type.lower())
        if animal_class is None:
            raise ValueError(f"未知动物类型: {animal_type}")
        return animal_class(name)
    
    @classmethod
    def register(cls, animal_type, animal_class):
        """注册新动物类型（可扩展！）"""
        cls._animal_types[animal_type.lower()] = animal_class


# 使用工厂
dog = AnimalFactory.create("dog", "旺财")
cat = AnimalFactory.create("cat", "咪咪")
print(dog.speak())  # 旺财: 汪汪！
print(cat.speak())  # 咪咪: 喵喵！

# 动态扩展
class Snake(Animal):
    def speak(self):
        return f"{self.name}: 嘶嘶~"

AnimalFactory.register("snake", Snake)
snake = AnimalFactory.create("snake", "小青")
print(snake.speak())  # 小青: 嘶嘶~
```

### 2.3 观察者模式 (Observer Pattern)

**问题**: 一个对象的状态变化了，需要通知其他对象。

**方案**: 被观察的对象维护一个"观察者"列表，有变化时通知所有观察者。

```python
class EventSystem:
    """事件系统（被观察者）"""
    def __init__(self):
        self._listeners = {}  # {"事件名": [回调函数1, 回调函数2]}
    
    def on(self, event, callback):
        """注册事件监听器"""
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)
    
    def emit(self, event, data=None):
        """触发事件，通知所有监听器"""
        if event in self._listeners:
            for callback in self._listeners[event]:
                callback(data)


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.events = EventSystem()
    
    def take_damage(self, damage):
        self.hp -= damage
        self.events.emit("damage", {"player": self.name, "damage": damage, "hp": self.hp})
        
        if self.hp <= 0:
            self.hp = 0
            self.events.emit("death", {"player": self.name})


# 创建UI和日志系统来监听事件
def on_damage(data):
    print(f"[UI] {data['player']} 受到 {data['damage']} 伤害! HP: {data['hp']}")

def on_death(data):
    print(f"[UI] ☠️ {data['player']} 已阵亡!")

def log_damage(data):
    print(f"[LOG] 伤害记录: {data}")


p = Player("勇者")
p.events.on("damage", on_damage)     # UI 监听伤害
p.events.on("damage", log_damage)    # 日志也监听伤害
p.events.on("death", on_death)       # UI 监听死亡

p.take_damage(30)
p.take_damage(80)
```

### 2.4 策略模式 (Strategy Pattern)

**问题**: 同一个操作有多种算法/策略，需要灵活切换。

**方案**: 把算法封装成类，可以动态替换。

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        print("  (使用冒泡排序)")
        return arr

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[0]
        left = [x for x in data[1:] if x <= pivot]
        right = [x for x in data[1:] if x > pivot]
        print("  (使用快速排序)")
        return self.sort(left) + [pivot] + self.sort(right)

class Sorter:
    def __init__(self, strategy=None):
        self.strategy = strategy or BubbleSort()
    
    def set_strategy(self, strategy):
        """动态切换排序策略"""
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy.sort(data)


data = [64, 34, 25, 12, 22, 11, 90]
sorter = Sorter()

result = sorter.sort(data)
print(f"  结果: {result}")

sorter.set_strategy(QuickSort())  # 切换策略
result = sorter.sort(data)
print(f"  结果: {result}")
```

---

## 第三部分：综合实战——在线商城系统 (45 分钟)

### 3.1 需求分析

我们要设计一个迷你在线商城，包含：
- **商品管理**: 不同类型的商品（书籍、电子产品、服装）
- **购物车**: 添加/删除商品，计算总价
- **用户系统**: 普通用户、VIP用户（不同折扣）
- **订单**: 创建订单、订单状态管理
- **支付**: 多种支付方式（多态）

### 3.2 类的设计思路

```
商城系统
├── Product (抽象类)
│   ├── Book
│   ├── Electronics
│   └── Clothing
│
├── User
│   ├── RegularUser
│   └── VIPUser
│
├── ShoppingCart
│
├── Order
│
└── Payment (抽象类)
    ├── CashPayment
    └── OnlinePayment
```

### 3.3 核心知识点映射

| 模块 | 用到的 OOP 知识 |
|------|-----------------|
| Product 体系 | 抽象类、继承、方法重写 |
| User 体系 | 继承、property、封装 |
| ShoppingCart | 组合、魔术方法(`__len__`, `__str__`) |
| Order | 封装、状态管理 |
| Payment | 多态、策略模式 |

---

## 第四部分：项目代码逐步实现 (讲解思路)

### 4.1 第一步：设计商品体系

使用**抽象类**定义商品接口，不同商品类型有不同的折扣计算方式。

**关键点**：
- `@abstractmethod` 强制子类实现 `get_discount()`
- `@property` 计算最终价格 `final_price`

### 4.2 第二步：设计用户体系

用**继承**区分普通用户和VIP用户：
- `RegularUser`: 无额外折扣
- `VIPUser`: 额外 9 折，有积分系统

**关键点**：
- `super()` 复用父类初始化
- 方法重写 `get_discount_rate()`

### 4.3 第三步：购物车

用**组合**方式，购物车持有商品列表。

**关键点**：
- `__len__`、`__str__`、`__contains__` 魔术方法
- 对象交互（Cart 和 Product 配合）

### 4.4 第四步：订单和支付

用**多态**实现不同支付方式。

**关键点**：
- 订单状态机（pending → paid → shipped → completed）
- 支付策略可替换

---

## 第五部分：课程总结与进阶路线 (15 分钟)

### 5.1 完整知识地图

```
Python OOP 知识体系
│
├── 第1课：基础
│   ├── class / object
│   ├── __init__ / self
│   ├── 实例属性 / 实例方法
│   └── __str__
│
├── 第2课：封装与进阶
│   ├── 访问控制 (_, __)
│   ├── @property
│   ├── 类属性 / 类方法 / 静态方法
│   └── 魔术方法大全
│
├── 第3课：继承与多态
│   ├── 继承 / super()
│   ├── 方法重写
│   ├── 多态 / 鸭子类型
│   └── 抽象类 ABC
│
└── 第4课：实战与设计
    ├── 设计模式（工厂、观察者、策略）
    ├── 综合项目实战
    └── 进阶路线
```

### 5.2 OOP 设计原则 (SOLID)

| 原则 | 含义 | 通俗解释 |
|------|------|----------|
| **S** - 单一职责 | 一个类只做一件事 | 不要让"瑞士军刀类"出现 |
| **O** - 开闭原则 | 对扩展开放，对修改关闭 | 加新功能时写新代码，不改旧代码 |
| **L** - 里氏替换 | 子类能替代父类 | 子类不应该破坏父类的行为 |
| **I** - 接口隔离 | 接口不要太大 | 别让类实现它不需要的方法 |
| **D** - 依赖倒置 | 依赖抽象，不依赖具体 | 通过接口交互，不直接依赖实现 |

### 5.3 学完 OOP 后的进阶方向

1. **异常处理**: 自定义异常类（继承 `Exception`）
2. **迭代器与生成器**: `__iter__`, `__next__`, `yield`
3. **装饰器模式**: 函数装饰器和类装饰器
4. **多继承与 Mixin**: 解决多继承的复杂性
5. **元类 (Metaclass)**: 高级话题，"类的类"
6. **数据类 `@dataclass`**: Python 3.7+ 的便捷类定义
7. **实际项目**: 
   - 用 Pygame 做游戏（大量 OOP）
   - 用 Flask/Django 做 Web 应用（MVC 架构）
   - 用 GUI 框架做桌面应用（事件驱动 OOP）

### 5.4 给学生的建议

> "不要为了 OOP 而 OOP。"

- 简单脚本（100行以内）→ 面向过程就够了
- 中型项目（几百到几千行）→ 用 OOP 组织代码
- 大型项目 → 必须 OOP + 设计模式
- **多读好代码**（GitHub 上的 Python 优秀项目）
- **多写项目**，实战是最好的老师
