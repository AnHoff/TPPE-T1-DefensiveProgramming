def get_predecessor(no, i):
    atual = no.filhos[i]
    while not atual.folha:
        atual = atual.filhos[-1]
    return atual.chaves[-1]

def get_sucessor(no, i):
    atual = no.filhos[i + 1]
    while not atual.folha:
        atual = atual.filhos[0]
    return atual.chaves[0]

def fundir(no, i):
    filho = no.filhos[i]
    irmao = no.filhos[i + 1]
    filho.chaves.append(no.chaves[i])
    filho.chaves.extend(irmao.chaves)
    if not filho.folha:
        filho.filhos.extend(irmao.filhos)
    no.chaves.pop(i)
    no.filhos.pop(i + 1)

def preencher(no, i):
    t = no.t
    if i != 0 and len(no.filhos[i - 1].chaves) >= t:
        pegar_do_irmao_esquerdo(no, i)
    elif i != len(no.chaves) and len(no.filhos[i + 1].chaves) >= t:
        pegar_do_irmao_direito(no, i)
    else:
        if i != len(no.chaves):
            fundir(no, i)
        else:
            fundir(no, i - 1)

def pegar_do_irmao_esquerdo(no, i):
    filho = no.filhos[i]
    irmao = no.filhos[i - 1]
    filho.chaves.insert(0, no.chaves[i - 1])
    if not filho.folha:
        filho.filhos.insert(0, irmao.filhos.pop())
    no.chaves[i - 1] = irmao.chaves.pop()

def pegar_do_irmao_direito(no, i):
    filho = no.filhos[i]
    irmao = no.filhos[i + 1]
    filho.chaves.append(no.chaves[i])
    if not filho.folha:
        filho.filhos.append(irmao.filhos.pop(0))
    no.chaves[i] = irmao.chaves.pop(0)

def dividir_filho(pai, i):
    from noB import NoB 

    t = pai.t
    y = pai.filhos[i]
    z = NoB(t, y.folha)

    pai.filhos.insert(i + 1, z)
    pai.chaves.insert(i, y.chaves[t - 1])

    z.chaves = y.chaves[t:(2 * t - 1)]
    y.chaves = y.chaves[0:t - 1]

    if not y.folha:
        z.filhos = y.filhos[t:(2 * t)]
        y.filhos = y.filhos[0:t]
