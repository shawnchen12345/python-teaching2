#🟦 封面页

标题：Python函数入门 —— 从不会写到能自己封装功能

讲课提示：
今天我们要学的是——Python里最重要的能力之一：写函数。
学会函数，代码才算真正“像程序”。

🟦 第1页：这节课你将学会什么

内容：

✔ 什么是函数，为什么一定要用函数
✔ 如何定义和调用函数
✔ 参数到底是干嘛的（重点）
✔ return 和 print 的区别
✔ 变量在函数里为什么会“消失”
✔ 递归是怎么回事（入门）
✔ 如何把乱代码改造成结构清晰的程序

讲课提示：
强调：函数是从“写脚本”到“写程序”的分水岭

🟦 第2页：如果没有函数会怎样？

代码：

print("欢迎 Alice")
print("今天是学习 Python 的好日子")
print("祝你学习愉快！")

print("欢迎 Bob")
print("今天是学习 Python 的好日子")
print("祝你学习愉快！")


讲课提示（互动）：

如果有 100 个人怎么办？

如果我要改一句话，要改几次？

👉 引出：代码重复、难改、难维护

🟦 第3页：函数的本质

内容：

👉 函数 = 给一段代码起名字，以后随时调用

生活类比：

遥控器按钮

洗衣机“标准模式”

外卖App“一键再来一单”

讲课提示：
函数就是把一组操作打包成一个“按钮”

🟦 第4页：第一个函数
def say_hello():
    print("你好！")


讲解要点：

部分	作用
def	定义函数
say_hello	函数名
()	参数位置
缩进代码	函数体
🟦 第5页：调用函数
say_hello()
say_hello()
say_hello()


讲课重点：
❗函数不会自动执行
❗必须“调用”才会运行

🟦 第6页：课堂练习 ①

练习：

1️⃣ 写函数 print_line() 打印

--------------------


2️⃣ 写函数 welcome() 打印三句欢迎语

讲课提示：
巡视学生，检查是否：

忘写括号

忘记缩进

🟦 第7页：函数可以接收数据（参数）
def greet(name):
    print("你好，", name)

greet("小明")
greet("Alice")


讲解：

概念	含义
形参	定义函数时的变量 name
实参	调用时传入的值 "小明"
🟦 第8页：多个参数
def introduce(name, age):
    print("我叫", name, "今年", age, "岁")

introduce("小红", 18)


重点：顺序必须一致

🟦 第9页：关键字参数
introduce(age=18, name="小红")


讲解：
✔ 顺序可以变
✔ 可读性更强

🟦 第10页：默认参数
def power(base, exponent=2):
    print(base ** exponent)

power(3)     # 平方
power(3, 3)  # 立方


规则：
👉 默认参数必须放在后面

🟦 第11页：课堂练习 ②（参数）

1️⃣ 写函数 area_rectangle(w, h) 返回面积
2️⃣ 写函数 student_info(name, grade="一年级")
3️⃣ 写函数 calc(a, b, op) 支持 + - *

🟦 第12页：print 和 return 不一样！
def add(a, b):
    print(a + b)


vs

def add(a, b):
    return a + b


讲课金句：
🖨 print 是给人看的
📦 return 是给程序用的

🟦 第13页：返回值参与运算
result = add(3, 5)
print(result * 2)


强调：
函数执行完会把 return 后的值“带回来”

🟦 第14页：多个返回值
def get_user():
    return "Alice", 18

name, age = get_user()


讲解：
本质是返回一个元组

🟦 第15页：课堂练习 ③（返回值）

1️⃣ 写函数 max_of_two(a, b) 返回较大的数
2️⃣ 写函数 circle_area(r) 返回圆面积
3️⃣ 写函数 swap(a, b) 返回交换后的两个值

🟦 第16页：变量作用域问题来了…
def test():
    x = 10

print(x)  # 报错


讲解：
函数内部的变量 = 局部变量

🟦 第17页：全局变量
x = 5

def show():
    print(x)


讲解：
函数里可以读取外面的变量（但不推荐乱改）

🟦 第18页：修改全局变量（了解）
x = 10

def change():
    global x
    x = 20


强调：⚠️ 新手阶段尽量别用

🟦 第19页：课堂练习 ④（作用域）

问：下面代码输出什么？

x = 10

def func():
    x = 5
    print(x)

func()
print(x)


答案：
函数内 5，外面还是 10

🟦 第20页：函数调用函数
def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)


讲解：
函数就像工具，可以互相配合

🟦 第21页：给函数写说明（好习惯）
def add(a, b):
    """返回两个数的和"""
    return a + b

🟦 第22页：递归是什么？

函数自己调用自己

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


强调：
✅ 必须有结束条件
❌ 否则无限循环

🟦 第23页：综合案例（重构代码）

原始代码：

name = input("姓名：")
math = int(input("数学成绩："))
english = int(input("英语成绩："))
total = math + english
avg = total / 2
print(name, "总分：", total)
print("平均分：", avg)

🟦 第24页：拆成函数版本
def input_score():
    ...

def calc_total(a, b):
    ...

def calc_avg(total):
    ...

def print_report(name, total, avg):
    ...


讲课提示：
让学生体会：结构变清晰了

🟦 第25页：课后作业

1️⃣ 判断一个数是否是素数
2️⃣ 计算圆面积（默认 π=3.14）
3️⃣ 秒数转“时:分:秒”
4️⃣ 用函数重写“猜数字游戏”

如果你需要，我可以下一步帮你把：

✅ 所有课堂练习的参考答案
或
✅ 把这套内容整理成可直接发给学生的讲义版