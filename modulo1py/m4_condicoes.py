"""a = int(input('Digite um numero: '))
b = int(input('Digite outro valor '))   
if a > b : 
    print('O primeiro valor é maior')
if b > a : 
    print('O segundo valor é maior. ')    """

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
"""
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
"""

### dois numeros e escolha a operação 
"""
numero_1 = float(input("Digite Um numero : "))
numero_2 = float(input("Digite Outro numero : "))
calculo = input("Escreva a Operação que deseja realizar  Soma (+)  , Subtração  (-) , Multiplicação (*) ,  divisão (/) : ")
if calculo == "+" :
    resul_1 = numero_1 + numero_2
    print(f"Resultado : {resul_1:6.2f} ")
elif calculo == "-" :
    resul_2 = numero_1 - numero_2
    print(f"Resultado : {resul_2:6.2f}")
elif calculo == "*" : 
    resul_3 = numero_1 * numero_2
    print(f"Resultado : {resul_3:6.2f}")
elif calculo == "/" :
    resul_4 = numero_1 / numero_2
    print(f"Resultado : {resul_4:6.2f}")

    """
"""
## Emprestimo para compra de uma casa 
valor_casa = float(input(" Qual o valor do imovél desejado ? "))
anos = int(input(" Em quantos anos pretende pagar : "))
salario = float(input("Qual o seu salário atual para analise : "))

tempo_pagamento = anos * 12 
valor_parcela = valor_casa / tempo_pagamento
percentual_salario = salario * 0.3
percentual_real = (valor_parcela * 100) / salario

if percentual_salario < valor_parcela :
    print(f"Desculpe Seu emprestimo não foi aprovado, O valor de {valor_parcela:6.2f} representa {percentual_real:6.2f}% do seu saário, ficando acima dos 30% recomendados.  ")
else :
    print(f"Emprestimo Aprovado, O valor final da parecela é de {valor_parcela:6.2f} , {percentual_real:6.2f}% so seu salário Se enquadrando nos 30% recomendados.")
    """

# calculo conta de energia 

consumo = float(input("Qual foi o seu consumo mensal em kWh ? "))
instalacao = input("Identifique o tipo de intação pela inicial R(Residencial), C(Comercial), I(Industrial ) :  ")
r_1 = 0.40
r_2 = 0.65
c_1 = 0.55
c_2 = 0.60
i_1 = 0.55
i_2 = 0.60

if consumo < 500 and instalacao == "R" : 
    calc_1 = consumo * 0.40
    print(f" Sua conta deu R$ {calc_1:5.3f}")
elif consumo >=  500 and instalacao == "R" : 
    calc_2 = consumo * 0.65 
    print(f" Sua conta deu R$ {calc_2:5.3f}")

if consumo < 1000 and instalacao == "C" :
    calc_3 = consumo * c_1
    print(f" Sua conta deu R$ {calc_3:5.3f}")
elif consumo >= 1000 and instalacao == "C" :
    calc_4 = consumo * c_2
    print(f" Sua conta deu R$ {calc_4:5.3f}")

if consumo < 5000 and instalacao == "I" : 
    calc_5 = consumo * i_1
    print(f" Sua conta deu R$ {calc_5:5.3f}") 
elif consumo >= 5000 and instalacao == "I" :
    calc_6 = consumo * i_2
    print(f" Sua conta deu R$ {calc_6:5.3f}")  



  


