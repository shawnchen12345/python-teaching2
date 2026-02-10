# ===================================================================
# OOP 第4课：综合实战 —— 参考答案
# ===================================================================
import random
from abc import ABC, abstractmethod
from datetime import datetime


# ===================================================================
# 练习 1: 动物工厂 (工厂模式)
# ===================================================================
print("=== 练习 1: 动物工厂 ===")


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Dog(Animal):
    def speak(self):
        return f"{self.name}: 汪汪汪！🐕"

    def move(self):
        return f"{self.name} 摇着尾巴跑过来"


class Cat(Animal):
    def speak(self):
        return f"{self.name}: 喵喵~ 🐱"

    def move(self):
        return f"{self.name} 轻盈地跳上桌子"


class Fish(Animal):
    def speak(self):
        return f"{self.name}: ...（鱼不会说话）🐟"

    def move(self):
        return f"{self.name} 在水中游来游去"


class Rabbit(Animal):
    def speak(self):
        return f"{self.name}: 吱吱！🐰"

    def move(self):
        return f"{self.name} 蹦蹦跳跳"


class AnimalFactory:
    """动物工厂"""
    _registry = {
        "dog": Dog,
        "cat": Cat,
        "fish": Fish,
    }

    @classmethod
    def create(cls, animal_type, name):
        animal_class = cls._registry.get(animal_type.lower())
        if animal_class is None:
            available = ", ".join(cls._registry.keys())
            raise ValueError(f"未知动物类型: '{animal_type}'。可用类型: {available}")
        return animal_class(name)

    @classmethod
    def register(cls, animal_type, animal_class):
        cls._registry[animal_type.lower()] = animal_class
        print(f"已注册新动物类型: {animal_type}")

    @classmethod
    def list_types(cls):
        return list(cls._registry.keys())


# 测试
print(f"可用类型: {AnimalFactory.list_types()}")

dog = AnimalFactory.create("dog", "旺财")
cat = AnimalFactory.create("cat", "咪咪")
fish = AnimalFactory.create("fish", "尼莫")

for animal in [dog, cat, fish]:
    print(f"  {animal.speak()}")
    print(f"  {animal.move()}")

# 注册新类型
AnimalFactory.register("rabbit", Rabbit)
rabbit = AnimalFactory.create("rabbit", "小白")
print(f"  {rabbit.speak()}")
print(f"  {rabbit.move()}")
print(f"更新后可用类型: {AnimalFactory.list_types()}")


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 2: 事件系统 (观察者模式)
# ===================================================================
print("=== 练习 2: 事件系统 ===")


class EventEmitter:
    """通用事件发射器"""

    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        """注册事件监听"""
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    def off(self, event, callback):
        """取消事件监听"""
        if event in self._listeners:
            self._listeners[event] = [
                cb for cb in self._listeners[event] if cb != callback
            ]

    def emit(self, event, *args, **kwargs):
        """触发事件"""
        if event in self._listeners:
            for callback in self._listeners[event]:
                callback(*args, **kwargs)


class GameCharacter:
    """使用事件系统的游戏角色"""

    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.level = 1
        self.exp = 0
        self.is_alive = True
        self.events = EventEmitter()

    def take_damage(self, damage):
        if not self.is_alive:
            return
        self.hp = max(0, self.hp - damage)
        self.events.emit("damage", self, damage)
        if self.hp <= 0:
            self.is_alive = False
            self.events.emit("death", self)

    def gain_exp(self, amount):
        self.exp += amount
        self.events.emit("exp_gain", self, amount)
        if self.exp >= self.level * 100:
            self.exp -= self.level * 100
            self.level += 1
            self.max_hp += 20
            self.hp = self.max_hp
            self.events.emit("levelup", self)

    def __str__(self):
        return f"{self.name} [Lv.{self.level} HP:{self.hp}/{self.max_hp}]"


