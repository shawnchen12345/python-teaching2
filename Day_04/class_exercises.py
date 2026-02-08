# Day 4 随堂练习 - 面向对象编程 (OOP)
# 本文件与 lecture.md 的"随堂练习"部分完全对应
# 请在每个 [TODO] 下方编写代码

# ===========================================================
# 随堂练习 1：定义第一个类
# 对应讲义 1.6 节
# ===========================================================

print("=" * 50)
print("随堂练习 1：定义第一个类")
print("=" * 50)

# 练习 1.1: 定义一个 Cat 类
# 要求:
# - 属性: name (名字), color (颜色)
# - 方法: meow() 打印 "{name}说：喵~"
# - 方法: info() 打印 "我是{name}，{color}的猫"

# [TODO] 在这里定义 Cat 类


# [TODO] 创建两只猫：
# cat1 = Cat("咪咪", "白色")
# cat2 = Cat("橘子", "橘色")


# [TODO] 调用它们的方法



# ===========================================================
# 随堂练习 2：属性与方法
# 对应讲义 2.4 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 2：计数器类")
print("=" * 50)

# 练习 2.1: 定义一个 Counter 类
# 要求:
# - 属性: count (初始值为 0)
# - 方法: increment() 使 count 加 1
# - 方法: decrement() 使 count 减 1
# - 方法: reset() 使 count 重置为 0
# - 方法: get_count() 返回当前 count 的值

# [TODO] 在这里定义 Counter 类


# [TODO] 测试:
# c = Counter()
# c.increment()
# c.increment()
# c.increment()
# c.decrement()
# print(f"当前计数: {c.get_count()}")  # 应该是 2
# c.reset()
# print(f"重置后: {c.get_count()}")    # 应该是 0



# ===========================================================
# 随堂练习 3：封装
# 对应讲义 3.4 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 3：封装 - 学生成绩")
print("=" * 50)

# 练习 3.1: 定义一个 Student 类（带封装）
# 要求:
# - 私有属性: __name, __score
# - __score 必须在 0-100 之间
# - 方法: get_name() 返回学生姓名
# - 方法: get_score() 返回学生成绩
# - 方法: set_score(score) 设置成绩
#   - 如果 score 不在 0-100 之间，打印"成绩必须在0-100之间"并拒绝修改
# - 方法: get_grade() 返回等级
#   - 90分以上: "A"
#   - 80-89: "B"
#   - 70-79: "C"
#   - 60-69: "D"
#   - 60以下: "F"

# [TODO] 在这里定义 Student 类


# [TODO] 测试:
# s = Student("小明", 85)
# print(f"{s.get_name()} 的成绩是 {s.get_score()}，等级 {s.get_grade()}")
# s.set_score(95)
# print(f"修改后成绩: {s.get_score()}，等级 {s.get_grade()}")
# s.set_score(150)  # 应该提示错误



# ===========================================================
# 随堂练习 4：继承
# 对应讲义 4.4 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 4：继承 - 交通工具")
print("=" * 50)

# 练习 4.1: 定义交通工具类层次
# 
# 基类 Vehicle:
#   - 属性: brand (品牌), speed (速度, 初始0)
#   - 方法: start()  打印 "{brand} 启动"
#   - 方法: stop()   打印 "{brand} 停止"，并将 speed 设为 0
#   - 方法: accelerate(amount) 加速，speed += amount
#
# 子类 Car(Vehicle):
#   - 新属性: wheels = 4
#   - 重写 start(): 打印 "{brand} 汽车启动，轰隆隆~"
#
# 子类 Motorcycle(Vehicle):
#   - 新属性: wheels = 2
#   - 重写 start(): 打印 "{brand} 摩托车启动，突突突~"

# [TODO] 在这里定义 Vehicle 类


# [TODO] 在这里定义 Car 类


# [TODO] 在这里定义 Motorcycle 类


# [TODO] 测试:
# car = Car("宝马")
# moto = Motorcycle("哈雷")
# car.start()
# moto.start()
# car.accelerate(60)
# print(f"{car.brand} 当前速度: {car.speed}")



