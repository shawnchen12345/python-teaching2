# Day 3 演示脚本 - Python 函数入门
# 本脚本与 lecture.md 内容完全对应，供教师边讲边演示

print("=" * 60)
print("Day 3: Python 函数入门 - 演示脚本")
print("=" * 60)

# ===========================================================
# 第一章：为什么需要函数？
# ===========================================================

print("\n" + "=" * 60)
print("第一章：为什么需要函数？")
print("=" * 60)

# --- 1.1 没有函数的世界 ---
print("\n--- 1.1 没有函数的重复代码 ---")

print("你好，小明！")
print("欢迎来到Python世界！")
print("祝你学习愉快！")
print()
print("你好，小红！")
print("欢迎来到Python世界！")
print("祝你学习愉快！")
print()
print("你好，小刚！")
print("欢迎来到Python世界！")
print("祝你学习愉快！")

# 讲解: 如果有100个人？要改一句话要改几处？

# --- 1.3 第一个函数 ---
print("\n--- 1.3 定义第一个函数 ---")

def say_hello():
    print("你好！")
    print("欢迎学习Python！")

# 讲解: 定义函数时不会执行，只是"教会"Python

# --- 1.4 定义 vs 调用 ---
print("\n--- 1.4 调用函数 ---")

say_hello()
say_hello()
say_hello()

# 讲解: 调用3次，执行3次

# 演示: 用函数解决重复问题
print("\n--- 用函数消除重复 ---")

def welcome(name):
    print(f"你好，{name}！")
    print("欢迎来到Python世界！")
    print("祝你学习愉快！")
    print()

welcome("小明")
welcome("小红")
welcome("小刚")


# ===========================================================
# 第二章：参数 - 让函数更灵活
# ===========================================================

print("\n" + "=" * 60)
print("第二章：参数 - 让函数更灵活")
print("=" * 60)

# --- 2.1 单个参数 ---
print("\n--- 2.1 单个参数 ---")

def greet(name):
    print(f"你好，{name}！")

greet("小明")
greet("Alice")

# --- 2.2 多个参数 ---
print("\n--- 2.2 多个参数 ---")

def introduce(name, age):
    print(f"我叫{name}，今年{age}岁")

introduce("小红", 16)
# introduce(16, "小红")  # 顺序错了会出问题！

# --- 2.3 关键字参数 ---
print("\n--- 2.3 关键字参数 ---")

introduce(age=16, name="小红")  # 顺序可以变

# --- 2.4 默认参数 ---
print("\n--- 2.4 默认参数 ---")

def power(base, exp=2):
    print(f"{base}的{exp}次方 = {base ** exp}")

power(5)       # 使用默认值 exp=2
power(5, 3)    # 覆盖默认值

# --- 2.5 类型提示 (选讲) ---
print("\n--- 2.5 类型提示 (选讲) ---")

def add_typed(a: int, b: int) -> int:
    return a + b

print(add_typed(3, 5))


# ===========================================================
# 第三章：返回值 - 让函数"交作业"
# ===========================================================

print("\n" + "=" * 60)
print("第三章：返回值 - 让函数交作业")
print("=" * 60)

# --- 3.1 print vs return ---
print("\n--- 3.1 print vs return ---")

def add_print(a, b):
    print(a + b)  # 只打印，不返回

def add_return(a, b):
    return a + b  # 返回结果

result1 = add_print(3, 5)
print(f"add_print返回值: {result1}")  # None

result2 = add_return(3, 5)
print(f"add_return返回值: {result2}")  # 8
print(f"result2 * 2 = {result2 * 2}")  # 可以继续计算

# --- 3.2 返回值的用途 ---
print("\n--- 3.2 返回值的用途 ---")

def double(x):
    return x * 2

# 赋值给变量
result = double(5)
print(f"double(5) = {result}")

# 参与计算
print(f"double(3) + 10 = {double(3) + 10}")

# 作为其他函数的参数
print(f"double(double(2)) = {double(double(2))}")

# --- 3.3 多个返回值 ---
print("\n--- 3.3 多个返回值 ---")

def get_user():
    return "Alice", 18