# ---- 监听函数 ----
def ui_on_damage(character, damage):
    bar_len = 20
    ratio = character.hp / character.max_hp
    filled = int(bar_len * ratio)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"  [UI] {character.name} -{damage}HP |{bar}| {character.hp}/{character.max_hp}")


def ui_on_death(character):
    print(f"  [UI] ☠️ {character.name} 阵亡了！游戏结束！")


def ui_on_levelup(character):
    print(f"  [UI] 🎉 {character.name} 升级到 Lv.{character.level}！")


def log_event(character, *args):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"  [LOG {timestamp}] {character}")


def sfx_on_damage(character, damage):
    if damage >= 30:
        print(f"  [SFX] 💥 重击音效！")
    else:
        print(f"  [SFX] ⚔️ 普通攻击音效")


# 注册事件
hero = GameCharacter("勇者", 100)
hero.events.on("damage", ui_on_damage)
hero.events.on("damage", sfx_on_damage)
hero.events.on("damage", log_event)
hero.events.on("death", ui_on_death)
hero.events.on("levelup", ui_on_levelup)

# 测试
print("受到15点伤害:")
hero.take_damage(15)
print("受到40点伤害:")
hero.take_damage(40)
print("获得150经验:")
hero.gain_exp(150)
print(f"当前状态: {hero}")


print("\n" + "=" * 50 + "\n")


# ===================================================================
# 练习 3: 在线商城系统
# ===================================================================
print("=== 练习 3: 在线商城系统 ===")


# ---- 商品体系 ----
class Product(ABC):
    _id_counter = 0

    def __init__(self, name, price, stock=10):
        Product._id_counter += 1
        self.product_id = Product._id_counter
        self.name = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def get_discount(self):
        """子类实现各自的折扣率 (0~1)"""
        pass

    @property
    def final_price(self):
        return round(self.price * (1 - self.get_discount()), 2)

    def __str__(self):
        discount_str = ""
        if self.get_discount() > 0:
            discount_str = f" ({int(self.get_discount()*100)}%off → ¥{self.final_price:.2f})"
        return f"[{self.__class__.__name__}] {self.name} ¥{self.price:.2f}{discount_str} (库存:{self.stock})"


class Book(Product):
    def __init__(self, name, price, author, isbn, stock=10):
        super().__init__(name, price, stock)
        self.author = author
        self.isbn = isbn

    def get_discount(self):
        return 0.1  # 9 折


class Electronics(Product):
    def __init__(self, name, price, brand, warranty_years=1, stock=10):
        super().__init__(name, price, stock)
        self.brand = brand
        self.warranty_years = warranty_years

    def get_discount(self):
        return 0.05  # 95 折


class Clothing(Product):
    def __init__(self, name, price, size, material, stock=10):
        super().__init__(name, price, stock)
        self.size = size
        self.material = material

    def get_discount(self):
        return 0.2  # 8 折


# ---- 用户体系 ----
class User:
    def __init__(self, username, balance=0):
        self.username = username
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def add_funds(self, amount):
        if amount <= 0:
            print("充值金额必须大于0")
            return
        self._balance += amount
        print(f"[{self.username}] 充值 ¥{amount:.2f}，余额: ¥{self._balance:.2f}")

    def _deduct(self, amount):
        """内部扣款方法"""
        if amount > self._balance:
            return False
        self._balance -= amount
        return True

    def _refund(self, amount):
        """内部退款方法"""
        self._balance += amount

    def get_discount_rate(self):
        return 1.0  # 无额外折扣

    def __str__(self):
        return f"用户 {self.username} (余额: ¥{self._balance:.2f})"


class VIPUser(User):
    def __init__(self, username, balance=0, vip_level=1):
        super().__init__(username, balance)
        self.vip_level = min(max(vip_level, 1), 3)  # 1-3 级
        self._points = 0

    def get_discount_rate(self):
        discounts = {1: 0.95, 2: 0.90, 3: 0.85}
        return discounts.get(self.vip_level, 1.0)

    def add_points(self, amount):
        self._points += amount
        print(f"  [{self.username}] +{amount}积分 (总积分: {self._points})")

    def __str__(self):
        stars = "⭐" * self.vip_level
        return (f"VIP{self.vip_level}{stars} {self.username} "
                f"(余额: ¥{self._balance:.2f}, 积分: {self._points})")


