tanque= 1000 # litros de gasolina
while tanque>0: 

    abastecida= int(input("litros abastecidos: "))
    if abastecida>tanque:
        print("nao temos essa quantidade")
    else:
        tanque= tanque - abastecida
    print(f"restam ainda{tanque} litros.")
    
print("Acabou a gasolina")