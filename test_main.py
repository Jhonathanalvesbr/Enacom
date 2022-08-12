import unittest

from main import buscarInstimento

class MyTestCase(unittest.TestCase):
    def test_melhor_opaco(self):
        acao = []
        investimento = 2
        preco = [2, 2, 2, 50]
        retorno = [302, 201, 101, 200]
        c = 0
        for k in range(0, len(preco)):
            acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
            c += 1
        self.assertEqual(buscarInstimento(investimento, acao), (302, [1]))

    def test_escolhe_opcao_1_ou_5(self):
        acao = []
        investimento = 4
        preco = [2, 2, 2, 2, 2]
        retorno = [500, 102, 101, 101, 500]
        c = 0
        for k in range(0, len(preco)):
            acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
            c += 1
        self.assertEqual(buscarInstimento(investimento, acao), (601, [1, 3]))

    def test_escolhe_opcao_1_ou_5(self):
        acao = []
        investimento = 4
        preco = [2, 2, 2, 2, 2]
        retorno = [500, 102, 101, 101, 502]
        c = 0
        for k in range(0, len(preco)):
            acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
            c += 1
        self.assertEqual((603, [3, 5]), buscarInstimento(investimento, acao))

    def test_escolhe_opcao_2_e_4(self):
        acao = []
        investimento = 4
        preco = [1, 2, 2, 2]
        retorno = [101, 102, 101, 101]
        c = 0
        for k in range(0, len(preco)):
            acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
            c += 1
        self.assertEqual(buscarInstimento(investimento, acao), (203, [2,4]))

    def test_investimento_inicial_vazio(self):
        acao = []
        investimento = 0
        preco = [2, 2, 2, 50]
        retorno = [302, 201, 101, 200]
        c = 0
        for k in range(0, len(preco)):
            acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
            c += 1
        self.assertEqual(buscarInstimento(investimento, acao), (0, []))

    def test_investimento_inicial_vazio_e_sem_opcao(self):
        acao = []
        investimento = 0
        preco = []
        retorno = []
        c = 0
        for k in range(0, len(preco)):
            acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
            c += 1
        self.assertEqual(buscarInstimento(investimento, acao), (0, []))

    def test_sem_opcao(self):
        acao = []
        investimento = 100
        preco = []
        retorno = []
        c = 0
        for k in range(0, len(preco)):
            acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
            c += 1
        self.assertEqual(buscarInstimento(investimento, acao), (0, []))

    def test_melhor_opcao_enacom(self):
        acao = []
        investimento = 1000000
        preco = [470000, 400000, 170000, 270000, 340000, 230000, 50000, 440000]
        retorno = [410000, 33000, 140000, 250000, 320000, 320000, 90000, 190000]
        c = 0
        for k in range(0, len(preco)):
            acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
            c += 1
        self.assertEqual(buscarInstimento(investimento,acao), (960000,[1, 3, 6, 7]))


if __name__ == '__main__':
    unittest.main()
