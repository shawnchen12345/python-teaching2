# Day 5 实战练习 & 答案
import json
import os

# ---------------------------------------------------------
# 练习 1: JSON 存储用户设置
# 1. 创建一个字典 user_settings = {"theme": "dark", "volume": 80}
# 2. 将其保存到 settings.json
# 3. 读取并打印出来验证
# ---------------------------------------------------------
print("--- 练习 1 ---")
# 在这里写代码:




# ---------------------------------------------------------
# 练习 2: 批量生成文件
# 在当前目录下创建一个 "test_files" 文件夹
# 在里面生成 5 个 txt 文件: "file_0.txt", "file_1.txt" ...
# 提示: os.makedirs, open
# ---------------------------------------------------------
print("\n--- 练习 2 ---")
# 在这里写代码:




# ---------------------------------------------------------
# [挑战题] 文件分类器 (核心逻辑)
# 模拟一个文件列表 filenames = ["a.jpg", "b.pdf", "c.png", "d.txt"]
# 循环遍历，根据后缀名打印应该移动到哪里:
# jpg/png -> "Move to Images"
# pdf/txt -> "Move to Docs"
# 提示: string.endswith() 或 os.path.splitext()
# ---------------------------------------------------------
print("\n--- 挑战题 ---")
filenames = ["a.jpg", "b.pdf", "c.png", "d.txt"]
# 在这里写代码:





# =========================================================
# ======================== 参考答案 ========================
# =========================================================

# --- 练习 1 ---
# settings = {"theme": "dark", "volume": 80}
# with open("settings.json", "w") as f:
#     json.dump(settings, f)
# 
# with open("settings.json", "r") as f:
#     print(json.load(f))

# --- 练习 2 ---
# folder = "test_files"
# if not os.path.exists(folder):
#     os.makedirs(folder)
# 
# for i in range(5):
#     with open(f"{folder}/file_{i}.txt", "w") as f:
#         f.write("content")
# print("文件生成完毕")

# --- 挑战题 ---
# for name in filenames:
#     ext = os.path.splitext(name)[1] # 获取 .jpg
#     if ext in ['.jpg', '.png']:
#         print(f"{name} -> Images")
#     elif ext in ['.pdf', '.txt']:
#         print(f"{name} -> Docs")
#     else:
#         print(f"{name} -> Others")
