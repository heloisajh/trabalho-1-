from tela_usuario import TelaUsuario
from usuario import Usuario
from controlador_geral import ControladorGeral


class ControladorUsuario:

    def __init__(self, controlador_geral):
        self.__usuarios = []
        if isinstance(controlador_geral, ControladorGeral):
            self.__controlador_geral = controlador_geral
        self.__tela_usuario = TelaUsuario()

    def achar_usuario(self, nome: str):
        if isinstance(nome, str):
            for usuario in self.__usuarios:
                if usuario.nome == nome:
                    return usuario
            return None

    def cadastrar_usuario(self):
        self.__tela_usuario.mostrar_mensagem("\n")
        self.__tela_usuario.mostrar_mensagem("Cadastro:")
        dados_usuario = self.__tela_usuario.pegar_usuario()
        u = self.achar_usuario(dados_usuario["nome"])
        if u is None:
            usuario = Usuario(dados_usuario["nome"], dados_usuario["senha"])
            self.__usuarios.append(usuario)
            self.__tela_usuario.mostrar_mensagem("Cadastro realizado com sucesso!")
            self.__tela_usuario.mostrar_mensagem("\n")
            self.login()
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário já cadastrado no sistema, por favor, faça o login.")
            self.__tela_usuario.mostrar_mensagem("\n")

    def login(self):
        self.__tela_usuario.mostrar_mensagem("\n")
        self.__tela_usuario.mostrar_mensagem("Login:")
        dados_usuario = self.__tela_usuario.pegar_usuario()
        usuario = self.achar_usuario(dados_usuario["nome"])
        if usuario is not None:
            if usuario.senha == dados_usuario["senha"]:
                self.__controlador_geral.usuario_logado = usuario
                self.__controlador_geral.abrir_tela()
            else:
                self.__tela_usuario.mostrar_mensagem("Senha incorreta, por favor, tente novamente")
                self.__tela_usuario.mostrar_mensagem("\n")
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário não cadastrado, por favor, primeiramente, realize o cadastro.")
            self.__tela_usuario.mostrar_mensagem("\n")

    def alterar_senha(self):
        self.__tela_usuario.mostrar_mensagem("\n")
        self.__tela_usuario.mostrar_mensagem("Alterar senha:")
        dados_usuario = self.__tela_usuario.pegar_senha()
        usuario = self.achar_usuario(dados_usuario["nome"])
        if usuario is not None:
            nova_senha = dados_usuario["senha"]
            usuario.senha = nova_senha
            self.__tela_usuario.mostrar_mensagem("Senha alterada com sucesso.")
            self.__tela_usuario.mostrar_mensagem("\n")
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário não encontrado.")
            self.__tela_usuario.mostrar_mensagem("\n")

    def abrir_tela(self):
        lista_opcoes = {1: self.login, 2: self.alterar_senha, 3: self.cadastrar_usuario}
        continua = True
        while continua:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
