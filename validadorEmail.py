import os
os.system("cls") 
email = input("Informe seu email: ")
contemArroba = False
contemPonto = False
for letra in email:
    if letra == "@":
        contemArroba = True
    elif letra == ".":
        contemPonto = True
if contemArroba == True and contemPonto == True :
    print ("email valido")
else:
    print("email invalido")

















'''#email = input("informe o seu email: ")
numeros= [4,7,3,1,8,9,11]
for numero in numeros:
    if numero % 2 == 0:
    print(f"o numero {numero} é par!")
     else :
    print(f"o numero{numero} é impar!")
    '''