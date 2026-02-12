# OOP 第3课 教师讲稿：继承与多态

> **使用说明**: 本讲稿是口语化的教师逐字稿，配合 `lecture_notes.md` 中的代码示例使用。  
> 📌 = 板书/PPT要点 | 💬 = 互动提问 | ⏸️ = 停顿等学生思考 | 💻 = 切换到编辑器现场写代码 | ⏰ = 时间提示

---

## 课前复习 (5 分钟)

⏰ *00:00 - 00:05*

好，上课！先来复习一下上节课。

💬 **谁来说说，封装是什么意思？用大白话说。**

⏸️ *点一个学生*

对！把数据藏起来，只允许通过方法来操作。就像 ATM 机——你用按钮取钱，而不是直接去金库拿。

💬 **`_name` 和 `__name` 的区别是什么？**

⏸️

单下划线是"请勿打扰"的标签，大家约定不要从外面直接碰它，但技术上还是可以碰。双下划线是"名称改编"，Python 会偷偷改名字，让你很难直接访问。

💬 **`@property` 是干什么的？**

⏸️

让方法看起来像属性一样使用！读取时自动调 getter，赋值时自动调 setter，setter 里面可以放验证逻辑。

好，复习完毕。今天我们进入 OOP 的**第三大武器**——**继承**，以及一个非常重要的概念——**多态**。

这是今天内容最精彩的一节课。

---

## 第一部分：继承——代码复用的艺术 (30 分钟)

### 什么是继承？ (10 分钟)

⏰ *00:05 - 00:15*

💬 **我问大家一个问题：你长得像你爸妈吗？**

⏸️ *笑一下*

不管你愿不愿意承认，你确实"继承"了父母的一些特征——比如肤色、身高、甚至说话的方式。但你也有自己**独特**的特征，对吧？你可以学吉他、打篮球，这些是你爸妈不一定会的。

编程里的继承也是一样的道理：

📌 **继承 = 子类自动获得父类的所有功能，还可以添加自己的功能**

我画个图给大家看：

📌 *(白板画继承关系图)*
```
        Animal（父类/基类）
        ├── name, age       ← 属性
        ├── eat(), sleep()  ← 方法
        │
        ├── Dog（子类）
        │   ├── 自动拥有: name, age, eat(), sleep()
        │   └── 新增: breed, bark()
        │
        └── Cat（子类）
            ├── 自动拥有: name, age, eat(), sleep()
            └── 新增: indoor, purr()
```

狗和猫都是动物，所以它们都能吃、能睡。但狗会汪汪叫，猫会呼噜——这是各自特有的。

我们不需要在 Dog 和 Cat 里面**重复写** eat 和 sleep 的代码！只要**继承** Animal，这些方法自动就有了。

### 代码实战 (12 分钟)

⏰ *00:15 - 00:27*

💻 *打开编辑器，边写边讲*

先写父类：

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self, food):
        print(f"{self.name} 正在吃 {food}")
    
    def sleep(self):
        print(f"{self.name} 正在睡觉 💤")
```

到目前为止都是之前学过的东西，没什么新的。

现在写子类——注意看语法：

```python
class Dog(Animal):     # 括号里写父类的名字！
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 让父类去处理 name 和 age
        self.breed = breed           # Dog 自己多了一个 breed
    
    def bark(self):                  # Dog 特有的方法
        print(f"{self.name}: 汪汪汪！🐕")
