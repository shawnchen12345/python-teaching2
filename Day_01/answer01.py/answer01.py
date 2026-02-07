num=[1,2,3,4,5]#原数组
re_num=num[::-1]#反向数组
print(re_num)
a=len(num)
s=sum(num)
print('平均数为：%s'%(s/a))
b=0
c=0
for i in num:
      if i%2==0:
          b=b+1
         # print(f'偶数有{b}个')
      else:
          c=c+1
         # print(f'奇数有{c}个')
print(f'偶数有{b}个')
print(f'奇数有{c}个')
