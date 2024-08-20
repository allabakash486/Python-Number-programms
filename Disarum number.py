# Check whether the number is disarum number or not.
num = int(input('Enter the number :'))
def Disarum(num,Dup,sol=0):
    count = len(str(num))
    while num!=0:
        sol += (num%10)**(count)
        num //= 10
        count -=1
    return sol == Dup
print(f"{num} Disarum number" if Disarum(num,num) else f"{num}  not Disarum number")