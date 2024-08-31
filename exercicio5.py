def inverte_string(texto):
    inverso = ""
    for i in range(len(texto) - 1, -1, -1):
        inverso += texto[i]
    return inverso

# Exemplo de uso:
texto = "Olá, mundo!"
inverso = inverte_string(texto)
print(inverso)
