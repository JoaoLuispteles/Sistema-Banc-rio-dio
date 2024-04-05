MAIOR_IDADE = 18
IDADE_ESPECIAL = 17 # CRIADO APENAS PARA RODAR O CODIGO.

idade = int(input("Infrome a sua idade:"))


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a CNH.")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Menor de idade, não pode tirar a CNH.")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade ==   IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer práticas.")
else:
    print("Menor de idade, não pode tirar a CNH.")

