# Converting the integer to binary value
num = int(input('Enter the integer: '))
def convert_binary(num,sol=0):
    while num!=0:
        sol = (sol*10)+(num%2)
        num //= 2
    return sol
print(f' {num}  binary value is {convert_binary(num)}')