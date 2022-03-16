def print_factors(x):
    print("Los factores de",x,"son:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            
num=int(input("Ingrese el numero: "))
print_factors(num)            