```

来测试一下：

```python
dog = Dog("旺财", 3, "金毛")
dog.eat("骨头")     # 这个方法是从 Animal 继承来的！
dog.bark()          # 这个是 Dog 自己的
print(dog.name)     # name 也是继承来的
```

💻 *运行*

看到了吗？`eat()` 方法我在 Dog 里面**一行代码都没写**，但 Dog 的对象可以直接调用它。因为它从 Animal **继承**过来了。

这就是继承的威力——**代码不用重复写**。

### `super()` 详解 (8 分钟)

⏰ *00:27 - 00:35*

大家注意到 `__init__` 里面有一行：

```python
super().__init__(name, age)
```

💬 **`super()` 是什么意思？谁能猜?**

⏸️

`super()` 就是"**父类**"的意思！准确说，它返回父类的一个代理对象。

`super().__init__(name, age)` 的意思是：**先让父类做它该做的初始化**（设置 name 和 age），然后我再做我自己多出来的初始化（设置 breed）。

你想想啊，Animal 的 `__init__` 会设置 `self.name` 和 `self.age`。如果你在 Dog 的 `__init__` 里不调 `super()`，那 name 和 age 就没设上，后面 `dog.name` 就报错了。

📌 **super() 的规则：先让父类做它的事，再做自己的事**

💬 **那能不能不写 super()，直接写 `Animal.__init__(self, name, age)` 呢？**

⏸️

技术上可以，但**不推荐**。如果以后继承结构变复杂了，直接写父类名字会出问题。`super()` 是 Python 推荐的方式，后面学多继承的时候你就知道为什么了。

来验证一下继承关系：

```python
print(isinstance(dog, Dog))     # True — 旺财是 Dog
print(isinstance(dog, Animal))  # True — 旺财也是 Animal！
```

一条狗既是"Dog"也是"Animal"，就像你既是"学生"也是"人"。

---

## 第二部分：方法重写 Override (25 分钟)

### 什么是方法重写？ (8 分钟)

⏰ *00:35 - 00:43*

继承的时候，子类可以**重新定义**父类已有的方法，让它有不同的行为。这个叫**方法重写 (Override)**。

💬 **我问大家，如果 Animal 有一个 `speak` 方法，打印"动物发出声音"，但是你希望 Dog 打印"汪汪汪"，Cat 打印"喵喵喵"，怎么办？**

⏸️

对！在子类里**重新写**一个同名方法就行了！

💻 *写代码*

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} 发出了声音")

class Dog(Animal):
    def speak(self):    # 同名方法 → 重写！
        print(f"{self.name}: 汪汪汪！🐕")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 喵喵喵！🐱")
```

```python
a = Animal("动物")
d = Dog("旺财")
c = Cat("咪咪")

a.speak()  # 动物 发出了声音     ← 父类版本
d.speak()  # 旺财: 汪汪汪！🐕   ← Dog 重写版本
c.speak()  # 咪咪: 喵喵喵！🐱   ← Cat 重写版本
```

💻 *运行*

同一个方法名 `speak`，不同的对象调用出来**效果不一样**！Dog 汪汪叫，Cat 喵喵叫。

Python 怎么知道用哪个版本呢？它的查找顺序是：**先在子类找 → 没找到再去父类找 → 再没有就去父类的父类找**。Dog 里有 `speak`，找到了，就用 Dog 的版本。

### 用 super() 扩展方法 (10 分钟)

⏰ *00:43 - 00:53*

有时候你不想**完全替换**父类的方法，而是想在父类的基础上**添加功能**。

比如经理也是员工。Employee 的 `work` 方法打印"正在工作"。Manager 的 `work` 除了"正在工作"之外，还要加上"正在管理部门"。

💻 *写代码*

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} 正在工作")
    
    def get_info(self):
        return f"姓名: {self.name}, 工资: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def work(self):
        super().work()          # 先执行父类的 work（"正在工作"）
        print(f"  正在管理 {self.department} 部门")  # 再加自己的
    
    def get_info(self):
        base = super().get_info()    # 先拿到父类的信息
        return f"{base}, 部门: {self.department}"  # 再拼上自己的
```

```python
e = Employee("小红", 8000)
m = Manager("张总", 20000, "技术部")

e.work()
# 小红 正在工作

m.work()
# 张总 正在工作            ← 来自 super().work()
#   正在管理 技术部 部门     ← Manager 自己加的
```

💻 *运行*

📌 **注意区别：**
- **完全重写**: 子类方法里不调 super()，完全替换父类逻辑
- **扩展重写**: 子类方法里先调 super()，保留父类逻辑，再加自己的

实际项目中，**扩展重写**更常见。因为你通常希望保留父类已有的功能，只是在上面锦上添花。

### MRO 方法解析顺序 (7 分钟)

⏰ *00:53 - 01:00*

再多说一个概念。Python 查找方法的顺序有个专业名词，叫 **MRO (Method Resolution Order)**。

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(B):
    pass  # C 没有 greet

c = C()
c.greet()  # Hello from B
```

💬 **为什么不是 "Hello from A"?**

⏸️

因为查找顺序是 C → B → A。C 里没有 greet，于是往上找 B，B 里有！就用 B 的了，不会再去找 A 的。

你可以用 `C.__mro__` 看到完整的查找链：

```python
print(C.__mro__)
# (C, B, A, object)
```

