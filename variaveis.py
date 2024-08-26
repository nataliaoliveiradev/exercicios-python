##No código a seguir, estamos criando duas variáveis (não vamos tratar do tipo, ainda). A primeira tem nome disciplina. A outra se chama nota e armazena uma nota tirada por alguém que cursa a disciplina
disciplina = 'Lógica de Programação e Algoritmos'
nota = 8.5
print(disciplina)
print(nota)
##Douglas Adams nos ensinou que a resposta para o sentido da vida, do  Universo e tudo mais é 42. Armazene, então, em uma variável, o sentido da vida. Crie uma mensagem que imprima na tela essa variável, junto de uma frase dizendo que ela é o sentido da vida.
texto = 'O sentido da vida é'
sentido = 42
print(texto,sentido)
# Vejamos o exemplo em que a variável a contém o valor 1 e a variável b, o valor 5.
a = 1 #a recebe 1
b = 5 #b recebe 5
#resposta recebe o resultado da comparação lógica de igualdade
resposta = a == b 
print('A resposta é:', resposta)
# Crie uma variável que receba uma nota de um aluno. Crie outra variável  que receba o resultado de uma comparação lógica entre a nota escolhida e o valor 7, que é a média para aprovação. Caso a nota seja maior ou  igual a 7, o resultado deve ser verdadeiro. Imprima o resultado da comparação na tela.
nota_aluno = 6
media = 7
aprovacao = nota_aluno >= media
print('Você foi aprovado?', aprovacao)
#Podemos armazenar uma string em uma só variável no Python:
frase = 'Olá, mundo!'
print(frase[0])
print(frase[1])
print(frase[2])
print(frase[3])
print(frase[4])
print(frase[5])
print(frase[6])
print(frase[7])
print(frase[8])
print(frase[9])
#Concatenar strings significa juntá-las ou somá-las.
s1 = 'Lógica de Programação'
s1 = s1 + ' e Algoritmos'
print(s1)
#Podemos repetir uma mesma string várias vezes, na concatenação, utilizando o símbolo de multiplicação (*). No exemplo a seguir, multiplicou-se o caractere do tracejado dez vezes, facilitando sua escrita.
s2 = 'Squirtle' + '-' * 10 + 'Wartotle'+ '-' * 10 + 'Blastoise'
print(s2)
#Podemos, por exemplo, colocar o valor de uma variável dentro de uma outra variável que seja do tipo string. Utilizamos, para isso, um símbolo de percentual (%), que vamos chamar de marcador de posição. Esse símbolo será colocado dentro de nosso texto, no local exato onde o valor de uma variável deve aparecer
nota = 8.5
s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1)
#Se estivermos trabalhando com números de ponto flutuante, podemos delimitar quantas casas decimais queremos colocar na tela. Para isso, inserimos, entre o símbolo de percentual e a letra do tipo da variável, um ponto e um número. O número indica quantas casas decimais teremos. Se usarmos .2, teremos duas casas decimais aparecendo 
nota = 8.5
s1 = 'Você tirou %.2f na disciplina de Algoritmos' % nota
print(s1)
#Observe o exemplo, a seguir com duas variáveis, uma do tipo ponto flutuante e outra do tipo string:
nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou %d na disciplina de %s' % (nota, disciplina)
print(s1)
#Composição moderna:  ao invés de % dentro do texto, usamos chaves; ao invés do percentual fora do texto, usamos .format
nota = 8
disciplina = 'Algoritmos'
s1 = 'Você tirou {} na disciplina de {}'.format(nota,disciplina)
print(s1)
#Composição com f-string: As f-strings permitem que você insira expressões diretamente em literais de strings precedidas do caractere f. Dentro da string, você pode colocar expressões, entre chaves {} que serão avaliadas e substituídas pelos valores correspondentes, durante a execução do programa
nota = 8
disciplina = 'Algoritmos'
s1 = f'Você tirou {nota} na disciplina de {disciplina}'
print(s1)
#Sua vez de praticar!
# Crie três variáveis distintas: uma contendo o nome da sua comida favorita; outra contendo o seu ano de nascimento; e a terceira contendo o resultado da divisão do seu ano de nascimento pela sua idade. 
# Armazene, em uma quarta variável, do tipo string, uma mensagem que contenha todas as informações das variáveis anteriores.
# Resolva o exercício pela maneira clássica de composição e também pela maneira moderna e com f-string. 
#classico
comida = 'hambúrguer'
ano = 1996
idade = 28
divisao = ano / idade
variavel = comida,ano,idade,divisao
print(variavel)
s1 ='Clássico: minha idade é %d, minha comida favorita é %s e a divisão é %f'%(idade,comida,divisao)
print(s1)
#moderno
s1 ='Moderno: minha idade é {}, minha comida favorita é {} e a divisão é {}'.format(idade,comida,divisao)
print(s1)
#f-string
s1 =f'F-string: minha idade é {idade}, minha comida favorita é {comida} e a divisão é {divisao}'
print(s1)

#Fatiamento
s1 = 'Lógica de Programação e Algoritmos'
print(s1[0:6])
#É possível omitir o número da esquerda (início) ou o da direita (final) para representar tudo a partir do início, ou tudo até o final, respectivamente
s1 = 'Lógica de Programação e Algoritmos'
print(s1[:6])
#criamos uma variável denominada tamanho, que  recebe o resultado da função len de uma string s1. O resultado é que a string contém 34 caracteres. Atente-se ao fato de que caracteres como espaços também entram nessa contagem, afinal, também são codificados
s1 = 'Lógica de Programação e Algoritmos'
tamanho = len(s1)
print(tamanho)

# desenvolva um algoritmo que solicite ao usuário dois números inteiros. Imprima a soma desses dois números na tela
x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))
res = f'O resultado da soma de {x} com {y} é {x + y}.'
print(res)

#desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos. Calcule o total de segundos resultante e imprima-o na tela, para o usuário.
d = int(input('Digite um número de dias: '))
h = int(input('Digite um número de horas: '))
m = int(input('Digite um número de minutos: '))
s = int(input('Digite um número de segundos: '))
total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)
res = 'O total de segundos calculado é {}.'.format(total)
print(res)

#desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule-o e exiba o valor do desconto e o preço final do produto
preco = int(input('Digite o valor do produto: '))
p = int(input('Digite o percentual de desconto a ser aplicado: '))
desconto = preco * (p/100)
total = preco - desconto
res = 'O valor do desconto é {}, e o preço final do produto é {}.'.format(desconto,total)
print(res)

#desenvolva um algoritmo que converta uma temperatura de Celsius (C) em Fahrenheit (F).
C = float(input('Digite uma temperatura em Celsius: '))
F = ((9 * C/5) + 32)
print('Temperatura em Celsius: {}, temperatura em Fahrenheit: {}'.format(C,F))