n1 = int(input ('Digite um numero :'))
n2 = int(input ('Digite outro numero: '))
s = n1 +n2
# print ('a soma entre' , n1 , 'e' , n2 , 'é ', s) uma forma melhor de se escrever é colocando chaves e depois do .format se especifica o valor que vai ser inserido em sequencia.
print ('A soma entre o Valor {} e o valor {}, será de {}'.format(n1,n2,s))

#outro exemplo 
n = input('digite algo')
print (n.isnumeric()) #vai mostrar se o valor digitado for numerico 

n3 = input('digite algo')
print (n3.isalpha())    #vai mostrar se for letra

n4 = input('digite algo')
print (n4.isalnum())  # aceita alfa numerico tanto numerico, quanto alfa ou os dois 

# isupper é se é só maiuscula 