print("Olá mundo")

print(7+4)
print("7 + 4")
print("7" + "4")#Contatenação de Strings

#Comentário é com #

'''Comentário
    de
    multiplas
    linhas'''

#Variáveis
nome = "Gustavo"
idade = 17
peso = 77.0
print(nome, idade, peso)
print(f"Oiiii, {nome}!!!!")

#inputs
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print("Oiii" , nome, "! Vc tem", idade, "anos")
print(f"Oiii {nome} ! Vc tem {idade} anos")

print(idade + 1)

if idade < 18:
        print("Menor de idade")