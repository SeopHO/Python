#4.function and argument
def hello(name):
    print("hi,hello",name,name,name)
    print("Hello world",name)
hello("HOSEOP!")

def plus(a,b=100):
    print(a+b)

def minus(a,b):
    return a-b

re_1=plus(10,30)
re_2=minus(10,30)

print(re_1,re_2)

def test(obj,feeling):
    return f"Hello my {obj} is {feeling}"
    #or "Hello my" + object + "is" + feeling

re=test(obj="phone",feeling="cool")
print(re)

