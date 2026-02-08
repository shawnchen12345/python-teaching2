import time
import random
import os

# =========================================================
# Day 3 课堂演示脚本: 流程控制与函数的力量
# =========================================================

print("\n" + "="*60)
print("📖 Day 3 课堂演示：流程控制 + 函数 + 标准库")
print("="*60)

# ---------------------------------------------------------
# 第一部分: 流程控制 - 条件与循环
# ---------------------------------------------------------
print("\n" + "="*60)
print("🔀 第一部分: 流程控制演示")
print("="*60)

# 演示 1: if-elif-else 条件判断
print("\n--- [演示 1] 成绩等级判定 ---")
def get_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        return "A (优秀)"
    elif score >= 80:
        return "B (良好)"
    elif score >= 60:
        return "C (及格)"
    else:
        return "D (不及格)"

test_scores = [95, 82, 65, 45]
for score in test_scores:
    grade = get_grade(score)
    print(f"分数 {score} -> 等级 {grade}")

# 演示 2: for 循环 + enumerate
print("\n--- [演示 2] 遍历与索引 ---")
students = ["Alice", "Bob", "Tom", "Jerry"]
print("方式1: 普通遍历")
for student in students:
    print(f"  - {student}")

print("\n方式2: 带索引遍历 (enumerate)")
for index, student in enumerate(students, start=1):
    print(f"  {index}. {student}")

# 演示 3: while 循环 - 猜数字游戏（简化版）
print("\n--- [演示 3] 猜数字游戏 (自动演示) ---")
secret = random.randint(1, 10)
attempts = 0
guess_list = [3, 7, 5, secret]  # 模拟用户猜测

print(f"秘密数字已生成 (1-10)...")
for guess in guess_list:
    attempts += 1
    print(f"第{attempts}次猜测: {guess}", end=" -> ")
    if guess == secret:
        print(f"✅ 恭喜！猜对了！秘密数字是 {secret}")
        break
    elif guess < secret:
        print("太小了")
    else:
        print("太大了")
else:
    print(f"❌ 次数用尽，正确答案是 {secret}")

# 演示 4: break 与 continue
print("\n--- [演示 4] break 与 continue ---")
print("只打印奇数 (使用 continue 跳过偶数):")
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i, end=" ")
print()

print("\n找到第一个能被7整除的数就停止 (使用 break):")
for i in range(1, 100):
    if i % 7 == 0:
        print(f"找到: {i}")
        break

# ---------------------------------------------------------
# 第二部分: 函数 - 参数与返回值
# ---------------------------------------------------------
print("\n" + "="*60)
print("🔧 第二部分: 函数演示")
print("="*60)

# 演示 5: 函数参数类型
print("\n--- [演示 5] 参数的多种形式 ---")

def connect_to_server(host, port=80, timeout=30):
    """演示默认参数"""
    return f"连接到 {host}:{port} (超时: {timeout}秒)"

print("1. 只传必需参数:")
print(connect_to_server("example.com"))

print("\n2. 指定端口:")
print(connect_to_server("example.com", 443))

print("\n3. 使用关键字参数:")
print(connect_to_server(host="api.github.com", timeout=60))

# 演示 6: *args 可变位置参数
print("\n--- [演示 6] *args 可变参数 ---")

def calculate_average(*scores):
    """计算任意数量分数的平均值"""
    if not scores:
        return 0
    return sum(scores) / len(scores)

print(f"3个分数的平均: {calculate_average(85, 90, 78):.1f}")
print(f"5个分数的平均: {calculate_average(92, 88, 76, 95, 81):.1f}")

# 演示 7: **kwargs 可变关键字参数
print("\n--- [演示 7] **kwargs 可变关键字参数 ---")

def build_user_profile(name, **extra_info):
    """构建用户档案"""
    profile = {"name": name}
    profile.update(extra_info)
    return profile

user1 = build_user_profile("Alice", age=25, city="北京", hobby="编程")
user2 = build_user_profile("Bob", age=30, email="bob@example.com")

