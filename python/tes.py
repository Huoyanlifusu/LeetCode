import multiprocessing
import time
import collections
from collections.abc import Iterator, Iterable
from functools import reduce
import copy

def run():
    for i in range(5):
        print("run"+str(i)+" ")

def look():
    for i in range(5):
        print("look"+str(i)+" ")

class MyList(object):
    def __init__(self):
        self.container = []
    
    def __iter__(self):
        pass
    
    def add(self, item):
        self.container.append(item)

class FibIterator(object):
    def __init__(self):
        self.num1 = 1
        self.num2 = 1

    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        tmp = self.num1
        self.num1, self.num2 = self.num2, self.num1 + self.num2
        return tmp

def fib_generator():
    num1 = 1
    num2 = 1
    while True:
        tmp = num1
        num1, num2 = num2, num1 + num2
        yield tmp

def add(n, i):
    return n+i

def test():
    for i in range(4):
        yield i

def person(name):
    def say(content):
        print(name + ":" + content)
    return say

class Line(object):
    def __init__(self, k, b):
        self.k = k
        self.b = b
    
    def __call__(self, x):
        print(self.k * x + self.b)

def bibao(k, b):
    def createline(x):
        return k * x + b
    return createline

def calculate_10w():
    sum_res = 0
    for i in range(100001):
        sum_res += i ** 3
    print(sum_res, "结束")

def check_login(func):
    def B():
        print("===========")
        func()
        print("===========")
    return B

@check_login
def A():
    print("A")

def test001(*args, **kwargs):
    print(args)
    print(kwargs)

# class Solution(object):
#     def __init__(self) -> None:
#         self.ans = ["0", "0", "0"]

#     def isValid(self, h, m, s):
#         if h != "":
#             if int(h) > 23:
#                 return False
#         if m != "":
#             if int(m) > 59:
#                 return False
#         if s != "":
#             if int(s) > 59:
#                 return False
#         return True

#     def isBigger(self, h, m, s):
#         if int(h) > int(self.ans[0]):
#             return True
#         elif int(h) < int(self.ans[0]):
#             return False
#         else:
#             if int(m) > int(self.ans[1]):
#                 return True
#             elif int(m) < int(self.ans[1]):
#                 return False
#             else:
#                 return int(s) >= int(self.ans[2])

#     def huisu(self, strs, time):
#         if not strs:
#             if self.isBigger(time[:2], time[2:4], time[4:6]):
#                 self.ans[0] = time[:2]
#                 self.ans[1] = time[2:4]
#                 self.ans[2] = time[4:6]
#             return
#         if not self.isValid(time[:2], time[2:4], time[4:6]):
#             return
#         for i in range(len(strs)):
#             self.huisu(strs[:i]+strs[i+1:], time+strs[i])

# 两个栈实现队列
# class Queue(object):
#     def __init__(self) -> None:
#         self.st = []
#         self.st_ref = []
    
#     def push(self, num):
#         try:
#             num = int(num)
#             self.st.append(num)
#         except:
#             pass
    
#     def pop(self):
#         if not self.st:
#             return None
#         while len(self.st) > 1:
#             self.st_ref.append(self.st.pop())
#         pop_num = self.st.pop()
#         while self.st_ref:
#             self.st.append(self.st_ref.pop())
#         return pop_num
    
#     def get_first(self):
#         if not self.st:
#             return None
#         while len(self.st) > 1:
#             self.st_ref.append(self.st.pop())
#         num = self.st.pop()
#         self.st.append(num)
#         while self.st_ref:
#             self.st.append(self.st_ref.pop())
#         return num

