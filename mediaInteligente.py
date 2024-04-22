import os 
os.system("cls")
nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
media = (nota1+nota2)/2
print(f"A media final é: {media}")
if media >=7:
    print("aluno aprovado!")
elif media>5:
      print("aluno em exame!")
else:
      print("aluno reprovado!")