# Day 4 课后作业 - 参考答案
# 请先尝试独立完成 homework.py，再对照本文件检查

import random
from datetime import datetime

# ===========================================================
# 作业 1：图书管理系统
# 难度：⭐⭐
# ===========================================================

print("=" * 50)
print("作业 1：图书管理系统")
print("=" * 50)


class Book:
    """图书类"""
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True  # 默认可借
    
    def __str__(self):
        status = "可借" if self.available else "已借出"
        return f"《{self.title}》 by {self.author} [{status}]"
    
    def borrow(self):
        """借书"""
        if self.available:
            self.available = False
            return True
        return False
    
    def return_book(self):
        """还书"""
        self.available = True


class Library:
    """图书馆类"""
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """添加图书"""
        self.books.append(book)
        print(f"已添加: {book}")
    
    def remove_book(self, isbn):
        """根据ISBN移除图书"""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"已移除: {book}")
                return True
        print(f"未找到ISBN为 {isbn} 的图书")
        return False
    
    def find_book(self, title_keyword):
        """根据书名关键字查找图书（模糊匹配）"""
        results = []
        for book in self.books:
            if title_keyword.lower() in book.title.lower():
                results.append(book)
        return results
    
    def list_available(self):
        """列出所有可借图书"""
        print(f"\n{self.name} - 可借图书:")
        print("-" * 40)
        available = [b for b in self.books if b.available]
        if available:
            for book in available:
                print(f"  {book}")
        else:
            print("  暂无可借图书")
    
    def list_all(self):
        """列出所有图书"""
        print(f"\n{self.name} - 全部图书:")
        print("-" * 40)
        for book in self.books:
            print(f"  {book}")


# 测试
print("\n--- 图书管理系统测试 ---")
library = Library("Python图书馆")

# 添加图书
library.add_book(Book("001", "Python入门", "张三"))
library.add_book(Book("002", "Python进阶", "李四"))
library.add_book(Book("003", "Python实战", "王五"))

# 显示所有图书
library.list_all()

# 借书
print("\n尝试借阅《Python入门》...")
book = library.find_book("入门")[0]
if book.borrow():
    print(f"借阅成功: {book}")
else:
    print("借阅失败")

# 显示可借图书
library.list_available()

# 还书
print("\n归还《Python入门》...")
book.return_book()
print(f"归还成功: {book}")

# 查找图书
print("\n查找包含'Python'的图书:")
results = library.find_book("Python")
for b in results:
    print(f"  {b}")


# ===========================================================
# 作业 2：银行账户系统
# 难度：⭐⭐⭐
# ===========================================================

print("\n" + "=" * 50)
print("作业 2：银行账户系统")
print("=" * 50)


class BankAccount:
    """银行账户基类"""
    _next_account = 10001
    
    def __init__(self, owner, initial_balance=0):
        self.account_number = BankAccount._next_account
        BankAccount._next_account += 1
        self.owner = owner
        self.__balance = initial_balance
    
    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            print("存款金额必须大于0")
            return False
        self.__balance += amount
        print(f"存款成功: +¥{amount}，余额: ¥{self.__balance}")
        return True
    
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            print("取款金额必须大于0")
            return False
        if amount > self.__balance:
            print(f"余额不足！当前余额: ¥{self.__balance}")
            return False
        self.__balance -= amount
        print(f"取款成功: -¥{amount}，余额: ¥{self.__balance}")
        return True
    
    def get_balance(self):
        """获取余额"""
        return self.__balance
    
    def _set_balance(self, value):
        """内部使用：设置余额（供子类调用）"""
        self.__balance = value
    
    def __str__(self):
        return f"账户{self.account_number} ({self.owner}): ¥{self.__balance}"


