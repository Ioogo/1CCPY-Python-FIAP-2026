#RELACIONAIS
idade = 20

maior_idade = idade >= 18

if maior_idade:
    print("Você é maior de idade")

#operadores lógicos
#AND, OR, NOT

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha

if not login:
    print("Errou")
    print(" ")
#Notas

nota_final = 1

if nota_final < 4:
    print("Reprovado")
elif nota_final > 6:
    print("Aprovado")
else:
    print("Recuperação")
print("FIM")