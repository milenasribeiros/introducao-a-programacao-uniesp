#1 - Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, 
#para evitar confusão, chame este dicionário de glossário.

#a - Pense em cinco palavras relacionada à programação que você conheceu nesta 
#disciplina. Use estas palavras como chaves em seu glossário e armazene seus 
#significados como valores.


glossario = {
'Algoritmo: ':'É um conjunto de etapas ou passos que nos permitem concluir uma tarefa específica.', 
'Programação: ':'É o processo de criação de um conjunto de instruções que dizem ao computador como realizar uma tarefa.',
'Variável: ':'Um dado que tem a possibilidade de ser alterado em algum instante no decorrer do tempo, dentro do algoritmo que está inserido.',
'Listas: ':' É uma sequência ou coleção ordenada de valores de qualquer tipo ou classe.',
'Matrizes: ':'Uma estrutura que precisasse de mais de um índice, [...], seria denominada estrutura composta multidimensional.',
'Operadores Aritméticos: ':'São aqueles que estudamos na escola, aquelas funções básicas de somar, subtrair, multiplicar, dividir e etc.'}


#b- Mostre cada palavra e seu significado em uma saída, formate a saída de uma 
#forma bem elegante. Por exemplo: você pode exibir a palavra seguida de 
#dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e 
#então exibir seu significado identado em uma segunda linha. Utilize o 
#caractere de quebra de linha (\n) para inserir uma linha em branco entre cada 
#par palavra-significado em sua saída.

#c - Sugestões de termos: Algoritmos, Python, Webscraping, Lógica de 
#Programação, Google Colab, Visual Studio Code.
print("------------------------------------------------------------------------------------------------------------------------------------")
print("Este dicionário foi desenvolvido através do conhecimento que foi obtido durantes as aulas da Disciplina de Introdução a Programação.")
print("------------------------------------------------------------------------------------------------------------------------------------")

for x, y in glossario.items():
    print(x,y)


