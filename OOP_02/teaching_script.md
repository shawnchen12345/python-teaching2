# OOP 第2课 教师讲稿：封装与进阶特性

> **使用说明**: 本讲稿是口语化的教师逐字稿，配合 `lecture_notes.md` 中的代码示例使用。  
> 📌 = 板书/PPT要点 | 💬 = 互动提问 | ⏸️ = 停顿等学生思考 | 💻 = 切换到编辑器现场写代码 | ⏰ = 时间提示

---

## 课前复习 (5 分钟)

⏰ *00:00 - 00:05*

同学们好！上节课我们学了什么？

💬 **谁能用一句话告诉我，类和对象是什么关系？**

⏸️ *点一个学生回答*

没错！类是模具，对象是产品。类是图纸，对象是照着图纸盖出来的房子。

💬 **那 `self` 是什么意思？**

⏸️

对，`self` 就是"我自己"——谁调用这个方法，`self` 就指向谁。

💬 **快速提问：`__init__` 一共有几个下划线？左边几个右边几个？**

⏸️

左边两个，右边两个，一共四个！如果你上节课的作业写对了，说明你没踩这个坑。

好，今天我们要学的东西比上节课更进阶。上节课是"入门"，今天是"进阶"。

今天的主题是三个字：**封装**。以及一些让你的类更强大的高级特性。

---

## 第一部分：封装——保护你的数据 (30 分钟)

### 为什么要封装？ (8 分钟)

⏰ *00:05 - 00:13*

我先问大家一个问题。

上节课我们写了银行账户，对吧？余额是 `self.balance`。那如果有人这样写呢：

💻 *打开编辑器*

```python
acc = BankAccount("小明", 1000)
acc.balance = -999999  # 直接把余额改成负数！
```

💬 **这有问题吗？**

⏸️ *让学生说*

有大问题！任何人都可以从外面直接改你的余额，把它改成负数、改成无穷大，你的存取钱方法里的验证全部绕过了。

这就好比——ATM 机没有密码，谁都能直接从金库里拿钱。

📌 **封装 = 把数据藏起来，只允许通过特定的方法来操作**

生活中到处都是封装：
- **手机**: 你按按钮打电话，不需要知道电路怎么工作的
- **ATM**: 插卡输密码取钱，不需要知道金库在哪
- **汽车**: 踩油门就加速，不需要了解发动机内部结构

外部只看到**能做什么**（接口），不关心**怎么做的**（实现细节）。

### Python 的访问控制 (12 分钟)

⏰ *00:13 - 00:25*

那 Python 怎么实现封装呢？

Python 跟 Java 不一样，Java 有 `private`、`public` 这些关键字来强制限制访问。Python 没有这些关键字。

Python 的态度是什么呢？有一句名言：

📌 **"We are all consenting adults."（我们都是成年人。）**

意思是：我**提醒**你不要碰这个东西，但我不会**强制阻止**你。你要非碰，算你自己的事。

Python 用**命名约定**来表达访问控制：

📌 *(板书三行)*
- `name` → 公开的，随便用
- `_name` → "**请勿打扰**"，你可以用但不应该用
- `__name` → "**强烈禁止**"，Python 会做手脚让你很难直接访问

我一个一个讲。

#### 单下划线 `_`：请勿打扰

💻 *写代码*

```python
class Player:
    def __init__(self, name, hp=100):
        self.name = name      # 公开：名字谁都能看
        self._hp = hp          # 内部：HP不应该被随意改
        self._max_hp = 100
    
    def take_damage(self, dmg):
        self._hp = max(0, self._hp - dmg)
        print(f"{self.name} 受伤，HP: {self._hp}/{self._max_hp}")
```

`_hp` 前面加了一个下划线。这是在告诉用你代码的人："嘿，这个属性是**内部逻辑**用的，你不应该从外面直接改它。要改 HP 请走 `take_damage()` 这个正门。"

但注意，技术上你**还是能改**的：

```python
p = Player("勇者")
p._hp = 999999  # 这样写不会报错——但你不应该这么做！
```

单下划线只是个**礼貌提醒**，不是强制。

#### 双下划线 `__`：名称改编

💻 *写代码*

```python
class Secret:
    def __init__(self):
        self.__password = "super_secret_123"
    
    def verify(self, pwd):
        return pwd == self.__password
```

```python
s = Secret()
print(s.verify("super_secret_123"))  # True
# print(s.__password)  # ❌ AttributeError!
```

💻 *运行，展示报错*

这次直接报错了！找不到 `__password`？

但其实 Python 只是偷偷地**改了名字**。它把 `__password` 改成了 `_Secret__password`。

```python
print(s._Secret__password)  # 这样能访问……但千万别这么做
```