class CheckingAccount(BankAccount):
    """支票账户：可以透支"""
    def __init__(self, owner, initial_balance=0, overdraft_limit=500):
        super().__init__(owner, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """取款（可透支）"""
        if amount <= 0:
            print("取款金额必须大于0")
            return False
        
        available = self.get_balance() + self.overdraft_limit
        if amount > available:
            print(f"超出透支额度！可用额度: ¥{available}")
            return False
        
        new_balance = self.get_balance() - amount
        self._set_balance(new_balance)
        
        if new_balance < 0:
            print(f"取款成功: -¥{amount}，余额: ¥{new_balance} (透支中)")
        else:
            print(f"取款成功: -¥{amount}，余额: ¥{new_balance}")
        return True


class SavingsAccount(BankAccount):
    """储蓄账户：有利息，限制取款次数"""
    def __init__(self, owner, initial_balance=0, 
                 interest_rate=0.02, withdrawal_limit=3):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit
        self.withdrawal_count = 0
    
    def withdraw(self, amount):
        """取款（有次数限制）"""
        if self.withdrawal_count >= self.withdrawal_limit:
            print(f"本月取款次数已用完！({self.withdrawal_count}/{self.withdrawal_limit})")
            return False
        
        result = super().withdraw(amount)
        if result:
            self.withdrawal_count += 1
            print(f"  (本月剩余取款次数: {self.withdrawal_limit - self.withdrawal_count})")
        return result
    
    def add_interest(self):
        """添加利息"""
        balance = self.get_balance()
        interest = balance * self.interest_rate
        if interest > 0:
            self._set_balance(balance + interest)
            print(f"利息已到账: +¥{interest:.2f}，余额: ¥{self.get_balance():.2f}")
    
    def reset_withdrawal_count(self):
        """重置取款次数（月初调用）"""
        self.withdrawal_count = 0
        print("取款次数已重置")


# 测试
print("\n--- 银行账户系统测试 ---")

# 普通账户
print("\n[普通账户测试]")
acc1 = BankAccount("张三", 1000)
print(acc1)
acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(2000)  # 余额不足

# 支票账户
print("\n[支票账户测试]")
acc2 = CheckingAccount("李四", 1000, overdraft_limit=500)
print(acc2)
acc2.withdraw(1200)  # 会透支200
acc2.withdraw(400)   # 超出透支额度

# 储蓄账户
print("\n[储蓄账户测试]")
acc3 = SavingsAccount("王五", 10000, interest_rate=0.03, withdrawal_limit=2)
print(acc3)
acc3.withdraw(1000)
acc3.withdraw(1000)
acc3.withdraw(1000)  # 超出次数限制
acc3.add_interest()
acc3.reset_withdrawal_count()
acc3.withdraw(500)


# ===========================================================
# 作业 3：动物园模拟
# 难度：⭐⭐⭐
# ===========================================================

print("\n" + "=" * 50)
print("作业 3：动物园模拟")
print("=" * 50)


class Animal:
    """动物基类"""
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def speak(self):
        return "..."
    
    def eat(self, food):
        print(f"🍽️ {self.name}正在吃{food}")
    
    def perform(self):
        print(f"🎪 {self.name}在表演")
    
    def __str__(self):
        return f"{self.name} ({self.species}, {self.age}岁)"


class Lion(Animal):
    """狮子"""
    def __init__(self, name, age):
        super().__init__(name, "狮子", age)
    
    def speak(self):
        return "吼!"
    
    def perform(self):
        print(f"🦁 {self.name}威风凛凛地走过")


class Elephant(Animal):
    """大象"""
    def __init__(self, name, age, trunk_length):
        super().__init__(name, "大象", age)
        self.trunk_length = trunk_length
    
    def speak(self):
        return "帕欧~"
    
    def perform(self):
        print(f"🐘 {self.name}用{self.trunk_length}米长的鼻子喷水表演")


class Monkey(Animal):
    """猴子"""
    def __init__(self, name, age, favorite_fruit):
        super().__init__(name, "猴子", age)
        self.favorite_fruit = favorite_fruit
    
    def speak(self):
        return "吱吱吱"
    
    def eat(self, food):
        super().eat(food)
        if food == self.favorite_fruit:
            print(f"  🍌 {self.name}: 太好吃了！")
    
    def perform(self):
        print(f"🐒 {self.name}表演倒挂金钩")


class Zoo:
    """动物园"""
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"欢迎新成员！{animal}")
    
    def feed_all(self, food):
        print(f"\n🍎 喂食时间 - {food}")
        print("-" * 30)
        for animal in self.animals:
            animal.eat(food)
    
    def perform_show(self):
        print(f"\n🎭 {self.name}表演秀")
        print("-" * 30)
        for animal in self.animals:
            animal.perform()
    
    def roll_call(self):
        print(f"\n📢 {self.name}点名")
        print("-" * 30)
        for animal in self.animals:
            print(f"  {animal.name}: {animal.speak()}")


# 测试
print("\n--- 动物园模拟测试 ---")
zoo = Zoo("欢乐动物园")

# 添加动物
zoo.add_animal(Lion("辛巴", 5))
zoo.add_animal(Elephant("大宝", 8, 2.5))
zoo.add_animal(Monkey("悟空", 3, "香蕉"))

