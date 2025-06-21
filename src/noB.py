import icontract
from balanceamento import *

# Invariantes estruturais do nó B
@icontract.invariant(lambda self: len(self.chaves) <= 2 * self.t - 1)
@icontract.invariant(lambda self: (self.folha or len(self.chaves) >= self.t - 1))
@icontract.invariant(lambda self: (self.folha and len(self.filhos) == 0) or (not self.folha and self.t <= len(self.filhos) <= 2 * self.t and len(self.filhos) == len(self.chaves) + 1))
@icontract.invariant(lambda self: all(self.chaves[i] < self.chaves[i+1] for i in range(len(self.chaves)-1)))
@icontract.invariant(lambda self: self.folha or all(
    (max(self.filhos[i].chaves) if self.filhos[i].chaves else float('-inf')) < self.chaves[i] < (min(self.filhos[i+1].chaves) if self.filhos[i+1].chaves else float('inf'))
    for i in range(len(self.chaves))
))
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
                dividir_filho(self, i)
                if k > self.chaves[i]:
                    i += 1
            self.filhos[i].inserir_nao_cheio(k)

    def dividir_filho(self, i):
        dividir_filho(self, i)

    def remover(self, k):
        t = self.t
        i = 0
        while i < len(self.chaves) and k > self.chaves[i]:
            i += 1

        if i < len(self.chaves) and self.chaves[i] == k:
            if self.folha:
                self.chaves.pop(i)
            else:
                if len(self.filhos[i].chaves) >= t:
                    pred = get_predecessor(self, i)
                    self.chaves[i] = pred
                    self.filhos[i].remover(pred)
                elif len(self.filhos[i + 1].chaves) >= t:
                    succ = get_sucessor(self, i)
                    self.chaves[i] = succ
                    self.filhos[i + 1].remover(succ)
                else:
                    fundir(self, i)
                    self.filhos[i].remover(k)
        else:
            if self.folha:
                return
            if len(self.filhos[i].chaves) < t:
                preencher(self, i)
            if i > len(self.chaves):
                self.filhos[i - 1].remover(k)
            else:
                self.filhos[i].remover(k)
