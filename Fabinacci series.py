num = int(input('Enter the number:'))
def Fabinacci(pos,first=0,second=1):
    for val in range(pos):
        Third = first+second
        yield first
        first,second=second,Third
print(list(Fabinacci(num)))
