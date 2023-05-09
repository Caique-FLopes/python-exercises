quantidade_sanduiches = int(input("Digite a quantidade de sanduíches a fazer: "))

quantidade_queijo = quantidade_sanduiches * 2 * 0.05
quantidade_presunto = quantidade_sanduiches * 1 * 0.05
quantidade_carne = quantidade_sanduiches * 1 * 0.1

print("Para fazer {} sanduíches, são necessários:".format(quantidade_sanduiches))
print("{:.2f} kg de queijo".format(quantidade_queijo))
print("{:.2f} kg de presunto".format(quantidade_presunto))
print("{:.2f} kg de carne".format(quantidade_carne))