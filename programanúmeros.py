um = int(input('Digite um valor: '))
dois = int(input('Digite outro valor: '))
enquanto = ''
enquanto2 = ''
escolha2 = ''
escolha3 = [1, 2, 3, 4]
print('O que você deseja?')
print('''
      [ 1 ] Somar
      [ 2 ] multiplicar
      [ 3 ] Maior
      [ 4 ] Novos números
      [ 5 ] Sair do programa''''')
escolha = int(input('Escolha uma opção: '))
if escolha == 1:
    um += dois 
    print('O resultado da soma dos números é {}'.format(um))
if escolha == 2:
    um *= dois
    print('O resultado da multiplicação é {}'.format(um))
if escolha == 3:
    maior_numero = max(um, dois)
    print('O maior número é {}'.format(maior_numero))
if escolha == 4:
    while escolha == 4:
        mais_numero = int(input('Digite os valores: '))
        enquanto = str(input('Quer adicionar mais números: ')).upper()
        if enquanto == 'NAO':
            print('''OPÇÕES
                  [ 1 ] SOMA
                  [ 2 ] MULTIPLICAÇÃO
                  [ 3 ] MAIOR
                  [ 4 ] SAIR DO PROGRAMA''')
            escolha2 = int(input('Escolha uma opção: '))
        if escolha2 != escolha3:
            print('Número invalido')
        if escolha2 == 1:
            um += dois + mais_numero
            print('O resultado da soma dos algaritimos é de {}'.format(um)) 
        if escolha2 == 2:
            um *= dois * mais_numero
            print('O resultado da multiplicação dos algaritimos é de {}'.format(um))
        if escolha2 == 3:
            maior = max(um, dois, mais_numero)
            print('O maior número é {}'.format(maior))
        if escolha2 == 4:
            print('Obrigado pela atenção')
            break
if escolha == 5: 
    print('Obrigado pela ateção!!')
print('FIM')
