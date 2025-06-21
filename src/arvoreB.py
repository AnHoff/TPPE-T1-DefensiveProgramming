from noB import NoB
from balanceamento import ajustar_raiz
import icontract
from imprimir import imprimir_horizontalmente, buscar_caminho

@icontract.invariant(lambda self:
    (self.raiz.folha and len(self.raiz.chaves) == 0 and len(self.raiz.filhos) == 0) or
    (
        1 <= len(self.raiz.chaves) <= 2 * self.t - 1 and (
            (self.raiz.folha and len(self.raiz.filhos) == 0) or
            (not self.raiz.folha and 2 <= len(self.raiz.filhos) <= 2 * self.t)
        )
    )
)
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

    @icontract.require(lambda self, k: self.buscar(k) is not None, description="Chave deve existir na árvore")
    @icontract.ensure(lambda self, k: len(self.raiz.chaves) <= 2 * self.t - 1)
    def remover(self, k):
        if not self.raiz:
            return
        self.raiz.remover(k)
        ajustar_raiz(self)

        if len(self.raiz.chaves) == 0:
            if self.raiz.folha:
                self.raiz = NoB(self.t, True)
            else:
                self.raiz = self.raiz.filhos[0]
    
    def imprimir(self):
        imprimir_horizontalmente(self)
