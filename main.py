import copy
import locale


def buscarInstimento(investimento, acao):
    global ACAO

    if(investimento <= 0 or len(acao) <= 0):
        return 0, []

    valor1, opcao1 = 0, []

    for k in range(len(acao)):
        acaoCopy = copy.deepcopy(acao)
        selecao = acaoCopy.pop(k)

        if(investimento - selecao.get("preco") >= 0):
            soma = selecao['preco']

            if (selecao['opcao'] == 1):
                for i in range(len(acaoCopy)):
                    if (acaoCopy[i] == 5):
                        acaoCopy.pop(i)
                        break
                valor1, opcao1 = buscarInstimento(investimento - soma, acaoCopy)
                valor1 += selecao.get('retorno')
                opcao1 = [selecao.get('opcao')] + opcao1

            elif (selecao['opcao'] == 5):
                for i in range(len(acaoCopy)):
                    if (acaoCopy[i]['opcao'] == 1):
                        acaoCopy.pop(i)
                        break
                valor1, opcao1 = buscarInstimento(investimento - soma, acaoCopy)
                valor1 += selecao.get('retorno')
                opcao1 = [selecao.get('opcao')] + opcao1

            elif (selecao['opcao'] == 2 and 4 in list(map(lambda a:a['opcao'], acaoCopy))):
                for i in range(len(acaoCopy)):
                    if (acaoCopy[i]['opcao'] == 4):
                        select = acaoCopy.pop(i)
                        soma += select['preco']
                        if (investimento - soma) >= 0:
                            valor1, opcao1 = buscarInstimento(investimento - soma, acaoCopy)
                            valor1 += selecao.get('retorno') + select.get('retorno')
                            opcao1 = [selecao.get('opcao')] + opcao1 + [select.get('opcao')]
                        break

            elif (selecao['opcao'] == 4 and 2 in list(map(lambda a: a['opcao'], acaoCopy))):
                for i in range(len(acaoCopy)):
                    if (acaoCopy[i] == 2):
                        select = acaoCopy.pop(i)
                        soma += select['preco']
                        if (investimento - soma) >= 0:
                            valor1, opcao1 = buscarInstimento(investimento - soma, acaoCopy)
                            valor1 += selecao.get('retorno') + select.get('retorno')
                            opcao1 = [selecao.get('opcao')] + opcao1 + [select.get('opcao')]
                        break

            else:
                valor1, opcao1 = buscarInstimento(investimento - soma, acaoCopy)
                valor1 += selecao.get('retorno')
                opcao1 = [selecao.get('opcao')] + opcao1



        valor2, opcao2 = buscarInstimento(investimento, acaoCopy)

        r = max(valor1, valor2)

        if (r == valor1):
            return (valor1, opcao1)
        else:
            return (valor2, opcao2)

if __name__ == "__main__":
    acao = []

    investimento = 1000000
    preco = [470000, 400000, 170000, 270000, 340000, 230000, 50000, 440000]
    retorno = [410000, 33000, 140000, 250000, 320000, 320000, 90000, 190000]
    c = 0
    for k in range(0, len(preco)):
        acao.append({"opcao": c + 1, 'preco': preco[k], 'retorno': retorno[k]})
        c += 1
    n = len(retorno)
    ACAO = copy.deepcopy(acao)
    retornoInvestimento, opcoes = buscarInstimento(investimento, acao)
    opcoes.sort()
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    print()
    print(f'Investimento: {locale.currency(investimento, grouping=True)}')
    for k in range(len(ACAO)):
        print(
            f'Opção {k + 1}: {locale.currency(ACAO[k].get("preco"), grouping=True)} | Retorno: {locale.currency(ACAO[k].get("retorno"), grouping=True)}')
    print("\nMelhores opções:")
    soma = investimento
    for n in opcoes:
        for k in range(len(ACAO)):
            if (ACAO[k].get('opcao') == n):
                print(
                    f'Opção {ACAO[k].get("opcao")}: {locale.currency(ACAO[k].get("preco"), grouping=True)} | Retorno: {locale.currency(ACAO[k].get("retorno"), grouping=True)}')
                soma -= ACAO[k].get("preco")
                break
    print(f'Restaram: {locale.currency(soma, grouping=True)}')
    print(opcoes)

    print(f'Retorno: {locale.currency(retornoInvestimento, grouping=True)}')
