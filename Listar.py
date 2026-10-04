def ListarPessoa(lista):
    if not lista:
        print('Não é possível listar, pois o sistema não tem cadastros.')
        return

    print('\n================ LISTA DE CADASTROS ================')
    for idx, pessoa in enumerate(lista, start=1):
        print(f'--- Pessoa #{idx} ---')
        print(f'Nome:     {pessoa["Nome"]}')
        print(f'Idade:    {pessoa["Idade"]}')
        print(f'Notas:    {pessoa["Notas"][0]} | {pessoa["Notas"][1]}')
        print(f'Média:    {pessoa["Média"]:.2f}')
        print(f'Situação: {pessoa["Situação"]}')
        print('-' * 25)
    print('====================================================\n')