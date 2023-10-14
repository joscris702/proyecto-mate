# Paso 1: Definimos el conjunto A con las letras que conforman el nombre del mes actual (en este caso, "octubre").
A = set("octubre")

# Paso 2: Definimos el conjunto B con las primeras 10 letras del alfabeto.
B = set("abcdefghij")

# Paso 3: Calculamos la intersección de los conjuntos A y B.
conjunto_resultante = A.intersection(B)

# Paso 4: Mostramos los conjuntos A y B.
print("Conjunto A:", A)
print("Conjunto B:", B)

# Paso 5: Mostramos el conjunto resultante.
print("Conjunto resultante (Intersección de A y B):", conjunto_resultante)

