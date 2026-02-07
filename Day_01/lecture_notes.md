# Day 1: 极速入门与流程控制 (详细讲义)

**课程时长**: 4-5 小时
**教学目标**: 从零开始，让学生理解程序是如何按顺序、分支、循环执行的，并在结束时能够编写较为复杂的逻辑游戏。

---

## 第一部分：环境搭建与 Python 初体验 (0.5 小时)

### 1.1 Python 是什么？
*   **解释型语言**: 不像 C/C++ 需要编译成 .exe 才能跑，Python 是一行一行读懂并执行的。
*   **胶水语言**: 可以轻松调用 C、Java 写的库（比如 AI 框架 PyTorch 底层就是 C++）。
*   **哲学**: "Life is short, use Python." (简洁、优美)。

### 1.2 开发环境 (IDE)
*   **VSCode 配置**: 
    1.  安装 Python 扩展 (Microsoft 出品)。
    2.  选择解释器 (Ctrl+Shift+P -> Select Interpreter)。
    3.  运行按钮 (右上角的 Play 键) vs 终端命令 (`python xxx.py`)。即使有三角形按钮，也要学会用终端！

### 1.3 Hello World 与 IPO 模型
所有程序都遵循 **IPO** 模型：
*   **I**nput (输入)
*   **P**rocess (处理)
*   **O**utput (输出)

```python
# Output
print("Hello World")
print("Line 1", "Line 2", sep=" | ", end="\n\n") # 进阶：分隔符与结尾符

# Input (永远是字符串！)
name = input("请输入你的名字: ")
print("你好", name)
```

**常见坑**:
*   `input` 输入数字 "10"，它其实是字符串 "10"，不能直接做加法，会报错或变成拼接 "1010"。

---

## 第二部分：变量与基本运算 (1 小时)

### 2.1 变量 (Variables)
变量是内存中的标签。
*   **动态类型**: 不需要像 Java 那样写 `int a = 10`，直接 `a = 10`。
*   **命名规范 (蛇形命名法)**:
    *   ✅ `user_name`, `student_score`, `max_value` (全小写，下划线连接)
    *   ❌ `userName` (驼峰，JS/Java习惯), `a`, `b` (无意义), `1name` (数字开头), `class` (关键字)

### 2.2 数据类型
我们可以用 `type()` 查看类型。
1.  **Integer (int)**: 整数。Python 的整数没有大小限制（只要内存够，几万位的数也能存）。
2.  **Float (float)**: 浮点数。 `0.1 + 0.2 != 0.3` (精度问题，了解即可)。
3.  **String (str)**: 字符串。
4.  **Boolean (bool)**: 逻辑真假 (`True`, `False`)。

### 2.3 类型转换 (Casting)
强制转换是新手的必修课。
```python
age = input("Age: ") # 假设输入 "18"
# print(age + 1) # 报错！ str + int
real_age = int(age) # 转成整数 18
print(real_age + 1) # 19
```

### 2.4 f-string (格式化字符串) —— Python 的杀手级特性
以前我们用 `%` 或 `.format()`，现在只用 f-string。
```python
name = "Tony"
salary = 9999.5678
# {} 里可以放变量，也可以放表达式
print(f"{name} 的工资是 {salary:.2f}") # .2f 保留两位小数
print(f"1 + 1 = {1 + 1}")
```

---

## 第三部分：逻辑判断 (1 小时)

### 3.1 布尔表达式
计算机只认识真 (`True`) 和 假 (`False`)。
*   **比较**: `==` (相等), `!=` (不等), `>`, `<`, `>=`, `<=`
*   **逻辑**: `and` (并且), `or` (或者), `not` (取反)

**练习**:
```python
age = 20
score = 85
# 既要是成年人，分数又要及格
is_qualified = (age >= 18) and (score >= 60) # True
```

### 3.2 if-elif-else 结构
注意缩进！Python 强制缩进（Tab 或 4个空格）。
```python
money = 100
if money >= 500:
    print("吃大餐")
elif money >= 100:
    print("吃快餐")
else:
    print("吃土")
```

**常见错误**: `if score = 100:` (赋值) 应该是 `if score == 100:` (比较)。

---

## 第四部分：循环与控制 (1.5 小时)

### 4.1 While 循环 (死循环的恐惧与利用)
只要条件成立，就一直做。
**场景**: 游戏主循环、监听用户输入。
```python
count = 0
while count < 3:
    print(f"Loop {count}")
    count += 1 # 别忘了这一步！否则死循环
```

### 4.2 For 循环 (遍历的艺术)
**场景**: 只要是“数数”或者“一个个过”，就用 for。
`range(start, stop, step)`: **包头不包尾**。
*   `range(5)` -> 0, 1, 2, 3, 4
*   `range(1, 4)` -> 1, 2, 3
*   `range(10, 0, -1)` -> 10, 9, ... 1

### 4.3 Break 与 Continue
*   `break`: 掀桌子不玩了，直接跳出整个循环。
*   `continue`: 如同“跳过”按钮，跳过本次剩下的代码，直接开始下一轮。

**图解案例**: 
```python
# 寻找 1-100 里的第一个 7 的倍数
for i in range(1, 101):
    if i % 7 == 0:
        print(i)
        break # 找到第一个就够了，打印 7 然后结束
```

---

## 第五部分：实战 Debug 技巧 (0.5 小时)

### 5.1 为什么程序会报错？
*   **SyntaxError**: 语法错误（比如少写了冒号，括号没闭合）。IDE 会标红。
*   **RuntimeError / Exception**: 运行一半崩了（比如除以0，变量没定义）。
*   **Logic Error（最难）**: 程序跑通了，但结果不对。

### 5.2 调试方法
1.  **Print 大法**: 在关键位置打印变量 `print(f"Debug: x={x}")`。
2.  **IDE 断点调试**: 
    *   在行号左边点红点。
    *   F5 启动调试。
    *   F10 (Step Over): 单步执行。
    *   F11 (Step Into): 进入函数内部。
    *   观察左侧 "Variables" 面板，看着变量变来变去，逻辑瞬间清晰。
