# Check whether the number is Happy number or not.
en = int(input("Enter the range :"))
def Squar(num,sol=0):
    while num!=0:
        sol += (num%10)**(2)
        num //= 10
    return sol
def Happy(num):
    while num > 9:
        num = (Squar(num))
    return  num == 1 or num==7
print(list(filter(Happy,range(1,en))))