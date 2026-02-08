# Day 2 实战练习 & 答案

# ---------------------------------------------------------
# 练习 1: 列表与所有权
# 有一个列表 names = ["Alice", "Bob", "Charlie", "David"]
# 1. 把 "Eve" 加到最后
# 2. 把 "Bob" 改成 "Bobby"
# 3. 打印倒数第2个名字
# 4. 打印前2个名字 (切片)
# ---------------------------------------------------------
print("--- 练习 1 ---")
names = ["Alice", "Bob", "Charlie", "David"]
# 在这里写代码:
names.append('Eve')#first step
names.remove('bob')#second step
names.insert(2,'bobby')#second step
print(names(-2))#third step
print(names(1))
print(names(2))




# ---------------------------------------------------------
# 练习 2: 简单的数据库 (字典列表)
# 创建一个列表，里面包含3个字典，每个字典代表一个学生(name, score)
# 循环遍历列表，打印所有分数不及格(<60)的学生名字
# ---------------------------------------------------------
print("\n--- 练习 2 ---")
students = [
    {"name": "A", "score": 55},
    {"name": "B", "score": 80},
    {"name": "C", "score": 40},
]
# 在这里写代码:
for x in students:

     if students('score')<60:
        print(students['name'])







# ---------------------------------------------------------
# 练习 3: 元组解包 (Tuple Unpacking)
# 有一个列表，存储了坐标点 (x, y)
# points = [(1, 2), (3, 4), (10, 20)]
# 循环遍历这个列表，直接解包成 x, y 两个变量
# 打印格式: "X坐标: 1, Y坐标: 2"
# ---------------------------------------------------------
print("\n--- 练习 3 ---")
points = [(1, 2), (3, 4), (10, 20)]
# 在这里写代码:
(a,b)=c

for c in points:
    print(f'x坐标:{a}','y坐标;{b}')




# ---------------------------------------------------------
# 练习 4: 集合运算 (Set)
# 技能池 A = {"Python", "Java", "C++"}
# 技能池 B = {"Python", "HTML", "CSS"}
# 1. 找出两个集合都有的技能 (交集)
# 2. 找出 A 有但 B 没有的技能 (差集)
# ---------------------------------------------------------
print("\n--- 练习 4 ---")
skills_a = {"Python", "Java", "C++"}
skills_b = {"Python", "HTML", "CSS"}
# 在这里写代码:
print(skills_a&sklls_b)
print(skills_a-skills_b)




# ---------------------------------------------------------
# [挑战题] 词频统计 Top 3
# 统计下面文段中每个单词出现的次数，打印出现最多的3个单词和次数。
# 提示: 
# 1. 标点符号可能需要处理 (replace)
# 2. 大小写统一 (lower)
# 3. 字典转元组列表进行排序: sorted(dict.items(), key=lambda x: x[1], reverse=True)
# ---------------------------------------------------------
print("\n--- 挑战题 ---")
text = "Python is good. Python is fast. I love python code."
# 在这里写代码:





# =========================================================
# ======================== 参考答案 ========================
# =========================================================

# --- 练习 1 ---
# names.append("Eve")
# names[1] = "Bobby"
# print(names[-2])
# print(names[:2])

# --- 练习 2 ---
# for stu in students:
#     if stu["score"] < 60:
#         print(f"{stu['name']} 不及格")

# --- 挑战题 ---
# 1. 清洗数据
# text = text.lower().replace(".", "")
# words = text.split()
#
# 2. 统计
# counts = {}
# for w in words:
#     counts[w] = counts.get(w, 0) + 1
#
# 3. 排序 (进阶技巧)
# # .items() 返回 [('python', 3), ('is', 2), ...]
# # key=lambda x: x[1] 表示按元组第二个元素(次数)排序
# sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
#
# print("频率最高的前3名:")
# for i in range(3):
#     if i < len(sorted_counts):
#         print(f"{sorted_counts[i][0]}: {sorted_counts[i][1]}")
