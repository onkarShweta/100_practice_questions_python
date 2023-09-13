# reverse a number

n = int(input("enter a 4 digit number: "))
rev=0
while(n>0):
    ld = n%10
    rev = (rev*10)+ld
    n = n//10
print(rev)    