# Impressão horizontal
def formatar_arvore(self, no):
    if no.folha:
        conteudo = f"[{', '.join(map(str, no.chaves))}]"
        return [conteudo]

    filhos_formatados = [formatar_arvore(self, filho) for filho in no.filhos]
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

def imprimir_horizontalmente(self):
    linhas = formatar_arvore(self, self.raiz)
    for linha in linhas:
        print(linha)

# Impressão vertical para resultado da busca
def buscar_caminho(arvore, chave):
    def _buscar_caminho(no, chave, prefixo="", eh_ultimo=True):
        marcador = "└── " if eh_ultimo else "├── "
        print(prefixo + marcador + "[" + ", ".join(map(str, no.chaves)) + "]")

        if chave in no.chaves:
            return True

        if no.folha:
            return False

        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1

        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")

        for j, filho in enumerate(no.filhos):
            if j == i:
                ultimo_filho = (j == len(no.filhos) - 1)
                return _buscar_caminho(filho, chave, novo_prefixo, ultimo_filho)
        return False

    _buscar_caminho(arvore.raiz, chave)