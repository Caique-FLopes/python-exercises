quantidade_frangos = int(input("Digite a quantidade de frangos na produção: "))

gasto_anel_chip = quantidade_frangos * 4.0
gasto_anel_alimento = quantidade_frangos * 2 * 3.5 

gasto_total = gasto_anel_chip + gasto_anel_alimento

print("O gasto total da granja para marcar seus frangos é de R$ %.2f" % gasto_total)