from tela import Tela


class TelaUsuario(Tela):

    def tela_opcoes(self):
        print("-------- USUÁRIO ----------")
        print("1 - Fazer login")
        print("2 - Esqueci a senha")
        print("3 - Sou novo usuário, quero me cadastrar")

        opcao = self.ler_num_inteiro("Opção: ", [1,2,3,4])
        return opcao

    def pegar_usuario(self):
        nome = input("Nome: ")
        senha = input("Senha: ")
        if isinstance(nome, str) and isinstance(senha, str):
            return {"nome": nome, "senha": senha}

    def pegar_senha(self):
        nome = input("Usuário: ")
        senha = input("Nova senha: ")
        if isinstance(senha, str):
            return {"nome": nome, "senha": senha}












