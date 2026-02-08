# Day 2 练习参考答案
# 对应 Day_02/exercises.py 中的习题

# =========================================================
# 练习 1: 列表与所有权
# =========================================================
print("--- 练习 1: 列表操作 ---")
names = ["Alice", "Bob", "Charlie", "David"]
print(f"原始列表: {names}")

# 1. 把 "Eve" 加到最后
names.append("Eve")
print(f"1. 添加 Eve 后: {names}")

# 2. 把 "Bob" 改成 "Bobby"
# 注意：index方法可以找到Bob的位置，或者已知是第二个元素
if "Bob" in names:
    index = names.index("Bob")
    names[index] = "Bobby"
print(f"2. 修改 Bob 后: {names}")

# 3. 打印倒数第2个名字
print(f"3. 倒数第2个名字: {names[-2]}")

# 4. 打印前2个名字 (切片)
print(f"4. 前2个名字: {names[:2]}")

print("\n" + "="*30 + "\n")

# =========================================================
# 练习 2: 简单的数据库 (字典列表)
# =========================================================
print("--- 练习 2: 学生成绩筛选 ---")
students = [
    {"name": "Alice", "score": 55},
    {"name": "Bob", "score": 80},
    {"name": "Charlie", "score": 40},
    {"name": "David", "score": 90},
]

print("不及格名单 (<60):")
found_failed = False
for stu in students:
    if stu["score"] < 60:
        print(f"- {stu['name']}: {stu['score']}分")
        found_failed = True

if not found_failed:
    print("没有不及格的学生！")

print("\n" + "="*30 + "\n")

# =========================================================
# 练习 3: 元组解包
# =========================================================
print("--- 练习 3: 元组解包 ---")
points = [(1, 2), (3, 4), (10, 20)]

for x, y in points:
    print(f"X坐标: {x}, Y坐标: {y}")

print("\n" + "="*30 + "\n")

# =========================================================
# 练习 4: 集合运算
# =========================================================
print("--- 练习 4: 集合运算 ---")
skills_a = {"Python", "Java", "C++"}
skills_b = {"Python", "HTML", "CSS"}

# 1. 交集 &
common = skills_a & skills_b
print(f"都会的技能 (交集): {common}")

# 2. 差集 -
only_a = skills_a - skills_b
print(f"只有 A 会的技能 (差集): {only_a}")

print("\n" + "="*30 + "\n")

# =========================================================
# [挑战题] 词频统计 Top 3
# =========================================================
print("--- 挑战题: 词频统计 ---")
text = "Python is good. Python is fast. I love python code."
print(f"原始文本: \"{text}\"")

# 1. 数据清洗
# 转小写，并把标点替换为空格 (避免 chained.words 连在一起)
clean_text = text.lower().replace(".", " ").replace(",", " ")
words = clean_text.split()
print(f"分词结果: {words}")

# 2. 统计
counts = {}
for w in words:
    # get(w, 0) 如果字典里没有w，就返回0；有就返回对应次数
    counts[w] = counts.get(w, 0) + 1

print(f"统计结果: {counts}")

# 3. 排序 (进阶)
# counts.items() 变成 [('python', 3), ('is', 2), ...]
# key=lambda x: x[1] 表示按第二个元素（次数）排序
# reverse=True 表示从大到小
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

print("\n频率最高的前3名:")
# 防止单词不足3个的情况
top_n = min(3, len(sorted_counts))
for i in range(top_n):
    word, count = sorted_counts[i]
    print(f"Top {i+1}: '{word}' 出现了 {count} 次")
