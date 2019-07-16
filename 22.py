#如何检测字符串中只含有数字
'''
a = input('aaaaa:')
for i in a:
    try:
        b = int(i)
    except ValueError as e:
        print(e.args)
        print('此字符串含有字符')
        break
'''
b = "11"
print(b.isdigit())




