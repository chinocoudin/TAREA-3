numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
ceroacincuenta_numeros = [x for x in numeros]
impares_numero = [x for x in numeros if x % 2 != 0]
fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] <= 50:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
fibonacci_serie = [x if x in fibonacci else 0 for x in numeros]

print (f"numero de cero a cincuenta: ", ceroacincuenta_numeros)

print (f"numeros impares: ", impares_numero)

print (f"fibonacci en el rango: ", fibonacci_serie)