print("用户1:", user1)
print("用户2:", user2)

# 演示 8: 作用域 (Scope)
print("\n--- [演示 8] 变量作用域 ---")

counter = 0  # 全局变量

def increment():
    global counter  # 声明要修改全局变量
    counter += 1
    print(f"  函数内: counter = {counter}")

print(f"调用前: counter = {counter}")
increment()
increment()
print(f"调用后: counter = {counter}")

# ---------------------------------------------------------
# 第三部分: Python 标准库
# ---------------------------------------------------------
print("\n" + "="*60)
print("📦 第三部分: 标准库演示")
print("="*60)

# 演示 9: random 模块
print("\n--- [演示 9] random 随机模块 ---")

# 1. 随机整数
dice = random.randint(1, 6)
print(f"掷骰子: {dice}")

# 2. 随机选择
participants = ["Alice", "Bob", "Tom", "Jerry", "Lucy"]
winner = random.choice(participants)
print(f"抽奖获胜者: {winner}")

# 3. 随机抽样（不重复）
top3 = random.sample(participants, 3)
print(f"前三名: {top3}")

# 4. 打乱列表
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(cards)
print(f"洗牌后: {cards[:5]}...")  # 只显示前5张

# 演示 10: time 模块
print("\n--- [演示 10] time 时间模块 ---")

print("倒计时3秒:")
for i in range(3, 0, -1):
    print(f"  {i}...", flush=True)
    time.sleep(1)
print("  ✅ 时间到！")

# 计算代码执行时间
print("\n计算耗时:")
start = time.time()
# 模拟耗时操作
total = sum(range(1000000))
end = time.time()
print(f"  计算 0 到 999999 的和: {total}")
print(f"  耗时: {(end - start)*1000:.2f} 毫秒")

# 演示 11: datetime 模块
print("\n--- [演示 11] datetime 日期模块 ---")
from datetime import datetime, timedelta

now = datetime.now()
print(f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 日期计算
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(f"明天: {tomorrow.strftime('%Y-%m-%d')}")
print(f"上周: {last_week.strftime('%Y-%m-%d')}")

# 演示 12: os 模块
print("\n--- [演示 12] os 系统模块 ---")

print(f"当前工作目录: {os.getcwd()}")
print(f"当前脚本所在目录: {os.path.dirname(os.path.abspath(__file__))}")

# 列出当前目录文件
files = os.listdir('.')
print(f"当前目录文件数: {len(files)}")
print(f"前3个文件: {files[:3]}")

# ---------------------------------------------------------
# 第四部分: 综合应用 - 简易任务管理器
# ---------------------------------------------------------
print("\n" + "="*60)
print("🚀 第四部分: 综合案例 - 任务管理器")
print("="*60)

class TaskManager:
    """简易任务管理器（演示类与函数结合）"""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task, priority="中"):
        """添加任务"""
        self.tasks.append({"name": task, "priority": priority, "done": False})
        print(f"✅ 已添加任务: {task} (优先级: {priority})")
    
    def complete_task(self, task_name):
        """完成任务"""
        for task in self.tasks:
            if task["name"] == task_name:
                task["done"] = True
                print(f"✅ 已完成: {task_name}")
                return
        print(f"❌ 未找到任务: {task_name}")
    
    def show_tasks(self):
        """显示所有任务"""
        if not self.tasks:
            print("📋 暂无任务")
            return
        
        print("\n📋 任务列表:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["done"] else "○"
            print(f"  {i}. [{status}] {task['name']} (优先级: {task['priority']})")

# 演示
manager = TaskManager()
manager.add_task("完成 Day 3 作业", "高")
manager.add_task("复习数据结构", "中")
manager.add_task("练习函数编写", "高")
manager.show_tasks()

print("\n--- 完成一个任务 ---")
manager.complete_task("复习数据结构")
manager.show_tasks()

print("\n" + "="*60)
print("演示结束")
print("="*60)
