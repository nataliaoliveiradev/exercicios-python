def realce(texto):
    print('+' + '-' * (len(texto) + 2) + '+')
    print('| ' + texto + ' |')
    print('+' + '-' * (len(texto) + 2) + '+')

def imprimir_menu():
    realce("Bem-vindo à Loja de Marmitas da Natalia Schillreff Oliveira")
    realce("Cardápio")
    print("|---------------------------------------------------|")
    print("| Tamanho | Bife Acebolado (BA)| Filé de Frango (FF)|")
    print("|---------|--------------------|--------------------|")
    print("|    P    | R$ 16,00           | R$ 15,00           |")
    print("|    M    | R$ 18,00           | R$ 17,00           |")
    print("|    G    | R$ 22,00           | R$ 21,00           |")
    print("|---------------------------------------------------|")

imprimir_menu()



valorDoPedido = 0
while True:
    sabor = input('Selecione um sabor (BA/FF): ')
    while ((sabor != 'BA') and (sabor != 'FF')):
        print('Sabor inválido. Tente novamente')
        sabor = input('Selecione um sabor (BA/FF): ')

    tamanho = input('Selecione o tamanho desejado (P/M/G): ')
    while ((tamanho != 'P') and (tamanho != 'M') and (tamanho != 'G')):
        print('Tamanho inválido. Tente novamente')
        tamanho = input('Selecione o tamanho desejado (P/M/G): ')
    
    if sabor == 'BA':
        if tamanho == 'P':
            preco = 16.00
        elif tamanho == 'M':
            preco = 18.00
        elif tamanho == 'G':
            preco = 22.00
        print('Você pediu um Bife Acebolado no tamanho {}, totalizando R$ {:.2f}'.format(tamanho, preco))
        valorDoPedido = valorDoPedido + preco
    elif sabor == 'FF':
        if tamanho == 'P':
            preco = 15.00
        elif tamanho == 'M':
            preco = 17.00
        elif tamanho == 'G':
            preco = 21.00
        print('Você pediu um Filé de Frango no tamanho {}, totalizando R$ {:.2f}'.format(tamanho, preco))
        valorDoPedido += preco
    resposta = input('Deseja pedir mais alguma coisa? (S/N): ')
    while ((resposta != 'S') and (resposta != 'N')):
        print('Comando inválido. Tente novamente')
        resposta = input('Deseja pedir mais alguma coisa? (S/N): ')
    if (resposta == 'N'):
        break
    elif (resposta == 'S'):
        continue      
print('O valor total do seu pedido é R$ {:.2f}'.format(valorDoPedido))