# ---- 购物车 ----
class ShoppingCart:
    def __init__(self):
        self._items = {}  # {Product: quantity}

    def add(self, product, quantity=1):
        if product.stock < quantity:
            print(f"  ❌ {product.name} 库存不足！(库存:{product.stock})")
            return
        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity
        print(f"  ✅ 添加 {product.name} × {quantity} 到购物车")

    def remove(self, product_name):
        for product in list(self._items.keys()):
            if product.name == product_name:
                del self._items[product]
                print(f"  已移除 {product_name}")
                return
        print(f"  购物车中没有 {product_name}")

    def get_total(self, user=None):
        total = 0
        for product, qty in self._items.items():
            total += product.final_price * qty
        if user:
            total *= user.get_discount_rate()
        return round(total, 2)

    def get_items(self):
        """返回购物车内容的副本"""
        return dict(self._items)

    def clear(self):
        self._items.clear()

    def __len__(self):
        return len(self._items)

    def __str__(self):
        if not self._items:
            return "🛒 购物车为空"
        lines = ["🛒 购物车:"]
        for product, qty in self._items.items():
            subtotal = product.final_price * qty
            lines.append(f"  {product.name} × {qty} = ¥{subtotal:.2f}")
        lines.append(f"  {'─' * 30}")
        lines.append(f"  小计: ¥{self.get_total():.2f}")
        return "\n".join(lines)


# ---- 订单 ----
class Order:
    _order_counter = 0

    def __init__(self, user, cart):
        Order._order_counter += 1
        self.order_id = f"ORD-{Order._order_counter:04d}"
        self.user = user
        self.items = cart.get_items()
        self.total_price = cart.get_total(user)
        self.status = "pending"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def pay(self):
        if self.status != "pending":
            print(f"  ❌ 订单状态 '{self.status}' 无法支付")
            return False
        if not self.user._deduct(self.total_price):
            print(f"  ❌ 余额不足！需要 ¥{self.total_price:.2f}，"
                  f"余额 ¥{self.user.balance:.2f}")
            return False

        # 扣减库存
        for product, qty in self.items.items():
            product.stock -= qty

        self.status = "paid"
        print(f"  ✅ 订单 {self.order_id} 支付成功！扣款 ¥{self.total_price:.2f}")

        # VIP 用户赠送积分
        if isinstance(self.user, VIPUser):
            points = int(self.total_price)
            self.user.add_points(points)

        return True

    def ship(self):
        if self.status != "paid":
            print(f"  ❌ 订单状态 '{self.status}' 无法发货")
            return
        self.status = "shipped"
        print(f"  📦 订单 {self.order_id} 已发货！")

    def complete(self):
        if self.status != "shipped":
            print(f"  ❌ 订单状态 '{self.status}' 无法确认收货")
            return
        self.status = "completed"
        print(f"  ✅ 订单 {self.order_id} 已完成！")

    def cancel(self):
        if self.status in ("completed", "cancelled"):
            print(f"  ❌ 订单已{self.status}，不能取消")
            return
        if self.status == "paid" or self.status == "shipped":
            self.user._refund(self.total_price)
            for product, qty in self.items.items():
                product.stock += qty
            print(f"  💰 已退款 ¥{self.total_price:.2f}")
        self.status = "cancelled"
        print(f"  ❌ 订单 {self.order_id} 已取消")

    def __str__(self):
        status_icons = {
            "pending": "🕐", "paid": "💳",
            "shipped": "📦", "completed": "✅", "cancelled": "❌"
        }
        icon = status_icons.get(self.status, "")
        lines = [
            f"{'═' * 40}",
            f"  📋 订单号: {self.order_id}",
            f"  👤 用户: {self.user.username}",
            f"  📅 创建时间: {self.created_at}",
            f"  {icon} 状态: {self.status}",
            f"  商品明细:",
        ]
        for product, qty in self.items.items():
            lines.append(f"    - {product.name} × {qty} = ¥{product.final_price * qty:.2f}")
        lines.append(f"  💰 总价: ¥{self.total_price:.2f}")
        lines.append(f"{'═' * 40}")
        return "\n".join(lines)


