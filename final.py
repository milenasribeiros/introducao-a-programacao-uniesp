'''
Desenvolva um programa utilizando os recursos que já vimos: if, elif, else, while, for, listas, dicionários.
Não precisa utilizar todos, apenas os que julgar necessários.

Desenvolva um algoritmo que apresente as seguintes opções ao usuário:
1 - Cadastrar um funcionário
2 - Listar (imprimir) todos os funcionários
3 - Alterar um funcionário
4 - Excluir um funcionário
5 - Adicionar um aumento de salário


Sabendo que todos os funcionários cadastrados precisam ter no mínimo os dados: Código do Funcionário, Nome, 
E-mail, Data de Admissão e Salário.
'''

def cadastro():
    print('1 - Cadastrar funcionario.')
    print('2 - Listar funcionario.')
    print('3 - Alterar funcionario.')
    print('4 - Aumentar salario.')
    print('5 - Excluir funcionario.')
    print('0 - Finalizar.')

cadastro()
listar_cadastro = int(input('Digite uma das opções: '))

lista_de_funcinarios = {}

while listar_cadastro != -2:
    if listar_cadastro == 1:
        print('Para cadastrar um funcionario, precisamos das seguintes informações: ')
        codigo = input('Digite um codigo de cadastro para o funcionario: ')
        nome = input('Digite o nome completo do funcionário: ')
        email = input('Digite o email do funcionario: ')
        dataadm = input('Digite a data de cadastramento do funcionario: ')
        salario = input('Digite o salario do funcionario: ')
        lista_de_funcinarios[codigo] = {'nome': nome, 'email': email, 'dataadm': dataadm, 'salario': salario}
        cadastro()
        listar_cadastro = int(input('Digite uma das opções: '))
    
    elif listar_cadastro == 2:
        if lista_de_funcinarios == {}:
            print('Ainda nao temos funcionarios cadastrados.')
        else:
            print(lista_de_funcinarios)
        lista_de_funcinarios[codigo] = {'nome': nome, 'email': email, 'dataadm': dataadm, 'salario': salario}
        cadastro()
        listar_cadastro = int(input('Digite uma das opções: '))
    
    elif listar_cadastro == 3:
        print('Funcionarios da empresa: ')
        for funcionarios in lista_de_funcinarios:
            print(funcionarios)
        alt_dados = input('Digite o codigo do funcionario que deseja realizar alteração: ')
        print('Dados do funcionario.')
        print(lista_de_funcinarios[alt_dados])
        dado_alterado = input('Dado que será alterado: ')
        novo_dado = input('Digite a alteração desejada: ')
        lista_de_funcinarios[alt_dados][dado_alterado] = novo_dado
        print(lista_de_funcinarios[alt_dados])
        print('Dado(s) alterado(s) com sucesso!')
        cadastro()
        listar_cadastro = int(input('Digite uma das opções: '))
    
    elif listar_cadastro == 4:
        print('Qual funcionario receberá uma alteração no salario?')
        print(lista_de_funcinarios)
        fun_alt_salario = input('Digite o codigo do funcionario que terá o salario alterado: ')
        alt_salario = input('Digite o novo valor do salario: ')
        lista_de_funcinarios[fun_alt_salario]['salario'] = alt_salario
        print(lista_de_funcinarios)
        cadastro()
        listar_cadastro = int(input('Digite uma das opções: '))

    elif listar_cadastro == 5:
        print(lista_de_funcinarios)
        demitir_funcionario = input('Digite o codigo do funcionario que será demitido: ')
        lista_de_funcinarios.pop(demitir_funcionario)
        print(lista_de_funcinarios)
        print('Funcionario demitido com sucesso!')
        cadastro()
        listar_cadastro = int(input('Digite uma das opções: '))
        
    elif listar_cadastro == 0:
        print('Isso é tudo pessoal. Bom trabalho!')
        break

#Grupo: Pedro, Emanuel, Maria Eduarda e Milena 