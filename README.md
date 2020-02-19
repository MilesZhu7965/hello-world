# hello-world
first project on Github

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
