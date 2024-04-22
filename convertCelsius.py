'''
step1- pedir ao usuario quanto esta em celsius
step1.2- realizar a conversão numerica (float- n.reais)
step2- realizar o calculo de conversao para farenheit
step2.1- descobrir a formula de conversão
step2.2 - montar a formula no algoritimo
step3- mostrar para o usuario a saída convertida
step3.3- formatar a saida para 3 casa decimais

'''
celsius = float(input("informe o valor da temperatura em graus celsius:"))
fahrenheit_= celsius * (9/5) + 32
print("Valor convertido em fahrenheit:", fahrenheit_)
print("{:.3f} celsius convertido em fahrenheit:{:.3f}".format(celsius, fahrenheit_))