# 点名
zoo.roll_call()

# 表演
zoo.perform_show()

# 喂食
zoo.feed_all("苹果")
zoo.feed_all("香蕉")  # 猴子会特别开心


# ===========================================================
# 作业 4：扩展 RPG 战斗系统
# 难度：⭐⭐⭐⭐
# ===========================================================

print("\n" + "=" * 50)
print("作业 4：扩展 RPG 战斗系统")
print("=" * 50)


class Role:
    """角色基类"""
    def __init__(self, name, hp, atk, dodge_rate=0.1):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.dodge_rate = dodge_rate
        self.status_effects = []  # 状态效果列表
    
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage, source=""):
        # 闪避判定
        if random.random() < self.dodge_rate:
            print(f"  ⚡ {self.name} 闪避了攻击！")
            return False
        
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"  💔 {self.name} 受到 {damage} 点伤害，HP: {self.hp}/{self.max_hp}")
        return True
    
    def attack(self, target):
        print(f"⚔️ {self.name} 攻击 {target.name}")
        target.take_damage(self.atk)
    
    def apply_poison(self, duration=3):
        """施加中毒状态"""
        self.status_effects.append({"type": "poison", "duration": duration, "damage": 5})
        print(f"  ☠️ {self.name} 中毒了！(持续{duration}回合)")
    
    def process_status_effects(self):
        """处理状态效果（每回合开始时调用）"""
        new_effects = []
        for effect in self.status_effects:
            if effect["type"] == "poison":
                self.hp -= effect["damage"]
                if self.hp < 0:
                    self.hp = 0
                print(f"  ☠️ {self.name} 受到中毒伤害 -{effect['damage']}HP")
                effect["duration"] -= 1
                if effect["duration"] > 0:
                    new_effects.append(effect)
                else:
                    print(f"  💚 {self.name} 的中毒状态消失了")
        self.status_effects = new_effects


class Warrior(Role):
    """战士"""
    def __init__(self, name):
        super().__init__(name, hp=150, atk=25, dodge_rate=0.05)
    
    def heavy_strike(self, target):
        damage = int(self.atk * 1.5)
        print(f"💪 {self.name} 使用重击 → {target.name}")
        target.take_damage(damage)


class Mage(Role):
    """法师"""
    def __init__(self, name):
        super().__init__(name, hp=80, atk=15, dodge_rate=0.1)
        self.mp = 100
    
    def fireball(self, target):
        if self.mp >= 20:
            self.mp -= 20
            print(f"🔥 {self.name} 火球术 → {target.name} (MP: {self.mp})")
            target.take_damage(50)
        else:
            self.attack(target)
    
    def poison_cloud(self, target):
        """毒云术"""
        if self.mp >= 15:
            self.mp -= 15
            print(f"☁️ {self.name} 毒云术 → {target.name} (MP: {self.mp})")
            target.apply_poison(3)
        else:
            print(f"{self.name} 魔力不足!")


class Healer(Role):
    """治疗师"""
    def __init__(self, name):
        super().__init__(name, hp=100, atk=10, dodge_rate=0.1)
        self.mp = 80
    
    def heal(self, target):
        if self.mp >= 15:
            self.mp -= 15
            heal_amount = 30
            target.hp = min(target.hp + heal_amount, target.max_hp)
            print(f"💚 {self.name} 治疗 → {target.name} +{heal_amount}HP")
        else:
            print(f"{self.name} 魔力不足!")


class Assassin(Role):
    """刺客：高暴击，高闪避"""
    def __init__(self, name):
        super().__init__(name, hp=90, atk=30, dodge_rate=0.25)
    
    def backstab(self, target):
        """背刺：30%几率3倍暴击，70%几率1.5倍伤害"""
        if random.random() < 0.3:
            damage = self.atk * 3
            print(f"🗡️ {self.name} 背刺 → {target.name} 💥暴击！")
        else:
            damage = int(self.atk * 1.5)
            print(f"🗡️ {self.name} 背刺 → {target.name}")
        target.take_damage(damage)


