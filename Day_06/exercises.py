# Day 6 实战练习 & 答案
# 注意: 运行此脚本前需在终端运行: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------
# 练习 1: 测试请求
# 访问 "http://www.baidu.com"
# 打印状态码 (status_code) 和 网页内容的长度 (len(text))
# ---------------------------------------------------------
print("--- 练习 1 ---")
# 在这里写代码:




# ---------------------------------------------------------
# 练习 2: 解析 HTML (BeautifulSoup 练习)
# 给定一段 HTML 字符串，提取其中的链接(href)和文本
# ---------------------------------------------------------
print("\n--- 练习 2 ---")
html_doc = """
<html>
<body>
    <a href="http://example.com/1" class="link">Link 1</a>
    <a href="http://example.com/2" class="link">Link 2</a>
</body>
</html>
"""
# 在这里写代码:




# ---------------------------------------------------------
# [挑战题] 简易爬虫
# 爬取 http://books.toscrape.com/ (一个专门供爬虫练习的网站)
# 获取首页所有书名 (h3 -> a -> title属性)
# ---------------------------------------------------------
print("\n--- 挑战题 ---")
# 在这里写代码:





# =========================================================
# ======================== 参考答案 ========================
# =========================================================

# --- 练习 1 ---
# url = "http://www.baidu.com"
# resp = requests.get(url)
# print(f"Status: {resp.status_code}")
# print(f"Length: {len(resp.text)}")

# --- 练习 2 ---
# soup = BeautifulSoup(html_doc, "html.parser")
# links = soup.find_all("a")
# for link in links:
#     print(f"Text: {link.text}, URL: {link['href']}")

# --- 挑战题 ---
# url = "http://books.toscrape.com/"
# resp = requests.get(url)
# soup = BeautifulSoup(resp.text, "html.parser")
# 
# # 找到所有 article class="product_pod"
# articles = soup.find_all("article", class_="product_pod")
# 
# print(f"找到 {len(articles)} 本书:")
# for article in articles:
#     title = article.h3.a["title"] # 获取属性
#     print(title)
