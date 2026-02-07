import json
import time
import os

# =========================================================
# Day 2 课堂演示脚本: 数据结构的力量
# =========================================================

# 获取脚本所在目录，确保文件路径正确
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "demo_data.json")

# ---------------------------------------------------------
# 第一部分: "真实世界"的数据交互 (JSON -> List/Dict)
# ---------------------------------------------------------
print("\n" + "="*50)
print("📚 第一部分: 从文件加载数据 (模拟真实开发)")
print("="*50)

try:
    print(f">>> 正在读取: {json_path} ...")
    with open(json_path, "r", encoding="utf-8") as f:
        employees = json.load(f)
    print(f"✅ 成功加载 {len(employees)} 条员工数据！\n")
except FileNotFoundError:
    print("❌ 找不到 demo_data.json 文件，请检查路径。")
    employees = []

# 演示: 简单的数据提取
if employees:
    first_emp = employees[0]
    print(f"演示数据结构 (List + Dict):")
    print(f"- 员工姓名: {first_emp['name']}")
    print(f"- 技能列表: {first_emp['skills']} (List)")
    print(f"- 个人档案: {first_emp['profile']} (Dict)")

    # 任务: 找出所有会 Python 的人
    print("\n[任务] 寻找 Python 开发者:")
    python_devs = [e["name"] for e in employees if "Python" in e["skills"]]
    print(f"-> 结果: {python_devs}")


# ---------------------------------------------------------
# 第二部分: "完美"的数据结构设计 (List + Dict + Tuple + Set)
# 对应 PPT 第 13 页的综合案例
# ---------------------------------------------------------
print("\n" + "="*50)
print("🚀 第二部分: 进阶结构演示 (班级成绩系统)")
print("="*50)

# 这是一个在内存中构建的复杂结构，JSON 做不到 (因为 JSON 不支持 Tuple/Set)
class_roster = [
    {
        "name": "Alice",
        "id": 1001,
        "exams": {        
            # Dict: 考试类型 -> 分数详情
            # Tuple: (得分, 满分) -> 数据不可变，安全！
            "Midterm": (88, 100),  
            "Final": (95, 100),
            "Gaokao": (650, 750)
        },
        # Set: 选课集合 -> 自动去重，支持交集运算
        "subjects": {"Math", "English", "Physics"} 
    },
    {
        "name": "Bob",
        "id": 1002,
        "exams": {
            "Midterm": (75, 100),
            "Final": (82, 100),
            "Gaokao": (590, 750)
        },
        "subjects": {"Math", "Chinese", "History"}
    }
]

print("✅ 复杂数据结构构建完成。\n")

# --- 场景 1: 深入挖掘 Alice 的数据 ---
print("--- [场景 1] 数据的层层提取 ---")
alice = class_roster[0]
gk_score = alice["exams"]["Gaokao"] # 拿到元组 (650, 750)

# 计算得分率
rate = gk_score[0] / gk_score[1]
print(f"学生: {alice['name']}")
print(f"高考成绩: {gk_score[0]}/{gk_score[1]}")
print(f"得分率: {rate:.2%}")

# --- 场景 2: 集合的威力 (交集运算) ---
print("\n--- [场景 2] 选课分析 (Set Operation) ---")
bob = class_roster[1]

# 求交集: 两人都选了什么课？
common_subjects = alice["subjects"] & bob["subjects"]
print(f"Alice 选课: {alice['subjects']}")
print(f"Bob   选课: {bob['subjects']}")
print(f"-> 共同选课: {common_subjects}")

# 求差集: Alice 选了但 Bob 没选的？
diff_subjects = alice["subjects"] - bob["subjects"]
print(f"-> Alice 独有的课: {diff_subjects}")

print("\n" + "="*50)
print("演示结束")
