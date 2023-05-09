salario_fixo = float(input("Digite o salário fixo do funcionário: "))
vendas = float(input("Digite o valor das vendas do funcionário: "))

comissao = vendas * 0.04
salario_final = salario_fixo + comissao

print("Valor da comissão: R$", comissao)
print("Salário final: R$", salario_final)