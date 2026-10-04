from Packages.validações import *
from Packages.Pesquisar import PesquisarPessoa
from time import sleep as s

def Editar(opcao, lista):
    if opcao == 6:
        print('Voltando à página inicial. Aguarde...')
        s(1)
        return
    nome_busca = input('Digite o nome da pessoa que você quer editar: ')
    pessoa = PesquisarPessoa(nome_busca, lista)
    if not pessoa:
        return
    if opcao == 1:
        pessoa["Nome"] = ValidaNomeInformado('Digite o novo Nome: ')
        print('Nome alterado com sucesso!')
    elif opcao == 2:
        pessoa["Idade"] = ValidaIdadeInformada('Nova Idade: ')
        print('Idade alterada com sucesso!')
    elif opcao == 3:
        pessoa["Notas"][0] = ValidaNota('Nova 1º Nota: ')
        AtualizaMédiaESituação(pessoa)
        print('Primeira nota e média atualizadas com sucesso!')
    elif opcao == 4:
        pessoa["Notas"][1] = ValidaNota('Nova 2º Nota: ')
        AtualizaMédiaESituação(pessoa)
        print('Segunda nota e média atualizadas com sucesso!')
    elif opcao == 5:
        pessoa["Nome"] = ValidaNomeInformado('Digite o novo Nome: ')
        pessoa["Idade"] = ValidaIdadeInformada('Nova Idade: ')
        pessoa["Notas"][0] = ValidaNota('Nova 1º Nota: ')
        pessoa["Notas"][1] = ValidaNota('Nova 2º Nota: ')
        AtualizaMédiaESituação(pessoa)
        print('Todos os dados foram alterados com sucesso!')