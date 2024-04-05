texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# exemplo usando interavel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # aDICIONA UMA QUEBRA DE LINHA

# exemplo com range
for numero in range(0, 51, 5):
    print(numero, end=" ")
