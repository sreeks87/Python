# def fib(n):
#     if n<=1:return n
#     else: return (fib(n-1)+fib(n-2))

# for i in range(10):
#     print(fib(i))

# a,b=0,1
# for i in range(10):
#     if i<=0:
#         print(i)
#     else:
#         c=a+b
#         print(c)
#         a=b
#         b=c
# f=1
# for i in range(1,6):
#     f*=i
# print(f)

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

