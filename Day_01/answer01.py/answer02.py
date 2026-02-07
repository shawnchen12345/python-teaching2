num_str = input("请输入一组数字 (用空格隔开): ")
# 处理空输入的情况
nums = [int(x) for x in num_str.split()]
print(f"原始数组: {nums}")

# 1. 反向
print(f"反向数组: {nums[::-1]}")

# 2. 平均值
if len(nums) > 0:
    avg = sum(nums) / len(nums)
    print(f"平均值: {avg:.2f}")
else:
    print("数组为空，无法计算平均值")

# 3. 奇偶统计
odds = 0
evens = 0
for n in nums:
    if n % 2 == 0: evens += 1
    else: odds += 1
print(f"奇数: {odds} 个, 偶数: {evens} 个")