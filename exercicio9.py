nome = input('Nome aluno: ')
disciplina = input('Digite o nome da disciplina: ')
primeiraProva = float(input('Nota da primeira prova: '))
segundaProva = float(input('Nota da segunda prova: '))
terceiraProva = float(input('Nota da terceira prova: '))
media = (primeiraProva + segundaProva + terceiraProva) / 3

if media <= 5:
    print(f"Aluno(a): {nome}\nPrimeira prova: {primeiraProva}\nPrimeira prova: {segundaProva}\nPrimeira prova: {terceiraProva}\nMedia Final: {media}\nAluno Reprovado")
else:
    print(f"Aluno(a): {nome}\nPrimeira prova: {primeiraProva}\nPrimeira prova: {segundaProva}\nPrimeira prova: {terceiraProva}\nMedia Final: {media}\nAluno Aprovado")