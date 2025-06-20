import unittest
from arvoreB import ArvoreB
from noB import NoB

class TesteArvoreB(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()

