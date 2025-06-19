class No:

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
     
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)
        
        else:
            print(f"Valor {valor} já existe na árvore.")

    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)
        print() 

    def _em_ordem_recursivo(self, no_atual):
        if no_atual is not None:
            self._em_ordem_recursivo(no_atual.esquerda)
            print(no_atual.valor, end=' ')
            self._em_ordem_recursivo(no_atual.direita)

# Teste
if __name__ == "__main__":
    arvore = ArvoreBinaria()
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arvore.inserir(v)

    print("Percurso em ordem:")
    arvore.em_ordem()

