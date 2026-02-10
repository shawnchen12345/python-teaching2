# OOP 第2课：封装与进阶特性

**课程时长**: 约 2 小时  
**前置知识**: OOP 第1课（类、对象、`__init__`、实例属性和方法）  
**教学目标**: 理解封装的意义，掌握访问控制、property 装饰器、类属性/类方法/静态方法、常用魔术方法。

---

## 第一部分：封装——保护你的数据 (30 分钟)

### 1.1 什么是封装？

封装 = **把数据藏起来，只通过方法来操作**

**生活类比**：
- 你的手机：你按按钮就能打电话，不需要知道内部电路怎么工作
- ATM 机：你插卡输密码就能取钱，不需要知道金库在哪
- 汽车：你踩油门就能加速，不需要知道发动机气缸怎么运转

**核心思想**: 外部只看到**接口**（能做什么），不关心**内部实现**（怎么做的）。

### 1.2 Python 的访问控制约定

Python 没有像 Java 那样的 `private` / `public` 关键字，而是用**命名约定**：

| 约定 | 含义 | 示例 |
|------|------|------|
| `name` | 公开属性，谁都能用 | `self.name = "小明"` |
| `_name` | "内部使用"，外部**不应该**直接用 | `self._balance = 0` |
| `__name` | "名称改编"，外部**很难**直接用 | `self.__password = "123"` |

**注意**: Python 的态度是 **"We are all consenting adults"**（我们都是成年人），单下划线只是礼貌提醒，不是强制限制。

### 1.3 单下划线 `_` ——"请勿打扰"

```python
class Player:
    def __init__(self, name, hp=100):
        self.name = name      # 公开：名字大家都能看
        self._hp = hp          # 内部：HP 不应该被随意修改
        self._max_hp = 100
    
    def take_damage(self, dmg):
        self._hp = max(0, self._hp - dmg)
        print(f"{self.name} 受伤，HP: {self._hp}/{self._max_hp}")
    
    def heal(self, amount):
        self._hp = min(self._max_hp, self._hp + amount)
        print(f"{self.name} 治疗，HP: {self._hp}/{self._max_hp}")

p = Player("勇者")
p.take_damage(30)

# 技术上可以直接改，但你不应该这么做：
# p._hp = 999999  # 这是作弊！虽然 Python 不阻止你
```

### 1.4 双下划线 `__` ——"名称改编" (Name Mangling)

```python
class Secret:
    def __init__(self):
        self.__password = "super_secret_123"
    
    def verify(self, pwd):
        return pwd == self.__password

s = Secret()
print(s.verify("super_secret_123"))  # True

# 直接访问会报错
# print(s.__password)  # ❌ AttributeError!

# 但其实 Python 只是把名字改了（不是真正隐藏）
print(s._Secret__password)  # 这样能访问，但千万别这么做！
```

**双下划线的真正用途**: 防止子类意外覆盖父类的属性（后面学继承时会理解）。

---

## 第二部分：Property ——优雅的属性访问控制 (30 分钟)

### 2.1 问题引入：Getter 和 Setter

在 Java 中，你需要这样写：
```java
private int age;
public int getAge() { return age; }
public void setAge(int age) { this.age = age; }
```

Python 有更优雅的方式——`@property` 装饰器。

