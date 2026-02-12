# ===================================================================
# OOP 第2课：封装与进阶特性 —— 参考答案
# ===================================================================
from datetime import datetime


# ===================================================================
# 练习 1: 安全的用户账户
# ===================================================================
print("=== 练习 1: 安全的用户账户 ===")

class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email          # 会触发 setter 验证
        self.__password = None
        self.password = password    # 会触发 setter 验证

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("邮箱格式无效，必须包含 '@'")
        self._email = value

    # password 只有 setter, 没有 getter (无法读取密码)
    @property
    def password(self):
        raise AttributeError("密码不可读取！")

    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("密码长度至少6位！")
        self.__password = value
        print(f"[{self.username}] 密码已更新")

    def verify_password(self, pwd):
        return pwd == self.__password

    def __str__(self):
        return f"用户: {self.username} (邮箱: {self._email})"


user = UserAccount("小明", "xiaoming@email.com", "abc123")
print(user)                                # 用户: 小明 (邮箱: xiaoming@email.com)
print(f"密码验证: {user.verify_password('abc123')}")   # True
print(f"密码验证: {user.verify_password('wrong')}")    # False

user.email = "new_email@test.com"          # 更新邮箱
print(user)

# user.email = "invalid_email"            # ❌ ValueError: 邮箱格式无效
# print(user.password)                    # ❌ AttributeError: 密码不可读取
# user.password = "12"                    # ❌ ValueError: 密码长度至少6位


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 2: 商品与购物车
# ===================================================================
print("=== 练习 2: 商品与购物车 ===")

class Product:
    discount_rate = 1.0  # 类属性：全场折扣率

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def final_price(self):
        return round(self.price * Product.discount_rate, 2)

    @classmethod
    def set_discount(cls, rate):
        if 0 < rate <= 1.0:
            cls.discount_rate = rate
            print(f"全场折扣已设为: {rate * 10:.1f}折")
        else:
            print("折扣率必须在 0 到 1 之间")

    @staticmethod
    def format_price(price):
        return f"¥{price:.2f}"

    def __str__(self):
        if Product.discount_rate < 1.0:
            return (f"{self.name} - {Product.format_price(self.price)} "
                    f"(折后: {Product.format_price(self.final_price)})")
        return f"{self.name} - {Product.format_price(self.price)}"


class ShoppingCart:
    def __init__(self):
        self.items = []  # [(Product, quantity), ...]

    def add_item(self, product, quantity=1):
        # 如果商品已在购物车中，增加数量
        for i, (p, q) in enumerate(self.items):
            if p.name == product.name:
                self.items[i] = (p, q + quantity)
                print(f"  {product.name} 数量更新为 {q + quantity}")
                return
        self.items.append((product, quantity))
        print(f"  已添加 {product.name} × {quantity}")

    def get_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.final_price * quantity
        return round(total, 2)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        lines = ["🛒 购物车:"]
        for product, quantity in self.items:
            subtotal = product.final_price * quantity
            lines.append(f"  {product.name} × {quantity} = {Product.format_price(subtotal)}")
        lines.append(f"  ----------")
        lines.append(f"  总计: {Product.format_price(self.get_total())}")
        return "\n".join(lines)


p1 = Product("Python编程书", 79.9)
p2 = Product("机械键盘", 299)
p3 = Product("鼠标垫", 29.9)

cart = ShoppingCart()
cart.add_item(p1, 2)
cart.add_item(p2)
cart.add_item(p3, 3)

print(cart)
print(f"商品种类: {len(cart)}")

print()
Product.set_discount(0.8)  # 全场8折
print(cart)


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 3: 自定义分数类
# ===================================================================
print("=== 练习 3: 自定义分数类 ===")

