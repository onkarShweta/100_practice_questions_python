# sum of digits

n = int(input("enter 3 digit number: "))
sum = 0
for i in range(n):
    ld = n%10
    sum = sum+ld
    n=n//10
print(sum)
