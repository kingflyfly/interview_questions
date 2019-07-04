b = []
a  = [1,2,3,4,1,2]
a.sort()
for i in a:
    if i in a and i not in b:
        b.append(i)
print(b)

