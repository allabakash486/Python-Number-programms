num = int(input("Enter the number:"))
def Reverse(num,result=0):
    while num!=0:
        result = result*10 + (num%10)
        num //=10
    return result
print(Reverse(num))