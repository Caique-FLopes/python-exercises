cont_fem_altura = 0
cont_masc_bom = 0
cont_masc = 0

for i in range(50):
    matricula = int(input("Matrícula do aluno: "))
    sexo = input("Sexo do aluno (M ou F): ")
    altura = float(input("Altura do aluno em cm: "))
    status = int(input("Status físico do aluno (1-bom, 2-regular, 3-ruim): "))

    if sexo == 'F' and altura > 170:
        cont_fem_altura += 1

    if sexo == 'M':
        cont_masc += 1
        if status == 1:
            cont_masc_bom += 1

print("Quantidade de alunas do sexo feminino com altura superior a 170 cm:", cont_fem_altura)

if cont_masc > 0:
    perc_masc_bom = (cont_masc_bom / cont_masc) * 100
    print("% de alunos do sexo masculino com status físico bom:", perc_masc_bom)
else:
    print("Não há alunos do sexo masculino")
