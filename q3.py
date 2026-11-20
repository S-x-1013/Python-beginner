nums=list(map(int,input("输入整数列表：").split()))
product=1
for num in nums:
    product*=num
print(product)
