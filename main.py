def cube(num):
    return num**3

def divisible3(num):
    if cube(num)%3 == 0:
        return(cube(num))
    
    else:
        return False
    
number = int(input("Enter a number: "))
print(divisible3(number))
