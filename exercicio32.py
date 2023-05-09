saque = int(input("Digite o valor a ser sacado: "))

if saque < 10 or saque > 600: 
    print(f"Valor invalido para saque!")
else:
    notas100 = saque // 100
    saque = saque % 100
    
    notas50 = saque // 50
    saque = saque % 50
    
    notas20 = saque // 20
    saque = saque % 20
    
    notas10 = saque // 10
    saque = saque % 10
    
    notas5 = saque // 5
    saque = saque % 5
    
    notas1 = saque
    
print(f"Notas de 100: {notas100}\nNotas de 50: {notas50}\nNotas de 20: {notas20}\nNotas de 10: {notas10}\nNotas de 5: {notas5}\nNotas de 1: {notas1}\n")