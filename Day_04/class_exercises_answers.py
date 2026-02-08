# Day 4 随堂练习 - 参考答案与详细解析
# 本文件与 class_exercises.py 一一对应

# ===========================================================
# 随堂练习 1：定义第一个类
# 对应讲义 1.6 节
# ===========================================================

print("=" * 50)
print("随堂练习 1：定义第一个类")
print("=" * 50)

# 练习 1.1: Cat 类
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def meow(self):
        print(f"{self.name}说：喵~")
    
    def info(self):
        print(f"我是{self.name}，{self.color}的猫")

# 创建对象并调用方法
cat1 = Cat("咪咪", "白色")
cat2 = Cat("橘子", "橘色")

cat1.meow()
cat2.meow()
cat1.info()
cat2.info()

# 【解析】
# - class 关键字定义类，类名首字母大写（大驼峰）
# - __init__ 是构造方法，创建对象时自动调用
# - self 指代当前对象本身，必须是每个方法的第一个参数
# - self.name = name 把传入的参数保存为对象的属性


# ===========================================================
# 随堂练习 2：属性与方法
# 对应讲义 2.4 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 2：计数器类")
print("=" * 50)

# 练习 2.1: Counter 类
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1
    
    def reset(self):
        self.count = 0
    
    def get_count(self):
        return self.count

# 测试
c = Counter()
c.increment()
c.increment()
c.increment()
c.decrement()
print(f"当前计数: {c.get_count()}")  # 2
c.reset()
print(f"重置后: {c.get_count()}")    # 0

# 【解析】
# - 方法可以修改对象的属性（self.count += 1）
# - 方法可以返回值（return self.count）
# - 调用方法时不需要传 self，Python 自动处理


# ===========================================================
# 随堂练习 3：封装
# 对应讲义 3.4 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 3：封装 - 学生成绩")
print("=" * 50)

# 练习 3.1: Student 类（带封装）
class Student:
    def __init__(self, name, score):
        self.__name = name
        # 初始化时也要检查合法性
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("初始成绩必须在0-100之间，已设为0")
            self.__score = 0
    
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("成绩必须在0-100之间")
    
    def get_grade(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >= 80:
            return "B"
        elif self.__score >= 70:
            return "C"
        elif self.__score >= 60:
            return "D"
        else:
            return "F"

# 测试
s = Student("小明", 85)
print(f"{s.get_name()} 的成绩是 {s.get_score()}，等级 {s.get_grade()}")
s.set_score(95)
print(f"修改后成绩: {s.get_score()}，等级 {s.get_grade()}")
s.set_score(150)  # 应该提示错误

# 【解析】
# - __name 和 __score 是私有属性，外部无法直接访问
# - 通过 get_xxx() 和 set_xxx() 方法来访问和修改
# - set_score() 中可以加入验证逻辑，保护数据合法性
# - 这就是封装的核心思想：数据保护 + 接口控制


# ===========================================================
# 随堂练习 4：继承
# 对应讲义 4.4 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 4：继承 - 交通工具")
print("=" * 50)

# 基类 Vehicle
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0
    
    def start(self):
        print(f"{self.brand} 启动")
    
    def stop(self):
        self.speed = 0
        print(f"{self.brand} 停止")
    
    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} 加速，当前速度: {self.speed}")

# 子类 Car
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.wheels = 4
    
    def start(self):  # 重写父类方法
        print(f"{self.brand} 汽车启动，轰隆隆~")

# 子类 Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.wheels = 2
    
    def start(self):  # 重写父类方法
        print(f"{self.brand} 摩托车启动，突突突~")

# 测试
car = Car("宝马")
moto = Motorcycle("哈雷")
car.start()
moto.start()
car.accelerate(60)
moto.accelerate(40)
print(f"{car.brand} 有 {car.wheels} 个轮子")
print(f"{moto.brand} 有 {moto.wheels} 个轮子")

# 【解析】
# - class Car(Vehicle): 表示 Car 继承自 Vehicle
# - super().__init__(brand) 调用父类的构造方法
# - 子类可以添加新属性（self.wheels）
# - 子类可以重写（override）父类的方法
# - 子类自动拥有父类的所有方法（如 accelerate, stop）


# ===========================================================
# 随堂练习 5：多态
# 对应讲义 5.4 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 5：多态 - 员工薪资")
print("=" * 50)

# 基类 Employee
class Employee:
    def __init__(self, name):
        self.name = name
    
    def get_salary(self):
        return 0

# 子类 FullTimeEmployee
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    
    def get_salary(self):
        return self.monthly_salary

# 子类 PartTimeEmployee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours
    
    def get_salary(self):
        return self.hourly_rate * self.hours

# 多态函数：处理不同类型的员工
def total_salary(employees):
    total = 0
    for emp in employees:
        salary = emp.get_salary()  # 多态：同样的方法调用，不同的行为
        print(f"  {emp.name}: ¥{salary}")
        total += salary
    return total

# 测试
employees = [
    FullTimeEmployee("张三", 8000),
    FullTimeEmployee("李四", 10000),
    PartTimeEmployee("王五", 50, 80),  # 时薪50，工作80小时
]

