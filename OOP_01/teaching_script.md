# OOP 第1课 教师讲稿：类与对象入门

> **使用说明**: 本讲稿是口语化的教师逐字稿，配合 `lecture_notes.md` 中的代码示例使用。  
> 📌 = 板书/PPT要点 | 💬 = 互动提问 | ⏸️ = 停顿等学生思考 | 💻 = 切换到编辑器现场写代码 | ⏰ = 时间提示

---

## 开场 (2 分钟)

同学们好！前面几节课我们学了变量、判断、循环、函数这些东西，对吧？你们现在已经能写不少程序了——计算器、猜数字、剪刀石头布这些。

但是呢，你们有没有发现一个问题？随着程序越写越长，代码就越来越乱。变量到处飞，函数一大堆，改一个地方可能别的地方就出 bug 了。

今天我们就来学一个**全新的编程思维**——它能帮你把代码组织得清清楚楚、明明白白。

这个思维叫做：**面向对象编程**，英文叫 Object-Oriented Programming，简称 **OOP**。

---

## 第一部分：为什么需要面向对象？ (18 分钟)

### 面向过程 vs 面向对象 (8 分钟)

⏰ *00:02 - 00:10*

我们之前写的所有代码都属于一种编程方式，叫**面向过程**。面向过程是什么意思呢？

📌 **面向过程 = 按步骤做事**

就像你做菜一样：第一步洗菜，第二步切菜，第三步开火，第四步炒菜，第五步装盘。一步一步地来。

这种方式在程序小的时候没问题。但是当程序变大了呢？

我给你们看一个例子。假设我们要管理学生信息：

💻 *打开编辑器，写面向过程版本*

```python
# 面向过程版本
student1 = {"name": "小明", "age": 18, "score": 95}
student2 = {"name": "小红", "age": 17, "score": 88}

def introduce(student):
    print(f"我叫{student['name']}，今年{student['age']}岁")

def study(student, subject):
    print(f"{student['name']}正在学习{subject}")
```

你们看，这里数据是数据，函数是函数，它们是**分开的**。

💬 **这有什么问题呢？谁能想到？**

⏸️ *等 5 秒*

对，问题就是——当你代码一多，比如有 20 个函数、50 个字典，你根本搞不清楚哪个函数配哪个数据。就像你的房间，衣服扔一堆，书扔一堆，充电线扔一堆，你想找个东西找半天。

面向对象就是来**收拾房间**的。

### 万物皆对象 (5 分钟)

⏰ *00:10 - 00:15*

📌 **面向对象 = 把数据和操作打包在一起**

你看看真实世界里的东西：

我拿一辆**汽车**来说。汽车有什么？

💬 **汽车有哪些特征？谁来说说？**

⏸️ *让学生回答*

对！颜色、品牌、速度——这些是它的**属性**，就是"它是什么样的"。

那汽车能干什么呢？加速、刹车、转弯——这些是它的**行为**，就是"它能做什么"。

📌 **属性(数据) + 行为(函数) = 打包在一起 → 这就是对象**

同样的道理：
- 一个**学生**：有名字、年龄、成绩（属性），能学习、考试（行为）
- 一只**猫**：有品种、颜色、体重（属性），能吃饭、睡觉、喵喵叫（行为）

在面向对象编程里，我们把这种"打包"叫做——**类 (Class)**。

### 类 vs 对象 (5 分钟)

⏰ *00:15 - 00:20*

📌 **类 = 模具/图纸 | 对象 = 用模具做出来的产品**

你们吃过月饼吗？做月饼需要什么？一个**模具**！

你用一个模具可以压出很多月饼来，对不对？但模具本身不是月饼，模具是一个**模板**。

在编程里：
- **类 (Class)** 就是模具——它定义了"这种东西长什么样，能做什么"
- **对象 (Object)** 就是用模具做出来的月饼——它是根据模板创建的一个**具体实例**

一个类可以创建**无数个**对象。就像一个模具可以做出无数个月饼。

📌 *(画在白板上)*
```
类: 学生
├── 属性: 姓名, 年龄, 成绩
├── 方法: 学习(), 考试()
│
├── 对象1: 小明, 18岁, 95分
├── 对象2: 小红, 17岁, 88分
└── 对象3: 小刚, 19岁, 72分
```

好，概念讲完了，是不是有点抽象？没关系，咱们直接写代码！代码一写，你就明白了。

---

## 第二部分：定义你的第一个类 (30 分钟)

### 最简单的类 (8 分钟)

⏰ *00:20 - 00:28*

💻 *新建一个 Python 文件*

来，我先写一个最简单的类，你们跟着看：

```python
class Cat:
    pass
```

就这两行，一个类就定义好了！`class` 是关键字，`Cat` 是类名，`pass` 表示里面暂时什么都没有。

📌 **类名用大驼峰命名**：每个单词首字母大写，比如 `Cat`、`BankAccount`、`GameCharacter`