最后面的 `object` 是 Python 所有类的**终极祖先**。每个类最终都继承自 `object`。

这个现在知道就行，后面遇到复杂继承关系的时候它会帮到你。

---

## 第三部分：多态 (25 分钟)

### 什么是多态 (8 分钟)

⏰ *01:00 - 01:08*

好，接下来是今天最精华的概念——**多态 (Polymorphism)**。

这个词听起来很吓人，但其实无比简单。

📌 **多态 = 同一个方法名，在不同对象上有不同的表现**

前面那个例子已经就是多态了！Dog 的 `speak` 汪汪叫，Cat 的 `speak` 喵喵叫——都叫 `speak`，但行为不同。

多态的威力在哪呢？看这个：

💻 *写代码*

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r ** 2

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h
```

现在看这个代码：

```python
shapes = [Rectangle(10, 5), Circle(7), Triangle(8, 6)]

for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area():.2f}")

total = sum(s.area() for s in shapes)
print(f"总面积: {total:.2f}")
```

💻 *运行*

💬 **注意看那个 for 循环。我调用 `shape.area()` 的时候，我需要知道它具体是 Rectangle、Circle 还是 Triangle 吗？**

⏸️

**不需要！** 我只知道它是个 Shape，它有 `area()` 方法就够了。至于具体怎么算面积，交给每个子类自己去实现。

📌 **这就是多态的精髓：写代码时不关心具体类型，只关心"能做什么"**

以后你加了一个五边形、六边形，**for 循环那段代码完全不用改**！你只需要新写一个子类、实现 `area()` 方法就行了。这叫"**对扩展开放，对修改关闭**"。

### 鸭子类型 (10 分钟)

⏰ *01:08 - 01:18*

Python 的多态还有一个独特的特点，它比 Java 更灵活，叫做**鸭子类型 (Duck Typing)**。

有一句著名的话：

📌 **"如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子。"**

什么意思呢？Python 不在乎你**是什么类型**，只在乎你**能做什么**。

💻 *写代码*

```python
class Duck:
    def quack(self):
        print("嘎嘎嘎！")

class Person:
    def quack(self):
        print("我在模仿鸭子：嘎嘎嘎！")

class RubberDuck:
    def quack(self):
        print("吱吱吱！（塑料鸭叫声）")

def make_it_quack(thing):
    thing.quack()   # 不管你是什么，只要你能 quack 就行

for obj in [Duck(), Person(), RubberDuck()]:
    make_it_quack(obj)
```

💻 *运行*

Person 和 RubberDuck 跟 Duck **完全没有继承关系**！它们不是 Duck 的子类，也没有共同的父类。

但是它们都有 `quack()` 方法，所以都能传给 `make_it_quack` 函数使用。

**Python 不看你的"身份证"（类型），只看你的"能力"（方法）。**

这跟 Java 很不一样。Java 的话你必须让 Person 和 RubberDuck 都实现一个 Quackable 接口才行。Python 说：你有这个方法？行，那你就能用。

💬 **其实你一直在用多态，只是没意识到。**

```python
# len() 对字符串、列表、字典的行为不同——这就是多态
len("Hello")       # 5
len([1, 2, 3])     # 3
len({"a": 1})      # 1

# + 对不同类型的行为不同——这也是多态
1 + 2              # 3
"ab" + "cd"        # "abcd"
[1, 2] + [3, 4]    # [1, 2, 3, 4]
```

所以多态不是什么高深的东西，你**一直在享受它**。

### 多态的好处总结 (7 分钟)

⏰ *01:18 - 01:25*

📌 **多态的三大好处：**

1. **代码更灵活**: 函数不需要知道具体类型，能接受所有"满足条件"的对象
2. **扩展不改旧代码**: 新加子类不影响已有的代码
3. **统一接口**: 不管底层实现多复杂，外面看到的是统一的方法名

以后你做大项目的时候，多态会帮你省无数行代码。

---

## 第四部分：抽象类 (20 分钟)

### 问题引入 (5 分钟)

⏰ *01:25 - 01:30*

我们回到形状的例子。如果有个粗心的程序员这样写：

```python
class Hexagon(Shape):
    def __init__(self, side):
        self.side = side
    # 忘记实现 area() 了！

