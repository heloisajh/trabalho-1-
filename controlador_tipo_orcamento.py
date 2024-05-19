from tela_tipo_orcamento import TelaTipoOrcamento
from tipo_orcamento import TipoOrcamento
from controlador_geral import ControladorGeral


class ControladorTipoOrcamento:

    def __init__(self, controlador_geral):
        self.__tipos = []
        if isinstance(controlador_geral, ControladorGeral):
            self.__controlador_geral = controlador_geral
        self.__tela_tipo_orcamento = TelaTipoOrcamento()

    def achar_tipo(self, categoria: str):
        for tipo in self.__tipos:
            if(categoria is not None and tipo.categoria == categoria):
                return tipo
        return None

    def listar_tipo(self):
        for tipo in self.__tipos:
            self.__tela_tipo_orcamento.mostrar_tipo({"categoria": tipo.categoria})

    def adicionar_tipo(self):
        dados_tipo_orcamento = self.__tela_tipo_orcamento.pegar_tipo()
        t = self.achar_tipo(dados_tipo_orcamento["categoria"])
        if t is None:
            tipo_orcamento = TipoOrcamento(dados_tipo_orcamento["categoria"])
            self.__tipos.append(tipo_orcamento)
            self.__tela_tipo_orcamento.mostrar_mensagem("Categoria adicionada com sucesso.")
        else:
            self.__tela_tipo_orcamento.mostrar_mensagem("Não é possível adicionar uma categoria já cadastrada.")

    def adicionar_categoria(self, tipo): #Uso para controlador movimentação e controlador orçamento
        t = self.achar_tipo(tipo)
        if t is None:
            tipo_orcamento = TipoOrcamento(tipo)
            self.__tipos.append(tipo_orcamento)
            return tipo_orcamento
        return t

    def excluir_tipo(self):
        self.listar_tipo()
        tipo = self.__tela_tipo_orcamento.selecionar_categoria()
        tipo_orcamento = self.achar_tipo(tipo)

        if tipo_orcamento is not None:
            self.__tipos.remove(tipo_orcamento)
            self.__tela_tipo_orcamento.mostrar_mensagem("Categoria excluída com sucesso.")
            self.__tela_tipo_orcamento.mostrar_mensagem("\n")
            self.listar_tipo()
        else:
            self.__tela_tipo_orcamento.mostrar_mensagem("Não é possível excluir uma categoria inexistente")

    def alterar_tipo(self):
        self.listar_tipo()
        tipo = self.__tela_tipo_orcamento.selecionar_categoria()
        tipo_orcamento = self.achar_tipo(tipo)

        if tipo_orcamento is not None:
            novo_tipo = self.__tela_tipo_orcamento.pegar_tipo()
            tipo_orcamento.categoria = novo_tipo["categoria"]
            self.__tela_tipo_orcamento.mostrar_mensagem("Categoria alterada com sucesso.")
            self.listar_tipo()
        else:
            self.__tela_tipo_orcamento.mostrar_mensagem("Não é possível alterar uma categoria inexistente.")

    def alterar_categoria(self, tipo): #Uso para controlador movimentação e controlador orçamento
        tipo_orcamento = self.achar_tipo(tipo)
        if tipo_orcamento is not None:
            return tipo_orcamento
        else:
            return None

    def retornar(self):
        self.__controlador_geral.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.listar_tipo, 2: self.adicionar_tipo, 3: self.alterar_tipo,
                            4: self.excluir_tipo, 5: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_orcamento.tela_opcoes()]()
