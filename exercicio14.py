conta = float(input("Digite o numero de sua conta:"))
saldo = float(input("Digite seu saldo:"))
debito = float(input("Digite seu debito:"))
credito = float(input("Digite seu credito:"))
saldoAtual = saldo - debito + credito

if saldoAtual >= 0:
    print(f"Seu saldo atual é de: {saldoAtual}\nSeu saldo esta positivo")
else:
    print(f"Seu saldo atual é de: {saldoAtual}\nSeu saldo esta negativo")