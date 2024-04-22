respostas1 = int(input("Telefonou para a vitima (1)Sim (0)Não " ))
respostas2 = int(input("esteve no local do crime (1)sim (0) Não " ))
respostas3 = int(input( "mora perto da vitima (1)sim (0) não" ))
respostas4 = int(input("devia para a vitima (1)sim (0) não" ))
respostas5 = int(input("ja trabalhou com a vitima(1) sim (0) não" ))


soma = respostas1 + respostas2+ respostas3+ respostas4+ respostas5

if soma ==0 :
    print(f"inocente")
elif soma ==2:
    print(f"suspeito")
elif soma == 3 or 4:
     print(f"cumplicie")
elif soma ==5 :
    print(f"ladrão")