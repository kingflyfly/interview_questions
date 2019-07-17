# 列表去重
a,b  = [1,2,3,4,1,2],[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

# 2 集合
a  = [1,2,3,4,1,2]
b = set(a)
print(list(b))
