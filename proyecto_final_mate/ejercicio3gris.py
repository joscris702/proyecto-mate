# Pregunta inicial
print("Pregunta: ¿Cuál es el Máximo Común Divisor (MCD) de 150 y 39?")
print("Procedimiento para calcular el MCD utilizando el Algoritmo de Euclides:")

# Paso 1: Definimos los dos números para los cuales deseamos calcular el MCD
num1 = 150
num2 = 39

# Paso 2: Iniciamos el procedimiento y mostramos los números iniciales
print("Comenzamos con {} y {}.".format(num1, num2))

# Paso 3: Aplicamos el algoritmo de Euclides para calcular el MCD
while num2 != 0:
    cociente = num1 // num2
    resto = num1 % num2
    print("Paso: Dividimos {} entre {}, cociente = {}, resto = {}.".format(num1, num2, cociente, resto))
    num1 = num2
    num2 = resto

# Paso 4: El MCD es el último valor no nulo de num1
print("El MCD de 150 y 39 es {}.".format(num1))
