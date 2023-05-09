turno = input("Qual periodo voce estuda?\nM - para Matutito\nV - para Vespertino\nN - para Noturno\n")

if turno == "M" or turno == "m":
    print(f"Bom dia, seja bem vindo!")
elif turno == "V" or turno == "v":
    print(f"Boa tarde, seja bem vindo!")
elif turno == "N" or turno == "n": 
    print(f"Boa noite, seja bem vindo!")
else:
    print(f"Valor Invalido")