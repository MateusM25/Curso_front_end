print ("olá mundo ")
print ('7' + '1' +'5') 
nome = input ( 'qual seu nome ? ')  # vai perguntar o nome para o usúario, com o comando input 
peso = input ('Qual é sua peso ?')
idade = input ("qual sua idade ? ")
print (nome, peso, idade)

#Exercicio 1

nome_1 = input ('Qual seu nome ? ')
print ( nome_1 , "Bem Vindo Safado(a)")

#Exercicio 2 
idade_1 = input ("Qual o dia do seu nascimento? " )
idade_2 = input (' Qual o mês do seu nascimento? ')
idade_3 = input ( ' Qual o ano ?')
print (nome_1 , "Você Nasceu Dia" , idade_1,'/',idade_2,'/',idade_3 , "coroa")

#Exercicio 3
numero_1 = int(input('Digite um numero'))
numero_2 =  int(input ('Digite outro num'))        # Tipo primitivo int, tudo que tiver dentro dos parenteses será convertido para numero inteiro 
t = (numero_1 + numero_2)
print ('A soma é :' , t)


#tipos primitivos
# int = numeros inteiros 
#float = numeros reias, ponto flutuante 
#bool = valores lógicos, booleanos True and False 
#str = string = 'olá'    entre aspas 

# Tem que ser especificado o tipo da variavel que irá ser recebida pela variavel 





print ('a soma vale {}' .format(t))