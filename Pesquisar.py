def PesquisarPessoa(busca, lista):
    """Busca pessoas na lista e retorna o dicionário da pessoa selecionada, ou None."""
    busca = busca.strip().lower()
    resultados = [pessoa for pessoa in lista if pessoa["Nome"].lower().startswith(busca)]
    if not resultados:
        print('A pessoa que você quer pesquisar não foi encontrada.')
        return None
    if len(resultados) == 1:
        pessoa_encontrada = resultados[0]
        MostrarResultado(pessoa_encontrada)
        return pessoa_encontrada
    print('\nMúltiplos cadastros encontrados:')
    for idx, pessoa in enumerate(resultados, start=1):
        print(f"[{idx}] {pessoa['Nome']} - Idade: {pessoa['Idade']}")
    while True:
        try:
            escolha = int(input('\nDigite o número do cadastro desejado: '))
            if 1 <= escolha <= len(resultados):
                pessoa_selecionada = resultados[escolha - 1]
                MostrarResultado(pessoa_selecionada)
                return pessoa_selecionada
            print('Número fora da lista. Tente novamente.')
        except ValueError:
            print('Digite apenas o número correspondente.')
def MostrarResultado(pessoa):
    print('\n--- Registro Encontrado ---')
    for chave, valor in pessoa.items():
        if chave == "Notas":
            print(f'Notas: {valor[0]} e {valor[1]}')
        elif chave == "Média":
            print(f'Média: {valor:.2f}')
        else:
            print(f'{chave}: {valor}')
    print('---------------------------\n')