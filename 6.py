''' xrange 和 range 的区别
    python3 中取消了 range 函数，而把 xrange 函数重命名为 range，所以现在直接用 range 函数即可。
'''
t = range(5)
for i in t:
    print(i)
