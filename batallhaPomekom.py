import os 
import time
os.system("cls") 
print("Bem vindo a batalha de pomekons!")
bonus= int(input("informe o valor do bonus da partida: "))
ataqueDabriel= int(input("dabriel- ataque:"))
defesaDabriel= int(input(" dabriel - defesa: "))
levelDabriel= int(input("dabriel- level: "))
ataqueGuarte= int(input("guarte- ataque:"))
defesaGuarte= int(input(" guarte - defesa: "))
levelGuarte= int(input("guarte- level: "))

valorGolpeDabriel = (ataqueDabriel+defesaDabriel)/2 
if levelDabriel % 2 == 0: 
    valorGolpeDabriel= valorGolpeDabriel+ bonus

valorGolpeGuarte = (ataqueGuarte+defesaGuarte)/2 
if levelGuarte % 2 == 0 :
    valorGolpeGuarte= valorGolpeGuarte + bonus

print(f"valor do golpe dabriel: {valorGolpeDabriel}")
print(f"valor do golpe do guarte: {valorGolpeGuarte}")

if valorGolpeGuarte > valorGolpeDabriel:
 print("Parabens Guarte, voce é o vencedor da batalha pomekon") 
elif valorGolpeDabriel > valorGolpeGuarte:
   print("Parabens Dabriel, voce é o vencedor da batalha pomekon")
else:
   print(" A batalha terminou empatada!!!!")
 
time.sleep(3) 
print(" Obrigado por jogar!")




 

