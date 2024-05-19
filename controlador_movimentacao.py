from datetime import datetime
from tela_movimentacao import TelaMovimentacao
from movimentacao import Movimentacao
from controlador_geral import ControladorGeral
from tipo_orcamento import TipoOrcamento


class ControladorMovimentacao:

    def __init__(self, controlador_geral: ControladorGeral):
        self.__tela_movimentacao = TelaMovimentacao()
        self.__movimentacoes = []
        if isinstance(controlador_geral, ControladorGeral):
            self.__controlador_geral = controlador_geral
        self.saldo_categoria = 0
        self.saldo_total = 0

    def achar_movimentacao(self, codigo):
        if isinstance(codigo, int):
            for movimentacao in self.__movimentacoes:
                if movimentacao.codigo == codigo:
                    return movimentacao
            else:
                return None

    def listar_movimentacao(self):
        if self.__movimentacoes:
            for movimentacao in self.__movimentacoes:
                self.__tela_movimentacao.mostrar_movimentacao({"codigo": movimentacao.codigo, "valor": movimentacao.valor,
                                                                "data": movimentacao.data, "descricao": movimentacao.descricao,
                                                                "tipo": movimentacao.tipo_movimentacao, "categoria":
                                                                movimentacao.categoria_movimentacao.categoria,
                                                                "fornecedor_pagador": movimentacao.fornecedor_pagador.nome})
        else:
            self.__tela_movimentacao.mostrar_mensagem("Você só pode visualizar suas movimentações, se registrar ao menos uma movimentação.")
        self.visualizar_saldo_atual()

    def adicionar_movimentacao(self):

        dados_movimentacao = self.__tela_movimentacao.pegar_movimentacao()
        m = self.achar_movimentacao(dados_movimentacao["codigo"])
        categoria = dados_movimentacao["categoria"]
        categ = self.__controlador_geral.controlador_tipo_orcamento.adicionar_categoria(categoria)
        usuario = self.__controlador_geral.usuario_logado
        pessoa = dados_movimentacao["fornecedor_pagador"]
        pes = self.__controlador_geral.controlador_pessoa.adicionar_fornecedor_pagador(pessoa)

        if m is None:

            mov = Movimentacao(dados_movimentacao["codigo"], usuario, dados_movimentacao["valor"],
                               dados_movimentacao["data"], dados_movimentacao["descricao"],
                               dados_movimentacao["tipo"], categ, pes)
            self.__movimentacoes.append(mov)
            self.__saldo_total_atualizado = False
            self.calcular_saldo_total()
            self.__tela_movimentacao.mostrar_mensagem("Movimentação adicionada com sucesso.")
            self.calcular_saldo_total()
        else:
            self.__tela_movimentacao.mostrar_mensagem("Não é possível adicionar uma movimentação repetida.")

    def excluir_movimentacao(self):
        self.listar_movimentacao()
        mov = self.__tela_movimentacao.selecionar_movimentacao()
        m = self.achar_movimentacao(mov["codigo"])
        if m is not None:
            self.__movimentacoes.remove(m)
            self.__saldo_total_atualizado = False
            self.calcular_saldo_total()
            self.__tela_movimentacao.mostrar_mensagem("Movimentação excluída com sucesso.")
            self.listar_movimentacao()
        else:
            self.__tela_movimentacao.mostrar_mensagem("Não é possível excluir uma movimentação inexistente.")

    def alterar_movimentacao(self):
        self.listar_movimentacao()
        mov = self.__tela_movimentacao.selecionar_movimentacao()
        m = self.achar_movimentacao(mov["codigo"])

        if m is not None:
            atributo = self.__tela_movimentacao.selecionar_atributo()
            novo_valor = self.__tela_movimentacao.pegar_movimentacao_por(atributo)

            if atributo == "VALOR":
                m.valor = novo_valor
                self.__tela_movimentacao.mostrar_mensagem("O valor da movimentação foi alterado com sucesso.")
                self.__saldo_total_atualizado = False
                self.calcular_saldo_total()

            elif atributo == "DATA":
                m.data = novo_valor
                self.__tela_movimentacao.mostrar_mensagem("A data da movimentação foi alterada com sucesso.")

            elif atributo in ["DESCRIÇÃO", "DESCRICAO", "DESCRIÇAO", "DESCRICÃO"]:
                m.descricao = novo_valor
                self.__tela_movimentacao.mostrar_mensagem("A descrição da movimentação foi alterada com sucesso")

            elif atributo == "TIPO":
                m.tipo_movimentacao = novo_valor
                self.__tela_movimentacao.mostrar_mensagem("O tipo da movimentação foi alterado com sucesso.")


            elif atributo == "CATEGORIA":
                categ = self.__controlador_geral.controlador_tipo_orcamento.alterar_categoria(novo_valor)
                if categ is not None:
                    if m.categoria_movimentacao != categ:
                        m.categoria_movimentacao.tipo = categ
                        self.__tela_movimentacao.mostrar_mensagem("A categoria do orçamento foi alterada com sucesso.")
                    else:
                        self.__tela_movimentacao.mostrar_mensagem("A categoria inserida já é a categoria do orçamento.")
                else:
                    self.__tela_movimentacao.mostrar_mensagem("Não é possível alterar para uma categoria inexistente, "
                                                           "por favor, adiciona esta nova categoria no menu "
                                                           "'Cadastrar categorias orçamentárias'.")
            elif atributo == "FORNECEDOR/PAGADOR":
                p = self.__controlador_geral.controlador_pessoa.alterar_fornecedor_pagador(novo_valor)
                if p is not None:
                    if m.fornecedor_pagador != p:
                        m.fornecedor_pagador = p
                    else:
                        self.__tela_movimentacao.mostrar_mensagem("O fornecedor/pagador inserido já é o fornecedor/pagador da movimentação")
                else:
                    self.__tela_movimentacao.mostrar_mensagem("Não é possível alterar para um fornecedor/pagador inexistente, "
                                                              "por favor, adicione este no menu 'Cadastrar pessoas'.")
        else:
            self.__tela_movimentacao.mostrar_mensagem("Não é possível alterar uma movimentação inexistente.")

    def obter_movimentacoes(self, periodo, tipo): #Para uso do controlador orçamento
        movimentacoes_filtradas = []
        for movimentacao in self.__movimentacoes:
            if movimentacao.categoria_movimentacao == tipo and(movimentacao.data.year == periodo.year
                                                               and movimentacao.data.month == periodo.month):
                movimentacoes_filtradas.append(movimentacao)
        return movimentacoes_filtradas

    def calcular_saldo_total(self):
        if not self.__saldo_total_atualizado:
            # Limpe o saldo total antes de recalculá-lo
            self.saldo_total = 0
            for mov in self.__movimentacoes:
                if mov.tipo_movimentacao == "ENTRADA":
                    self.saldo_total += mov.valor
                elif mov.tipo_movimentacao == "SAIDA" or mov.tipo_movimentacao == "SAÍDA":
                    self.saldo_total -= mov.valor
            self.__saldo_total_atualizado = True

    def visualizar_saldo_total(self):
        self.__tela_movimentacao.mostrar_mensagem(f"Saldo atual: R$ {self.saldo_total}")

    def retornar(self):
        self.__controlador_geral.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.listar_movimentacao, 2: self.adicionar_movimentacao,
                            3: self.alterar_movimentacao, 4: self.excluir_movimentacao,
                            5: self.visualizar_saldo_total, 6: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_movimentacao.tela_opcoes()]()





