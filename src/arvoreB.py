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

@icontract.invariant(lambda self: self._todas_folhas_no_mesmo_nivel(), description="Todas as folhas devem estar no mesmo nível")
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

    def _todas_folhas_no_mesmo_nivel(self):
        niveis = []
        def _coletar_niveis_folhas(no, nivel):
            if no.folha:
                niveis.append(nivel)
            else:
                for filho in no.filhos:
                    _coletar_niveis_folhas(filho, nivel + 1)

        _coletar_niveis_folhas(self.raiz, 0)
        return len(niveis) == 0 or all(n == niveis[0] for n in niveis)

    def _get_altura(self, no=None):
        if no is None:
            no = self.raiz
        h = 0
        atual = no
        while not atual.folha:
            h += 1
            if not atual.filhos:
                return h
            atual = atual.filhos[0]
        return h

    def buscar(self, k):
        return self.raiz.buscar(k)
    
    def buscar_caminho(self, k):
        buscar_caminho(self, k)

    @icontract.require(lambda self, k: self.buscar(k) is None, description="Chave já existente na árvore")
    @icontract.ensure(
        lambda self, result:
            self._get_altura() == result or self._get_altura() == result + 1,
        description="Altura após inserção deve ser a mesma ou aumentar em 1"
    )
    @icontract.ensure(lambda self: _validar_no(self.raiz, self.t, True))
    def inserir(self, k):
        altura_antes = self._get_altura()
        
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.t) - 1:
            nova_raiz = NoB(self.t, False)
            nova_raiz.filhos.insert(0, raiz)
            nova_raiz.dividir_filho(0)
            self.raiz = nova_raiz
            nova_raiz.inserir_nao_cheio(k)
        else:
            raiz.inserir_nao_cheio(k)
        return altura_antes

    @icontract.require(lambda self, k: self.buscar(k) is not None, description="Chave deve existir na árvore")
    @icontract.ensure(
        lambda self, result:
            self._get_altura() == result or self._get_altura() == result - 1,
        description="Altura após remoção deve ser a mesma ou diminuir em 1"
    )
    @icontract.ensure(lambda self: _validar_no(self.raiz, self.t, True))
    def remover(self, k):
        altura_antes = self._get_altura()
        if not self.raiz:
            return altura_antes   
        self.raiz.remover(k)
        ajustar_raiz(self)

        if len(self.raiz.chaves) == 0:
            if self.raiz.folha:
                self.raiz = NoB(self.t, True)
            else:
                self.raiz = self.raiz.filhos[0]
        return altura_antes

    def imprimir(self):
        imprimir_horizontalmente(self)
