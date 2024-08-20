# Check whether the number harshad number or not 
num = int(input("Enter the number:"))
def Niven(num,dup,sol=0):
    while num!=0:
        sol += (num%10)
        num //= 10
    return dup%sol==0 
print(f"{num} Harshad Number " if Niven(num,num) else f"{num} Harshad Number ")