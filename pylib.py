#v1.00.0000
from time import *
#四舍五入函数
def rounding(n):
    n=float(n)
    intn=int(n)+0.5
    if n<intn:
        return int(intn-0.5)
    return int(intn+1)
#逐字输出函数
def printf(text=" ",times=0.3):
    text=str(text);
    for i in range(len(text)):
        print("\r"+text[0:i+1],end="")
        sleep(times)
    print()
#最大函数
def max(lists):
    maxs=lists[0]
    for i in lists:
        if i>maxs:
            maxs=i
    return maxs
#最小函数
def min(lists):
    mins=lists[0]
    for i in lists:
        if i<mins:
            mins=i
    return mins
#排序函数
def sort(lists,big=True):
    if big:
        if len(lists)>=2:
            mid=lists[len(lists)//2]
            left,right=[],[]
            lists.remove(mid)
            for num in lists:
                if num>=mid:
                    right.append(num)
                else:
                    left.append(num)
            return sort(left)+[mid]+sort(right)
        else:
            return lists
    else:
        if len(lists)>=2:
            mid=lists[len(lists)//2]
            left,right=[],[]
            lists.remove(mid)
            for num in lists:
                if num<=mid:
                    right.append(num)
                else:
                    left.append(num)
            return sort(left,False)+[mid]+sort(right,False)
        else:
            return lists
#指数函数
def pow(a,b):
    n=1
    for i in range(b):
        n*=a
    return n
#质数函数
def prinum(n):
    num=0
    for i in range(n):
        if n%(i+1)==0:
            num+=1
    if num==2:
        return True
    return False
#最大公因数函数
def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)
#最小公倍数函数
def lcm(a,b):
    return int(a*b/(gcd(a,b)))
#是否是整型函数
def is_int(x):
    return type(x)==type(0)
#是否是浮点型函数
def is_float(x):
    return type(x)==type(0.0)
#是否是字符串函数
def is_str(x):
    return type(x)==type("0")
#是否是列表函数
def is_list(x):
    return type(x)==type([0,0])
#是否是元组函数
def is_tuple(x):
    return type(x)==type((0,0))
#是否是字典函数
def is_dict(x):
    return type(x)==type({0:0})
#使用教程函数
def help():
    printf("\033[0;33m||||||| |||   ||| |||    ||| |||||||\033[0m",0.05)
    printf("\033[0;33m||| |||  ||| |||  |||    ||| |||  |||\033[0m",0.05)
    printf("\033[0;33m|||||||   |||||   |||    ||| |||||||\033[0m",0.05)
    printf("\033[0;33m|||        |||    |||    ||| |||   |||\033[0m",0.05)
    printf("\033[0;33m|||        |||    |||||| ||| |||||||   v1.00.0000\033[0m",0.05)
    print()
    print()
    printf("1.逐字书出函数",0.15)
    printf("使用方法：void printf(int text;float times=0.3);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：printf(文字内容——字符串,停顿时间（可以不写，不写为0.3）——浮点型)",0.15)
    print()
    printf("2.四舍五入函数",0.15)
    printf("使用方法：int rounding(float n);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：rounding(要四舍五入的小数（四舍五入成整数）)",0.15)
    print()
    printf("3.判断类型是否是整数型的函数",0.15)
    printf("使用方法：bool is_int(x);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：is_int(要检测的内容)",0.15)
    print()
    printf("4.判断类型是否是浮点型的函数",0.15)
    printf("使用方法：bool is_float(x);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：is_float(要检测的内容)",0.15)
    print()
    printf("5.判断类型是否是字符串的函数",0.15)
    printf("使用方法：bool is_str(x);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：is_str(要检测的内容)",0.15)
    print()
    printf("6.判断类型是否是列表的函数",0.15)
    printf("使用方法：bool is_list(x);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：is_list(要检测的内容)",0.15)
    print()
    printf("7.判断类型是否是元组的函数",0.15)
    printf("使用方法：bool is_tuple(x);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：is_tuple(要检测的内容)",0.15)
    print()
    printf("8.判断类型是否是字典的函数",0.15)
    printf("使用方法：bool is_dict(x);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：is_dict(要检测的内容)",0.15)
    print()
    printf("9.指数函数",0.15)
    printf("使用方法：int pow(int a;int b);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：pow(底数,指数)",0.15)
    print()
    printf("10.质数函数",0.15)
    printf("使用方法：bool prinum(int n);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：prinum(要判断的数（不得为0或1）)",0.15)
    print()
    printf("11.最大公因数函数",0.15)
    printf("使用方法：int gcd(int a;int b);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：gcd(数1,数2)",0.15)
    print()
    printf("12.最小公倍数函数",0.15)
    printf("使用方法：int lcm(int a;int b);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：lcm(数1,数2)",0.15)
    print()
    printf("13.排序函数",0.15)
    printf("使用方法：list sort(int list;bool Big=True);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：sort(列表,False为从大到小)",0.15)
    print()
    printf("14.获取最小数函数",0.15)
    printf("使用方法：float max(float list);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：max(列表或元组)",0.15)
    print()
    printf("15.获取最小数函数",0.15)
    printf("使用方法：float min(int list);",0.15)
    printf("\033[0;31m给我说人话！\033[0m",0.25)
    printf("使用方法：min(列表或元组)",0.15)
    print()
    printf("如有任何问题、意见、建议均可通过邮箱的方式通知作者",0.2)
    printf("线路一：nameweiwen@gmail.com（推荐使用）")
    printf("线路二：nameweiwen@hotmail.com（也不错）")
    printf("线路三：17762312512@qq.com（也还行）")
help()
#共发现5个bug
