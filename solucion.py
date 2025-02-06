# Define una función llamada solution que recibe una lista de palabras
def solution(words):
    # Inicializa un contador en 0
    c = 0
    # Itera sobre cada palabra en la lista de palabras
    for word in words:
        # Limpia la palabra: crea una nueva cadena solo con caracteres alfanuméricos
        # join: une todos los caracteres que cumplen la condición isalnum()
        clean_word = ''.join(char for char in word if char.isalnum())
        # Verifica si la palabra limpia tiene 3 o menos caracteres y no está vacía
        if len(clean_word) <= 3 and clean_word: 
            # Incrementa el contador si se cumple la condición
            c += 1
    # Devuelve el total de palabras que cumplen con el criterio
    return c

# Lee una línea de entrada y la divide en palabras
words = input().split()
# Imprime el resultado de llamar a la función solution con las palabras
print(solution(words))