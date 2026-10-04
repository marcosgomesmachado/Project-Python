from Packages.Pesquisar import PesquisarPessoa

def Deletar(lista):
    if not lista:
        print('Não é possível deletar, pois o sistema ainda não possui cadastros.')
        return
    nome_para_deletar = input('Digite o nome da pessoa que quer deletar: ')
    pessoa = PesquisarPessoa(nome_para_deletar, lista)
    if pessoa:
        while True:
            confirmar = input(f'Tem certeza que deseja deletar "{pessoa["Nome"]}"? [S/N]: ').strip().lower()
            if confirmar in ['s', 'n']:
                break
            print('Opção inválida. Digite apenas S ou N.')
        if confirmar == 's':
            lista.remove(pessoa)
            print('Pessoa removida com sucesso!')
        else:
            print('Operação cancelada.')