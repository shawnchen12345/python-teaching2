# Day 5 参考答案
# 可以直接运行此文件查看效果

# =========================================================
# 练习 1: 写入名字
# =========================================================
print("--- 练习 1 ---")
try:
    with open("names.txt", "w", encoding="utf-8") as f:
        f.write("Alice\nBob\nCharlie\n")
    print("写入 names.txt 成功")
except Exception as e:
    print(f"写入失败: {e}")

# =========================================================
# 练习 2: 读取统计
# =========================================================
print("\n--- 练习 2 ---")
try:
    with open("names.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(f"读取到的名字: {lines}")
        print(f"一共有 {len(lines)} 个名字")
except FileNotFoundError:
    print("names.txt 不存在，请先运行练习 1")

# =========================================================
# 练习 3: 安全的除法
# =========================================================
print("\n--- 练习 3 ---")
while True:
    try:
        a_str = input("请输入被除数 a (输入 q 退出): ")
        if a_str == 'q': break
        a = float(a_str)
        b = float(input("请输入除数 b: "))
        print(f"Result: {a / b}")
        break  # 成功后退出
    except ValueError:
        print("错误: 请输入有效的数字")
    except ZeroDivisionError:
        print("错误: 不能除以0")

# =========================================================
# 练习 4: 处理不存在的文件
# =========================================================
print("\n--- 练习 4 ---")
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("missing.txt 不存在，正在创建...")
    with open("missing.txt", "w") as f:
        f.write("现在它存在了！")
    print("已创建 missing.txt")

# =========================================================
# 挑战题: CSV 分析
# =========================================================
print("\n--- 挑战题 ---")
# 准备数据
csv_content = "item,price\napple,5\nbanana,3\norange,4"
with open("temp.csv", "w", encoding="utf-8") as f:
    f.write(csv_content)

# 读取并计算
total = 0
try:
    with open("temp.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # lines[0] 是表头，跳过
        for line in lines[1:]: 
            # line 可能是 "apple,5\n"
            parts = line.strip().split(',')
            # parts 是 ["apple", "5"]
            price = int(parts[1])
            total += price
    print(f"商品总价: {total}")
except Exception as e:
    print(f"处理CSV时出错: {e}")