# ============ 测试流程 ============

# 1. 创建商品
print("📦 创建商品...")
book1 = Book("Python编程从入门到实践", 89.9, "Eric Matthes", "978-7-115-54608-1")
book2 = Book("算法导论", 128.0, "CLRS", "978-7-111-40701-0")
laptop = Electronics("MacBook Pro", 14999, "Apple", 3)
mouse = Electronics("罗技鼠标", 199, "Logitech", 2)
shirt = Clothing("纯棉T恤", 99, "L", "100%棉")
jacket = Clothing("冲锋衣", 599, "XL", "Gore-Tex")

all_products = [book1, book2, laptop, mouse, shirt, jacket]
print("商品列表:")
for p in all_products:
    print(f"  {p}")

# 2. 创建用户
print("\n👤 创建用户...")
user1 = User("小明")
user2 = VIPUser("张总", vip_level=2)
print(f"  {user1}")
print(f"  {user2}")

# 3. 充值
print("\n💰 充值中...")
user1.add_funds(500)
user2.add_funds(20000)

# 4. 小明购物
print("\n🛒 小明购物...")
cart1 = ShoppingCart()
cart1.add(book1, 1)
cart1.add(mouse, 1)
cart1.add(shirt, 2)
print(cart1)
print(f"总价 (无用户折扣): ¥{cart1.get_total():.2f}")
print(f"总价 (小明): ¥{cart1.get_total(user1):.2f}")

# 5. 张总购物
print("\n🛒 张总购物...")
cart2 = ShoppingCart()
cart2.add(laptop, 1)
cart2.add(book2, 1)
cart2.add(jacket, 1)
print(cart2)
print(f"总价 (张总 VIP2 享9折): ¥{cart2.get_total(user2):.2f}")

# 6. 创建订单
print("\n📋 创建订单...")
order1 = Order(user1, cart1)
order2 = Order(user2, cart2)

# 7. 支付
print("\n💳 支付订单...")
order1.pay()
print(f"  {user1}")

order2.pay()
print(f"  {user2}")

# 8. 发货 & 收货
print("\n📦 订单流程...")
order1.ship()
order1.complete()

order2.ship()
order2.complete()

# 9. 打印订单
print("\n" + str(order1))
print(str(order2))


print("\n" + "=" * 50 + "\n")


# ===================================================================
# [挑战题] 练习 4: 文字冒险游戏引擎
# ===================================================================
print("=== 挑战题: 文字冒险游戏引擎 ===")


class Item:
    """游戏物品"""
    def __init__(self, name, description, effect=None):
        self.name = name
        self.description = description
        self.effect = effect  # {"type": "heal", "value": 30}

    def __str__(self):
        return f"{self.name}: {self.description}"


class Room:
    """游戏房间"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}  # {"north": Room对象, "south": Room对象}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                return self.items.pop(i)
        return None

    def describe(self):
        print(f"\n{'─' * 40}")
        print(f"📍 {self.name}")
        print(f"  {self.description}")
        if self.items:
            print(f"  🔍 你看到了: {', '.join(item.name for item in self.items)}")
        if self.exits:
            directions = ", ".join(self.exits.keys())
            print(f"  🚪 出口: {directions}")
        print(f"{'─' * 40}")


class Inventory:
    """玩家背包"""
    def __init__(self, capacity=10):
        self._items = []
        self.capacity = capacity

    def add(self, item):
        if len(self._items) >= self.capacity:
            print("  背包已满！")
            return False
        self._items.append(item)
        return True

    def remove(self, item_name):
        for i, item in enumerate(self._items):
            if item.name == item_name:
                return self._items.pop(i)
        return None

    def has_item(self, item_name):
        return any(item.name == item_name for item in self._items)

    def __contains__(self, item_name):
        return self.has_item(item_name)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        if not self._items:
            return "🎒 背包: (空)"
        items_str = ", ".join(item.name for item in self._items)
        return f"🎒 背包 ({len(self._items)}/{self.capacity}): {items_str}"


class Player:
    """玩家角色"""
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.inventory = Inventory()
        self.current_room = None

    def move(self, direction):
        if direction not in self.current_room.exits:
            print(f"  ❌ 这个方向没有出口！可用方向: {', '.join(self.current_room.exits.keys())}")
            return False
        self.current_room = self.current_room.exits[direction]
        print(f"  🚶 你向 {direction} 走去...")
        self.current_room.describe()
        return True

    def pick_up(self, item_name):
        item = self.current_room.remove_item(item_name)
        if item is None:
            print(f"  ❌ 这里没有 '{item_name}'")
            return
        if self.inventory.add(item):
            print(f"  ✅ 捡起了 {item.name}！")
        else:
            self.current_room.add_item(item)  # 放回

    def use_item(self, item_name):
        item = self.inventory.remove(item_name)
        if item is None:
            print(f"  ❌ 背包里没有 '{item_name}'")
            return
        if item.effect:
            if item.effect["type"] == "heal":
                old_hp = self.hp
                self.hp = min(self.max_hp, self.hp + item.effect["value"])
                healed = self.hp - old_hp
                print(f"  💚 使用 {item.name}，恢复 {healed} HP！(HP: {self.hp}/{self.max_hp})")
            elif item.effect["type"] == "damage":
                print(f"  ⚔️ {item.name} 散发出力量！攻击力+{item.effect['value']}")
            else:
                print(f"  ✨ 使用了 {item.name}！")
        else:
            print(f"  🤔 {item.name} 似乎没有效果...")
            self.inventory.add(item)  # 放回背包

    def status(self):
        bar_len = 20
        ratio = self.hp / self.max_hp
        filled = int(bar_len * ratio)
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"\n  👤 {self.name}")
        print(f"  ❤️ HP: |{bar}| {self.hp}/{self.max_hp}")
        print(f"  {self.inventory}")


class Game:
    """游戏主引擎"""

    def __init__(self):
        self.player = None
        self.rooms = {}
        self.is_running = False

    def setup(self):
        """初始化游戏世界"""
        # 创建房间
        entrance = Room("城堡入口", "你站在一座古老城堡的大门前。空气中弥漫着神秘的气息。")
        hall = Room("大厅", "宽敞的大厅，墙上挂满了油画。中央有一张巨大的圆桌。")
        library = Room("图书馆", "书架上摆满了落满灰尘的古书。角落有一张破旧的书桌。")
        dungeon = Room("地下室", "阴暗潮湿的地下室。你听到远处传来奇怪的声音。")
        garden = Room("花园", "一座美丽的花园，阳光明媚。空气中飘来花香。")
        treasure = Room("宝藏室", "✨ 金光闪闪的宝藏室！你找到了宝藏！恭喜通关！")

        # 连接房间
        entrance.add_exit("north", hall)
        hall.add_exit("south", entrance)
        hall.add_exit("east", library)
        hall.add_exit("west", garden)
        hall.add_exit("down", dungeon)
        library.add_exit("west", hall)
        garden.add_exit("east", hall)
        dungeon.add_exit("up", hall)
        dungeon.add_exit("north", treasure)  # 隐藏通道

        # 放置物品
        entrance.add_item(Item("火把", "可以照亮黑暗的角落"))
        hall.add_item(Item("面包", "看起来还很新鲜", {"type": "heal", "value": 20}))
        library.add_item(Item("古书", "记载着地下室秘密通道的古书"))
        library.add_item(Item("药水", "红色的回复药水", {"type": "heal", "value": 50}))
        garden.add_item(Item("草药", "清香的草药，可以恢复少量体力", {"type": "heal", "value": 15}))
        dungeon.add_item(Item("钥匙", "一把生锈的钥匙，不知道能打开什么"))

        self.rooms = {
            "entrance": entrance, "hall": hall, "library": library,
            "dungeon": dungeon, "garden": garden, "treasure": treasure,
        }

        # 创建玩家
        self.player = Player("冒险者", hp=80)
        self.player.current_room = entrance

    def process_command(self, command):
        """解析并执行命令"""
        parts = command.strip().lower().split(maxsplit=1)
        if not parts:
            return True

        action = parts[0]
        arg = parts[1] if len(parts) > 1 else ""

        if action in ("quit", "exit", "q"):
            print("  👋 游戏结束！再见！")
            return False

        elif action in ("go", "move", "walk") or action in ("north", "south", "east", "west", "up", "down"):
            direction = arg if arg else action
            self.player.move(direction)

        elif action in ("look", "l"):
            self.player.current_room.describe()

        elif action in ("pick", "take", "get"):
            if arg:
                self.player.pick_up(arg)
            else:
                print("  拾取什么？用法: pick <物品名>")

        elif action == "use":
            if arg:
                self.player.use_item(arg)
            else:
                print("  使用什么？用法: use <物品名>")

        elif action in ("bag", "inventory", "i"):
            print(f"  {self.player.inventory}")

        elif action in ("status", "stats", "s"):
            self.player.status()

        elif action in ("help", "h", "?"):
            self.show_help()

        else:
            print(f"  ❓ 未知命令: '{action}'。输入 'help' 查看帮助。")

        # 检查是否到达宝藏室
        if self.player.current_room == self.rooms.get("treasure"):
            print("\n🎊🎊🎊 恭喜你找到了宝藏！你是真正的冒险家！🎊🎊🎊")
            return False

        return True

    def show_help(self):
        print("""
  ╔══════════════════════════════════╗
  ║          📜 命令帮助             ║
  ╠══════════════════════════════════╣
  ║ go <方向>   移动 (north/south..)║
  ║ look        查看当前房间         ║
  ║ pick <物品> 拾取物品             ║
  ║ use <物品>  使用物品             ║
  ║ bag         查看背包             ║
  ║ status      查看状态             ║
  ║ help        显示帮助             ║
  ║ quit        退出游戏             ║
  ╚══════════════════════════════════╝""")

    def run(self):
        """游戏主循环"""
        self.is_running = True
        print("\n" + "🏰" * 20)
        print("  欢迎来到《城堡冒险》！")
        print("  输入 'help' 查看可用命令")
        print("🏰" * 20)

        self.player.current_room.describe()

        while self.is_running:
            try:
                command = input("\n> ").strip()
                if not command:
                    continue
                self.is_running = self.process_command(command)
            except (EOFError, KeyboardInterrupt):
                print("\n  游戏结束。")
                break


# ===== 演示模式（不需要用户输入）=====
print("📝 以下是游戏的自动演示：\n")

game = Game()
game.setup()

# 自动执行一系列命令来演示
demo_commands = [
    "look",
    "pick 火把",
    "bag",
    "north",
    "pick 面包",
    "use 面包",
    "status",
    "east",
    "pick 古书",
    "pick 药水",
    "west",
    "west",
    "pick 草药",
    "bag",
    "east",
    "down",
    "pick 钥匙",
    "use 药水",
    "status",
    "north",  # 进入宝藏室！
]

for cmd in demo_commands:
    print(f"\n> {cmd}")
    if not game.process_command(cmd):
        break

print("\n" + "=" * 50)
print("💡 提示: 要进行交互式游戏，请取消注释下面的代码:")
print("   game = Game()")
print("   game.setup()")
print("   game.run()")

# 取消下面的注释来进行交互式游戏：
# game = Game()
# game.setup()
# game.run()
