pares=[]
sumatoria=0
num=-1
while ( num!=0 ) :
    num=int(input("ingrese el numero "))
    sumatoria=num+sumatoria
    if (num % 2) == 0:
        pares.append(num)



print("Suma de todos los valores ingreados= ",sumatoria)
print(pares)