### 2.2 @property 基础用法

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # 内部存储
    
    @property
    def radius(self):
        """getter: 获取半径"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """setter: 设置半径（带验证）"""
        if value <= 0:
            raise ValueError("半径必须大于0！")
        self._radius = value
    
    @property
    def area(self):
        """只读属性：面积（没有 setter，不能赋值）"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """只读属性：周长"""
        return 2 * 3.14159 * self._radius

c = Circle(5)
print(c.radius)          # 5  (像访问属性一样，但其实调用了 getter)
print(f"面积: {c.area:.2f}")  # 78.54

c.radius = 10            # 像赋值一样，但其实调用了 setter
print(f"面积: {c.area:.2f}")  # 314.16

# c.radius = -1           # ❌ ValueError: 半径必须大于0！
# c.area = 100            # ❌ AttributeError: 没有 setter，不能赋值
```

**精髓**: 外部使用起来像普通属性（`c.radius`），但内部有验证逻辑。

### 2.3 实际应用：温度转换器

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度！")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """华氏度（只读，自动计算）"""
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        """开尔文（只读，自动计算）"""
        return self._celsius + 273.15
    
    def __str__(self):
        return f"{self._celsius}°C = {self.fahrenheit:.1f}°F = {self.kelvin:.1f}K"

t = Temperature(100)  # 水的沸点
print(t)              # 100°C = 212.0°F = 373.1K
print(t.fahrenheit)   # 212.0

t.celsius = 0         # 冰点
print(t)              # 0°C = 32.0°F = 273.1K
```

---

## 第三部分：类属性、类方法与静态方法 (30 分钟)

### 3.1 实例属性 vs 类属性

```python
class Dog:
    # 类属性：所有 Dog 对象共享
    species = "Canis lupus familiaris"  # 物种
    dog_count = 0                       # 总狗数
    
    def __init__(self, name):
        # 实例属性：每个对象独有
        self.name = name
        Dog.dog_count += 1  # 每创建一只狗，计数+1
    
    def __str__(self):
        return f"{self.name} ({Dog.species})"

d1 = Dog("旺财")
d2 = Dog("大黄")
d3 = Dog("小白")

print(Dog.dog_count)     # 3（通过类名访问类属性）
print(d1.dog_count)      # 3（也可以通过对象访问，但读到的是同一个值）
print(Dog.species)       # Canis lupus familiaris
```

**类属性 vs 实例属性**：

```
Dog 类
├── species = "Canis lupus familiaris"  ← 类属性（共享）
├── dog_count = 3                       ← 类属性（共享）
│
├── d1 → name = "旺财"                  ← 实例属性（独有）
├── d2 → name = "大黄"                  ← 实例属性（独有）
└── d3 → name = "小白"                  ← 实例属性（独有）
```

### 3.2 类方法 `@classmethod`

类方法操作的是**类本身**，而不是某个具体对象。第一个参数是 `cls`（类），而不是 `self`（对象）。

```python
class Student:
    school = "清华附中"  # 类属性
    all_students = []    # 所有学生
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.all_students.append(self)
    
    @classmethod
    def change_school(cls, new_school):
        """修改学校名（影响所有学生）"""
        cls.school = new_school
        print(f"学校更名为: {cls.school}")
    
    @classmethod
    def from_string(cls, info_str):
        """替代构造方法：从字符串创建对象"""
        # "小明-高三" → Student("小明", "高三")
        name, grade = info_str.split("-")
        return cls(name, grade)  # cls 就是 Student
    
    @classmethod
    def get_count(cls):
        return len(cls.all_students)
    
    def __str__(self):
        return f"{self.name} ({self.grade}) - {Student.school}"

s1 = Student("小明", "高三")
s2 = Student.from_string("小红-高二")  # 用类方法创建对象

print(s1)  # 小明 (高三) - 清华附中
print(s2)  # 小红 (高二) - 清华附中
print(f"总学生数: {Student.get_count()}")  # 总学生数: 2

Student.change_school("北大附中")  # 学校更名为: 北大附中
print(s1)  # 小明 (高三) - 北大附中  ← 所有学生都变了！
```

### 3.3 静态方法 `@staticmethod`

静态方法跟类和对象都**没关系**，它就是一个"恰好放在类里的普通函数"。

没有 `self` 也没有 `cls` 参数。

```python
class MathUtils:
    """数学工具类：纯粹的工具函数集合"""
    
    @staticmethod
    def is_even(n):
        return n % 2 == 0
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# 不需要创建对象，直接用类名调用
print(MathUtils.is_even(4))      # True
print(MathUtils.factorial(5))    # 120
print(MathUtils.is_prime(17))    # True
```

### 3.4 三种方法对比总结

| 类型 | 装饰器 | 第一个参数 | 用途 |
|------|--------|-----------|------|
| **实例方法** | 无 | `self` (对象) | 操作具体对象的数据 |
| **类方法** | `@classmethod` | `cls` (类) | 操作类级别的数据，替代构造 |
| **静态方法** | `@staticmethod` | 无 | 工具函数，恰好放在类里 |

---

## 第四部分：魔术方法大全 (25 分钟)

### 4.1 什么是魔术方法？

双下划线开头结尾的方法 (`__xxx__`) 被称为**魔术方法** (Magic Methods / Dunder Methods)。

它们让你的对象能使用 Python 内置语法（`+`, `==`, `len()`, `print()` 等）。

### 4.2 字符串表示

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        """给人看的（print 时调用）"""
        return f"{self.name} - ¥{self.price}"
    
    def __repr__(self):
        """给开发者看的（调试时调用）"""
        return f"Product(name='{self.name}', price={self.price})"

p = Product("手机", 4999)
print(p)       # 手机 - ¥4999        (调用 __str__)
print(repr(p)) # Product(name='手机', price=4999)  (调用 __repr__)
print([p])     # [Product(name='手机', price=4999)]  (列表里用 __repr__)
```

### 4.3 比较运算符

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __eq__(self, other):
        """=="""
        return self.score == other.score
    
    def __lt__(self, other):
        """< (定义了 < 后，Python 自动推导 >)"""
        return self.score < other.score
    
    def __le__(self, other):
        """<="""
        return self.score <= other.score
    
    def __str__(self):
        return f"{self.name}({self.score}分)"

s1 = Student("小明", 95)
s2 = Student("小红", 88)
s3 = Student("小刚", 95)

print(s1 == s3)     # True  (分数相同)
print(s1 > s2)      # True  (95 > 88)
print(s2 < s1)      # True

# 有了比较方法，就能排序！
students = [s1, s2, s3]
students.sort()  # 默认用 __lt__ 排序
for s in students:
    print(s)
```

### 4.4 算术运算符

```python
class Vector:
    """二维向量"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """+"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """-"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """* (向量 × 标量)"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __abs__(self):
        """abs() 求模长"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)     # Vector(4, 6)
print(v1 - v2)     # Vector(2, 2)
print(v1 * 3)      # Vector(9, 12)
print(abs(v1))     # 5.0 (3² + 4² = 25, √25 = 5)
```

### 4.5 容器协议：`__len__`, `__getitem__`, `__contains__`

```python
class Playlist:
    """播放列表"""
    def __init__(self, name):
        self.name = name
        self._songs = []
    
    def add(self, song):
        self._songs.append(song)
    
    def __len__(self):
        """len(playlist)"""
        return len(self._songs)
    
    def __getitem__(self, index):
        """playlist[i]"""
        return self._songs[index]
    
    def __contains__(self, song):
        """'xxx' in playlist"""
        return song in self._songs
    
    def __str__(self):
        return f"🎵 {self.name} ({len(self)} 首歌)"

pl = Playlist("我的最爱")
pl.add("晴天")
pl.add("七里香")
pl.add("稻香")

print(len(pl))          # 3
print(pl[0])            # 晴天
print(pl[-1])           # 稻香
print("晴天" in pl)     # True
print("夜曲" in pl)     # False

# 因为有 __getitem__，还能用 for 循环遍历！
for song in pl:
    print(f"  ♪ {song}")
```

### 4.6 魔术方法速查表

| 魔术方法 | 对应操作 | 示例 |
|----------|----------|------|
| `__init__` | 构造 | `obj = MyClass()` |
| `__str__` | print | `print(obj)` |
| `__repr__` | 调试输出 | `repr(obj)` |
| `__len__` | 长度 | `len(obj)` |
| `__getitem__` | 索引 | `obj[i]` |
| `__setitem__` | 赋值索引 | `obj[i] = x` |
| `__contains__` | in | `x in obj` |
| `__eq__` | == | `a == b` |
| `__lt__` | < | `a < b` |
| `__add__` | + | `a + b` |
| `__sub__` | - | `a - b` |
| `__mul__` | * | `a * b` |
| `__bool__` | 布尔值 | `if obj:` |
| `__call__` | 调用 | `obj()` |

---

## 第五部分：重点总结 (5 分钟)

### 知识地图

```
OOP 第2课
│
├── 封装
│   ├── 公开属性 (name)
│   ├── 约定内部 (_name)
│   └── 名称改编 (__name)
│
├── Property 装饰器
│   ├── @property (getter)
│   ├── @xxx.setter (setter)
│   └── 只读属性（无 setter）
│
├── 三种方法
│   ├── 实例方法 (self)
│   ├── 类方法 @classmethod (cls)
│   └── 静态方法 @staticmethod (无)
│
├── 类属性 vs 实例属性
│   ├── 类属性：共享数据
│   └── 实例属性：独有数据
│
└── 魔术方法
    ├── __str__ / __repr__
    ├── __eq__ / __lt__ (比较)
    ├── __add__ / __sub__ (运算)
    └── __len__ / __getitem__ (容器)
```
