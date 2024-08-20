# Check whether the number is armstrong number or not.
num = int(input('Enter the number :'))
def Armstrong_number(num,Dup,sol=0):
    count = len(str(num))
    while num!=0:
        sol += (num%10)**(count)
        num //= 10
    return sol == Dup
print(f"{num} Armstong number" if Armstrong_number(num,num) else f"{num}  not Armstong number")