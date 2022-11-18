list_hogwarts=[1,2,3]
"""
append只能在尾部插入
list [1, 2, 3, 0]
"""
list_hogwarts.append(0)
print("list",list_hogwarts)

"""
append能在索引插入
list [9, 1, 2, 3, 0]
"""
list_hogwarts.insert(0,9)
print("list",list_hogwarts)

"""
删除元素
list [9, 1, 2, 3, 0]
list [9, 2, 3, 0]
"""
list_hogwarts.remove(1)
print("list",list_hogwarts)

"""
list [2, 3, 0]
"""
y = list_hogwarts.pop(0)
print("返回值",y)
print("list",list_hogwarts)


"""
排序
list [0, 2, 3]
"""
list_hogwarts.sort()
print("list",list_hogwarts)
"""
list [3, 2, 0]
"""

list_hogwarts.sort(reverse=True)
print("list",list_hogwarts)

"""
list [0, 2, 3]
"""
list_hogwarts.reverse()
print("list",list_hogwarts)


list_square=[]
for i in range(4):
    list_square.append(i**2)

"""
list_square [0, 1, 4, 9]
"""
print("list_square",list_square)
"""
list_square2 [0, 1, 4, 9]
"""
list_square2=[i**2 for i in range(1,4)]
print("list_square2",list_square)

list_square3=[i**2 for i in range(1,4) if i!= 1 ]
"""
list_square3 [4, 9]
"""
print("list_square3",list_square3)

list_square4=[]
for i in range(1,4):
    for j in range(1,4):
        list_square4.append(i*j)
"""
list_square4 [1, 2, 3, 2, 4, 6, 3, 6, 9]
"""
print("list_square4",list_square4)

"""
元祖
"""

#元祖的定义
tuple_hogwarts = [1,2,3]
tuple_hogwarts2 = 1,2,3

"""
tuple_hogwarts [1, 2, 3]
<class 'list'>
tuple_hogwarts2 (1, 2, 3)
<class 'tuple'>
"""
print("tuple_hogwarts",tuple_hogwarts)
print(type(tuple_hogwarts))
print("tuple_hogwarts2",tuple_hogwarts2)
print(type(tuple_hogwarts2))

#元祖的不可变特性
list1_hogwarts = [1,2,3]
list1_hogwarts[0] = "a"
"""
list1_hogwarts ['a', 2, 3]
"""
print("list1_hogwarts",list1_hogwarts)

""""
(<class 'TypeError'>, TypeError("'set' object does not support item assignment"), <traceback object at 0x10c9b0c00>)
"""
# tuple_hogwarts3 = (1,2,3)
# tuple_hogwarts3[0] = "a"
# print("tuple_hogwarts3",tuple_hogwarts3)

a = [1,2,3]
tuple_hogwarts4 = (1,2,a)
"""
tuple_hogwarts4 (1, 2, [1, 2, 3])
"""
print("tuple_hogwarts4",tuple_hogwarts4)
#4540400384
print(id(tuple_hogwarts4[2]))
tuple_hogwarts4[2][0] = "a"
#4540400384
print(id(tuple_hogwarts4[2]))

"""
tuple_hogwarts4 (1, 2, ['a', 2, 3])
不是说元祖不可变么？其实可以看出a的内存地址的确是没有变化，变化的只是里面的元素
"""
print("tuple_hogwarts4",tuple_hogwarts4)

a = (1,2,3,"a","a")
#2
print(a.count("a"))
#2
print(a.index(3))


## 集合
"""
集合是由不重复元祖组成的无序的集
它的基本用法包括成员检测和消除重复元素
可以使用{}或者set()函数创建集合
要创建一个空集合只能用set()而不能用{}
"""
a = {1}
b = set()

"""
0
<class 'set'>
<class 'set'>
"""
print(len(b))
print(type(a))
print(type(b))


c = {1,2,3}
d = {1,5,6}
"""
并集{1, 2, 3, 5, 6}
"""
print(c.union(d))
"""
交集{1}
"""
print(c.intersection(d))
"""
差集{2, 3}
"""
print(c.difference(d))

"""
集合去重{'a', 'f', 'd'} 
"""
print({i for i in "afdfdfdfdfdfdfdfdfd"})

e = "fdsfsfsdkfskwifskfjsfjlsjflsdfdfs"
"""
{'w', 'i', 'l', 's', 'f', 'j', 'd', 'k'}
"""
print(set(e))

#字典
hogwarts_dict = {"a":1,"b":2}
hogwarts_dict2 = dict(a=1,b=2)
"""
hogwarts_dict {'a': 1, 'b': 2}
hogwarts_dict2 {'a': 1, 'b': 2}
"""
print("hogwarts_dict",hogwarts_dict)
print("hogwarts_dict2",hogwarts_dict2)

"""
dict_keys(['a', 'b'])
"""
print(hogwarts_dict.keys())
"""
dict_values([1, 2])
"""
print(hogwarts_dict.values())

"""
输出key的value：1，并且删除该key和value
"""
print(hogwarts_dict.pop("a"))

"""
{'b': 2}
"""
print(hogwarts_dict)

hogwarts_dict3 = {}
b = hogwarts_dict3.fromkeys([1,2,3])
"""
{1: None, 2: None, 3: None}
"""
print(b)

c = hogwarts_dict3.fromkeys([1,2,3],"a")
"""
{1: 'a', 2: 'a', 3: 'a'}
"""
print(c)

# print(hogwarts_dict.popitem()) 随机删除一个对象，并且返回

"""
{1: 2, 2: 4}
"""
print({i: i * 2 for i in range(1, 3)})