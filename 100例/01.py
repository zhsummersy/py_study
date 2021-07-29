# range(1,5)
# for i in range(1,5):
#     print(i)
#遍历得到4位数
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i==j)and(i==k)and(j==k):
                print(i,j,k)
#遍历查找相同的位数或者不同的位数
print('我是分割线--------------------------------------')


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j)and(i!=k)and(j!=k):
                print(i,j,k)