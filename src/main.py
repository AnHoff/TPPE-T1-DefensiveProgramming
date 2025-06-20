from arvoreB import ArvoreB
from noB import NoB

if __name__ == "__main__":
    btree = ArvoreB(t = 2)  # Grau mínimo t = 2

    elementos = [40, 20, 60, 80, 10, 15, 30, 50, 70, 90, 95, 5, 7, 12, 18, 25, 35, 45, 55, 65, 75, 85, 92, 98, 99]
    for elem in elementos:
        btree.inserir(elem)

    print("Árvore-B construída:")
    btree.imprimir_horizontalmente()

    print("\n\nBuscando valores:")
    print("Busca por 6:", "Encontrado" if btree.buscar(6) else "Não encontrado")
    print("Busca por 15:", "Encontrado" if btree.buscar(15) else "Não encontrado")

    elementos = [60, 92]
    for elem in elementos:
        btree.remover(elem)

    print("\n\nÁrvore-B com elementos removidos:")
    btree.imprimir_horizontalmente()

    for elem in elementos:
        btree.inserir(elem)

    print("\n\nÁrvore-B com elementos re-inseridos:")
    btree.imprimir_horizontalmente()