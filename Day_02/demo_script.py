import json
import time
import os

# =========================================================
# Day 2 课堂演示脚本: 数据结构的力量
# =========================================================

# 1. 模拟从服务器获取数据 (读取 JSON 文件)
print(">>> 正在从 '服务器' 下载员工数据...")
time.sleep(1) # 模拟网络延迟

# 获取脚本所在目录的绝对路径，确保能在任何地方运行
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "demo_data.json")

try:
    with open(json_path, "r", encoding="utf-8") as f:
        employees = json.load(f)
    print(f"✅ 成功加载 {len(employees)} 条员工记录！\n")
except FileNotFoundError:
    print(f"❌ 错误：找不到数据文件！\n请检查该路径是否存在文件:\n{json_path}")
    exit()


# ---------------------------------------------------------
# 演示 1: 复杂数据结构的层级访问 (列表 -> 字典 -> 列表)
# ---------------------------------------------------------
print("--- [演示 1] 复杂嵌套数据的提取 ---")
first_emp = employees[0]
print(f"第一位员工: {first_emp['name']}")
print(f"他的第2个技能: {first_emp['skills'][1]}") # 索引从0开始
print(f"他的邮箱地址: {first_emp['profile']['email']}")
print("-" * 40 + "\n")

# ---------------------------------------------------------
# 演示 2: 数据筛选与清洗 (Python 的优雅)
# 任务: 找出所有会 Python 的员工名字
# ---------------------------------------------------------
print("--- [演示 2] 寻找 Python 大神 ---")
# 方式 A: 传统循环 (C/Java 风格)
print("方式 A (笨办法):")
python_devs = []
for emp in employees:
    # 这里的 skills 是一个列表，用 in 判断成员
    if "Python" in emp["skills"]:
        python_devs.append(emp["name"])
print(f"找到: {python_devs}")

# 方式 B: 列表推导式 (Pythonic 风格)
print("\n方式 B (一行流):")
# [只要名字 for 员工 in 全体员工 if 会Python]
python_devs_v2 = [e["name"] for e in employees if "Python" in e["skills"]]
print(f"找到: {python_devs_v2}")
print("-" * 40 + "\n")

# ---------------------------------------------------------
# 演示 3: 数据的统计 (字典应用)
# 任务: 统计每种技能有多少人会
# ---------------------------------------------------------
print("--- [演示 3] 技能热度统计 ---")
skill_counts = {}

for emp in employees:
    for skill in emp["skills"]:
        # 如果这个技能还没记录过，初始化为0
        if skill not in skill_counts:
            skill_counts[skill] = 0
        skill_counts[skill] += 1

# 打印结果 (按技能名排序)
print("技能分布:")
for skill, count in sorted(skill_counts.items()):
    # 使用 f-string 对齐输出
    # :<10 表示左对齐占10格
    print(f"  {skill:<10}: {'#' * count} ({count})") 

print("-" * 40 + "\n")

# ---------------------------------------------------------
# 演示 4: 数据的增删改 (模拟人事变动)
# ---------------------------------------------------------
print("--- [演示 4] 人事变动操作 ---")

# 1. 查找并修改
target_name = "Alice"
print(f"正在寻找 {target_name} 进行晋升...")
for emp in employees:
    if emp["name"] == target_name:
        emp["role"] = "Tech Lead" # 升职
        emp["skills"].append("Team Management") # 加技能
        print(f"✅ {target_name} 已晋升! 当前技能: {emp['skills']}")
        break
else:
    # for-else 语法: 如果循环没被 break (没找到人)，执行这里
    print(f"❌ 查无此人: {target_name}")

# 2. 删除 (根据ID)
fire_id = 1003
print(f"\n正在开除 ID={fire_id} 的员工...")
# 一种安全的删除方法: 重建列表 (保留不需要删除的人)
# 只要 ID 不等于 fire_id 的人都留下
employees = [e for e in employees if e["id"] != fire_id]

print(f"当前剩余员工数: {len(employees)}")
print([e["name"] for e in employees])

print("\n=== 演示结束 ===")
