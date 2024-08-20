num = int(input("Enter the number: "))
def  Palindrome(num,dup,sol=0):
    while num!=0:
        sol = sol *10 + (num%10)
        num //= 10
    return sol == dup 
print('Palindrome' if Palindrome(num,num) else 'Not Palindrome')