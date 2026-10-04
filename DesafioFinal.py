from Packages.Cadastro import Cadastro
from Packages.Listar import ListarPessoa
from Packages.Pesquisar import PesquisarPessoa
from Packages.MostrarEstatisticas import MostrarEstatisticas
from Packages.Editar import Editar
from Packages.Delete import Deletar
from Packages.Sair import Sair  
from Packages.Menu import CriaMenu
from Packages.MenuDeEdição import CriaMenuDeEdição
from Packages.validações import *
from time import sleep as s

lista = []

while True:
    s(0.5)
    CriaMenu()
    opcao = ValidarOpcaoEscolhida(max_opcao=7)
    if opcao == 1:
        nome = ValidaNomeInformado()
        idade = ValidaIdadeInformada()
        nota1 = ValidaNota('1º Nota: ')
        nota2 = ValidaNota('2º Nota: ')
        media = CalculaMedia(nota1, nota2)
        situacao = VerificaSituacao(media)
        Cadastro(nota1, nota2, nome, idade, media, situacao, lista)
    elif opcao == 2:
        ListarPessoa(lista)
    elif opcao == 3:
        if not lista:
            print('O sistema ainda não possui cadastros.')
            continue
        nome_busca = input('Digite o nome da pessoa que quer pesquisar: ')
        PesquisarPessoa(nome_busca, lista)
    elif opcao == 4:
        MostrarEstatisticas(lista)
    elif opcao == 5:
        if not lista:
            print('O sistema ainda não possui cadastros para editar.')
            continue
        CriaMenuDeEdição()
        opcao_edicao = ValidarOpcaoEscolhida(max_opcao=6)
        Editar(opcao_edicao, lista)
    elif opcao == 6:
        Deletar(lista)
    elif opcao == 7:
        break
Sair()