h = Hexagon(5)
print(h.area())  # 0 ← 返回了父类的默认值，不报错！
```

💬 **这有什么问题？**

⏸️

程序悄悄地返回了 0，没有任何报错。但这个答案是**错的**！六边形的面积怎么可能是 0 呢？

这种 bug 非常隐蔽——程序跑得好好的，结果是错的，你还以为一切正常。

我们需要一种方法来**强制**子类必须实现某些方法。如果忘了实现，就**直接报错**。

### 抽象类 ABC (15 分钟)

⏰ *01:30 - 01:45*

Python 用 `abc` 模块来解决这个问题。ABC = Abstract Base Class，抽象基类。

💻 *写代码*

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
        """普通方法：子类可以直接用"""
        return f"{self.__class__.__name__}: 面积={self.area():.2f}"
```

注意两个变化：
1. `Shape(ABC)` —— 继承自 ABC
2. `@abstractmethod` —— 标记"这个方法子类**必须**实现"

现在试试：

```python
# s = Shape()  # ❌ TypeError: 不能实例化抽象类！
```

💻 *运行，展示报错*

看到了吗？你不能创建 Shape 的对象了！因为它是抽象的——模具不完整，你没法用它做产品。

你必须先实现所有抽象方法，才能创建对象：

```python
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)

# 如果漏了其中一个方法呢？
class BadShape(Shape):
    def area(self):
        return 0
    # 忘了 perimeter!

# b = BadShape()  # ❌ TypeError!
```

💻 *运行展示*

漏了 `perimeter` 就报错！Python 不会让你"蒙混过关"了。

📌 **抽象类的作用 = 定义规范/契约**：告诉所有子类"你必须实现这些方法，否则你就不是一个合格的 Shape"。

这在大项目里特别有用。比如你团队有 10 个人，每人写一种图形。有了抽象类，谁忘了实现 `area()`，代码直接报错，不会等到上线才发现问题。

但注意，`describe()` 没有 `@abstractmethod`，它是一个**普通方法**——子类可以直接用，也可以重写，但不是必须的。

---

## 第五部分：继承 vs 组合 + 总结 (15 分钟)

### 继承 vs 组合 (10 分钟)

⏰ *01:45 - 01:55*

最后一个重要的话题。

💬 **你们说，引擎是一种汽车吗？**

⏸️

当然不是！引擎**不是**汽车。但是汽车**有**引擎。

这两种关系在 OOP 里叫：

📌 **is-a (是一个) → 用继承**
📌 **has-a (有一个) → 用组合**

- Dog **is-a** Animal（狗**是**动物）→ `class Dog(Animal)` ✅
- Car **has-a** Engine（汽车**有**引擎）→ `self.engine = Engine()` ✅
- Car **is-a** Engine？→ `class Car(Engine)` ❌ 不对！

💻 *快速展示*

```python
# ❌ 错误的继承（汽车不是引擎）
class Car(Engine):
    pass

# ✅ 正确的组合（汽车有引擎）
class Car:
    def __init__(self):
        self.engine = Engine()  # 组合
```

📌 **经验法则：能用组合就用组合，只有真正的 is-a 关系才用继承。**

为什么？因为继承耦合太紧了——子类和父类绑在一起，父类一改，子类可能全崩。组合更灵活——换个引擎就行，不影响汽车的其他部分。

### 课程总结 (5 分钟)

⏰ *01:55 - 02:00*

📌 **今天学到的知识：**

```
继承：class 子类(父类) + super()
   └── 子类自动拥有父类的一切

方法重写：子类重新定义父类的方法
   ├── 完全替换
   └── super() 扩展

多态：同一方法名，不同表现
   ├── 基于继承的多态
   └── 鸭子类型（不需要继承！）

抽象类：ABC + @abstractmethod
   └── 强制子类实现某些方法

设计原则：
   ├── is-a → 继承
   └── has-a → 组合（优先使用）
```

好，作业时间！打开 `exercises.py`：

- **练习 1**（动物王国）和 **练习 2**（薪资系统）是**课堂练习**
- **练习 3**（图形计算器）和 **练习 4**（交通工具模拟器）是**课后作业**
- **练习 5**（RPG战斗系统）是**挑战题**——这个相当有意思，你会做一个回合制战斗的游戏

下节课是我们 OOP 系列的**最后一课**——综合实战！我们会把前三课学的所有东西串在一起，做一个完整的项目。而且还会学几个常用的**设计模式**——就是前人总结出来的最佳实践写法。

作业记得写！下节课见！
