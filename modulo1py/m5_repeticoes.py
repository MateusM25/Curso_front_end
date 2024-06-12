"""x = 10 
while x >= 0 :
    print(x)
    x = x - 1
"""
# Imprimir numeros pares
"""fim = int(input("Digite o último Numero a Imprimir : "))
x = 0 
while x <= fim : 
    if x % 2 == 0 :
        print(x)
    x = x + 1 
"""
 # primeiros 10 multiplos de 30
#x = 0
#while x <= 30 : 
 #   print(x)
  #  x = x + 1 * 3

#tabuada 
"""n = int(input("Tabuada de : "))
x = 1
while x <= 10:
    print(n + x)
    x = x + 1 
#Qualquer numero 2 x 2 = 4
n = int(input("Digite um numero : "))
x = 0 

while x <= 9 : 
    b = (x + 1) * n     
    x = x + 1
    print(f"{x}x {n} = {b} ")"""
"""
n = int(input("Digite um numero  que será multiplica : "))
v = int(input("Até que numúro ele será multiplicado ?"))
x = int(input("E começará por qual? "))
x = x - 1 
v = v - 1 
while x <= v: 
    b = (x + 1) * n     
    x = x + 1
    print(f"{x}x {n} = {b} ")"""

# correção de questão 
"""
pontos = 0
questao = 1 
while questao <= 3: 
    resposta = input(f"Resposta da questão {questao}:")
    if questao == 1 and resposta == "b" or resposta == "B" :
        pontos = pontos + 1 
    if questao == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1 
    if questao == 3 and resposta == "d" or resposta == "D" : 
        pontos = pontos + 1 
    questao = questao + 1 
print(f"O aluno fez {pontos} ponto(s)")
"""


# Acumuladores 
"""
n = 1
soma = 0 
while n <= 10 :
    x = int(input(f"Digite o {n} Número : "))
    soma = soma + x 
    n = n + 1
    print(f"soma : {soma}")
"""
# exercicio 5.11 
"""
deposito = float(input("Qual o valor será depositado : "))
taxa = float(input("Taxa de juros a ser aplicada a.m :"))
g = deposito 
x = 1 
while x <= 24 : 
    deposit = (deposito * taxa) / 100 + deposito    
    deposito = deposit
    print(f" No mês {x} o seu capital é de R$ {deposit:5.2f}")
    x = x + 1

total = deposito - g
print(f"No fim dos 24 Mêses seu dinheiro rendeu um total de R$ {total:5.2f}") 
"""

# Deposito com aplicação mês a mês  exerc 5.12
"""
deposito = float(input("Qual o valor do primeiro deposito ? "))
taxa = float(input("Qual a Taxa de Juros a ser aplicada ? "))
mensal = float(input("Qual o valor mensal que será depositado ? "))
g = deposito 
x = 1 
mensal_1 = mensal * 24 
while x <= 24 :
   
    deposit = (deposito * taxa ) / 100 + deposito 
    h = deposit + mensal 
    deposito = h 
    print(f"No mês {x} O seu capital inicial com juros mais o depositado mensalmente é de {deposito:5.2f}") 
    x = x + 1 
     
total = deposito - g - mensal_1
print(f"No fim dos 24 Mêses seu dinheiro rendeu um total de R$ {total:5.2f}")

"""
# QUitamento de divida  exerc 5.13
"""
divida = float(input("Qual o valor total da sua divida ?"))
juros = float(input("Qual o Valor do juros aplicado mensalmente ?"))
pagamento = float(input("Qual o Valor a ser pago mensalmente ?"))
x = 0
divida = divida
while divida >= 0 :
    sub_total = (divida - pagamento) * juros / 100
    x = x + 1
    print(f"o Valor restante a ser pago é de {sub_total:5.2f} sendo quitado em ")   
"""
# atribuidores de operações especiais 
"""
# Interronpendo repetições  
s = 0 
n = 0
m = 0
while True:
    v = int(input("Digite um número a somar Ou 0 para sair: "))
    if v == 0: 
        break
    s += v  
    n = n + 1
    m = s / n   
print(f"a Soma dos Números digitados até a iunterrupção é {s:.1f}, a quantidade de vezes inserida é {n:.1f} e a média {m:5.3f}")
"""
"""#exerc 5.15    refazer 
1 == "0.5"
2 == 1.00
3 == 4.00
5 == 7.00
9 == 8.00
numeros_validos = {1,2,3,5,9}
soma = 0 
while True:    
    if numeros_validos :
    codigo = int(input("digite O codigo do produto : "))
    print("Codigo Invalido ! ")        
    quantidade = int(input("Digite a quantidade : "))
    soma = quantidade * codigo
    print(f"TOTAL: {soma}")  """

"""
#programa 5.1 - conntagem de cédulas 
valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} Cédulas de R$ {atual}")
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10 
        elif atual == 10:
            atual =5 
        elif atual == 5 :
            atual =1 
        cedulas = 0 

#exercicio 5.18 
valor = float(input("Digite o valor a Pagar : "))
cedulas = 0 
atual = 100
apagar = valor 
while True :
    if atual <= apagar : 
       apagar -= atual 
       cedulas += 1 
    else :
       print(f"{cedulas} Cédulas de R$ {atual}" )
       if apagar == 0 :
           break
       if atual == 100:
           atual = 50
       elif atual == 50:
           atual = 20
       elif atual == 20 :
           atual = 10
       elif atual == 10:
           atual = 5
       elif atual == 5:
           atual = 1
       elif atual == 1:
           atual = 0.5
       elif atual == 0.5:
           atual = 0.10
       elif atual == 0.10 :
           atual = 0.05
       elif atual == 0.05:
           atual == 0.02 
       elif atual == 0.02 :
           atual = 0          
       cedulas = 0
      """  

# 5.4 Repetições aninhadas 
"""
tabuada = 1 
while tabuada <= 10: 
    numero = 1
    while numero <= 10 :
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada +=1
  
   
   ###
def eh_palindromo(numero):
    # Converte o número para string
    numero_str = str(numero)
    
    # Verifica se a string é igual à sua reversa
    return numero_str == numero_str[::-1]

# Exemplo de uso
numero = int(input("Digite um número: "))
if eh_palindromo(numero):
    print(f"O número {numero} é um palíndromo.")
else:
    print(f"O número {numero} não é um palíndromo.")
 """
 
 # exercicio 5.22

operacao = input("Digite a Operção que deseja obter a tabuada, Adição , Multiplicação , Subtração , Divisão  :")
tabuada = 1

while operacao == "Adição" :
        tabuada <= 10
        numero = 1
        while numero <= 10 :
            print(f"{tabuada} + {numero} = {tabuada + numero}") 
        numero + 1
        tabuada =     
    
if operacao == "Multiplicacao" :
    print ("Multiplicação")
elif operacao == "subtração" :
    print("subtração")
elif operacao == "sair":
    print("saiu")
    
     