print("各员工薪资:")
total = total_salary(employees)
print(f"总薪资: ¥{total}")

# 【解析】
# - 多态 = 同一方法名，在不同对象上有不同行为
# - total_salary 函数不关心员工是全职还是兼职
# - 只要员工有 get_salary() 方法，就能正常工作
# - 这让代码更灵活，新增员工类型时不需要修改计算逻辑


# ===========================================================
# 随堂练习 6：特殊方法
# 对应讲义 6.5 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 6：特殊方法 - 图书类")
print("=" * 50)

# Book 类
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"《{self.title}》 - {self.author} - ¥{self.price}"
    
    def __eq__(self, other):
        # 书名和作者都相同时返回 True
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        # 按价格比较
        return self.price < other.price

# 测试
b1 = Book("Python入门", "张三", 59)
b2 = Book("Python进阶", "李四", 79)
b3 = Book("Python入门", "张三", 59)

print(b1)
print(b2)
print(f"b1 == b3? {b1 == b3}")  # True (同书名同作者)
print(f"b1 == b2? {b1 == b2}")  # False

# 按价格排序
books = [b2, b1]
books_sorted = sorted(books)
print("按价格排序:")
for book in books_sorted:
    print(f"  {book}")

# 【解析】
# - __str__ 定义 print(obj) 时的输出格式
# - __eq__ 定义 obj1 == obj2 的比较逻辑
# - __lt__ 定义 obj1 < obj2 的比较逻辑，用于排序
# - 这些特殊方法让自定义类能与 Python 内置功能（print, ==, sorted）协作


# ===========================================================
# 挑战练习：迷你银行系统
# ===========================================================

print("\n" + "=" * 50)
print("挑战练习：迷你银行系统")
print("=" * 50)

class Account:
    """银行账户基类"""
    _next_id = 1001  # 类变量：自动生成账号
    
    def __init__(self, owner, initial_balance=0):
        self.account_id = Account._next_id
        Account._next_id += 1
        self.owner = owner
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存款成功: +¥{amount}，余额: ¥{self.__balance}")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("取款金额必须大于0")
        elif amount > self.__balance:
            print(f"余额不足！当前余额: ¥{self.__balance}")
        else:
            self.__balance -= amount
            print(f"取款成功: -¥{amount}，余额: ¥{self.__balance}")
    
    def get_balance(self):
        return self.__balance
    
    def transfer(self, target_account, amount):
        if amount <= 0:
            print("转账金额必须大于0")
        elif amount > self.__balance:
            print(f"余额不足！当前余额: ¥{self.__balance}")
        else:
            self.__balance -= amount
            target_account.deposit(amount)
            print(f"转账成功: {self.owner} → {target_account.owner} ¥{amount}")
    
    def __str__(self):
        return f"账户{self.account_id} ({self.owner}): ¥{self.__balance}"


class SavingsAccount(Account):
    """储蓄账户：有利息"""
    def __init__(self, owner, initial_balance=0, interest_rate=0.03):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        balance = self.get_balance()
        interest = balance * self.interest_rate
        self.deposit(interest)
        print(f"利息已到账: +¥{interest:.2f} (利率: {self.interest_rate*100}%)")


class Bank:
    """银行类"""
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def create_account(self, owner, initial_deposit=0, account_type="normal"):
        if account_type == "savings":
            acc = SavingsAccount(owner, initial_deposit)
        else:
            acc = Account(owner, initial_deposit)
        self.accounts.append(acc)
        print(f"账户创建成功: {acc}")
        return acc
    
    def find_account(self, account_id):
        for acc in self.accounts:
            if acc.account_id == account_id:
                return acc
        return None
    
    def total_deposits(self):
        return sum(acc.get_balance() for acc in self.accounts)
    
    def show_all_accounts(self):
        print(f"\n{self.name} 所有账户:")
        print("-" * 40)
        for acc in self.accounts:
            print(f"  {acc}")
        print(f"  {'─'*30}")
        print(f"  银行总存款: ¥{self.total_deposits()}")


# 测试
print("\n--- 银行系统测试 ---")
bank = Bank("Python银行")

# 创建账户
acc1 = bank.create_account("张三", 1000)
acc2 = bank.create_account("李四", 2000)
acc3 = bank.create_account("王五", 5000, "savings")  # 储蓄账户

print()
# 操作
acc1.deposit(500)
acc1.transfer(acc2, 300)

print()
# 储蓄账户加息
if isinstance(acc3, SavingsAccount):
    acc3.add_interest()

# 显示所有账户
bank.show_all_accounts()

# 【解析】
# - Account 类使用私有属性 __balance 保护余额
# - 类变量 _next_id 用于自动生成账号
# - SavingsAccount 继承 Account，添加利息功能
# - Bank 类使用组合关系，管理多个 Account
# - 这个例子综合运用了：封装、继承、方法重写、类属性等知识点


print("\n" + "=" * 50)
print("所有练习答案演示完毕！")
print("=" * 50)
