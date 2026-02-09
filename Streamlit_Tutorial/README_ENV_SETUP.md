# 如何添加环境变量 (解决 `streamlit` 命令找不到的问题)

因为 `streamlit` 安装在了用户目录下的脚本文件夹中，而该文件夹没有被添加到系统的 PATH 环境变量中，所以终端无法识别它。

## 方法一：如果不添加环境变量 (推荐临时使用)
直接使用 `python -m` 来运行，这可以绕过环境变量问题：
```powershell
python -m streamlit run 01_hello.py
```

## 方法二：添加环境变量 (永久解决)

你需要将 **用户脚本文件夹** 路径添加到系统的 PATH 中。

### 步骤：
1.  **按 Win 键**，搜索 "编辑系统环境变量" (Edit the system environment variables) 并打开。
2.  点击右下角的 **"环境变量" (Environment Variables)** 按钮。
3.  在 **"用户变量" (User variables)** 区域（上面那栏），找到名为 **`Path`** 的变量，选中它，点击 **"编辑" (Edit)**。
4.  点击右侧的 **"新建" (New)**。
5.  输入以下路径（这是你电脑上 streamlit 的实际安装位置）：
    `C:\Users\chenx\AppData\Roaming\Python\Python314\Scripts`
6.  点击 **确定 (OK)** -> **确定** -> **确定**，关闭所有窗口。
7.  **重启 VS Code** (完全关闭再打开)，或者点击终端右上角的垃圾桶图标关闭当前终端，建立一个新的终端。

### 验证：
在新终端中输入：
```powershell
streamlit --version
```
如果显示版本号，说明设置成功！
