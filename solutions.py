# ===================================================================
# OOP 第1课：类与对象入门 —— 参考答案
# ===================================================================
import random
class Cat:
    def __init__(self, name,age):
    


# ===================================================================
# 练习 1: 宠物猫
# ===================================================================
print("=== 练习 1: 宠物猫 ===")

class Cat:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.energy = 100

    def eat(self, food):
        self.energy += 15
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name}吃了{food}，精力恢复到{self.energy}")

    def play(self, hours):
        cost = 20 * hours
        if cost > self.energy:
            print(f"{self.name}太累了，需要休息")
        else:
            self.energy -= cost
            print(f"{self.name}玩了{hours}小时，精力剩余{self.energy}")

    def status(self):
        print(f"猫咪 {self.name}, {self.age}岁, 精力: {self.energy}")


cat1 = Cat("咪咪", 3)
cat2 = Cat("大橘", 5)

cat1.status()          # 猫咪 咪咪, 3岁, 精力: 100
cat1.play(3)           # 咪咪玩了3小时，精力剩余40
cat1.eat("小鱼干")      # 咪咪吃了小鱼干，精力恢复到55
cat1.play(4)           # 咪咪太累了，需要休息
cat1.status()          # 猫咪 咪咪, 3岁, 精力: 55

print()
cat2.play(2)           # 大橘玩了2小时，精力剩余60
cat2.eat("猫粮")        # 大橘吃了猫粮，精力恢复到75
cat2.status()          # 猫咪 大橘, 5岁, 精力: 75


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 2: 银行账户
# ===================================================================
print("=== 练习 2: 银行账户 ===")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("存款金额必须大于0")
            return
        self.balance += amount
        print(f"[{self.owner}] 存入 {amount} 元，余额: {self.balance} 元")

    def withdraw(self, amount):
        if amount <= 0:
            print("取款金额必须大于0")
            return
        if amount > self.balance:
            print(f"[{self.owner}] 余额不足！当前余额: {self.balance} 元")
            return
        self.balance -= amount
        print(f"[{self.owner}] 取出 {amount} 元，余额: {self.balance} 元")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("转账金额必须大于0")
            return
        if amount > self.balance:
            print(f"[{self.owner}] 余额不足，无法转账")
            return
        self.balance -= amount
        other_account.balance += amount
        print(f"[转账] {self.owner} → {other_account.owner}: {amount} 元")
        print(f"  {self.owner} 余额: {self.balance} 元")
        print(f"  {other_account.owner} 余额: {other_account.balance} 元")

    def __str__(self):
        return f"账户({self.owner}): 余额{self.balance}元"


acc1 = BankAccount("小明", 1000)
acc2 = BankAccount("小红", 500)

print(acc1)            # 账户(小明): 余额1000元
print(acc2)            # 账户(小红): 余额500元

acc1.deposit(500)      # [小明] 存入 500 元，余额: 1500 元
acc1.withdraw(200)     # [小明] 取出 200 元，余额: 1300 元
acc1.transfer(acc2, 300)  # 转账 小明 → 小红: 300 元

print(acc1)            # 账户(小明): 余额1000元
print(acc2)            # 账户(小红): 余额800元


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 3: 学生成绩管理
# ===================================================================
print("=== 练习 3: 学生成绩管理 ===")

class Student:
    def __init__(self, name, scores=None):
        self.name = name
        # ⚠️ 避免可变默认参数陷阱！
        # 如果写 scores={}，所有没传 scores 的对象会共享同一个字典
        self.scores = scores if scores is not None else {}

    def add_score(self, subject, score):
        self.scores[subject] = score
        print(f"已添加 {self.name} 的 {subject} 成绩: {score}")

    def get_average(self):
        if not self.scores:
            return 0.0
        avg = sum(self.scores.values()) / len(self.scores)
        return round(avg, 1)

    def get_best_subject(self):
        if not self.scores:
            return "暂无成绩"
        # max 的 key 参数：按字典的 value 找最大
        return max(self.scores, key=self.scores.get)

    def __str__(self):
        return f"学生 {self.name}: {self.scores}"


