'''
Created on 6 Nov 2019

@author: Fanqiu Huang
'''
from _ast import Try

if __name__ == '__main__':
    pass
"""""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))


#练习1：华氏温度转换为摄氏温度。
#提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

F1 = float(input('Please input :'))
C1 = (F1-32) / 1.8
print(C1)
"""

#输入年份判断是不是闰年。

while True:
    try:
        year = int(input("Please input a year:"))
    except ValueError:
        print("Sorry, Please input a valid year!")
        #better try again... Return to the start of the loop
        continue
    else:
        break

if (year%4 == 0 & year%100 ==0) or (year%400 ==0): 
    RuenYear = True
else:
    RuenYear=False
    
print(RuenYear)   


