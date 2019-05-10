print("hello world")
print("你好")

print('------------------')
print('测试一下缩进')
if True:
    print(True)
    print("走到这一步啦")
else:
    print(False)
    print(nihao)

#多行表示
print('------------------')
print('测试一下多行表示')
a = 1
b = 2
c = 3
d = a + \
    b + \
    c
print(d)

# 字符串
print('------------------')
print('测试一下字符串')
word = 'hello'
sentence = "邰文思"
paragraph = """这是一个段落,
可以有多行组成
未完待续"""
print(paragraph)
print(sentence)
print(sentence, word)
print('------------------')
# \转义字符的使用以及r的使用，放在最前面,这里的 r 指 raw，即 raw string
print("测试一下转义字符\n")
print(r"测试一下r的功能，不转义\n")
print('hello\nRunoob')
print(r'hello\nRunoob')
print('------------------')
#字符串分割
str = "Hello Runoob"
print('测试以下字符串分割')
print(str)
print(str[1:2])
print(str[0:-1])
print(str[0:5])
print(str[0:])
print(str[2:5])
print(str[2:])
print(str, '你好')
print(str + '你好')
print('------------------')

print('------------------')
print('测试一下keyword')
import keyword
array = keyword.kwlist
print(array)

#索引
greeting = "hello"
