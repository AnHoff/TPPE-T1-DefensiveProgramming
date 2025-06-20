from noB import NoB

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

    def remover(self, k):
        if not self.raiz:
            return
        self.raiz.remover(k)
        if len(self.raiz.chaves) == 0:
            if self.raiz.folha:
                self.raiz = NoB(self.t, True)
            else:
                self.raiz = self.raiz.filhos[0]

    def imprimir_horizontalmente(self):
        linhas = self._formatar_arvore(self.raiz)
        for linha in linhas:
            print(linha)

    def _formatar_arvore(self, no):
        if no.folha:
            conteudo = f"[{', '.join(map(str, no.chaves))}]"
            return [conteudo]

        filhos_formatados = [self._formatar_arvore(filho) for filho in no.filhos]
        alturas = [len(f) for f in filhos_formatados]
        altura_max = max(alturas)

        for i, filho in enumerate(filhos_formatados):
            while len(filho) < altura_max:
                filhos_formatados[i].append(" " * len(filho[0]))

        largura_filhos = [len(f[0]) for f in filhos_formatados]
        espacamento = 4

        total_largura = sum(largura_filhos) + espacamento * (len(filhos_formatados) - 1)
        linha_no = f"[{', '.join(map(str, no.chaves))}]".center(total_largura)

        linha_conexao = ""
        pos = 0
        for i, largura in enumerate(largura_filhos):
            meio_filho = pos + largura // 2
            linha_conexao += " " * (meio_filho - len(linha_conexao))
            pos += largura + espacamento

        linhas_filhos = []
        for i in range(altura_max):
            linha = ""
            for j, filho in enumerate(filhos_formatados):
                linha += filho[i]
                if j < len(filhos_formatados) - 1:
                    linha += " " * espacamento
            linhas_filhos.append(linha)

        return [linha_no, linha_conexao] + linhas_filhos


