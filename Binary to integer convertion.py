# Binary value to integer convertion
num = int(input('Enter the integer: '))
def convert_integer(num,sol=0,power=0):    
    while num!=0:
        sol += (num%10)*(2**(power))
        num //= 10
        power +=1
    return sol
print(f' {num}  integer value is {convert_integer(num)}')