peso = float(input("Peso do peixe: "))

if peso <= 50 :
    print("Tudo limpo cumpadi")
else:
    excesso = peso - 50
    multa = excesso * 4
    print(f"sua multa sera de {multa}")