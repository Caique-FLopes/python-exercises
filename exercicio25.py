qtd_pequenas = int(input("Digite a quantidade de camisetas pequenas vendidas: "))
qtd_medias = int(input("Digite a quantidade de camisetas médias vendidas: "))
qtd_grandes = int(input("Digite a quantidade de camisetas grandes vendidas: "))

valor_total = qtd_pequenas * 10 + qtd_medias * 12 + qtd_grandes * 15

print("O valor total da compra é R$ {:.2f}".format(valor_total))
