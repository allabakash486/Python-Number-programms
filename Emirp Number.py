num = int(input('Enter the number:'))
def prime(num):
    for val in range(2,int(num**0.5 + 1)):
        if num%val ==0:
            return False
    return True
def palindrome(num,dup,sol=0):
    while num != 0:
        sol = (sol * 10) +(num%10)
        num //= 10
    return sol
revse_num = palindrome(num,num)
print('Emrip Number' if prime(num) and prime(revse_num) and num != revse_num else 'Not Emirp number' )