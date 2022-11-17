## 函数的定义
def func1(a,b,c):
    #使用tab缩进
    print("这是一个函数")
    print("这是一个参数a",a)
    print("这是一个参数b", b)
    print("这是一个参数c", c)

##函数的调用
func1(1,2,3)

def func2(a,b,c):
    return a + b + c;

sum = func2(3,2,1)
print(sum)

## 默认参数的函数
"""
默认参数再定义函数的时候使用k=v形式定义
调用函数时，如果没有传递参数，则会使用默认参数
"""
def func3(a=1):
    print("参数的a的值为",a);

func3(3)


## 关键字参数
"""
在调用函数的时候，使用k=v的方式传参
在函数调用/定义中，关键字参数必须跟随在位置参数的寿面
"""
def func4(a,b,c,d):
    print("参数a的值为",a)
    print("参数b的值为", b)
    print("参数c的值为", c)
    print("参数d的值为", d)


func4(10,b=1,d=-1,c=0)

def func4(a,b,c,*,d):
    print("参数a的值为",a)
    print("参数b的值为", b)
    print("参数c的值为", c)
    print("参数d的值为", d)


func4(10,1,-1,d=1)


## lamba 表达式
func5 = lambda x: x*2;

print("打印lamba的值")
print(func5(3))

