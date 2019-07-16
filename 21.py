a = 'hello world yan zhe wlo'
b = a.split()
"""
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
"""
def test(c):
    return c.capitalize()
L2 = list(map(test,b))
print(" ".join(L2))


