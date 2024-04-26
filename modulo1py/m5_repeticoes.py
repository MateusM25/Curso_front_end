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

