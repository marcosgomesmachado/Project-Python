# 📚 Sistema de Gerenciamento

## 📌 Sobre o projeto

Este projeto consiste em um **Sistema de Gerenciamento de Pessoas**, desenvolvido inicialmente em **Python**, com o objetivo de colocar em prática os conhecimentos adquiridos durante o curso de **Python do Curso em Vídeo — Mundo 3**.

O sistema funciona através do terminal e permite realizar operações de cadastro, consulta, edição, exclusão e visualização de estatísticas dos dados cadastrados.

Esta é a **primeira versão do projeto**. A ideia é continuar evoluindo o sistema conforme novos conhecimentos de programação forem adquiridos.

---

## 🎯 Objetivo

O principal objetivo é desenvolver um sistema funcional utilizando conceitos fundamentais de Python, como:

* Variáveis e tipos de dados;
* Estruturas condicionais;
* Estruturas de repetição;
* Funções;
* Listas;
* Tuplas;
* Dicionários;
* Módulos e pacotes;
* Importação de funções;
* Validação de dados;
* Organização do código em diferentes arquivos;
* Operações de CRUD.

---

## ⚙️ Funcionalidades

### 👤 Cadastro

Permite cadastrar uma nova pessoa informando:

* Nome;
* Idade;
* Primeira nota;
* Segunda nota.

A partir das notas informadas, o sistema calcula automaticamente a média e determina a situação da pessoa.

### 🔎 Pesquisa

Permite pesquisar pessoas cadastradas pelo nome.

Quando existem vários resultados para uma mesma pesquisa, o sistema permite que o usuário escolha qual pessoa deseja acessar.

### 📋 Listagem

Exibe as pessoas cadastradas no sistema e suas respectivas informações.

### ✏️ Edição

Permite alterar os dados de uma pessoa cadastrada.

É possível editar:

* Nome;
* Idade;
* Primeira nota;
* Segunda nota;
* Todos os dados simultaneamente.

Quando as notas são alteradas, a média e a situação da pessoa também são atualizadas.

### 🗑️ Exclusão

Permite excluir uma pessoa cadastrada no sistema.

### 📊 Estatísticas

O sistema também possui funções para obter informações gerais sobre os dados cadastrados, como:

* Total de pessoas;
* Maior idade;
* Menor idade;
* Média das notas;
* Média das idades;
* Pessoa mais velha;
* Pessoa mais nova;
* Quantidade de aprovados;
* Quantidade de reprovados.

---

## 🗂️ Estrutura do projeto

O projeto foi dividido em diferentes módulos para facilitar a organização e manutenção do código.

```
Sistema de Gerenciamento/
│
├── DesafioFinal.py
│
└── Packages/
    ├── Cadastro.py
    ├── Editar.py
    ├── Listar.py
    ├── Menu.py
    ├── MenuDeEdicao.py
    ├── Pesquisar.py
    ├── MostrarEstatisticas.py
    ├── Sair.py
    └── validacoes.py
```

> A estrutura pode sofrer alterações conforme o projeto for evoluindo.



## 🛠️ Tecnologias utilizadas

* **Python**
* **VS Code**
* **Terminal**



## 📖 Origem do projeto

Este projeto foi desenvolvido como um **desafio final de prática do estudo de Python**, utilizando os conhecimentos adquiridos ao longo do **Mundo 3 do Curso em Vídeo**.

O projeto foi construído de forma incremental, adicionando funcionalidades conforme novos conceitos eram aprendidos.



## 🚀 Próximas versões

A primeira versão do sistema está concluída, mas o projeto continuará sendo desenvolvido.

### Versão 2

* [ ] Reestruturar o projeto utilizando POO;
* [ ] Criar classes e objetos;
* [ ] Melhorar a organização interna do sistema;
* [ ] Implementar persistência utilizando **banco de dados**.

### Versão 3

* [ ] Transformar o sistema em uma aplicação web;
* [ ] Utilizar Flask;
* [ ] Criar interface com HTML e CSS;
* [ ] Utilizar banco de dados;
* [ ] Implementar arquitetura MVC.



## 📈 Evolução planejada

A ideia é utilizar este mesmo projeto como uma forma de acompanhar minha evolução na programação.


Python básico
      ↓
Funções e módulos
      ↓
CRUD
      ↓
POO
      ↓
Banco de dados
      ↓
Flask
      ↓
HTML + CSS
      ↓
MVC
      ↓
Sistema Web completo


Dessa forma, o projeto não será apenas um exercício final, mas um projeto que continuará sendo aprimorado conforme novos conhecimentos forem adquiridos.



👨‍💻 Status

**Versão atual: 1.0 — CRUD funcional**

O sistema possui as principais operações de gerenciamento de dados funcionando através do terminal.

> 🚧 Projeto em desenvolvimento — novas funcionalidades e melhorias serão adicionadas futuramente.
