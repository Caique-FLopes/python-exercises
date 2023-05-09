salarioAtual = float(input("digite o valor salarial atual do colaborador: "))
salarioApos = salarioAtual + salarioApos 
aumento = (salarioAtual * reajuste)

if salarioAtual < 280.00:
    reajuste = 0.2
    print(f"Salario antes do reajuste: {salarioAtual}\nPercentual Aplicado: 20%\nValor aumentado: {aumento}\nSalario com reajuste: {salarioApos}")
elif salarioAtual >= 280.00 and salarioAtual < 700.00:
    reajuste = 0.15
    print(f"Salario antes do reajuste: {salarioAtual}\nPercentual Aplicado: 15%\nValor aumentado: {aumento}\nSalario com reajuste: {salarioApos}")
elif salarioAtual == 700.00 and salarioAtual <= 1500.00:
    reajuste = 0.1
    print(f"Salario antes do reajuste: {salarioAtual}\nPercentual Aplicado: 10%\nValor aumentado: {aumento}\nSalario com reajuste: {salarioApos}")
else:
    reajuste = 0.5
    print(f"Salario antes do reajuste: {salarioAtual}\nPercentual Aplicado: 5%\nValor aumentado: {aumento}\nSalario com reajuste: {salarioApos}")
    