# ===================================================================
# OOP 第3课：继承与多态 —— 课堂练习
# ===================================================================
# 完成以下练习，巩固继承、方法重写、super()、多态、抽象类
# 答案在 solutions.py 中
# ===================================================================


# -------------------------------------------------------------------
# 练习 1: 动物王国 (基础继承)
# 定义基类 Animal：
#   属性: name, age, sound
#   方法:
#     - speak(): 打印 "{name} 说: {sound}"
#     - info(): 打印 "我是{name}, 今年{age}岁"
#
# 定义子类 Dog(Animal)：
#   额外属性: breed (品种)
#   重写 speak(): 打印 "{name}(品种:{breed}): 汪汪汪！"
#   新增 fetch(item): 打印 "{name} 捡起了 {item}"
#
# 定义子类 Cat(Animal)：
#   额外属性: indoor (是否室内猫, 默认True)
#   重写 speak(): 打印 "{name}: 喵喵~"
#   新增 scratch(): 打印 "{name} 在磨爪子"
#
# 定义子类 Parrot(Animal)：
#   额外属性: vocabulary (已学单词列表)
#   重写 speak(): 打印 "{name}: " + 随机一个已学单词
#   新增 learn(word): 学习新单词
#
# 创建各类动物，放入列表，用循环调用 speak()
# -------------------------------------------------------------------
print("=== 练习 1: 动物王国 ===")
# 在这里写代码:




# -------------------------------------------------------------------
# 练习 2: 员工薪资系统 (方法重写 + super)
# 基类 Employee：
#   属性: name, base_salary
#   方法:
#     - calculate_pay(): 返回 base_salary
#     - __str__(): 返回 "{name} - 月薪: ¥{calculate_pay()}"
#
# 子类 SalaryEmployee(Employee)：（月薪制）
#   完全继承 calculate_pay()
#
# 子类 HourlyEmployee(Employee)：（时薪制）
#   额外属性: hours_worked, hourly_rate
#   重写 calculate_pay(): 返回 hours_worked * hourly_rate
#
# 子类 CommissionEmployee(Employee)：（底薪+提成）
#   额外属性: sales_amount, commission_rate (提成比例)
#   重写 calculate_pay(): 返回 base_salary + sales_amount * commission_rate
#
# 子类 Manager(SalaryEmployee)：（经理=月薪+管理奖金）
#   额外属性: bonus
#   重写 calculate_pay(): 用 super() 获取基础工资 + bonus
#
# 创建不同类型的员工，计算工资总额
# -------------------------------------------------------------------
print("\n=== 练习 2: 员工薪资系统 ===")
# 在这里写代码:




# -------------------------------------------------------------------
# 练习 3: 图形面积计算器 (抽象类 + 多态)
# 用 abc 模块定义抽象基类 Shape：
#   抽象方法: area(), perimeter()
#   普通方法: describe() 返回 "{类名}: 面积={area()}, 周长={perimeter()}"
#   魔术方法: __lt__() 按面积比较大小
#
# 实现子类:
#   - Rectangle(width, height)
#   - Square(side)  ← 继承自 Rectangle！
#   - Circle(radius)
#   - Triangle(a, b, c)  ← 三条边长度, 用海伦公式算面积
#     海伦公式: s = (a+b+c)/2, 面积 = sqrt(s*(s-a)*(s-b)*(s-c))
#
# 创建多个图形，按面积排序，打印信息
# -------------------------------------------------------------------
print("\n=== 练习 3: 图形面积计算器 ===")
# 在这里写代码:




# -------------------------------------------------------------------
# 练习 4: 交通工具模拟器 (多层继承)
# 基类 Vehicle：
#   属性: name, max_speed, current_speed=0
#   方法:
#     - accelerate(amount): 加速(不超过max_speed)
#     - brake(amount): 减速(不低于0)
#     - __str__(): "{name}: {current_speed}/{max_speed} km/h"
#
# 子类 Car(Vehicle)：
#   额外属性: fuel(油量, 默认100)
#   重写 accelerate: 调用super加速，但每加速10km/h消耗5格油
#     如果没油了，打印 "没油了！" 并不加速
#
# 子类 ElectricCar(Car)：
#   额外属性: battery(电量, 默认100)
#   重写 accelerate: 用电池代替燃油 (每10km/h消耗3格电)
#   新增 charge(): 充电到100
#
# 子类 Bicycle(Vehicle)：
#   额外属性: rider_stamina(骑手体力, 默认100)
#   重写 accelerate: 每10km/h消耗10点体力
#   方法 rest(): 恢复50体力
#
# 创建不同交通工具，模拟一段旅程
# -------------------------------------------------------------------
print("\n=== 练习 4: 交通工具模拟器 ===")
# 在这里写代码:




# -------------------------------------------------------------------
# [挑战题] 练习 5: RPG 战斗系统
# 抽象基类 Character(ABC)：
#   属性: name, hp, max_hp, attack_power, defense, is_alive
#   抽象方法: special_skill(target) (特殊技能)
#   普通方法:
#     - attack(target): 普通攻击，伤害 = max(1, 攻击力 - 对方防御)
#     - take_damage(damage): 受伤（HP不低于0），HP=0时死亡
#     - __str__(): "{name} [HP: {hp}/{max_hp}]"
#
# 子类 Warrior(Character)：（战士）
#   special_skill: "猛击" = 1.5倍攻击力，无视防御
#
# 子类 Mage(Character)：（法师）
#   额外属性: mana(法力, 默认50)
#   special_skill: "火球术" = 消耗20法力，造成 attack_power * 2 伤害
#     如果法力不足，打印提示
#
# 子类 Healer(Character)：（治疗师）
#   special_skill: "治疗" = 恢复自己 30 HP（不超过max_hp）
#
# 创建角色，进行一场回合制战斗模拟
# -------------------------------------------------------------------
print("\n=== 挑战题: RPG 战斗系统 ===")
# 在这里写代码:

