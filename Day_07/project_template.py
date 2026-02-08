# Day 7 综合项目代码模板
# 这是一个文字冒险游戏的框架，你可以基于此完善，或者完全重写做别的。

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = [] # 背包

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0: self.hp = 0
        print(f"哎呦！你受到了 {dmg} 点伤害。剩余HP: {self.hp}")

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100: self.hp = 100
        print(f"舒服！你恢复了 {amount} 点HP。当前HP: {self.hp}")

# 地图数据 (简单的图结构)
# 每个房间有描述，和各个方向通向的房间名
rooms = {
    "Hall": {
        "desc": "你站在一个昏暗的大厅里。北边有一扇大门。",
        "north": "Corridor",
        "item": None
    },
    "Corridor": {
        "desc": "一条长长的走廊。南边是大厅，东边有一个小房间。",
        "south": "Hall",
        "east": "TreasureRoom",
        "monster": True # 这里有怪物
    },
    "TreasureRoom": {
        "desc": "房间里金光闪闪！",
        "west": "Corridor",
        "item": "Gold",
        "win": True # 到了这就赢了
    }
}

current_room_name = "Hall"
player = None

def fight_monster():
    print("\n突然跳出一只哥布林！")
    time.sleep(1)
    # 简单的回合制战斗逻辑
    # 请自行补充...
    dmg = random.randint(10, 30)
    player.take_damage(dmg)
    if player.is_alive():
        print("你费尽九牛二虎之力打跑了哥布林。")
    # 清除怪物防止重复打
    rooms[current_room_name].pop("monster", None) 

def play_game():
    global current_room_name, player
    name = input("请输入勇者的名字: ")
    player = Player(name)
    
    print(f"\n欢迎来到地下城, {player.name}!")
    
    while player.is_alive():
        room = rooms[current_room_name]
        print("\n------------------------------")
        print(f"当前位置: {current_room_name}")
        print(room["desc"])
        
        # 检查事件
        if "monster" in room:
            fight_monster()
            if not player.is_alive(): break
            
        if "win" in room:
            print("\n恭喜！你找到了宝藏，游戏通关！")
            break
            
        if "item" in room and room["item"]:
            print(f"你发现地上有一个: {room['item']}")
            action = input("要捡起来吗？(y/n): ")
            if action == 'y':
                player.inventory.append(room["item"])
                print(f"你获得了 {room['item']}")
                room["item"] = None # 物品被拿走了

        # 移动指令
        user_input = input("\n往哪走? (north/south/east/west/quit): ").lower()
        
        if user_input == "quit":
            print("勇者逃跑了...")
            break
            
        if user_input in room:
            current_room_name = room[user_input]
        else:
            if user_input in ["north", "south", "east", "west"]:
                print("那边是墙，走不通。")
            else:
                print("无效的指令。")

    if not player.is_alive():
        print("\n胜败乃兵家常事，大侠请重新来过。")

if __name__ == "__main__":
    play_game()
