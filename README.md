# T1: Defensive Programming
O presente repositório é dedicado à elaboração e entrega do Trabalho Prático 1 da disciplina Técnicas de Programação para Plataformas Emergentes da Universidade de Brasília.

O grupo é constituído por 4 pessoas, conforme se segue:

| Matrícula | Nome |
| -- | --|
| 202015901 | Ana Luiza Hoffmann Ferreira |
| 190086971 | Felipe Direito Corrieri de Macedo |
| 232014727 | Kauan de Torres Eiras |
| 190105071 | Davi Gonçalves Akegawa Pierre |

## Enunciado
Esse trabalho consiste na implementação da estrutura de dados Árvore-B e seus algoritmos, principais e auxiliares, com a utilização das técnicas de programação por contratos (Design by Contracts).

⚠️⚠️⚠️ Toda a estrutura da Árvore-B e suas operações deverão ser implementadas pelos grupos, utilizando o paradigma de orientação por objetos em seu desenvolvimento. Não serão aceitos trabalhos que utilize implementações de Árvore-B já disponibilizadas por bibliotecas.

Os trabalhos deverão ser desenvolvidos em Python3, com a utilização da biblioteca icontract para implementação dos contratos. Os contratos a serem implementados, descritos em termos de invariantes e pré- e pós-condições, estão apresentados na seção Pontuação e critérios de correção, apresentada em seguida.

Os elementos a serem inseridos na árvore são valores inteiros. Os grupos podem usar os valores apresentados no exemplo desse trabalho para que possam avaliar a implementação.

## Como rodar

```bash
# Instalar o icontract
pip install icontract

# executar exemplo
python3 src\main.py

# rodar testes
cd src
python3 arvore-b-test.py -v
```


## Resolução

A implementação encontra-se em `src/` e é composta pelos seguintes módulos principais:

| Arquivo | Responsabilidade |
| --- | --- |
| `arvoreB.py` | Classe `ArvoreB`, ponto de entrada das operações (inserir, remover, buscar) |
| `noB.py` | Classe `NoB`, representa nós internos/folhas |
| `balanceamento.py` | Funções auxiliares de split, merge e redistribuição |
| `imprimir.py` | Saídas de depuração da árvore (horizontal e caminho de busca) |
| `main.py` | Script-exemplo que constrói a árvore, remove e reinsere chaves |
| `arvore-b-test.py` | Testes unitários básicos |
