nome = input("Digite o nome:\n")
idade = int(input("Digite a idade:\n"))

if idade <= 2:
    tipo = ("bebê")
elif idade >= 3 and idade <=11:
    tipo = ("criança")
elif idade >= 12 and idade <=21:
    tipo = ("jovem")
elif idade >= 22 and idade <=64:
    tipo = ("adulto")
elif idade >= 65 and idade <=100:
    tipo = ("idoso")
else:
    tipo = ("bem velhinho")
    
mensagem = f"{nome} esta com {idade}, e pela tabela, é considerado {tipo}"

print(mensagem)