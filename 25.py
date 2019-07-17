#有一个字符串开头和末尾都有空格，比如“ adabdw ”,要求写一个函数把这个字符串的前后空格都去掉
a = ' adabdw '
#print(a.strip())
#def test(a):
print(''.join(a.split()))