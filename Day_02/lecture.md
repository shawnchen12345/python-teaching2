第1页：为什么要学数据结构？

程序 = 数据 + 操作

数据结构决定：

代码是否清晰

性能是否高效

逻辑是否容易维护

💡 举个栗子（班级成绩单）：
-----------------------
❌ 方式 A：没有结构（变量散乱）
score_1 = 85
score_2 = 92
score_3 = 78
... 如果班里有 50 个人？
算平均分：(score_1 + score_2 + ... + score_50) / 50
👉 缺点：代码写死，难维护，无法应对人数变化。

✅ 方式 B：使用数据结构（List 列表）
scores = [85, 92, 78, ...]
算平均分：sum(scores) / len(scores)
👉 优点：代码简洁，只需一行，人数变了代码不用改。
-----------------------

Python 最常用的 5 种数据结构：

List

Tuple

Dict

Set

String

📦 第2页：列表 List 是什么？

列表（List） = 有序、可变、可重复 的数据集合

示例：

nums = [10, 20, 30]
names = ["Alice", "Bob"]
mixed = [1, "hi", 3.14]


✔ 按顺序存储
✔ 可以修改
✔ 可以存不同类型

⚙️ 第3页：List 常用操作
nums.append(40)      # 追加
nums.insert(1, 15)   # 插入
nums.remove(20)      # 删除指定值
nums.pop()           # 删除最后一个
nums.sort()          # 排序
len(nums)            # 长度


📌 List = Python 中最常用的数据结构

🎯 第4页：案例 — 成绩统计
scores = [85, 92, 78, 90, 88]

avg = sum(scores) / len(scores)
top = max(scores)

scores.sort(reverse=True)

print("平均分:", avg)
print("最高分:", top)
print("排名:", scores)


👉 适合：批量数据、排名、队列

📝 课堂练习 1（List）

题目：

有一个列表：

nums = [3, 7, 2, 9, 7, 5]


请完成：

计算列表的平均值

删除其中一个 7

把列表按从小到大排序

🔒 第5页：元组 Tuple 是什么？

元组（Tuple） = 有序但不可变

point = (3, 5)
rgb = (255, 255, 0)

特性	是否支持
有序	✅
可修改	❌
可重复	✅
💡 第6页：Tuple 的典型用途

✔ 表示不会改变的数据
✔ 函数返回多个值

def get_user():
    return ("Alice", 25)

name, age = get_user()


📌 Tuple = “只读列表”

📝 课堂练习 2（Tuple）

函数返回一个学生的信息（姓名、年龄、分数），
请用一个元组表示并打印出来。

📒 第7页：字典 Dict 是什么？（重点）

字典（Dict） = 键值对结构（key-value）

student = {
    "name": "Alice",
    "age": 20,
    "score": 95
}


通过 key 快速找 value
类似现实中的“通讯录”

⚙️ 第8页：Dict 常用操作
student["age"] = 21
student["gender"] = "女"
del student["score"]

student.get("name")      # 安全访问
student.keys()
student.values()
student.items()


📌 Dict 查找速度极快

🎯 第9页：案例 — 单词统计
text = "apple banana apple orange banana apple"

words = text.split()
counter = {}

for w in words:
    counter[w] = counter.get(w, 0) + 1

print(counter)


输出：

{'apple': 3, 'banana': 2, 'orange': 1}


👉 Dict = 统计类问题神器

📝 课堂练习 3（Dict）

统计一句话中每个字符出现的次数：

text = "hello world"


提示：用字典保存字符和次数

🎲 第10页：集合 Set 是什么？

集合（Set） = 无序 + 不重复

nums = {1, 2, 3, 3, 2}
print(nums)   # {1, 2, 3}


📌 自动去重

➕ 第11页：Set 的数学运算
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a & b   # 交集
a | b   # 并集
a - b   # 差集


👉 适合：去重、关系判断

📝 课堂练习 4（Set）

有两个班级学生名单：

a = {"Alice", "Bob", "Tom"}
b = {"Tom", "Jerry", "Bob"}


找出两个班都在的人

找出只在 A 班的人

🔤 第12页：字符串 String

字符串是不可变字符序列

text = "Hello Python"


常用方法：

text.lower()
text.upper()
text.split()
text.replace("Python", "World")

📝 课堂练习 5（String）

给定字符串：

s = "  Python Is Fun  "


请：

去掉两边空格

变成小写

把空格替换成 -

🧠 第13页：综合案例 — 完美的数据结构设计

需求：管理班级成绩，区分期中、期末、高考，并记录选考科目。

# 🏆 终极结构设计：

class_roster = [
    {
        "name": "Alice",  # String: 姓名
        "id": 1001,
        "exams": {        # Dict: 考试类型 -> 分数详情
            "期中": (88, 100),  # Tuple: (得分, 满分) 不可变，数据安全
            "期末": (95, 100),
            "高考": (650, 750)
        },
        "subjects": {"Math", "English", "Physics"} # Set: 选课集合(自动去重)
    },
    {
        "name": "Bob",
        "id": 1002,
        "exams": {
            "期中": (75, 100),
            "期末": (82, 100),
            "高考": (590, 750)
        },
        "subjects": {"Math", "Chinese", "History"}
    }
]

# 💡 结构解析 (为什么要这么组合？)
# 1. List []: 班级要把所有学生排在一起，有序且方便遍历。
# 2. Dict {}: 每个人有不同属性(名字、分数、课程)，键值对查找最快。
# 3. Tuple (): (得分, 满分) 是一组固定搭配，且不应被轻易修改（只读）。
# 4. Set {}: 课程列表重点在于“有没有选”，集合可以高效做交集/并集运算。

# 🚀 实战操作：
# 1. 打印 Alice 的高考得分率：
alice = class_roster[0]
score, full = alice["exams"]["高考"]
print(f"得分率: {score/full:.2%}")

# 2. 找出两人共同选修的课 (Set 交集)：
bob = class_roster[1]
common = alice["subjects"] & bob["subjects"]
print("共同选课:", common)

🎯 第14页：总结对比表
数据结构	是否有序	是否可变	典型用途
List	      ✅	      ✅	       批量数据
Tuple	      ✅	      ❌	       固定数据
Dict	      ✅	      ✅	       映射/统计
Set	          ❌	      ✅	       去重
String	      ✅	      ❌	       文本处理
🏁 第15页：课后思考

为什么字典查找比列表快？

什么时候应该用 Tuple 而不是 List？

如何用 Set 判断两个列表是否有重复元素？

如果你愿意，我可以再帮你加一版：
✅ 每道练习的参考答案
✅ 或改成「面试常考数据结构题型版」