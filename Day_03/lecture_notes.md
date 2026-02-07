# Day 3: 函数与模块化 (详细讲义)

**课程时长**: 4-5 小时
**教学目标**: 从“写脚本”进阶到“写工程”。学会封装代码、复用代码，理解作用域，并熟悉 Python 强大的标准库。

---

## 第一部分：函数进阶 (1.5 小时)

### 1.1 为什么需要函数？ (DRY原则)
展示一段重复复制粘贴 3 次的代码，然后演示如何将其提取为函数。
**Definiton**: 函数是逻辑的黑盒。

### 1.2 参数的魔力
1.  **位置参数**: `func(1, 2)` 必须按顺序。
2.  **关键字参数**: `func(y=2, x=1)` 明确指定，顺序无关。
3.  **默认参数**: `def connect(host, port=80):`
    *   **大坑预警**: 默认参数如果是列表/字典等可变对象，会陷阱！
    *   *错误示范*: `def bad(l=[]): l.append(1)` -> 第二次调用 l 居然不是空！
    *   *正确做法*: `def good(l=None): if l is None: l = []`

### 1.3 可变参数 (*args, **kwargs)
当你不确定有多少个参数时。
```python
def sum_all(*nums): # nums 会变成一个元组 (1, 2, 3...)
    total = 0
    for n in nums:
        total += n
    return total

print(sum_all(1, 2, 3, 4))
```

### 1.4 作用域与 global
*   **LEGB 规则**: Local -> Enclosing -> Global -> Built-in
*   函数内部可以**读取**全局变量，但不能直接**修改**（赋值）它，除非声明 `global x`。

---

## 第二部分：Python 标准库 (Batteries Included) (1.5 小时)

### 2.1 random (随机)
*   `random.randint(1, 100)`
*   `random.choice(['A', 'B', 'C'])`
*   `random.shuffle(deck)`: 原地打乱牌组。

### 2.2 time & datetime (时间)
*   时间戳 (`time.time()`): 1970年1月1日到现在的秒数（计算程序耗时用）。
*   日期对象 (`datetime`):
    *   `delta = dt1 - dt2`: 时间差计算。
    *   `dt.strftime('%Y-%m-%d')`: 格式化输出 (2024-01-01)。

### 2.3 os & sys (系统相关)
*   `os.getcwd()`: 获取当前工作目录。
*   `sys.argv`: 获取命令行运行时的参数（如 `python main.py arg1`）。
*   `sys.exit()`: 退出程序。

---

## 第三部分：模块化与包 (1 小时)

### 3.1 Import 的艺术
*   `import xxx`: 使用时需写 `xxx.func()`。
*   `from xxx import func`: 直接用 `func()`（小心命名冲突）。
*   `import xxx as x`: 别名。
*   **循环导入 (Circular Import)**: A import B, B import A，会报错，架构设计要避免。

### 3.2 入口检查 (__name__)
```python
def main():
    print("Doing work...")

# 只有当该文件被直接运行时，才执行 main
# 如果被 import 到别的文件，这块不执行
if __name__ == "__main__":
    main()
```
*这是 Python 新手最容易忽视但也最重要的规范之一。*

### 3.3 安装第三方库 (pip)
*   `pip install requests`
*   **镜像源加速**: `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests`
*   **虚拟环境 (venv)** (简单介绍概念): 为什么不同的项目需要隔离的环境？防止依赖冲突。

---

## 第四部分：综合练习 - 工具箱 (1 小时)
构建一个 `MyTools` 文件夹项目结构：
```
project/
  ├── main.py
  ├── tools/
  │   ├── __init__.py (空)
  │   ├── math_tools.py (自定义加减乘除、面积计算)
  │   └── str_tools.py (生成随机验证码、反转字符串)
```
任务：在 `main.py` 中引入 `tools` 包下的模块，完成一系列任务。目的是让学生习惯多文件协作开发。
