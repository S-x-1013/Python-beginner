p1=list(map(int,input("输入第一个坐标：").split()))
p2=list(map(int,input("输入第二个坐标：").split()))
dist=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
print(dist)
