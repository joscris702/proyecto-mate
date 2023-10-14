# Mostramos un mensaje inicial con la pregunta
print("Para calcular el número de partidos en un torneo de fútbol universitario:")
print("1. Resta 1 al número de universidades para calcular cuántos partidos juega cada universidad.")
print("2. Multiplica el número de universidades por la cantidad de partidos que juega cada universidad.")
print("3. Divide el resultado entre 2, ya que cada partido involucra a dos universidades.")
print("4. Multiplica el número total de partidos por la duración de cada partido (en minutos) para obtener la duración total del torneo.")

# Paso 1: Definir el número de universidades participantes en el torneo
numero_de_universidades = 15

# Paso 2: Calcular la cantidad de partidos que cada universidad juega
partidos_por_universidad = numero_de_universidades - 1

# Paso 3: Establecer la duración de cada partido en minutos
duracion_por_partido = 30

# Paso 4: Calcular el número total de partidos en el torneo
numero_total_de_partidos = (numero_de_universidades * partidos_por_universidad) / 2

# Paso 5: Calcular la duración total del torneo en minutos
duracion_total_en_minutos = numero_total_de_partidos * duracion_por_partido

# Paso 6: Imprimir los resultados explicando cada uno
print("En un torneo de fútbol universitario con", numero_de_universidades, "universidades:")
print("Cada universidad juega", partidos_por_universidad, "partidos contra otras sin revancha.")
print("El número total de partidos en el torneo es de", numero_total_de_partidos, "partidos.")
print("Si cada partido dura", duracion_por_partido, "minutos,")
print("la duración total del torneo es de", duracion_total_en_minutos, "minutos.")