现在我创建一个对象：

```python
my_cat = Cat()
print(my_cat)
print(type(my_cat))
```

💻 *运行，展示输出*

你看，`type` 告诉我们 `my_cat` 的类型是 `Cat`。它就是我们自己创造的一种新类型！

之前我们用的 `int`、`str`、`list` 都是 Python 内置的类。现在我们自己**创造了一种新的类型**！

### `__init__` 构造方法 (10 分钟)

⏰ *00:28 - 00:38*

但是一只没有名字、没有年龄的猫有什么意义呢？我们需要给它加上属性。

这就要用到一个非常重要的东西——`__init__` 方法。

💻 *在编辑器里修改代码*

```python
class Cat:
    def __init__(self, name, breed):
        print(f"一只叫 {name} 的猫诞生了！")
        self.name = name
        self.breed = breed
        self.energy = 100

my_cat = Cat("咪咪", "橘猫")
```

💻 *运行，看到 "一只叫 咪咪 的猫诞生了！"*

你看！我写了 `Cat("咪咪", "橘猫")`，它就自动打印出来了！我并没有手动调用 `__init__`，它是**自动执行**的。

📌 **`__init__` = 构造方法 = 出生仪式**
- 双下划线开头结尾的方法叫**魔术方法** (Magic Method)
- 创建对象时**自动调用**
- 作用：给新出生的对象设置初始属性

💬 **注意看这个名字，是两个下划线 init 两个下划线，不是一个！谁来告诉我一共几个下划线？**

⏸️

对，一共四个。这是新手最容易拼错的地方，写成一个下划线 `_init_` 或者写成 `__int__`，程序不会报错但也不会工作，特别坑！

### `self` 到底是什么 (12 分钟)

⏰ *00:38 - 00:50*

你们肯定注意到了这个 `self`。

💬 **谁能猜猜 self 是什么意思？**

⏸️ *让学生猜*

`self` 就是**自己**。

你想一下，你在写自我介绍的时候会说"**我**叫小明，**我**今年18岁"。对于 Python 的类来说，这个"我"就是 `self`。

当你写 `self.name = name` 的意思是：**把这个名字存到"我自己"身上**。

我来证明给你看：

💻 *写代码演示*

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name}: 汪汪汪！")

dog1 = Dog("旺财")
dog2 = Dog("大黄")

dog1.bark()  # self = dog1
dog2.bark()  # self = dog2
```

💻 *运行*

你看，`dog1.bark()` 的时候，Python 自动把 `dog1` 这个对象传给了 `self`。所以 `self.name` 就是 `dog1` 的 `name`，也就是"旺财"。

`dog2.bark()` 的时候呢？`self` 就变成了 `dog2`，所以打印"大黄"。

📌 **self = 谁调用这个方法，self 就是谁**

两个重要的注意事项：
1. `self` 是约定俗成的名字，你写 `this` 也行，但**千万别这么干**，所有 Python 程序员都用 `self`
2. 调用方法时**不用传 self**，Python 帮你自动传

💬 **到这里有没有问题？**

⏸️ *等一等，确认学生跟上了*

好，接下来我们给类加更多功能。

---

## 第三部分：给对象添加行为——实例方法 (30 分钟)

### 银行账户实战 (15 分钟)

⏰ *00:50 - 01:05*

概念讲够了，我们来做一个有意思的东西——**银行账户**。

💬 **银行账户有什么属性？能做什么操作？大家来说说**

⏸️ *让学生说，把答案记下来*

很好！属性有：户主名字、余额。操作有：存钱、取钱、查余额。

💻 *开始现场写代码，边写边讲解*

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
```

注意这里 `balance=0` 是默认参数，如果不传的话默认是 0。

```python
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"存入 {amount} 元，余额: {self.balance} 元")
        else:
            print("存款金额必须大于0")
```

存钱的时候我们要**验证**——不能存负数对吧？这就是封装的雏形，我们在方法内部做保护。

```python
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"余额不足！当前余额: {self.balance} 元")
        elif amount <= 0:
            print("取款金额必须大于0")
        else:
            self.balance -= amount
            print(f"取出 {amount} 元，余额: {self.balance} 元")
    
    def show_balance(self):
        print(f"{self.owner}的账户余额: {self.balance} 元")
```

来，测试一下：

```python
acc = BankAccount("小明", 1000)
acc.show_balance()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)  # 余额不足！
```

💻 *运行代码，展示结果*

看到了吗？数据（余额）和操作（存取钱）**住在同一个房子里**了。你不需要把 `balance` 传来传去，对象自己知道自己的余额。

### `__str__` 让 print 更好看 (5 分钟)

⏰ *01:05 - 01:10*

现在如果我直接 `print(acc)`，你们猜会输出什么？

💻 *演示*

```python
print(acc)
# 输出: <__main__.BankAccount object at 0x7f...>
```

