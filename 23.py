#将字符串"ilovechina"进行反转
a = 'ilovechina'
b = list(a)
print(a)
c = []
for i in range(len(a)):
    c.append(b.pop())
print(''.join(c))

print(''.join(reversed(a)))
print(a[::-1])