s1 = Student("小明")
s1.add_score("数学", 95)
s1.add_score("英语", 88)
s1.add_score("物理", 92)
print(s1)                           # 学生 小明: {'数学': 95, '英语': 88, '物理': 92}
print(f"平均分: {s1.get_average()}")  # 平均分: 91.7
print(f"最强科目: {s1.get_best_subject()}")  # 最强科目: 数学

s2 = Student("小红")
s2.add_score("语文", 98)
s2.add_score("数学", 85)
print(s2)                           # 学生 小红: {'语文': 98, '数学': 85}
print(f"平均分: {s2.get_average()}")  # 平均分: 91.5


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 4: 骰子游戏
# ===================================================================
print("=== 练习 4: 骰子游戏 ===")

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.history = []

    def roll(self):
        result = random.randint(1, self.sides)
        self.history.append(result)
        return result

    def roll_multiple(self, times):
        results = []
        for _ in range(times):
            results.append(self.roll())
        return results

    def get_stats(self):
        if not self.history:
            return {"总次数": 0, "平均值": 0, "最大值": 0, "最小值": 0}
        return {
            "总次数": len(self.history),
            "平均值": round(sum(self.history) / len(self.history), 2),
            "最大值": max(self.history),
            "最小值": min(self.history),
        }

    def __str__(self):
        return f"{self.sides}面骰子, 已投掷{len(self.history)}次"


class DiceGame:
    def __init__(self, player_name, dice=None):
        self.player_name = player_name
        self.dice = dice if dice else Dice()
        self.total_score = 0

    def play_round(self):
        result = self.dice.roll()
        self.total_score += result
        print(f"[{self.player_name}] 掷出了 {result} 点! 总分: {self.total_score}")

    def show_score(self):
        print(f"{self.player_name} 的总分: {self.total_score}")


# 测试 Dice
d = Dice()
print(f"投掷结果: {d.roll_multiple(5)}")
print(f"统计: {d.get_stats()}")
print(d)

print()

# 测试 DiceGame
game = DiceGame("玩家1")
for _ in range(3):
    game.play_round()
game.show_score()


print("\n" + "=" * 50 + "\n")


# ===================================================================
# [挑战题] 练习 5: 简易通讯录
# ===================================================================
print("=== 挑战题: 简易通讯录 ===")

class Contact:
    def __init__(self, name, phone, email="无"):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"  📇 {self.name} | 📞 {self.phone} | ✉️ {self.email}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        # 检查是否已存在同名联系人
        for i, c in enumerate(self.contacts):
            if c.name == contact.name:
                self.contacts[i] = contact
                print(f"已更新联系人: {contact.name}")
                return
        self.contacts.append(contact)
        print(f"已添加联系人: {contact.name}")

    def remove_contact(self, name):
        for i, c in enumerate(self.contacts):
            if c.name == name:
                self.contacts.pop(i)
                print(f"已删除联系人: {name}")
                return
        print(f"未找到联系人: {name}")

    def search(self, keyword):
        results = []
        for c in self.contacts:
            if keyword in c.name or keyword in c.phone:
                results.append(c)
        return results

    def show_all(self):
        if not self.contacts:
            print("通讯录为空")
            return
        print(f"--- 通讯录 ({len(self.contacts)}位联系人) ---")
        for c in self.contacts:
            print(c)

    def __str__(self):
        return f"通讯录: {len(self.contacts)}位联系人"


# 使用示例
book = AddressBook()
book.add_contact(Contact("张三", "13800001111", "zhangsan@email.com"))
book.add_contact(Contact("李四", "13900002222"))
book.add_contact(Contact("王五", "13700003333", "wangwu@email.com"))
book.add_contact(Contact("张伟", "15800004444"))

print()
book.show_all()

print()
print("搜索 '张':")
results = book.search("张")
for c in results:
    print(c)

print()
book.remove_contact("李四")
print(book)
