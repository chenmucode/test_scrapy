import re
import struct

# 这个正则用来匹配数字
pattern = re.compile(r'\d+')

################################
# # match是头部匹配
# m1 = pattern.match("one12twothree34four")
# print(m1) # 没有匹配到
# # 指定起始和终止位置
# m2 = pattern.match("one12twothree34four",3,10)
# # 使用group方法查看
# print(m2.group())
####################################

# search方法。从任意位置匹配
# m1 = pattern.search("one12twothree34four")
# print(m1.group())

# findall方法。返回一个列表，没有则返回空列表
# result = pattern.findall("hello 12 world 456")
# print(result)

# split方法.通过空格、逗号、分号进行分割，返回一个列表
# pattern = re.compile(r"[\s\,\;]+")
# string = "a,b;; c  d"
# print(pattern.split(string))

# sub方法
string = '<h1 class="test">imooc</h1>'
pattern = re.compile('\d')  # 匹配数字
print(pattern.sub("2",string))
print(pattern.sub("2",string,1))    # count参数用于指定替换次数，默认全部替换
# 分组乱入，使用search方法获取分组里的数据，通过group()里的数字来确定分组
pattern = re.compile('<(.\d)\sclass="(.*?)">.*?</(.\d)>')
print(pattern.search(string).group(2))

def func(m):
    return 'after sub '+ m.group(2)
print(pattern.sub(func, string))
