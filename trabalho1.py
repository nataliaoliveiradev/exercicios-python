#Mensagens de boas-vindas
print('Bem-vindos à loja da Natalia Schillreff Oliveira')
#Input do valor do pedido e quantidade de parcelas
valorDoPedido = float(input('Digite o valor do pedido: '))
quantidadeParcelas = int(input('Digite um número de parcelas: '))
# Cálculo da taxa de juros com base na quantidade de parcelas escolhida
#Estrutura condicional para cálculo da taxa de juros
#Se a quantidade de parcelas for menor que 4, o Juros será de 0% (0 / 100);
if quantidadeParcelas < 4:
    taxaDeJuros = 0
#Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4% (4 / 100)
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    taxaDeJuros = 4/100
#Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8% (8 / 100);
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    taxaDeJuros = 8/100
#Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16% (16 / 100);
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    taxaDeJuros = 16/100
#Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32% (32 / 100);
else:
    taxaDeJuros = 32/100
#Cálculo dos Valores
valorTotal = ((valorDoPedido * taxaDeJuros) + valorDoPedido)
valorDaParcela = (valorTotal / quantidadeParcelas)
#Saída de console com o valor das parcelas e valor total do parcelamento
print('O valor das parcelas é de: {:.2f} e o valor total parcelado é de: {:.2f}'.format(valorDaParcela,valorTotal))
