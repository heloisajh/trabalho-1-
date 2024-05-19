import datetime
from tela import Tela


class TelaOrcamento(Tela):

    def tela_opcoes(self):
        print("\n")
        print("-------- ORÇAMENTOS ----------")
        print("Escolha uma das opções abaixo:")
        print("1 - Listar orçamentos")
        print("2 - Adicionar orçamento")
        print("3 - Alterar orçamento")
        print("4 - Excluir orçamento")
        print("5 - Emitir relatório de metas de gastos")
        print("6 - Retornar")

        opcao = self.ler_num_inteiro("Opção: ", [1,2,3,4,5,6])
        return opcao

    def pegar_orcamento(self):
        while True:
            periodo = input("Mês/Ano (formato mm/yyyy): ")
            try:
                # Validar o formato do período
                mes, ano = map(int, periodo.split('/'))
                if len(periodo) != 7 or not (1 <= mes <= 12):
                    raise ValueError("Mês/Ano no formato incorreto.")
                mes_ano = datetime.datetime(ano, mes, 1)
                break
            except ValueError:
                print("Por favor, digite o período no formato especificado (mm/yyyy).")
        valor = input("Valor: R$ ")
        valor = float(valor)
        tipo = input("Categoria: ")
        return {"mes_ano": mes_ano, "valor": valor, "tipo": tipo}

    def pegar_orcamento_por(self, atributo):
        if atributo in ["PERIODO", "PERÍODO"]:
            while True:
                try:
                    periodo = input("Insira o novo período (formato mm/yyyy): ")
                    mes, ano = map(int, periodo.split('/'))
                    if len(periodo) != 7 or not (1 <= mes <= 12):
                        raise ValueError("Período no formato incorreto.")
                    mes_ano = datetime.datetime(ano, mes, 1)
                    return mes_ano
                except ValueError:
                    print("Por favor, digite o período no formato especificado (mm/yyyy).")
        elif atributo == "VALOR":
            while True:
                try:
                    valor = float(input("Insira o novo valor: "))
                    return valor
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
        elif atributo == "CATEGORIA":
            categoria = input("Insira a nova categoria: ")
            return categoria
        return None

    def mostrar_orcamento(self, dados_orcamento):
        mes_ano = dados_orcamento["mes_ano"].strftime("%m/%Y")
        print("Período: ", mes_ano)
        print("Valor: ", dados_orcamento["valor"])
        print("Categoria: ", dados_orcamento["tipo"])

    def mostrar_movimentacoes_orcamento(self, dados_movimentacoes):
        dia_mes_ano = dados_movimentacoes["data"].strftime("%d/%m/%Y")
        print("Código: ", dados_movimentacoes["codigo"])
        print("Data: ", dia_mes_ano)
        print("Valor: R$ ", dados_movimentacoes["valor"])
        print(dados_movimentacoes["tipo"])
        print("Fornecedor/Pagador: ", dados_movimentacoes["fornecedor_pagador"])
        print("Descrição: ", dados_movimentacoes["descricao"])

    def selecionar_orcamento(self):
        print("Insira os dados abaixo:")
        while True:
            periodo = input("Período (formato mm/yyyy): ")
            try:
                mes, ano = map(int, periodo.split('/'))
                if len(periodo) != 7 or not (1 <= mes <= 12):
                    raise ValueError("Período no formato incorreto.")
                mes_ano = datetime.datetime(ano, mes, 1)
                break
            except ValueError:
                print("Por favor, digite o período no formato especificado (mm/yyyy).")
        categoria = input("Categoria: ")
        return {"mes_ano": mes_ano, "tipo": categoria}

    def selecionar_atributo(self):
        atributos_validos = ["PERÍODO", "PERIODO", "VALOR", "CATEGORIA"]
        while True:
            atributo = input("Insira o que você deseja alterar: ").upper()
            if atributo in atributos_validos:
                return atributo
            print("Não foi possível encontrar o que você deseja alterar.")
            print("Por favor, insira apenas: Período, Valor ou Categoria.")














