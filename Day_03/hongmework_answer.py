# ===========================================================
# ====================== 参考答案 ======================
# ===========================================================
"""
# --- 作业 1: 判断素数 ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# --- 作业 2: 圆面积 ---
def circle_area(r, pi=3.14):
    return pi * r * r


# --- 作业 3: 秒数转时间 ---
def seconds_to_time(total_seconds):
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return f"{hours}:{minutes}:{seconds}"


# --- 作业 4: 猜数字游戏 ---
def generate_secret():
    return random.randint(1, 100)

def get_guess():
    user_input = input("请输入你的猜测 (1-100): ")
    return int(user_input)

def check_guess(guess, secret):
    if guess == secret:
        return 0
    elif guess < secret:
        return -1
    else:
        return 1

def play_game():
    secret = generate_secret()
    print("游戏开始！我想了一个1-100之间的数字。")
    
    count = 0
    while True:
        guess = get_guess()
        count += 1
        result = check_guess(guess, secret)
        
        if result == 0:
            print(f"🎉 恭喜你猜对了！答案就是 {secret}")
            print(f"你一共猜了 {count} 次")
            break
        elif result == -1:
            print("太小了，再大一点！")
        else:
            print("太大了，再小一点！")


# --- 挑战题: 斐波那契 ---
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
"""

print("\n" + "=" * 50)
print("作业完成后，取消测试代码的注释运行验证！")
print("=" * 50)