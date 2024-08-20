# Prime number Logic hear
def Prime(num):
    for value in range(2,int(num**(0.5)+1)):
        if num%value==0:
            return 'Not a prime Number'
    return 'Prime Number'
print(Prime(int(input('Enter number: '))))