这个技术叫 **Name Mangling（名称改编）**。它不是为了"加密安全"，而是为了防止子类**意外覆盖**父类的属性——这个后面学继承的时候你们就理解了。

💬 **所以记住：单下划线是"请勿打扰"标签，双下划线是"改名让你找不到"。但本质上 Python 都没有真正阻止你。**

### @property 装饰器 (10 分钟)

⏰ *00:25 - 00:35*

好，那问题来了。我想要一个**既方便又安全**的访问方式怎么办？

在 Java 里，你得写 `getBalance()` 和 `setBalance()` 方法——又啰嗦又丑。

Python 有个优雅的解决方案——`@property` 装饰器。

💻 *写代码*

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """读取半径"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """设置半径，带验证"""
        if value <= 0:
            raise ValueError("半径必须大于0！")
        self._radius = value
    
    @property
    def area(self):
        """面积：只读属性"""
        return 3.14159 * self._radius ** 2
```

```python
c = Circle(5)
print(c.radius)     # 5   — 像属性一样读取
print(c.area)       # 78.54

c.radius = 10       # 像属性一样赋值——但内部有验证！
# c.radius = -1     # ❌ ValueError!
# c.area = 100      # ❌ 没有setter，不能改！
```

💻 *运行展示*

📌 **精髓: 外面用起来像普通属性，但内部有验证逻辑。**

你看 `c.radius` 读取的时候，其实调用了 getter 方法。`c.radius = 10` 赋值的时候，其实调用了 setter 方法，setter 里面会验证值必须大于 0。

而 `area` 只有 `@property` 没有 `setter`——它就是一个**只读属性**，你不能给它赋值。

这不是"为了好看而好看"，这是真的有用！你可以在 setter 里做任何验证逻辑，防止非法数据进入。

---

## 第二部分：类属性、类方法和静态方法 (30 分钟)

### 类属性 vs 实例属性 (10 分钟)

⏰ *00:35 - 00:45*

到目前为止，我们写的所有属性都是**实例属性**——每个对象独有一份。

但有时候我们需要所有对象**共享**一个数据。比如说：

💬 **所有狗的物种名是什么？**

⏸️

对，"犬科"。这个信息不是旺财自己的，也不是大黄自己的，是**所有狗**共享的。

💻 *写代码*

```python
class Dog:
    # 类属性：写在方法外面，所有对象共享
    species = "犬科"
    dog_count = 0
    
    def __init__(self, name):
        # 实例属性：每个对象独有
        self.name = name
        Dog.dog_count += 1  # 注意是 Dog.dog_count，不是 self

d1 = Dog("旺财")
d2 = Dog("大黄")
d3 = Dog("小白")

print(Dog.dog_count)   # 3
print(Dog.species)     # 犬科
```

📌 *(板书)*
```
Dog 类本身持有：
  species = "犬科"      ← 共享
  dog_count = 3         ← 共享
  
d1 持有: name = "旺财"  ← 独有
d2 持有: name = "大黄"  ← 独有
d3 持有: name = "小白"  ← 独有
```

类属性通过**类名**访问（`Dog.dog_count`），实例属性通过**对象**访问（`d1.name`）。

### 三种方法对比 (20 分钟)

⏰ *00:45 - 01:05*

Python 的类里有**三种**方法，上节课我们只学了一种（实例方法）。今天补全另外两种。

📌 *(板书表格)*

| 类型 | 装饰器 | 第一个参数 | 用途 |
|------|--------|-----------|------|
| 实例方法 | 无 | `self` (对象) | 操作具体某个对象 |
| 类方法 | `@classmethod` | `cls` (类) | 操作类级别的东西 |
| 静态方法 | `@staticmethod` | 无 | 工具函数 |

#### 类方法 `@classmethod`

💻 *写代码*

```python
class Student:
    school = "清华附中"
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        print(f"学校更名为: {cls.school}")
    
    @classmethod
    def from_string(cls, info_str):
        """从字符串创建对象"""
        name, grade = info_str.split("-")
        return cls(name, grade)
```

类方法的第一个参数是 `cls`——代表**类本身**（不是某个具体对象）。

两个常见用法：
1. **修改类属性**（影响所有对象）——比如 `change_school`
2. **替代构造方法**（提供另一种创建对象的方式）——比如 `from_string`

```python
s1 = Student("小明", "高三")
s2 = Student.from_string("小红-高二")  # 另一种创建方式！

Student.change_school("北大附中")  # 所有学生的学校都变了！
```

#### 静态方法 `@staticmethod`

静态方法跟类和对象**都没有关系**。它就是一个普通函数，刚好"住在"类里面。

没有 `self`，也没有 `cls`。

💻 *写代码*

```python
class MathUtils:
    @staticmethod
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

print(MathUtils.is_prime(17))  # True
```

💬 **那它为什么不直接写成普通函数呢？为什么要放在类里面？**

⏸️

因为逻辑上它**属于这个类的范畴**。MathUtils 里放数学工具函数，结构更清晰。就像把工具都放在工具箱里，虽然每个工具单独也能用，但放一起更整齐。

---

## 第三部分：魔术方法大全 (25 分钟)

### 比较运算符 (8 分钟)

⏰ *01:05 - 01:13*

上节课学了 `__init__` 和 `__str__`。今天我们来认识更多魔术方法。

魔术方法让你的对象能使用 Python 的**内置语法**——加减乘除、比较大小、for 循环遍历等等。

💻 *写 Student 类*

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __eq__(self, other):
        """== 比较"""
        return self.score == other.score
    
    def __lt__(self, other):
        """< 比较"""
        return self.score < other.score
    
    def __str__(self):
        return f"{self.name}({self.score}分)"

s1 = Student("小明", 95)
s2 = Student("小红", 88)

print(s1 > s2)  # True!
```

💬 **等等，我只定义了 `__lt__`（小于），为什么 `>` 也能用？**

⏸️

因为 Python 很聪明——你告诉了它 A < B 怎么判断，它就自动推出 B > A。

而且有了比较方法，你就能**排序**了！

```python
students = [s1, s2, Student("小刚", 72)]
students.sort()
for s in students:
    print(s)
```

### 算术运算符 (10 分钟)

⏰ *01:13 - 01:23*

来做个更酷的东西——**二维向量**。

数学课上学过向量吧？(3, 4) 这种？

💻 *写 Vector 类*

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)    
    
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)   # Vector(4, 6) — 看，向量能相加了！
print(v1 * 3)     # Vector(9, 12)
print(abs(v1))    # 5.0 — 勾股定理
```

💻 *运行*

看到了吧？我们**自定义**了加号、减号、乘号的含义！

`v1 + v2` 的时候，Python 在背后调用了 `v1.__add__(v2)`。我们在 `__add__` 里定义了向量加法的规则，所以它自动就会算了。

这就是魔术方法的魅力！你的对象可以像内置类型一样使用各种运算符。

### 容器协议 (7 分钟)

⏰ *01:23 - 01:30*

最后一组魔术方法——让你的对象像列表一样可以遍历、取索引、用 `in` 判断。

💻 *写 Playlist 类*

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []
    
    def add(self, song):
        self._songs.append(song)
    
    def __len__(self):
        return len(self._songs)
    
    def __getitem__(self, index):
        return self._songs[index]
    
    def __contains__(self, song):
        return song in self._songs
```

```python
pl = Playlist("我的最爱")
pl.add("晴天")
pl.add("七里香")
pl.add("稻香")

print(len(pl))       # 3
print(pl[0])          # 晴天
print("晴天" in pl)   # True

for song in pl:
    print(f"♪ {song}")
```

当你实现了 `__getitem__`，`for` 循环就自动可以遍历了！Python 会从索引 0 开始一个一个取，直到 `IndexError`。

📌 **常用魔术方法速查表**（发给学生参考）

---

## 第四部分：总结与练习 (30 分钟)

### 总结 (5 分钟)

⏰ *01:30 - 01:35*

📌 **今天的三大主题：**

1. **封装**: `_`（请勿打扰）和 `__`（名称改编）+ `@property`
2. **三种方法**: 实例方法(self)、类方法(cls)、静态方法(无)
3. **魔术方法**: 让你的对象支持 +、-、==、len()、for 循环等内置操作

这三个加在一起，你的类就从"能用"变成了"好用"。

### 布置练习 (25 分钟)

⏰ *01:35 - 02:00*

打开 `exercises.py`：

- **练习 1**（用户账户）和 **练习 2**（购物车）是**课堂练习**，现在写
- **练习 3**（分数类）和 **练习 4**（日志记录器）是**课后作业**
- **练习 5**（自定义列表）是**挑战题**——需要你把今天学的魔术方法全用上

练习 3 特别有意思，你会实现一个分数类，让 `Fraction(1,2) + Fraction(1,3)` 自动算出 `5/6`。这个练习能帮你彻底理解魔术方法。

💬 **现在开始，有问题举手！**

*（课堂练习时间，教师巡场辅导）*

---

## 下课总结

今天的信息量比较大，但核心思想很简单：**让你的类更规范、更安全、更好用**。

下节课我们会学**继承和多态**——这是 OOP 的另外两大核心特性。学完继承之后，你就可以让一个类"继承"另一个类的所有功能，不用重复写代码。

作业记得写！分数类那个蛮有挑战的，好好想想。下节课见！
