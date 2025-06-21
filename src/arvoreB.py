from noB import NoB
from balanceamento import ajustar_raiz
import icontract
from imprimir import imprimir_horizontalmente, buscar_caminho

def _validar_no(no, t, is_root=False):
    if is_root and no.folha and len(no.chaves) == 0:
        return True
    min_chaves = 1 if is_root else t - 1
    max_chaves = 2 * t - 1
    if not (min_chaves <= len(no.chaves) <= max_chaves):
        return False

    if any(no.chaves[i] >= no.chaves[i + 1] for i in range(len(no.chaves) - 1)):
        return False

    if no.folha:
        return len(no.filhos) == 0

    min_filhos = 2 if is_root else t
    max_filhos = 2 * t
    if not (min_filhos <= len(no.filhos) <= max_filhos):
        return False
    if len(no.filhos) != len(no.chaves) + 1:
        return False

    for i in range(len(no.chaves)):
        if max(no.filhos[i].chaves) >= no.chaves[i]:
            return False
        if min(no.filhos[i + 1].chaves) <= no.chaves[i]:
            return False

    return all(_validar_no(child, t) for child in no.filhos)


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

    @icontract.require(lambda self, k: self.buscar(k) is None, description="Chave já existente na árvore")
    @icontract.ensure(lambda self, k: _validar_no(self.raiz, self.t, True))
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
    @icontract.ensure(lambda self, k: _validar_no(self.raiz, self.t, True))
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
