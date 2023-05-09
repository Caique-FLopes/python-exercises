sexo = input("Digite o sexo (M ou F): ")
altura = float(input("Digite a altura em metros: "))

if sexo == "M":
  peso_ideal = (72.7 * altura) - 58
  print("O peso ideal é", peso_ideal, "kg")
elif sexo == "F":
  peso_ideal = (62.1 * altura) - 44.7
  print("O peso ideal é", peso_ideal, "kg")
else:
  print("Sexo inválido!")
