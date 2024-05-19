from orcamento import Orcamento
from tela_orcamento import TelaOrcamento
from tipo_orcamento import TipoOrcamento
from datetime import datetime
from controlador_geral import ControladorGeral


class ControladorOrcamento:

    def __init__(self, controlador_geral):
        self.__tela_orcamento = TelaOrcamento()
        self.__orcamentos = []
        if isinstance(controlador_geral, ControladorGeral):
            self.__controlador_geral = controlador_geral

    def achar_orcamento(self, mes_ano: datetime, tipo: TipoOrcamento):
        if isinstance(mes_ano, datetime) and isinstance(tipo, TipoOrcamento):
            for orcamento in self.__orcamentos:
                if orcamento.mes_ano == mes_ano and orcamento.tipo == tipo:
                    return orcamento
            else:
                return None

    def listar_orcamento(self):
        self.__tela_orcamento.mostrar_mensagem("\n")
        for orcamento in self.__orcamentos:
            self.__tela_orcamento.mostrar_orcamento({"mes_ano": orcamento.mes_ano,
                                                        "valor": orcamento.valor, "tipo": orcamento.tipo.categoria})

    def listar_movimentacoes_orcamento(self):
        dados_orcamento = self.__tela_orcamento.selecionar_orcamento()
        tipo = dados_orcamento["tipo"]
        periodo = dados_orcamento["mes_ano"]
        t = self.__controlador_geral.controlador_tipo_orcamento.achar_tipo(tipo)
        if t is None:
            self.__tela_orcamento.mostrar_mensagem("Categoria orçamentária não encontrada.")
            return
        orcamento = self.achar_orcamento(periodo, t)
        if orcamento is None:
            self.__tela_orcamento.mostrar_mensagem("Orçamento não encontrado.")
            return
        # Calcula e compare os saldos
        dados_saldos = self.comparar_saldos(orcamento)
        saldo_categoria = dados_saldos["saldo_categoria"]
        saldo_comparado = dados_saldos["saldo_comparado"]
        movimentacoes_orcamento = self.adicionar_movimentacoes(orcamento)
        self.__tela_orcamento.mostrar_mensagem(f"-------- Movimentações {orcamento.tipo.categoria} ----------".upper())
        if movimentacoes_orcamento:
            for movimentacao in movimentacoes_orcamento:
                self.__tela_orcamento.mostrar_movimentacoes_orcamento({"codigo": movimentacao.codigo, "valor": movimentacao.valor, "data": movimentacao.data,
                                                                       "descricao": movimentacao.descricao,
                                                                       "tipo": movimentacao.tipo_movimentacao,
                                                                       "fornecedor_pagador": movimentacao.fornecedor_pagador.nome})

            self.__tela_orcamento.mostrar_mensagem(f"Saldo Total: {saldo_categoria}")
            self.__tela_orcamento.mostrar_mensagem(f"Valor orçamentário: {orcamento.valor}")
            self.__tela_orcamento.mostrar_mensagem((f"Diferença: {saldo_comparado}"))

            if saldo_comparado >= 0:
                self.__tela_orcamento.mostrar_mensagem("Meta cumprida com sucesso!")
            else:
                self.__tela_orcamento.mostrar_mensagem(
                    "Parece que a meta esperada não foi alcançada...")
                self.__tela_orcamento.mostrar_mensagem("Que tal olhar as suas movimentações "
                    "para uma visão mais detalhada sobre o que aconteceu?")
                self.__tela_orcamento.mostrar_mensagem("A responsabilidade financeira é "
                    "um dos pilares para a qualidade de vida e para um futuro próspero!")

            self.__tela_orcamento.mostrar_mensagem("\n")
        else:
            self.__tela_orcamento.mostrar_mensagem("Parece que não há nenhuma movimentação registrada para esta categoria...")
            self.__tela_orcamento.mostrar_mensagem("Por gentileza, primeiramente, registre-as no menu 'Registrar movimentações'.")

    def adicionar_orcamento(self):
        dados_orcamento = self.__tela_orcamento.pegar_orcamento()
        tipo = dados_orcamento["tipo"]
        t = self.__controlador_geral.controlador_tipo_orcamento.adicionar_categoria(tipo)
        if t is None:
            self.__tela_orcamento.mostrar_mensagem("Tipo de orçamento inválido.")
            return
        o = self.achar_orcamento(dados_orcamento["mes_ano"], t)
        if o is None:
            orc = Orcamento(dados_orcamento["mes_ano"], dados_orcamento["valor"], t)
            self.__orcamentos.append(orc)
            self.__tela_orcamento.mostrar_mensagem("Orçamento adicionado com sucesso.")
        else:
            self.__tela_orcamento.mostrar_mensagem("Não é possível adicionar mais um orçamento para esta categoria.")

    def excluir_orcamento(self):
        self.listar_orcamento()
        orc = self.__tela_orcamento.selecionar_orcamento()
        tipo = orc["tipo"]
        t = self.__controlador_geral.controlador_tipo_orcamento.achar_tipo(tipo)
        o = self.achar_orcamento(orc["mes_ano"], t)
        if o is not None:
            self.__orcamentos.remove(o)
            self.__tela_orcamento.mostrar_mensagem("Orçamento excluído com sucesso.")
            self.listar_orcamento()
        else:
            self.__tela_orcamento.mostrar_mensagem("Não é possível excluir um orçamento inexistente.")

    def alterar_orcamento(self):
        self.listar_orcamento()
        orc = self.__tela_orcamento.selecionar_orcamento()
        tipo = orc["tipo"]
        t = self.__controlador_geral.controlador_tipo_orcamento.achar_tipo(tipo)
        o = self.achar_orcamento(orc["mes_ano"], t)

        if o is not None:
            atributo = self.__tela_orcamento.selecionar_atributo()
            novo_valor = self.__tela_orcamento.pegar_orcamento_por(atributo)

            if atributo == "PERIODO" or atributo == "PERÍODO":
                o.mes_ano = novo_valor
                self.__tela_orcamento.mostrar_mensagem("A data do orçamento foi alterada com sucesso.")
            elif atributo == "VALOR":
                o.valor = novo_valor
                self.__tela_orcamento.mostrar_mensagem("O valor orçamentário foi alterado com sucesso.")
            elif atributo == "CATEGORIA":
                categ = self.__controlador_geral.controlador_tipo_orcamento.alterar_categoria(novo_valor)
                if categ is not None:
                    if o.tipo != categ:
                        o.tipo = categ
                        self.__tela_orcamento.mostrar_mensagem("A categoria do orçamento foi alterada com sucesso.")
                    else:
                        self.__tela_orcamento.mostrar_mensagem("A categoria inserida já é a categoria do orçamento.")
                else:
                    self.__tela_orcamento.mostrar_mensagem("Não é possível alterar para uma categoria inexistente, "
                                                           "por favor, adiciona esta nova categoria no menu "
                                                           "'Cadastrar categorias orçamentárias'")
        else:
            self.__tela_orcamento.mostrar_mensagem("Não é possível alterar um orçamento inexistente.")

    def adicionar_movimentacoes(self, orcamento):
        periodo = orcamento.mes_ano
        tipo = orcamento.tipo
        mov = self.__controlador_geral.controlador_movimentacao.obter_movimentacoes(periodo, tipo)
        # Adiciona um conjunto para rastrear IDs de movimentações já adicionadas
        ids_movimentacoes_adicionadas = {m.codigo for m in orcamento.movimentacoes}
        for m in mov:
            if m.codigo not in ids_movimentacoes_adicionadas:
                orcamento.adicionar_movimentacao(m)
                ids_movimentacoes_adicionadas.add(m.codigo)
        movimentacoes_orcamento = orcamento.movimentacoes
        return movimentacoes_orcamento

    def comparar_saldos(self, orcamento):
        movimentacoes_orcamento = self.adicionar_movimentacoes(orcamento)
        saldo_categoria = 0
        for m in movimentacoes_orcamento:
            if m.tipo_movimentacao == 'ENTRADA':
                saldo_categoria += m.valor
            else:
                saldo_categoria -= m.valor
        saldo_comparado = orcamento.valor - abs(saldo_categoria)
        return {"saldo_categoria": saldo_categoria, "saldo_comparado": saldo_comparado}

    def retornar(self):
        self.__controlador_geral.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.listar_orcamento, 2: self.adicionar_orcamento,
                            3: self.alterar_orcamento, 4: self.excluir_orcamento,
                            5: self.listar_movimentacoes_orcamento, 6: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_orcamento.tela_opcoes()]()















