# Olá mundo 
print("Olá Mundo!")

#anos = int(input("Anos de Serviço: "))
#valor_por_ano = float(input("Valor Por Ano:" ))
#bonus = anos * valor_por_ano
#print(f"Bonus De R$ {bonus:5.2f}")

#num1 = int(input("digite um numero : "))
#num2 = int(input("digite um numero para a soma: "))
#num3 = num1 + num2
#print(num3)

#metros em milimetros 

#metros = float(input("digite a metragem :"))
#milimetros = metros * 1000
#print(f"{milimetros:10.2f} milimetros")            

# Transformar hora, minuto em segundo 

#hora = int(input("Digite quantas horas voce dorme :"))
#minutos = int(input("e quantos minutos :"))
#segundos = int(input("quantos segundos"))
#seg = hora * 3600 + minutos * 60 + segundos
#print(f"você dorme {seg} Segundos" )

#calculo de aumento de salário 

#salario_atual = float(input("Digite o seu salário atual : "))
#percentual = float(input("digite quantos Porcenton de aumento deseja :"))
#novo = salario_atual * percentual / 100
#novo_salario = salario_atual + novo
#print(f"Seu novo salário será de {novo_salario}")

# preço de uma mercadoria, o desconto e o valor final
#mercadoria = float(input("Qual o valor do produto ?"))
#desconto = float(input("Percentual de desconto"))
#valor_desconto = mercadoria * desconto / 100
#print(f"O valor que será descontado é de : R${valor_desconto}")
#valor_final = mercadoria - valor_desconto
#print(f"O produto Terá o custo de : R${valor_final}")

# Viagem e o tempo de viagem 
#kilometragem = float(input("Quantos Km será rodado ? "))
#velocidade = float(input("Qual a velocidade ?"))
#tempo = kilometragem / velocidade
#print(f"o tempo de viagem é {tempo} horas ")

# Temperatura em celcius para farenighty
#celsius = float(input("Qual a temperatura em Celsius :"))
#fare = 9 * celsius / 5 + 32
#print(f"A temperatura em fahrenheit é de {fare}")

#Quantos dias , quantos Km e o valor a pagar pelo aluguel do carro 
#km = float(input("Qual foi a km rodada ? "))
#dias = int(input("Quantos dias ficou com o carro : "))
#valor_km = km * 0.15
#valor_dias = dias * 60
#total = valor_km + valor_dias
#print(f"O valor a ser pago pelos dias e km rodados são de : R$ {total}")

#dias perdidos na vida de um fumante

#cigarros_diarios = int(input("Quantos cigarros fuma por dia ? "))
#tempo_f = float(input("quanto anos fuma ? " ))
#cigarros_dia = cigarros_diarios * tempo_f * 365
#minutos_perdidos = cigarros_dia * 10
#anos_perdidos = minutos_perdidos / (24 * 60)
#total_de_anos = anos_perdidos / 365
#print(f"Você perdeu {anos_perdidos:5.2f} Dias de vida, um total de {total_de_anos:5.2f} anos por causa do cigarro.")


# erros Comuns   

#ano_carro = int(input("digite o ano do seu carro"))

#if ano_carro <= 3: 
 #   print("Seu carro é novo")
#if ano_carro > 3 : 
#    print("Seu carro é antigo")

    #multa 
#velocidade = int(input("DIgite a velocidade que passou na pista : "))

#if velocidade <= 80 :
 #   print("Parabéns está dentro da velocidade permitida, não foi multado")
#if velocidade > 80 : 
 #   multa = (velocidade - 80) * 5
#    print(f" Você ultrapassou o limite de velocidade, e foi multado em {multa:5.2f} Reais. ")    

# calculo imposto de renda 
#salario = float(input("Digite o salário para calculo de imposto :"))
#base = salario 
#imposto = 0 
#if base > 3000 :
#    imposto  = imposto + ((base - 3000) * 0.35)
#    base = 3000 
#if base > 1000 :
 #   imposto = imposto + ((base - 1000) * 0.20)    
#print(f"Salario: R${salario:6.2f} IMPOSTO A PAGAR: R${imposto:6.2f}")

# imprimir valor maoir e menor



#def encontrar_maior_e_menor(numero1, numero2, numero3):
   # maior = max(numero1, numero2, numero3)
 #   menor = min(numero1, numero2, numero3)
  #  return maior, menor

#def main():
  #  try:
     #   numero1 = float(input("Digite o primeiro número: "))
      #  numero2 = float(input("Digite o segundo número: "))
       # numero3 = float(input("Digite o terceiro número: "))

      #  maior, menor = encontrar_maior_e_menor(numero1, numero2, numero3)

     #   print("O maior número é:", maior)
    #    print("O menor número é:", menor)
  #  except ValueError:
   #     print("Por favor, insira apenas números válidos.")

#if __name__ == "__main__":
 #   main()

# calculo de aumento 
#salario = float(input("Digite Seu Salário :  "))

#if salario > 1250 :
 #   aumento_1 = salario * 0.10 
 #   print(f'O seu salario irá haver um aumento de {aumento_1:5.2f} Passando a ser de {aumento_1 + salario:5.2f}')

#if salario <= 1250 : 
 #   aumento_2 = salario * 0.15 
#    print(f"O seu salario haverá um aumento de {aumento_2:5.2f} Passando a ser o valor bruto de {aumento_2 + salario:5.2f}")

#idade = int(input("DIgite a Idade do seu carro :  "))

#if idade <= 3 : 
#    print("Sua carroça é nova !!") 
#else :     
 #   print("Sua caranga ta velha :< ")            



 # Perguntando a distancia 
"""
distancia = float(input("Qual a distancia que será percorrida ? "))
if distancia <= 200 :
    passage_1 = distancia * 0.5
    print(f" Sua passagem custará um total de {passage_1:5.2f} !")
else :
    passagem_2 = distancia * 0.45
    print(f"Sua passagem custará um total de {passagem_2:5.2f}")
"""


# Estruturas aninhadas
"""
minutos = int(input("Quantos Minutos você utilizou este mês ? "))
if minutos < 200 :
    preco = 0.20
else : 
    if minutos < 400 :
        preco = 0.18
    else : 
        preco = 0.15
print(f"Você irá pagar de conta R$ {minutos * preco:6.2f} ")
"""
"""
# Programa categoria X preço 
categoria = int(input("digite a categoria do produto : "))
if categoria == 1 :
    preco = 10
else:
    if categoria == 2 : 
        preco = 18
    else :
        if categoria == 3 :
            preco = 23 
        else : 
            if categoria == 4 :
                preco = 26 
            else : 
                if categoria == 5 :
                    preco = 31
                else : 
                    print("Ctegoria invalida, digite um valor entre 1 e 5 ! ")
                    preco = 0
print(f"O preço do produto é de R$ {preco:6.2f}")

"""
# categoria x preço usando ELIF
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1 : 
    preco = 10
elif categoria == 2 :
    preco = 18        
elif categoria == 3 :
    preco = 23
elif categoria == 4 :
    preco = 26
elif categoria == 5 :
    preco = 31
else :
    print("Categoria Inválida, digite um valor entre 1 e 5 !")
    preco = 0 
print(f"O preço do produto é : R${preco:6.2f}")