class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("分母不能为0！")

        # 处理负号：始终让分母为正
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # 约分
        g = Fraction._gcd(abs(numerator), denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    @staticmethod
    def _gcd(a, b):
        """辗转相除法求最大公约数"""
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        """分数加法: a/b + c/d = (ad + bc) / bd"""
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """分数减法"""
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """分数乘法"""
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __eq__(self, other):
        """判等（已约分，直接比较）"""
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __lt__(self, other):
        """比较大小"""
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


f1 = Fraction(1, 2)   # 1/2
f2 = Fraction(1, 3)   # 1/3
f3 = Fraction(2, 4)   # 会自动约分为 1/2

print(f"f1 = {f1}")             # 1/2
print(f"f2 = {f2}")             # 1/3
print(f"f3 = {f3}")             # 1/2
print(f"f1 == f3: {f1 == f3}")  # True (都是 1/2)

print(f"{f1} + {f2} = {f1 + f2}")   # 1/2 + 1/3 = 5/6
print(f"{f1} - {f2} = {f1 - f2}")   # 1/2 - 1/3 = 1/6
print(f"{f1} × {f2} = {f1 * f2}")   # 1/2 × 1/3 = 1/6
print(f"f1 < f2: {f1 < f2}")         # False (1/2 > 1/3)
print(f"float(f1) = {float(f1)}")     # 0.5

# 连续运算
result = Fraction(1, 4) + Fraction(1, 4) + Fraction(1, 2)
print(f"1/4 + 1/4 + 1/2 = {result}")  # 1


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 4: 日志记录器
# ===================================================================
print("=== 练习 4: 日志记录器 ===")

class Logger:
    _instance = None
    _logs = []
    _level_priority = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}
    min_level = "DEBUG"

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        """单例模式：确保只有一个 Logger 实例"""
        if cls._instance is None:
            cls._instance = cls()
            print("Logger 实例已创建")
        return cls._instance

    @classmethod
    def set_level(cls, level):
        if level in cls._level_priority:
            cls.min_level = level
            print(f"日志级别设为: {level}")
        else:
            print(f"无效级别: {level}，可用: {list(cls._level_priority.keys())}")

    def log(self, level, message):
        if level not in Logger._level_priority:
            print(f"无效日志级别: {level}")
            return
        if Logger._level_priority[level] >= Logger._level_priority[Logger.min_level]:
            timestamp = datetime.now().strftime("%H:%M:%S")
            log_entry = f"[{timestamp}] [{level}] {message}"
            Logger._logs.append(log_entry)
            print(log_entry)

    def show_logs(self):
        print(f"--- 日志记录 ({len(Logger._logs)} 条) ---")
        for log in Logger._logs:
            print(f"  {log}")

    def clear(self):
        Logger._logs.clear()
        print("日志已清空")


# 使用
logger1 = Logger.get_instance()  # Logger 实例已创建
logger2 = Logger.get_instance()  # 不会再创建
print(f"logger1 is logger2: {logger1 is logger2}")  # True（同一个对象）

logger1.log("INFO", "程序启动")
logger1.log("DEBUG", "加载配置文件")
logger1.log("WARNING", "磁盘空间不足")
logger1.log("ERROR", "连接数据库失败")

print()
Logger.set_level("WARNING")  # 只记录 WARNING 及以上
logger1.log("DEBUG", "这条不会被记录")
logger1.log("INFO", "这条也不会被记录")
logger1.log("WARNING", "这条会被记录")

print()
logger1.show_logs()


print("\n" + "=" * 50 + "\n")


# ===================================================================
# [挑战题] 练习 5: 自定义列表
# ===================================================================
print("=== 挑战题: 自定义列表 ===")

class SmartList:
    def __init__(self, data=None):
        self._data = list(data) if data else []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __contains__(self, item):
        return item in self._data

    def __add__(self, other):
        return SmartList(self._data + other._data)

    def __mul__(self, n):
        return SmartList(self._data * n)

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        return f"SmartList({self._data})"

    def __repr__(self):
        return self.__str__()

    def append(self, item):
        self._data.append(item)

    def map(self, func):
        """对每个元素应用函数，返回新列表"""
        return SmartList([func(x) for x in self._data])

    def filter(self, func):
        """过滤元素，返回新列表"""
        return SmartList([x for x in self._data if func(x)])

    def reduce(self, func, initial=0):
        """归约操作"""
        result = initial
        for item in self._data:
            result = func(result, item)
        return result


# 测试基本操作
sl = SmartList([1, 2, 3, 4, 5])
print(f"列表: {sl}")
print(f"长度: {len(sl)}")
print(f"第1个元素: {sl[0]}")
print(f"最后一个元素: {sl[-1]}")
print(f"3 in sl: {3 in sl}")
print(f"9 in sl: {9 in sl}")

# 合并和重复
sl2 = SmartList([6, 7, 8])
print(f"合并: {sl + sl2}")
print(f"重复: {SmartList([1, 2]) * 3}")

# 高阶操作
print(f"每个元素 ×2: {sl.map(lambda x: x * 2)}")
print(f"偶数: {sl.filter(lambda x: x % 2 == 0)}")
total = sl.reduce(lambda acc, x: acc + x, 0)
print(f"总和: {total}")

# for 循环
print("遍历:")
for item in sl:
    print(f"  -> {item}")
