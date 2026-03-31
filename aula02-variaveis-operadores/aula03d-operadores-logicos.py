#logica

verifica_email = True #ou false
verifica_senha = False #ou false

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login: #nao printa se tiver um ou ambos false ali em cima
    print('entrar no programa')

#logica ou (or)

logica_ou = False or False or True
print(logica_ou)

#operador de negacao
negacao = not False
print(negacao)

if not verifica_login:
    print('loga certo ai')
