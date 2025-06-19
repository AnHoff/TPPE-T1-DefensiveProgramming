class NoB:
    def __init__(self, t, folha=False):
        self.t = t  
        self.folha = folha 
        self.chaves = [] 
        self.filhos = []

    def buscar(self, k):
        i = 0
        while i < len(self.chaves) and k > self.chaves[i]:
            i += 1

        if i < len(self.chaves) and self.chaves[i] == k:
            return self

        if self.folha:
            return None
        return self.filhos[i].buscar(k)

    def inserir_nao_cheio(self, k):
        i = len(self.chaves) - 1

        if self.folha:
            self.chaves.append(None)
            while i >= 0 and k < self.chaves[i]:
                self.chaves[i + 1] = self.chaves[i]
                i -= 1
            self.chaves[i + 1] = k
        else:
            while i >= 0 and k < self.chaves[i]:
                i -= 1
            i += 1
            if len(self.filhos[i].chaves) == (2 * self.t) - 1:
                self.dividir_filho(i)
                if k > self.chaves[i]:
                    i += 1
            self.filhos[i].inserir_nao_cheio(k)

    def dividir_filho(self, i):
        t = self.t
        y = self.filhos[i]
        z = NoB(t, y.folha)
        self.filhos.insert(i + 1, z)
        self.chaves.insert(i, y.chaves[t - 1])

        z.chaves = y.chaves[t:(2 * t - 1)]
        y.chaves = y.chaves[0:t - 1]

        if not y.folha:
            z.filhos = y.filhos[t:(2 * t)]
            y.filhos = y.filhos[0:t]


class ArvoreB:
    def __init__(self, t):
        self.raiz = NoB(t, True)
        self.t = t

    def buscar(self, k):
        return self.raiz.buscar(k)

    def inserir(self, k):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.t) - 1:
            nova_raiz = NoB(self.t, False)
            nova_raiz.filhos.insert(0, raiz)
            nova_raiz.dividir_filho(0)
            self.raiz = nova_raiz
            nova_raiz.inserir_nao_cheio(k)
        else:
            raiz.inserir_nao_cheio(k)

    def imprimir(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
        print("Nível", nivel, ":", no.chaves)
        if not no.folha:
            for filho in no.filhos:
                self.imprimir(filho, nivel + 1)

if __name__ == "__main__":
    btree = ArvoreB(t=2)  # Grau mínimo t = 2

    elementos = [10, 20, 5, 6, 12, 30, 7, 17]
    for elem in elementos:
        btree.inserir(elem)

    print("Árvore-B construída:")
    btree.imprimir()

    print("\n Buscando valores:")
    print("Busca por 6:", "Encontrado" if btree.buscar(6) else "Não encontrado")
    print("Busca por 15:", "Encontrado" if btree.buscar(15) else "Não encontrado")

