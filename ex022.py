nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome em minúsculas é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome.replace(' ',''))))
nome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(nome[0], len(nome[0])))