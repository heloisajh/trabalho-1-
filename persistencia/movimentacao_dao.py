from persistencia.dao import DAO
from entidade.movimentacao import Movimentacao
from persistencia.tipo_orcamento_dao import TipoOrcamentoDAO
from persistencia.pessoa_dao import PessoaDAO
from persistencia.usuario_dao import UsuarioDAO

class MovimentacaoDAO(DAO):

    __instance = None

    def __init__(self):
        super().__init__('movimentacoes.pkl')

    def __new__(cls):
        if MovimentacaoDAO.__instance is None:
            MovimentacaoDAO.__instance = object.__new__(cls)
        return MovimentacaoDAO.__instance

    def add(self, movimentacao: Movimentacao):
        if isinstance(movimentacao, Movimentacao) and (movimentacao.codigo, int):
            super().add(movimentacao.codigo, movimentacao)

    def update(self, movimentacao):
        for i in range(len(self.movimentacoes)):
            if self.movimentacoes[i].codigo == movimentacao.codigo:
                self.movimentacoes[i] = movimentacao
                return True
        return False

    def load(self):
        super().load()
        tipo_orcamento_dao = TipoOrcamentoDAO()
        usuario_dao = UsuarioDAO()
        pessoa_dao = PessoaDAO()
        for movimentacao in self.get_all():
            movimentacao.tipo_movimentacao = tipo_orcamento_dao.get(movimentacao.categoria_movimentacao.categoria)
            movimentacao.fornecedor_pagador = pessoa_dao.get(movimentacao.fornecedor_pagador.nome)
            movimentacao.usuario = usuario_dao.get(movimentacao.usuario)

    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, movimentacao: Movimentacao):
        if isinstance(movimentacao, Movimentacao) and (movimentacao.codigo, int):
            return super().remove(movimentacao.codigo)
