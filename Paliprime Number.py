num = int(input('Enter the number:'))
def Palindrome(num,dup,sol=0):
        while num!=0:
            sol = sol*10 + (num%10)
            num //=10
        return sol == dup
def prime(num):
    for val in range(2,num//2+1):
        if num%val ==0:
            return False
    return True
print('Paliprime' if prime(num) and Palindrome(num,num) else 'Not a Paliprime')