# ===========================================================
# 随堂练习 5：多态
# 对应讲义 5.4 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 5：多态 - 员工薪资")
print("=" * 50)

# 练习 5.1: 定义员工类层次
#
# 基类 Employee:
#   - 属性: name
#   - 方法: get_salary() 返回 0
#
# 子类 FullTimeEmployee(Employee): 全职员工
#   - 新属性: monthly_salary (月薪)
#   - 重写 get_salary(): 返回月薪
#
# 子类 PartTimeEmployee(Employee): 兼职员工
#   - 新属性: hourly_rate (时薪), hours (工时)
#   - 重写 get_salary(): 返回 时薪 × 工时

# [TODO] 在这里定义 Employee 类


# [TODO] 在这里定义 FullTimeEmployee 类


# [TODO] 在这里定义 PartTimeEmployee 类


# [TODO] 定义函数 total_salary(employees) 计算总薪资
# def total_salary(employees):
#     pass


# [TODO] 测试:
# employees = [
#     FullTimeEmployee("张三", 8000),
#     FullTimeEmployee("李四", 10000),
#     PartTimeEmployee("王五", 50, 80),  # 时薪50，工作80小时
# ]
# print(f"总薪资: ¥{total_salary(employees)}")



# ===========================================================
# 随堂练习 6：特殊方法
# 对应讲义 6.5 节
# ===========================================================

print("\n" + "=" * 50)
print("随堂练习 6：特殊方法 - 图书类")
print("=" * 50)

# 练习 6.1: 定义一个 Book 类
# 要求:
# - 属性: title (书名), author (作者), price (价格)
# - __str__ 方法: 返回 "《书名》 - 作者 - ¥价格"
# - __eq__ 方法: 当书名和作者都相同时，返回 True
# - __lt__ 方法: 按价格比较，价格低的"小于"价格高的
#   (这样可以用 sorted() 对书籍列表按价格排序)

# [TODO] 在这里定义 Book 类


# [TODO] 测试:
# b1 = Book("Python入门", "张三", 59)
# b2 = Book("Python进阶", "李四", 79)
# b3 = Book("Python入门", "张三", 59)
# 
# print(b1)
# print(b2)
# print(f"b1 == b3? {b1 == b3}")  # 应该是 True
# print(f"b1 == b2? {b1 == b2}")  # 应该是 False
# 
# # 按价格排序
# books = [b2, b1]
# books_sorted = sorted(books)
# print("按价格排序:")
# for book in books_sorted:
#     print(f"  {book}")



# ===========================================================
# 挑战练习：迷你银行系统
# ===========================================================

print("\n" + "=" * 50)
print("挑战练习：迷你银行系统")
print("=" * 50)

# 设计一个银行账户系统:
#
# 类 Account:
#   - 属性: account_id (账号), owner (户主), __balance (余额, 私有)
#   - 方法: deposit(amount) 存款
#   - 方法: withdraw(amount) 取款 (余额不足时拒绝)
#   - 方法: get_balance() 查询余额
#   - 方法: transfer(target_account, amount) 转账给另一个账户
#
# 类 SavingsAccount(Account): 储蓄账户
#   - 新属性: interest_rate (年利率, 如 0.03 表示 3%)
#   - 新方法: add_interest() 根据利率增加利息
#
# 类 Bank:
#   - 属性: accounts (账户列表)
#   - 方法: create_account(owner, initial_deposit) 创建账户并返回
#   - 方法: find_account(account_id) 根据账号查找账户
#   - 方法: total_deposits() 返回所有账户的总余额

# [TODO] 在这里编写代码


# [TODO] 测试场景:
# bank = Bank()
# acc1 = bank.create_account("张三", 1000)
# acc2 = bank.create_account("李四", 2000)
# acc1.deposit(500)
# acc1.transfer(acc2, 300)
# print(f"张三余额: {acc1.get_balance()}")
# print(f"李四余额: {acc2.get_balance()}")
# print(f"银行总存款: {bank.total_deposits()}")



print("\n" + "=" * 50)
print("随堂练习完成！")
print("=" * 50)