这是什么鬼？一堆看不懂的内存地址！

我们可以定义 `__str__` 方法来告诉 Python：当有人 `print` 我的时候，应该显示什么。

```python
def __str__(self):
    return f"账户({self.owner}): 余额{self.balance}元"
```

再 `print(acc)` 试试？

💻 *演示*

漂亮多了！这就是魔术方法的威力。

### 方法之间互相调用 (10 分钟)

⏰ *01:10 - 01:20*

方法内部可以用 `self.其他方法()` 来调用自己的其他方法。

💻 *写 Player 类*

```python
class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.is_alive = True
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} 受到 {damage} 伤害, HP: {self.hp}")
        self._check_alive()   # 调用自己的另一个方法
    
    def _check_alive(self):
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.name} 已阵亡！")
```

注意 `_check_alive` 前面有个**单下划线**。这是 Python 程序员的约定，表示"这个方法是内部使用的，外面别直接调"。就像餐厅厨房的门上写着"仅限员工"一样。

你不需要从外面去调 `player._check_alive()`，在受伤的时候它内部自己会调。

💻 *测试*

```python
hero = Player("勇者")
hero.take_damage(30)
hero.take_damage(100)
```

---

## 第四部分：对象之间的交互 (20 分钟)

### 对象作为属性 (10 分钟)

⏰ *01:20 - 01:30*

一个对象可以是另一个对象的属性！

💬 **比如一辆汽车，它"有"一个引擎。引擎也可以是一个对象。这种关系叫什么？**

⏸️

这叫**组合**——一个东西里面包含另一个东西。

💻 *写代码*

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def start(self):
        print(f"引擎启动！{self.horsepower}马力！")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # engine 是另一个对象！
    def start(self):
        print(f"{self.brand} 准备出发...")
        self.engine.start()   # 调用 engine 对象的方法

v8 = Engine(450)
my_car = Car("特斯拉", v8)
my_car.start()
```

💻 *运行*

你看，`Car` 对象里面有个 `Engine` 对象。启动汽车的时候，汽车会让引擎去启动。对象和对象之间可以**协作**。

### 对象放在列表里 (10 分钟)

⏰ *01:30 - 01:40*

对象也可以放在列表、字典这些容器里面。这个很实用！

💻 *演示*

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name}: {self.score}分"

classroom = [
    Student("小明", 95),
    Student("小红", 88),
    Student("小刚", 72),
]

# 找最高分
best = max(classroom, key=lambda s: s.score)
print(f"最高分: {best}")

# 排序
classroom.sort(key=lambda s: s.score, reverse=True)
for i, s in enumerate(classroom, 1):
    print(f"第{i}名: {s}")
```

💻 *运行*

是不是很方便？你可以把一整个班的学生放在列表里，然后排序、搜索、统计，各种操作。

---

## 第五部分：总结与练习 (20 分钟)

### 总结 (5 分钟)

⏰ *01:40 - 01:45*

📌 **今天学到的核心概念**：

| 概念 | 一句话解释 |
|------|-----------|
| `class` | 定义模板（模具） |
| `对象 = 类名()` | 用模具做产品 |
| `__init__` | 出生仪式，创建时自动调用 |
| `self` | "我自己"，谁调用就是谁 |
| `self.xxx` | 把数据绑到自己身上 |
| 实例方法 | 对象能做的事情 |
| `__str__` | 告诉 print 怎么显示我 |

### 常见错误提醒 (5 分钟)

⏰ *01:45 - 01:50*

在你们去写练习之前，我先提醒几个**必踩的坑**：

💻 *快速展示每个错误*

1. **忘记 `self.`**：写了 `name = name` 而不是 `self.name = name`——数据没绑上去！
2. **方法忘写 `self` 参数**：`def greet():` 少了 `self`——调用时报错！
3. **`__init__` 拼错**：写成 `_init_`（一个下划线）或 `__int__`——不报错但不工作，最坑！
4. **在类外面用 `self`**：`self` 只能在类的方法里用！

### 布置练习 (10 分钟)

⏰ *01:50 - 02:00*

好，打开 `exercises.py`，今天的练习一共 5 道题：

- **练习 1 和 2**（宠物猫、银行账户）是**课堂练习**，现在就动手写
- **练习 3 和 4**（学生成绩、骰子游戏）是**课后作业**
- **练习 5**（通讯录）是**挑战题**，学有余力的同学尝试

💬 **现在开始写练习1，有问题随时举手！我来巡场。**

*（课堂练习时间，教师巡场辅导）*

---

## 下课总结

同学们，今天我们迈出了面向对象的第一步。记住核心公式：

> **类 = 属性 + 方法 = 数据 + 操作**

下节课我们会学**封装**——怎么保护你的数据不被胡乱修改，还有一些高级的方法类型和更多的魔术方法。

课后把练习 3 和练习 4 完成了哈！下节课开始前我会抽查。再见！
