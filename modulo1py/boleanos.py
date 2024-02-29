# Váriaveis Boleanas

# Definição 
# True e False

saldo_em_conta = 200
valor_do_saque = 200

pode_executar_saque = valor_do_saque <= saldo_em_conta
print(pode_executar_saque)

#cartão de credito
codigo_de_seguranca = '980'
codigo_de_seguranca_cadastro = '233'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

# tabela Verdade            A OR B |     A and B  &       NOT A not
# treu treu                 True        True            False
# treu false                False       False           False
# false false               False       False           True 
# false True                True        False           True

# Tabela verdade do operador (ou)
print(True | False)

#Tabela Verdade do operador & (e)
print(True & False)

# Tabela Verdade do operador not (não)
 
print(not True)

# String vazia e o numero 0 em boleano é convertido para um valor falso
 
usuario = 'mateuzao'
senha = 'mateus123'

usuario_cadastro = 'mateuzao'
senha_cadastro = 'mateus123'

login_usuario = usuario == usuario_cadastro
login_senha = senha == senha_cadastro
print(login_usuario)
print(login_senha)

conceder_acesso = login_usuario & login_senha 
print(conceder_acesso)