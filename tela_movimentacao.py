import datetime
from tela import Tela


class TelaMovimentacao(Tela):

    def tela_opcoes(self):
        print("\n")
        print("-------- MOVIMENTAÇÕES ----------")
        print("Escolha uma das opções abaixo:")
        print("1 - Listar movimentações")
        print("2 - Adicionar movimentação")
        print("3 - Alterar movimentação")
        print("4 - Excluir movimentação")
        print("5 - Visualizar saldo atual")
        print("6 - Retornar")

        opcao = self.ler_num_inteiro("Opção: ", [1,2,3,4,5,6])
        return opcao

    def pegar_movimentacao(self):
        codigo = int(input("Código: "))

        while True:
            dat = input("Data (formato dd/mm/yyyy): ")
            try:
                dia, mes, ano = map(int, dat.split('/'))
                data = datetime.datetime(ano, mes, dia)
                if len(dat) != 10:
                    raise ValueError
                break
            except (ValueError, IndexError):
                print("Por favor, digite a data no formato especificado (dd/mm/yyyy).")

        valor = float(input("Valor: R$ "))

        while True:
            tipo = input("Entrada/Saída: ").upper()
            if tipo in ["ENTRADA", "SAIDA", "SAÍDA"]:
                break
            else:
                print(f"{tipo} não é um tipo de movimentação aceito.")
                print("Por favor, insira apenas: Entrada ou Saída")

        categoria = input("Categoria: ")
        fornecedor_pagador = input("Fornecedor/Pagador: ")
        descricao = input("Descrição: ")

        return {
            "codigo": codigo,
            "valor": valor,
            "data": data,
            "descricao": descricao,
            "tipo": tipo,
            "categoria": categoria,
            "fornecedor_pagador": fornecedor_pagador
        }

    def pegar_movimentacao_por(self, atributo):
        descricoes = ["DESCRIÇÃO", "DESCRICAO", "DESCRIÇAO", "DESCRICÃO"]

        if atributo == "VALOR":
            while True:
                try:
                    valor = float(input("Insira o novo valor: R$ "))
                    return valor
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")

        if atributo == "DATA":
            while True:
                dat = input("Insira a nova data (formato dd/mm/yyyy): ")
                try:
                    dia, mes, ano = map(int, dat.split('/'))
                    data = datetime.datetime(ano, mes, dia)
                    return data
                except (ValueError, IndexError):
                    print("Por favor, digite a data no formato especificado (dd/mm/yyyy).")

        if atributo in descricoes:
            descricao = input("Insira a nova descrição: ")
            return descricao

        if atributo == "TIPO":
            while True:
                tipo = input("Entrada/Saída: ").upper()
                if tipo in ["ENTRADA", "SAIDA", "SAÍDA"]:
                    return tipo
                else:
                    print(f"{tipo} não é um tipo de movimentação aceito.")
                    print("Por favor, insira apenas: Entrada ou Saída")

        if atributo == "CATEGORIA":
            categoria = input("Insira a nova categoria: ")
            return categoria

        if atributo == "FORNECEDOR/PAGADOR":
            fornecedor_pagador = input("Insira o novo fornecedor/pagador: ")
            return fornecedor_pagador

        return None

    def mostrar_movimentacao(self, dados_movimentacao):
        dia_mes_ano = dados_movimentacoes["data"].strftime("%d/%m/%Y")
        print("\n")
        print("Código: ", dados_movimentacao["codigo"])
        print("Data: ", dia_mes_ano)
        print("Valor: R$ ", dados_movimentacao["valor"])
        print(dados_movimentacao["tipo"])
        print("Categoria: ", dados_movimentacao["categoria"])
        print("Fornecedor/Pagador: ", dados_movimentacao["fornecedor_pagador"])
        print("Descrição: ", dados_movimentacao["descricao"])
        print("\n")

    def selecionar_movimentacao(self):
        print("\n")
        codigo = int(input("Código da movimentação: "))
        return {"codigo": codigo}

    def selecionar_atributo(self):
        atributos_validos = ["VALOR", "DATA", "TIPO", "CATEGORIA", "DESCRIÇÃO", "DESCRICAO", "DESCRIÇAO", "DESCRICÃO",
                             "FORNECEDOR/PAGADOR"]

        while True:
            atributo = input("Insira o que você deseja alterar: ").upper()
            if atributo in atributos_validos:
                return atributo
            else:
                print("Não foi possível encontrar o que você deseja alterar.")
                print("Por favor, insira apenas: Valor, Data, Tipo, Categoria, Descrição ou Fornecedor/Pagador.")
























