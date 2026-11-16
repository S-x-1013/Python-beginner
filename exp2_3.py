lst=list(map(int,input("输入列表元素，逗号隔开：").split("，")))
lst_sort=sorted(lst)
max_val=max(lst)
avg_val=sum(lst)/len(lst)

print(f"原列表：{lst}")
print(f"排序后列表：{lst_sort}")
print(f"最大值：{max_val}")
print(f"平均值：{avg_val:.2}")
