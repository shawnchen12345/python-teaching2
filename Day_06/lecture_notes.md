# Day 6: 网络爬虫入门 (详细讲义)

**课程时长**: 4-5 小时
**教学目标**: 理解 Web 工作原理，掌握使用 Python 发送 HTTP 请求并提取数据的能力。

---

## 第一部分：Web 基础知识 (0.5 小时)

### 1.1 浏览器是怎么工作的？
*   **Client (客户端)**: 你的浏览器/爬虫脚本。
*   **Server (服务器)**: 存放网页数据的地方。
*   **Request/Response**: 有来有回。
    *   你输入 URL -> 浏览器发送 GET 请求。
    *   服务器返回 HTML 代码。
    *   浏览器解析 HTML -> 渲染成好看的网页。

### 1.2 HTTP 协议简述
*   **Method**: `GET` (查), `POST` (增/提交表单)。
*   **Header**: 请求头。最重要的伪装 `User-Agent` (告诉服务器我是 Chrome，不是 Python)。
*   **Status Code**:
    *   `200`: OK。
    *   `403`: Forbidden (反爬虫拦截)。
    *   `404`: Not Found。
    *   `500`: 服务器崩了。

---

## 第二部分：Requests 库 - 发送请求 (1 小时)

### 2.1 基本用法
```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0..." # 必须加！否则大部分网站会拦截
}
url = "https://movie.douban.com/top250"
resp = requests.get(url, headers=headers)

if resp.status_code == 200:
    print("成功获取!")
    # resp.text 是网页源码 (HTML string)
    # resp.content 是二进制 (下载图片用)
```

### 2.2 带参数请求
*   搜索 URL 通常是 `baidu.com/s?wd=python`。
*   `requests.get(..., params={"wd": "python"})`。

---

## 第三部分：HTML 解析 - 这里有金矿 (1.5 小时)

### 3.1 网页结构 (DOM 树)
HTML 是一层套一层的标签。
```html
<div class="movie-list">
    <div class="item">
        <span class="title">肖申克的救赎</span>
        <span class="rating">9.7</span>
    </div>
    ...
</div>
```

### 3.2 使用 Chrome 开发者工具 (F12)
**这是爬虫最重要的技能**。
1.  按 F12 打开工具。
2.  点击左上角的小箭头 (Inspect)。
3.  点击网页上的元素，右侧 Elements 面板会自动定位到代码位置。
4.  观察它的 `tag` 名，`class` 名，`id` 名。

### 3.3 BeautifulSoup 实战
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "html.parser")

# Find: 找一个
h1 = soup.find("h1")

# Find_all: 找所有
items = soup.find_all("div", class_="item")

for item in items:
    # 层级查找
    title = item.find("span", class_="title").text
    print(title)
```

---

## 第四部分：爬虫伦理与反爬对抗 (0.5 小时)

### 4.1 爬虫协议 (robots.txt)
访问 `site.com/robots.txt` 查看允许爬什么。
*   **法律底线**: 不爬取个人隐私，不破坏服务器运行，不通过爬虫获利（倒卖数据）。

### 4.2 常见反爬与应对
*   **IP 封锁**: 一秒请求 100 次 -> 封 IP。
    *   *应对*: `time.sleep(2)`，慢一点。使用代理 IP (高级内容)。
*   **需要登录**: Cookie。
    *   *应对*: 浏览器登录后复制 Cookie 放到 headers 里。

---

## 第五部分：实战 - 豆瓣 Top250 数据抓取 (1.5 小时)
**任务**: 抓取豆瓣 Top250 前 2 页 (50部) 电影数据。
1.  **翻页分析**: 观察 URL 规律 `start=0`, `start=25`。
2.  **数据提取**: 电影名、评分、引言(Quote)、评价人数。
3.  **持久化**: 将数据保存为 `douban_top50.csv`，方便明天做数据可视化。
    *   格式: `排名,电影名,评分,人数`
