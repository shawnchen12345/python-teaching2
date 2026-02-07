# Day 3 参考答案
# 可以直接运行此文件查看效果

# =========================================================
# 练习 1: 列表基础
# =========================================================
print("--- 练习 1 ---")
foods = ["Pizza", "Burger", "Coke"]
print(f"原列表: {foods}")

foods.append("Sushi")
print(f"添加后: {foods}")

del foods[0]
print(f"删除后: {foods}")

# =========================================================
# 练习 2: 列表切片与统计
# =========================================================
print("\n--- 练习 2 ---")
scores = [85, 92, 78, 65, 99, 50, 88, 72]

# 不修改原列表进行排序
sorted_scores = sorted(scores, reverse=True)
print(f"最高分前三: {sorted_scores[:3]}")

avg = sum(scores) / len(scores)
print(f"平均分: {avg}")

# =========================================================
# 练习 3: 字典查询
# =========================================================
print("\n--- 练习 3 ---")
phone_book = {"Alice": "123", "Bob": "456", "Charlie": "789"}
name = input("查谁的电话(Alice/Bob/Charlie): ")
print(phone_book.get(name, "查无此人"))

# =========================================================
# 练习 4: 单词计数
# =========================================================
print("\n--- 练习 4 ---")
sentence = "apple banana apple orange banana apple"
words = sentence.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(f"统计结果: {counts}")

# =========================================================
# 挑战题: 列表去重并排序
# =========================================================
print("\n--- 挑战题 ---")
nums = [3, 1, 2, 3, 4, 1, 5, 2]
unique_nums = list(set(nums))
unique_nums.sort()
print(f"结果: {unique_nums}")
