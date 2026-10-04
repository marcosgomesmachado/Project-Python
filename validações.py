import re

def ValidarOpcaoEscolhida(max_opcao=7):
    while True:
        try:
            opcao = int(input('Escolha: '))
            if 1 <= opcao <= max_opcao:
                return opcao
            print('Opção inválida. Escolha um número dentro do menu.')  
        except ValueError:
            print('Problema com o tipo de dado informado. Digite um número inteiro.')

def ValidaNomeInformado(txt='Nome: '):
    padrao = r"^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ ]+$"
    while True:
        try:
            nome = input(txt).strip()
            if not nome:
                raise ValueError('A entrada do nome não pode ficar vazia.')
            if not re.match(padrao, nome):
                raise ValueError('O nome não deve conter números ou caracteres especiais.')
            return nome.title()
        except ValueError as erro:
            print(f'Erro: {erro}')

def ValidaIdadeInformada(txt='Idade: '):
    while True:
        try:
            idade = int(input(txt))
            if 0 <= idade <= 120:
                return idade
            print('Idade inválida. Digite um valor entre 0 e 120.')
        except ValueError:
            print('Problema com o tipo de dado informado. Digite um número inteiro.')

def ValidaNota(txt='Nota: '):
    while True:
        try:
            nota = float(input(txt))
            if 0.0 <= nota <= 10.0:
                return nota
            print('Nota inválida. A nota deve ser entre 0.0 e 10.0.')
        except ValueError:
            print('Problema com o tipo de dado informado. Digite um número decimal/inteiro.')

def CalculaMedia(nota1, nota2):
    return (nota1 + nota2) / 2

def VerificaSituacao(media):
    return 'Aprovado' if media >= 6.0 else 'Reprovado'

def AtualizaMédiaESituação(pessoa):
    pessoa["Média"] = CalculaMedia(pessoa["Notas"][0], pessoa["Notas"][1])
    pessoa["Situação"] = VerificaSituacao(pessoa["Média"])