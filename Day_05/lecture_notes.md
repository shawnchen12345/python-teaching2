# Day 5: 文件操作与自动化脚本 (详细讲义)

**课程时长**: 4-5 小时
**教学目标**: 将 Python 应用于真实的文件系统。学会处理各种格式的文件 (txt, csv, json)，并编写实用的自动化脚本来提高效率。

---

## 第一部分：文件读写基础 (1 小时)

### 1.1 路径的学问
*   **绝对路径**: `C:\Users\Tony\Desktop\file.txt` (换电脑就挂了)
*   **相对路径**: `./data/file.txt` (推荐，基于当前运行目录)
*   **Windows 的反斜杠坑**: Windows 路径用 `\`，但在 Python 字符串里这是转义符。
    *   解决: 使用原始字符串 `r"C:\New_folder"` 或直接用斜杠 `"C:/New_folder"`。
*   `os.path.join("folder", "file.txt")`: 最安全的路径拼接方式，跨平台通用。

### 1.2 读写文本
*   `open()` 模式: `r`(只读), `w`(覆盖写), `a`(追加), `rb/wb`(二进制，读写图片视频)。
*   **Context Manager (with)**:
    ```python
    # 只要出了缩进，文件自动关闭，哪怕报错也能关
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"Log at {datetime.now()}\n")
    ```
*   **编码问题**: 永远显式指定 `encoding="utf-8"`，否则在 Windows 中文系统下默认可能是 GBK，导致乱码。

---

## 第二部分：结构化数据处理 (1.5 小时)

### 2.1 CSV (Excel 的亲戚)
*   虽然可以用 `split(",")` 手撸，但推荐用 `csv` 模块。
*   处理带逗号的内容（比如这里有一列是 "Hello, World"），`csv` 模块会自动处理引号包裹。

### 2.2 JSON (互联网通用语)
*   **序列化 (Dump)**: Python 字典/列表 -> JSON 字符串 (存文件/发网络)。
*   **反序列化 (Load)**: JSON 字符串 -> Python 对象。
*   **注意事项**: JSON key 必须是字符串，不支持 Python 的元组、集合等类型（会自动转列表）。

---

## 第三部分：文件系统管理 (os & shutil) (1 小时)

### 3.1 遍历操作
*   `os.listdir()`: 简单的列出 filenames。
*   `os.walk(path)`: **递归遍历**所有子文件夹（神器）。
    ```python
    for root, dirs, files in os.walk("."):
        for name in files:
            print(os.path.join(root, name)) # 打印所有文件的完整路径
    ```

### 3.2 搬运工 shutil
*   `shutil.copy(src, dst)`: 复制文件。
*   `shutil.move(src, dst)`: 移动/重命名。
*   `shutil.rmtree(path)`: 强力删除整个文件夹（慎用！）。

---

## 第四部分：异常处理 Exception Handling (0.5 小时)

### 4.1 为什么要捕获异常？
脚本在处理 1000 个文件，处理到第 500 个时某个文件损坏了。
*   **没有 try**: 脚本崩溃，后面 500 个没跑，前面 500 个的状态未知。
*   **有 try**: 记录并在日志里报错 "File 500 Error"，然后 `continue` 继续处理第 501 个。

### 4.2 语法
```python
try:
    process_file(f)
except FileNotFoundError:
    print("文件丢了")
except PermissionError:
    print("权限不够，跳过")
except Exception as e:
    print(f"未知错误: {e}")
```

---

## 第五部分：实战 - "桌面清理大师" (1 小时)
**任务**: 编写脚本，整理乱糟糟的 "Desktop" 文件夹。
1.  自动创建 `Images`, `Docs`, `Installers`, `Archives` 文件夹。
2.  扫描桌面所有文件。
3.  根据后缀名 (`.jpg`, `.docx`, `.exe`, `.zip` 等) 将文件移动到对应文件夹。
4.  并生成一个 `report.txt`，记录移动了多少个文件，以及哪些文件移动失败了。
