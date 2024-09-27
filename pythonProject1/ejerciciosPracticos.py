# Ejercicio 1: Presentación con nombre, edad y comida favorita
name = "Luis"
age = 27
favouriteFood = "Pasta con salsa Boloñesa"
introduction = f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}."
print(introduction)

# Ejercicio 2: Contar letras en el nombre completo
fullName = "Juan Pablo Carmona Cabrera "
letterCount = len(fullName.replace(" ", ""))
greeting = f"Hola, {fullName}! Tu nombre tiene {letterCount} letras, excluyendo los espacios."
print(greeting)

# Ejercicio 3: Mostrar porcentajes de ventas e ingresos
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
salesInfo = f"Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}% y los ingresos crecieron un {revenueGrowthPercent:.2f}%."
print(salesInfo)

# Ejercicio 4: Decodificar un mensaje secreto
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
decodedMessage = secretMessage[3::2]  # Omite los primeros tres caracteres y luego omite todos los demás
print(decodedMessage)

# Ejercicio 5: Contar el número de palabras en una frase
text = 'El nombre "Python" viene dado por la afición de Van Rossum al grupo Monty Python.'
wordCount = len(text.split())
print(f"Numero de palabras en la frase: {wordCount}")

# Ejercicio 6: Reemplazar letras en una cadena
word = "Camila"
modifiedWord = word.replace("a", "e")
print(modifiedWord)

# Ejercicio 7: Invertir el orden de las palabras en una frase
sentence = "La historia del lenguaje de programación Python"
reversedSentence = ' '.join(sentence.split()[::-1])
print(reversedSentence)
