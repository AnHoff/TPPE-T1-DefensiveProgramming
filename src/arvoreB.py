from noB import NoB
from imprimir import imprimir_horizontalmente, buscar_caminho

class ArvoreB:
    def __init__(self, t):
        self.raiz = NoB(t, True)
        self.t = t

    def buscar(self, k):
        return self.raiz.buscar(k)
    
    def buscar_caminho(self, k):
        buscar_caminho(self, k)

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

    def remover(self, k):
        if not self.raiz:
            return
        self.raiz.remover(k)
        if len(self.raiz.chaves) == 0:
            if self.raiz.folha:
                self.raiz = NoB(self.t, True)
            else:
                self.raiz = self.raiz.filhos[0]
    
    def imprimir(self):
        imprimir_horizontalmente(self)
