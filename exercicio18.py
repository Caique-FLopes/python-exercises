valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2

sindicato = salario_bruto * 0.03
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11

total_descontos = ir + sindicato + inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}): R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir/salario_bruto*100:.0f}%): R$ {ir:.2f}")
print(f"(-) INSS ({inss/salario_bruto*100:.0f}%): R$ {inss:.2f}")
print(f"(-) Sindicato ({sindicato/salario_bruto*100:.0f}%): R$ {sindicato:.2f}")
print(f"FGTS ({fgts/salario_bruto*100:.0f}%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")