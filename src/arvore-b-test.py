import unittest
from arvoreB import ArvoreB
from noB import NoB

class TesteArvoreB(unittest.TestCase):

    def assert_root_invariant(self, b):
        raiz = b.raiz
        t = b.t
        self.assertLessEqual(len(raiz.chaves), 2 * t - 1,
                             f"Raiz com muitas chaves: {len(raiz.chaves)} > {2*t-1}")
        if not raiz.folha:
            self.assertGreaterEqual(len(raiz.chaves), 1,
                                    "Raiz interna precisa de ao menos 1 chave")

    def conta_altura(self, no):
        h = 0
        atual = no
        while not atual.folha:
            h += 1
            atual = atual.filhos[0]
        return h

    def setUp(self):
        self.b = ArvoreB(t=2)
        for v in [10, 20, 5, 6, 12, 30, 7, 17]:
            self.b.inserir(v)

    def test_busca_existente(self):
        for v in [10, 20, 5, 6, 12, 30, 7, 17]:
            self.assertIsNotNone(self.b.buscar(v), f"Valor {v} deveria estar na árvore")

    def test_busca_inexistente(self):
        for v in [1, 9, 100]:
            self.assertIsNone(self.b.buscar(v), f"Valor {v} não deveria estar na árvore")

    def test_chaves_ordenadas_nos_nos(self):
        def verificar_ordenacao(no):
            self.assertEqual(no.chaves, sorted(no.chaves), f"Chaves do nó não estão ordenadas: {no.chaves}")
            if not no.folha:
                for filho in no.filhos:
                    verificar_ordenacao(filho)
        verificar_ordenacao(self.b.raiz)

    def test_root_invariant_e_altura(self):
        b = ArvoreB(t=3)
        alturas = []
        for k in range(100):
            altura_antes = self.conta_altura(b.raiz)
            b.inserir(k)
            self.assert_root_invariant(b)
            altura_depois = self.conta_altura(b.raiz)
            self.assertIn(altura_depois - altura_antes, (0, 1),
                          "Altura aumentou mais que 1 após inserção")

    def test_altura_folhas_iguais(self):
        alturas = []

        def visitar(no, nivel):
            if no.folha:
                alturas.append(nivel)
            else:
                for filho in no.filhos:
                    visitar(filho, nivel + 1)

        visitar(self.b.raiz, 0)
        self.assertTrue(all(h == alturas[0] for h in alturas),
                        "Todas as folhas devem estar na mesma altura")

    def test_insercao_duplicada_violacao(self):
        with self.assertRaises(Exception):
            self.b.inserir(10)

    def test_overflow_aumenta_altura_da_raiz(self):
        b = ArvoreB(t=2)
        altura_antes = self.conta_altura(b.raiz)
        for k in range(50):
            b.inserir(k)
        altura_depois = self.conta_altura(b.raiz)
        self.assertGreaterEqual(altura_depois, altura_antes + 1)

    def test_underflow_diminui_altura_da_raiz(self):
        b = ArvoreB(t=2)
        valores = list(range(50))
        for k in valores:
            b.inserir(k)
        altura_inicial = self.conta_altura(b.raiz)
        for k in reversed(valores):
            b.remover(k)
        altura_final = self.conta_altura(b.raiz)
        self.assertLess(altura_final, altura_inicial)

    def test_fuzzing_inserir_remover(self):
        import random
        b = ArvoreB(t=2)
        dados = list(range(100))
        random.shuffle(dados)
        for k in dados:
            b.inserir(k)
        random.shuffle(dados)
        for k in dados[:50]:
            b.remover(k)
        self.assertTrue(all(child.folha == b.raiz.filhos[0].folha for child in b.raiz.filhos))

if __name__ == '__main__':
    unittest.main()

