# Check whether the number is Special number or not.
num = int(input('Enter the number :'))
def Factorial(num,sum1=1):
    for val in range(1,num+1):
        sum1 *= val
    return sum1
def Special(num,dup,result=0):
    while num !=0:
        ld = (num%10)
        result += Factorial(ld)
        num //= 10 
    return result == dup
print(f"{num} Happy number" if Special(num,num) else f"{num}  not Happy number")