def battle(team_a, team_b, max_rounds=20):
    """回合制战斗"""
    print("\n" + "=" * 50)
    print("⚔️  战 斗 开 始  ⚔️")
    print("=" * 50)
    
    print("\n队伍A:", ", ".join(m.name for m in team_a))
    print("队伍B:", ", ".join(m.name for m in team_b))
    
    round_num = 1
    while round_num <= max_rounds:
        print(f"\n{'─'*40}")
        print(f"📍 第 {round_num} 回合")
        print(f"{'─'*40}")
        
        # 处理状态效果
        for member in team_a + team_b:
            if member.is_alive() and member.status_effects:
                member.process_status_effects()
        
        # 检查是否有队伍全灭
        if not any(m.is_alive() for m in team_a):
            return "B"
        if not any(m.is_alive() for m in team_b):
            return "A"
        
        # 队伍A行动
        print("\n[队伍A行动]")
        for member in team_a:
            if not member.is_alive():
                continue
            
            # 选择目标
            alive_enemies = [m for m in team_b if m.is_alive()]
            if not alive_enemies:
                break
            target = random.choice(alive_enemies)
            
            # 选择技能
            if isinstance(member, Assassin):
                member.backstab(target)
            elif isinstance(member, Warrior):
                if random.random() > 0.5:
                    member.heavy_strike(target)
                else:
                    member.attack(target)
            elif isinstance(member, Mage):
                if random.random() > 0.7:
                    member.poison_cloud(target)
                else:
                    member.fireball(target)
            elif isinstance(member, Healer):
                injured = [m for m in team_a if m.is_alive() and m.hp < m.max_hp * 0.5]
                if injured:
                    member.heal(min(injured, key=lambda m: m.hp))
                else:
                    member.attack(target)
            else:
                member.attack(target)
        
        # 检查队伍B是否全灭
        if not any(m.is_alive() for m in team_b):
            return "A"
        
        # 队伍B行动
        print("\n[队伍B行动]")
        for member in team_b:
            if not member.is_alive():
                continue
            
            alive_enemies = [m for m in team_a if m.is_alive()]
            if not alive_enemies:
                break
            target = random.choice(alive_enemies)
            
            # 简单AI：直接攻击
            if isinstance(member, Assassin):
                member.backstab(target)
            elif isinstance(member, Warrior):
                member.heavy_strike(target)
            else:
                member.attack(target)
        
        # 检查队伍A是否全灭
        if not any(m.is_alive() for m in team_a):
            return "B"
        
        round_num += 1
    
    return "Draw"


# 测试战斗
print("\n--- RPG 战斗系统测试 ---")

team_heroes = [
    Warrior("勇者"),
    Mage("魔导师"),
    Assassin("暗影")
]

team_monsters = [
    Role("哥布林", 60, 12),
    Role("哥布林", 60, 12),
    Warrior("哥布林王")
]

result = battle(team_heroes, team_monsters)
print("\n" + "=" * 50)
if result == "A":
    print("🎉 英雄队伍获胜！")
elif result == "B":
    print("💀 怪物队伍获胜！")
else:
    print("⏰ 战斗超时，平局！")
print("=" * 50)


# ===========================================================
# 作业 5：设计模式实践 - 单例模式
# 难度：⭐⭐⭐⭐⭐
# ===========================================================

print("\n" + "=" * 50)
print("作业 5：单例模式")
print("=" * 50)


class GameConfig:
    """游戏配置（单例模式）"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # 初始化配置
            cls._instance.difficulty = "Normal"
            cls._instance.sound_volume = 80
            cls._instance.resolution = "1920x1080"
        return cls._instance
    
    def __str__(self):
        return (f"GameConfig(difficulty={self.difficulty}, "
                f"volume={self.sound_volume}, resolution={self.resolution})")


class Logger:
    """日志管理器（单例模式）"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._logs = []
        return cls._instance
    
    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self._logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self):
        return self._logs.copy()


# 测试单例模式
print("\n--- 单例模式测试 ---")

# GameConfig 测试
config1 = GameConfig()
config2 = GameConfig()
print(f"config1 is config2? {config1 is config2}")  # True
print(f"config1: {config1}")

config1.difficulty = "Hard"
print(f"config2.difficulty: {config2.difficulty}")  # Hard (同一个实例)

# Logger 测试
print()
logger1 = Logger()
logger2 = Logger()
print(f"logger1 is logger2? {logger1 is logger2}")  # True

logger1.log("游戏启动")
logger2.log("玩家进入")
logger1.log("战斗开始")

print(f"\n所有日志 ({len(logger1.get_logs())}条):")
for log in logger1.get_logs():
    print(f"  {log}")


print("\n" + "=" * 50)
print("所有作业答案演示完毕！")
print("=" * 50)
