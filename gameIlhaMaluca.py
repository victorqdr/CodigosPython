import os
import time
os.system("cls")
print("Bem vindo a ilha misteriosa... ")
time.sleep(3)
os.system("cls")
print('''" Resolva os desafios a seguir e siga as instruções para encontrar o caminho certo." ''')
time.sleep(5)
os.system("cls")
print("###### DESAFIO 1 #####")
time.sleep(3)
os.system("cls")
print(" Voce se depara com uma porta enorme, guardada por um gigante adormecido, para passar pela porta e seguir sua jornada, vode deve responde a seguinta questão:")
print("")
print("")
print(" Quantos cocos o macaco tem se eu pegar a metade dos cocos que ele tem, mais dois cocos e depois subtrair 3 cocos? ")
cocosMacaco = int(input("Quantos cocos o macaco tinha?: "))
cocosResultado = cocosMacaco/2 +2 - 3 
cocosJogador = float(input(" Com quantos cocos o macaco ficou?"))
if cocosJogador == cocosResultado:
    print("Otimo, pode prosseguir...")
else:
    print("resposta errada, voce se ferrou!")
    quit()
time.sleep(5)
os.system("cls")
os.system("color4")
print("##### DESAFIO 2 ######")
time.sleep(3)
os.system("cls")
print('''Apos passar pela porta, voce encontra um labirinto infestado de crocodilos famintos.
      para escapar deles voce deve resolver o seguinte problema:''')

print("")
print("")
print("")
print('''Se eu tenho uma corda de 12 metros e preciso atravessar um rio de 7 metros de largura, 
quantos metros de corda a mais eu tenho para amarrar nas árvores e atravessar com 
segurança?''')
cordaSobra = 12-7
cordaJogador = int(input("Quantos metros sobram de corda? "))
if cordaJogador==cordaSobra:
   print("Resposta correta, pode prosseguir!")
else:
    print("Resposta errada, voce se ferrou!")
quit()

time.sleep(3)
os.system("cls")
print("#### DESAFIO 3 #####")
time.sleep(3)
os.system("cls")
print("Voce finalmente chega a camara do tesouro, mas para abri-la voce precisa resolver um desafio final :")
print("")
print("")
print("Se o numero de tesouros enterrados na ilha é igual ao dobro do numero de palmeiras, e o numero de palmeiras é igual a tres vezes o numero de periquitos que é 42, quantos tesouros ha na ilha?")
palmeiras = 42*3
tesouros = palmeiras*2
tesouroJogador = (int(input("quantos tesouros tem na ilha?")))
if tesouroJogador == tesouros:
    os.system("cls")
    print("PARABENS, VOCE GANHOU!!")
else:
    print("resposta errada, voce se ferrou!")
quit()