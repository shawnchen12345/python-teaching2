# Day 2 家庭作业 (Homework)

#完成以下 3 道题目，并将代码保存在此文件中。

# ---------------------------------------------------------
# 作业 1: 列表大洗牌
# ---------------------------------------------------------
# 题目:
# 有一个包含 1-10 的列表: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 请写代码完成以下操作（不要直接重新定义列表）:
# 1. 将列表中的 5 修改为 55
# 2. 删除列表中的 1
# 3. 将列表中的偶数全部取出来，放入一个新的列表 evens 中
# 4. 打印修改后的 nums 和新的 evens 列表

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 在这里写代码:
nums[4]=55
nums.remove(1)
evens=[]
for x in nums:
    if x%2==0:
        evens.append(x)
print(nums)
print(evens)



print("-" * 30)

# ---------------------------------------------------------
# 作业 2: 超市购物小票 (综合数据结构)
# ---------------------------------------------------------
# 题目:
# 有一个复杂的购物车列表 cart，内部包含多个商品信息。
# 每个商品是一个字典，包含:
# - name: 商品名 (String)
# - price: 单价 (Float)
# - amount: 数量 (Int)
# - tags: 标签集合 (Set) - 如 {"food", "sweet", "import"}
#
# cart = [
#     {"name": "Apple", "price": 5.0, "amount": 3, "tags": {"food", "fresh"}},
#     {"name": "Cola", "price": 3.5, "amount": 2, "tags": {"drink", "sugar"}},
#     {"name": "Milk", "price": 12.0, "amount": 1, "tags": {"drink", "fresh"}}
# ]
#
# 请完成以下任务:
# 1. 计算所有商品的总价 (Total Cost)
# 2. 找出所有属于 "fresh" (生鲜) 标签的商品，打印它们的名字
# 3. (挑战) 如果有优惠券 coupon = ("sugar", 0.9)，
#    意思是所有包含 "sugar" 标签的商品打 9 折。
#    请计算打折后的总价。

cart = [
    {"name": "Apple", "price": 5.0, "amount": 3, "tags": {"food", "fresh"}},
    {"name": "Cola", "price": 3.5, "amount": 2, "tags": {"drink", "sugar"}},
    {"name": "Milk", "price": 12.0, "amount": 1, "tags": {"drink", "fresh"}}
]
coupon = ("sugar", 0.9) # 标签为 sugar 的商品打 9 折

# 在这里写代码:
b=0
b1=0
c=[]
for a in cart:

    per_re=a['price']*a['amount']
    b+=per_re
    if a['tags']&{'fresh'}=={'fresh'}:
       c.append(a['name'])
       b1+=per_re
    else:
       b1+=per_re*0.9 

          
print(b)
print(*c, sep=',' )
print(b1)




print("-" * 30)

# ---------------------------------------------------------
# 作业 3: 字符串魔法
# ---------------------------------------------------------
# 题目:
# 用户输入一行英文句子 (例如: "Hello World Python is Great")
# 1. 算出这句子里有多少个单词
# 2. 将句子里的 "Python" 替换为 "Coding"
# 3. 将所有字母变成大写打印出来

sentence = "Hello World Python is Great" # 你可以用 input() 替换这行
# 在这里写代码:
word=sentence.split()
n=0
print(len(word))
word[2]='Coding'
print(*word)
word=str(word)
print(word.upper())


print("-" * 30)

# =========================================================
# ======================== 参考答案 ========================
# =========================================================

# --- 作业 1: 列表大洗牌 ---
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# # 1. 修改 5 -> 55 (索引是4)
# nums[4] = 55
# 
# # 2. 删除 1 (值删除)
# if 1 in nums:
#     nums.remove(1)
# 
# # 3. 提取偶数
# evens = []
# for n in nums:
#     if n % 2 == 0:
#         evens.append(n)
# 
# # 或者用列表推导式: evens = [n for n in nums if n % 2 == 0]
# 
# print(f"修改后的 nums: {nums}")
# print(f"新的 evens: {evens}")


# --- 作业 2: 超市购物小票 ---
# total_cost = 0
# for item in cart:
#     total_cost += item["price"] * item["amount"]
# print(f"1. 商品总价: {total_cost}")
# 
# print("2. 生鲜商品 (fresh):")
# for item in cart:
#     if "fresh" in item["tags"]:
#         print(f"   - {item['name']}")
# 
# # 3. (挑战) 优惠券
# discount_tag, discount_rate = coupon
# final_cost = 0
# for item in cart:
#     cost = item["price"] * item["amount"]
#     if discount_tag in item["tags"]:
#         cost *= discount_rate  # 打折
#     final_cost += cost
# print(f"3. 打折后总价: {final_cost}")


# --- 作业 3: 字符串魔法 ---
# sentence = input("请输入句子: ")
# # 1. 单词数量
# words = sentence.split()
# print(f"单词数量: {len(words)}")
# 
# # 2. 替换
# new_sentence = sentence.replace("Python", "Coding")
# print(f"替换后: {new_sentence}")
# 
# # 3. 全大写
# print(f"全大写: {sentence.upper()}")
