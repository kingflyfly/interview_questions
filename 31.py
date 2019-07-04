##对字符串的操作方法都不会改变原来字符串的值
a = "1,2,3,4"
print(a.replace(",",""))
c = a.replace(",","")
print(list(c))