valor_aquisicao = float(input("Digite o valor de aquisição do produto: "))

if valor_aquisicao < 50:
  valor_venda = valor_aquisicao * 1.45
else:
  valor_venda = valor_aquisicao * 1.3

print(f"O valor de venda do produto é: R$ {valor_venda:.2f}")