name, age = get_user()
print(f"姓名: {name}, 年龄: {age}")

# 本质是返回元组
result = get_user()
print(f"返回值类型: {type(result)}")

# --- 3.4 return 结束函数 ---
print("\n--- 3.4 return 结束函数 ---")

def check(x):
    if x > 0:
        return "正数"
    return "非正数"

print(check(5))
print(check(-3))


# ===========================================================
# 第四章：变量作用域
# ===========================================================

print("\n" + "=" * 60)
print("第四章：变量作用域")
print("=" * 60)

# --- 4.1 局部变量 vs 全局变量 ---
print("\n--- 4.1 局部变量 vs 全局变量 ---")

x_global = 100  # 全局变量

def test_scope():
    y_local = 50  # 局部变量
    print(f"函数内: x_global={x_global}, y_local={y_local}")

test_scope()
print(f"函数外: x_global={x_global}")
# print(y_local)  # 会报错！

# --- 4.2 同名变量的遮蔽 ---
print("\n--- 4.2 同名变量的遮蔽 ---")

x = 100

def test_shadow():
    x = 50  # 这是新建的局部变量！
    print(f"函数内: x = {x}")

test_shadow()
print(f"函数外: x = {x}")  # 全局的 x 没变

# --- 4.3 global 关键字 ---
print("\n--- 4.3 global 关键字 ---")

count = 0

def add_one():
    global count
    count += 1

add_one()
add_one()
print(f"count = {count}")


# ===========================================================
# 第五章：函数进阶技巧
# ===========================================================

print("\n" + "=" * 60)
print("第五章：函数进阶技巧")
print("=" * 60)

# --- 5.1 函数调用函数 ---
print("\n--- 5.1 函数调用函数 ---")

def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

print(f"sum_of_squares(3, 4) = {sum_of_squares(3, 4)}")

# --- 5.2 文档字符串 ---
print("\n--- 5.2 文档字符串 ---")

def add_documented(a, b):
    """
    计算两个数的和
    
    参数:
        a: 第一个数
        b: 第二个数
    返回:
        两数之和
    """
    return a + b

print(add_documented(3, 5))
print(f"函数文档: {add_documented.__doc__}")

# --- 5.3 不定长参数 *args ---
print("\n--- 5.3 不定长参数 *args ---")

def sum_all(*nums):
    print(f"收到的参数: {nums}, 类型: {type(nums)}")
    total = 0
    for n in nums:
        total += n
    return total

print(f"sum_all(1, 2) = {sum_all(1, 2)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# --- 5.4 不定长关键字参数 **kwargs ---
print("\n--- 5.4 不定长关键字参数 **kwargs ---")

def show_info(**kwargs):
    print(f"收到的参数: {kwargs}, 类型: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_info(name="Alice", age=18, city="Beijing")


# ===========================================================
# 第六章：递归初探
# ===========================================================

print("\n" + "=" * 60)
print("第六章：递归初探")
print("=" * 60)

# --- 6.1 计算阶乘 ---
print("\n--- 6.1 递归计算阶乘 ---")

def factorial(n):
    print(f"  计算 factorial({n})")
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

# --- 6.3 递归 vs 循环 ---
print("\n--- 6.3 循环版阶乘 ---")

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"5! (循环版) = {factorial_loop(5)}")


# ===========================================================
# 第七章：综合实战
# ===========================================================

print("\n" + "=" * 60)
print("第七章：综合实战 - 代码重构")
print("=" * 60)

# 函数化版本的成绩单程序 (演示用固定值)
def get_scores_demo():
    """模拟获取成绩"""
    return 90, 85

def calc_stats(math, english):
    """计算统计数据"""
    total = math + english
    avg = total / 2
    return total, avg

def print_report(name, total, avg):
    """打印报告"""
    print(f"{name} 总分：{total}")
    print(f"平均分：{avg}")

# 主程序
name = "演示同学"
math, english = get_scores_demo()
total, avg = calc_stats(math, english)
print_report(name, total, avg)


# ===========================================================
# 演示结束
# ===========================================================

print("\n" + "=" * 60)
print("Day 3 演示脚本结束")
print("=" * 60)
