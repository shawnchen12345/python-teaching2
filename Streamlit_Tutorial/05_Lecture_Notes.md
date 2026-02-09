# Streamlit 详细讲稿 (第二至四阶段)

这份文档是为了配合代码演示使用的详细讲解脚本。

---

## 第二阶段：布局与状态 (Layouts & State)
**对应文件**: `02_layout_and_state.py`

### 1. 页面布局 (Layouts)
**引入**:
> "大家写的第一个 App 是不是所有东西都从上往下排？如果你想左边放图片，右边放文字怎么办？Streamlit 提供了几种极其简单的布局方式。"

**核心组件**:
*   **Sidebar (侧边栏)**:
    *   *概念*: 这里的控件永远在大纲视图的位置，不会随着主页面滚动而消失。通常用来放“全局设置”或“导航”。
    *   *代码*: `st.sidebar.title(...)`, `st.sidebar.button(...)`。
*   **Columns (多列)**:
    *   *概念*: 把横向空间切分成几份。
    *   *代码*: `col1, col2 = st.columns(2)`。
    *   *用法*: 使用 `with col1:` 来把内容塞进第一列。
*   **Tabs (选项卡)**:
    *   *概念*: 类似于浏览器的标签页，在有限的空间展示更多的内容。
    *   *代码*: `tab1, tab2 = st.tabs(["A", "B"])`。

### 2. 会话状态 (Session State) —— **本课最难点**
**引入**:
> "现在的 App 有个大问题：它是金鱼记忆。每次你点任何按钮，Streamlit 都会**从头到尾重新运行一遍代码**。这意味着所有变量都会被重置。"

**演示**:
1.  创建一个普通变量 `count = 0`。
2.  写一个按钮，点击让 `count += 1`。
3.  打印 `count`。
4.  **现象**: 无论怎么点，`count` 永远是 1。
5.  **原因**: 每次点击 -> 脚本重跑 -> `count` 又变回 0 -> 加 1 -> 显示 1。

**解决方案**: `st.session_state`
> "把它想象成一个**只要不关浏览器就永远存在的全局字典**。"

**三步走口诀**:
1.  **检查**: "这个变量在字典里吗？" (`if 'key' not in st.session_state:`)
2.  **初始化**: "不在的话，给个初始值。" (`st.session_state.key = 0`)
3.  **使用**: "之后就用 `st.session_state.key` 来读写。"

---

## 第三阶段：数据可视化 (Data Visualization)
**对应文件**: `03_data_display.py`

**引入**:
> "Python 最强大的地方之一就是处理数据。Streamlit 让你可以用一行代码把枯燥的数据变成图表。"

### 1. 表格展示
*   `st.dataframe()`: 它是**活的**。你可以排序、拉伸列宽、甚至搜索。适合展示详细数据。
*   `st.table()`: 它是**死的** (静态 HTML)。适合展示少量、固定的汇总数据。

### 2. 绘制图表
*   **数据源**: 通常是 `pandas.DataFrame`。如果你还没学 pandas，普通的字典列表也可以，但推荐 DataFrame。
*   **常用图**:
    *   `st.line_chart(df)`: 折线图 (趋势)。
    *   `st.bar_chart(df)`: 柱状图 (对比)。
    *   `st.area_chart(df)`: 面积图。

### 3. 交互式图表 (Streamlit 的杀手锏)
**演示思路**:
1.  先画一个静态图。
2.  在上面加一个 `slider` (滑块)。
3.  在代码逻辑里，根据滑块的值**过滤数据**。
4.  把过滤后的数据传给图表。
> "看，因为 Streamlit 每次都重跑代码，所以当你拖动滑块，数据会被重新过滤，图表就会自动更新！不需要写任何回调函数。"

---

## 第四阶段：实战项目 - 任务管理器 (Task Manager)
**对应文件**: `04_project_template.py` (填空版) -> `solutions/final_project_completed.py` (完成版)

### 项目结构分析
在这个项目中，我们要把之前学的所有东西串起来：
1.  **Input**: 输入框 (添加任务)。
2.  **State**: 列表 (存储所有任务)。
3.  **Layout**: 侧边栏 (添加) + 主区域 (显示)。
4.  **Output**: 循环生成 Checkbox (显示任务状态)。

### 核心逻辑讲解

#### 1. 数据结构设计
我们需要一个列表来存任务，每个任务不能只是一个字符串，因为还得记录“是否完成”和“优先级”。
```python
task = {
    'name': '买牛奶',
    'priority': '高',
    'done': False
}
```

#### 2. 添加任务 (Create)
*   **位置**: 侧边栏 `st.sidebar`。
*   **动作**: 点击按钮 -> 构建字典 -> `st.session_state.tasks.append(new_task)` -> `st.rerun()`。
*   *注意*: `st.rerun()` 用来强制刷新页面，立刻看到新任务出现在列表中。

#### 3. 显示与更新 (Read & Update)
*   **难点**: 怎么根据列表生成一堆 Checkbox？
*   **方法**: 使用 `for` 循环。
```python
for i, task in enumerate(st.session_state.tasks):
    # 使用 enumerate 是为了获取索引 i，方便定位修改哪一个任务
    col1, col2 = st.columns(...)
    with col1:
        # key 必须唯一！所以用 f"task_{i}"
        is_done = st.checkbox(..., key=f"task_{i}") 
        # 实时更新状态
        task['done'] = is_done
```

#### 4. 删除 (Delete)
*   **思路**: 我们很难直接删除“被勾选的索引”，因为删了一个，后面的索引会变。
*   **更聪明的方法**: "列表推导式" (List Comprehension)。
    *   "我只想要那些**没完成**的任务。"
    ```python
    st.session_state.tasks = [t for t in st.session_state.tasks if not t['done']]
    ```
    *   把这个新列表赋值回去，旧的（已完成的）就被“清洗”掉了。
