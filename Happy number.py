# Check whether the number is Happy number or not.
num = int(input('Enter the number :'))
def Squar(num,sol=0):
    while num!=0:
        sol += (num%10)**(2)
        num //= 10
    return sol
def Happy(num):
    while num > 9:
        num = (Squar(num))
    return  num == 1 or num==7
print(f"{num} Happy number" if Happy(num) else f"{num}  not Happy number")
