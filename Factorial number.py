num = int(input('Enter the number:'))
def Factorial_number(num,sol=1):
    for value in range(1,num+1):
        sol *= value
    print(sol)
Factorial_number(num)