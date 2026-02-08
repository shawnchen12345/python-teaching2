def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return "不支持的运算符"

result = calc(10, 5, "+")
print(f"10 + 5 = {result}") 