# 华为 1 队列 + 栈 + 哈希表 + 模拟
def houzipagan():
    m = int(input("请输入玩家数"))
    n = int(input("请输入一共有多少牌"))
    a = []
    while m:
        m -= 1
        pai = input("请输入玩家的牌 1-13").split(" ")
        a.append(list(map(int, pai)))
    
    m = len(a)
    k = m
    r = 0
    desk = []
    dic = collections.defaultdict(int)
    while k > 1:
        r += 1
        for i in range(m):
            if not a[i]:
                continue
            card = a[i].pop(0)
            desk.append(card)
            if dic[card] > 0:
                seq = [card]
                desk.pop()
                while desk[-1] != card:
                    tmp_card = desk.pop()
                    dic[tmp_card] -= 1
                    seq.append(tmp_card)
                seq.append(desk.pop())
                dic[card] -= 1
                a[i] += seq
            else:
                dic[card] += 1
            if a[i] == []:
                k -= 1
            print(a, desk)
    index = -1
    for i in range(m):
        if a[i] != []:
            index = i

    print(r)
    print(index+1)
    print(a[index])



if __name__ == "__main__":
    # houzipagan()

    # a = reduce(lambda x, y: x*10 + y, [1,2,3,4, 5])
    # print(a)

    # map函数第二个参数一定是可迭代对象
    # a = map(lambda x, y: x+y, 1, 2)

    # 异常处理
    # try:
    #     a = 1
    # except:
    #     print(2)
    # else:
    #     print(2.5)
    # finally:
    #     print(3)

    # 对不可变类型的浅拷贝等于引用
    # a = (11, 12)
    # b = copy.copy(a)
    # print(id(a))
    # print(id(b))

    # c = 11
    # d = copy.copy(c)
    # print(id(c))
    # print(id(d))

    # 浅拷贝只考顶层
    # a = [11, 22]
    # b = [33, 44]
    # c = [a, b]
    # d = copy.deepcopy(c)
    # c.append(55)
    # a.append(55)
    # print(c)
    # print(d)


    # q = Queue()
    # q.push(7)
    # print(q.st)
    # q.push(9)
    # print(q.st)
    # q.push(10)
    # print(q.st)
    # q.push(3)
    # print(q.st)
    # q.pop()
    # print(q.st)
    # print(q.get_first())
    # q.pop()
    # print(q.st)
    # print(q.get_first())

    # input_l = [1, 1, 2, 2, 3, 4]
    # strs = list(map(str, input_l))
    # solution = Solution()
    # solution.huisu(strs, "")
    # print(solution.ans)
    # 装饰器定义
    # A()

    # n = "大象"
    # print("我吃了%s" % (n))

    # 引入装饰器
    # starttime = time.time()
    # calculate_10w()
    # endtime = time.time()
    # print("总时长", endtime-starttime)


    # 闭包和面向对象区别
    # bb = bibao(1, 5)
    # print(bb(4))
    # print(bb(5))

    # line = Line(2, 2)
    # line(1)
    # line(5)

    # 闭包定义
    # zhang = person("张三")
    # li = person("李四")

    # zhang("你好李四")
    # li("你好张三")

    # 生成器不取值，一直存储算法
    # g = test()
    # for n in [1, 10, 5, 2]:
    #     print(n)
    #     g = (add(n, i) for i in g)
    # print(list(g))

    # fib = FibIterator()
    # for _ in range(10):
    #     print(next(fib))

    # 生成器和列表比较
    # nums = [x for x in range(5)]
    # print(type(nums))

    # nums = (x for x in range(50000000000000000000000000000000000))
    # print(type(nums))
    # print(nums)

    #自定义迭代器
    # myList = MyList()
    # myList.add(5)
    # myList.add(6)
    # myList.add(7)

    # print(isinstance(myList, Iterable))

    # 迭代器构建for循环
    # nums = [11, 22, 33, 44]
    # nums_iter = iter(nums)

    # try:
    #     while True:
    #         print(next(nums_iter))
    # except StopIteration as stp:
    #     pass

    # processRun = multiprocessing.Process(target=run)
    # processLook = multiprocessing.Process(target=look)
    # processRun.start()
    # processRun.join()
    # processLook.start()
    # processLook.terminate()