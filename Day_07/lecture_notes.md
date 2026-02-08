# Day 7: 数据可视化与结课 (详细讲义)

**课程时长**: 4-5 小时
**教学目标**: 让数据“说话”。学习如何将枯燥的 CSV 数据转化为直观、美观的图表，并总结整个课程的学习路径。

---

## 第一部分：Matplotlib 基础 (1 小时)

### 1.1 什么是 Matplotlib?
Python 绘图届的元老。虽然现在有 Seaborn/Plotly 等更高级库，但它们底层都是 Matplotlib。

### 1.2 画布与基本绘图
```python
import matplotlib.pyplot as plt

# 解决中文乱码 (Windows)
plt.rcParams['font.sans-serif'] = ['SimHei'] 

plt.figure(figsize=(10, 6)) # 设定画布大小 (宽, 高)
plt.plot([1, 2, 3], [4, 5, 6], label="上升趋势", color="red", linestyle="--")

plt.title("我的第一张图")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.legend() # 显示图例
plt.grid(True) # 显示网格
plt.show()
```

---

## 第二部分：常用图表类型 (1 小时)

### 2.1 柱状图 (Bar Chart) - 比较大小
*   场景: 各科成绩比较、电影票房排名。
*   `plt.bar(keys, values)`
*   **技巧**: 给柱子上方添加数值标签 (plt.text)。

### 2.2 饼图 (Pie Chart) - 占比
*   场景: 预算分配、男女比例。
*   `plt.pie(sizes, labels=labels, autopct='%1.1f%%')`
*   **注意**: 饼图不宜分类过多，超过5-7个就很乱了。

### 2.3 散点图 (Scatter Plot) - 找规律
*   场景: 身高与体重的关系（正相关）。
*   `plt.scatter(x, y, alpha=0.5)` (alpha是透明度，点多了能看出密度)。

---

## 第三部分：综合项目 (1.5 小时)
**任务**: 加载 Day 6 生成的 `douban_top50.csv` 并进行分析。

### 3.1 数据加载 (简单版)
虽然数据分析一般用 Pandas，但为了巩固基础，我们先用 CSV 模块加载。
```python
import csv
movies = []
with open("../Day_06/douban_top50.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader) # 跳过表头
    for row in reader:
        # row: ['1', '肖申克', '9.7', '100000']
        movies.append({"title": row[1], "score": float(row[2])})
```

### 3.2 绘图任务
1.  **评分分布直方图**: 统计 8.0-8.5, 8.5-9.0, 9.0-9.5, 9.5+ 各区间的电影数量。
2.  **Top 10 评分榜**: 取前10名绘制横向柱状图 (`plt.barh`)。

---

## 第四部分：课程总结与未来路线 (0.5 小时)

### 4.1 我们学到了什么？
*   **语法**: 变量、循环、函数、类。
*   **工具**: 爬虫(requests)、数据处理(json/csv)、可视化(matplotlib)。
*   **思维**: 无论多复杂的问题，都是 IPO (输入-处理-输出) 的组合。

### 4.2 下一步学什么？ (学习路线图)
*   **方向 A: Web 开发 (做网站/小程序)**
    *   学习框架: **Flask** (简单) -> **Django** (全能)。
    *   补充: HTML/CSS/JS (前端基础), SQL (数据库)。
*   **方向 B: 数据科学与 AI (最火)**
    *   工具库: **Pandas** (Excel杀手), **Numpy** (数学计算)。
    *   进阶: PyTorch / TensorFlow (深度学习)。
*   **方向 C: 办公自动化 / 脚本**
    *   深入 `openpyxl` (操作Excel), `selenium` (浏览器自动化)。

### 4.3 最后的建议
**"做项目，不要只是看书。"**
找一个你想解决的实际问题（比如自动抢票、自动记账、分析偶像微博），去搜、去写、去补漏。这才是编程最快的学习方式。

Happy Coding!
