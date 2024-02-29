nome = "mateus"
sobrenome = 'marques'

# para concatenar sem que necessite do ++  é necessário colocar a letra f e as variaveis em {}

apresentacao = f'Olá meu nome é {nome} {sobrenome}'
print(apresentacao)

#Operação de fatiamento, sendo possivel extrair um caractere ou um trecho de uma string

email = "mateusmarques@hotmail.com"

print("0: " + email[0])

#Se utilizar indicativos negativos será contado ao contrtio 
print("0: " + email[-2])

email_usuario = email[0:13] # final -1 = fatiamento por intervalo
print(email_usuario)

# Métodos 
endereco = "Rua Elzo oliva martins , 11292 , Cuiabá , Mato Grosso , Brasil. "
# O metodos upper coloca todas as letras em maiúculo
print(endereco.upper())

# Método find, busca dentro da string a string que está dentro do método -- retorna -1 se não houver a string --  se houver retorna a posição da primeira letra
posicao = endereco.find('Cuiabá')
print(posicao)

# Substituição de uma string por outra replace
print(endereco.replace("Rua" , "Avenida")) 

#CONVERSÃO  
idade = 15
print(type(idade))

idade = str(idade)
print(type(idade))
#extraindo valores e transformando prar inteiro 
faturamento = 'R$ 35 bilhões '
print(faturamento)
print(type(faturamento))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))


#exercicio Problema, colocar a longitude e latude separados , 0:posicao_car_divisao é até onde tem o ; -1 e 
# posicao_car_divisao+1:len é da ; com +1 e o len é a extenção da string indicando o ultimo caractere

lon = '9821445'
lat = '-32032'

latlon = '-232323 ; 2309203'

posicao_char_divisao = latlon.find(';')
print(posicao_char_divisao)

lat_startup = latlon[0:posicao_char_divisao]
print(lat_startup)

lon_startup = latlon[posicao_char_divisao+1:len(latlon)]
print(lon_startup)

