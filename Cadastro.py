lista = []
def Cadastro(nota1, nota2, nome, idade, media, situacao, lista):
    dados = {}
    notas = []
    notas.append(nota1)
    notas.append(nota2)
    dados["Nome"] = nome
    dados["Idade"] = idade
    dados["Notas"] = notas
    dados["Média"] = media
    dados["Situação"] = situacao
    lista.append(dados.copy())