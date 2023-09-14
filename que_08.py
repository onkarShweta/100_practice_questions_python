#  leap year or not

year = int(input("enter a year: "))
if year % 4==0 and year % 100 != 0:
    print("it is a leap year")
elif year % 400 == 0 and year % 100== 0:
    print("leap year")    
else:
    print("not a leap year")