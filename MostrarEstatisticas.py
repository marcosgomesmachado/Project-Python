def MostrarEstatisticas(lista):
    if not lista:
        print('Não é possível exibir estatísticas, pois não há cadastros no sistema.')
        return
    total = len(lista)
    pessoa_mais_velha = max(lista, key=lambda p: p["Idade"])
    pessoa_mais_nova = min(lista, key=lambda p: p["Idade"])
    media_turma = sum(p["Média"] for p in lista) / total
    media_idade = sum(p["Idade"] for p in lista) / total
    aprovados = sum(1 for p in lista if p["Situação"] == 'Aprovado')
    reprovados = total - aprovados
    print('\n=============== ESTATÍSTICAS DA TURMA ===============')
    print(f'Total de cadastros:          {total}')
    print(f'Pessoa mais velha:           {pessoa_mais_velha["Nome"]} ({pessoa_mais_velha["Idade"]} anos)')
    print(f'Pessoa mais nova:            {pessoa_mais_nova["Nome"]} ({pessoa_mais_nova["Idade"]} anos)')
    print(f'Média de idade da turma:     {media_idade:.1f} anos')
    print(f'Média geral de notas:        {media_turma:.2f}')
    print(f'Alunos Aprovados:            {aprovados}')
    print(f'Alunos Reprovados:           {reprovados}')
    print('=====================================================\n')