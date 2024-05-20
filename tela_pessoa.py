from tela import Tela


class TelaPessoa(Tela):

    def tela_opcoes(self):
        print("\n")
        print("-------- PESSOAS ----------")
        print("Escolha uma das opções abaixo:")
        print("1 - Listar pessoas")
        print("2 - Adicionar pessoa")
        print("3 - Alterar pessoa")
        print("4 - Excluir pessoa")
        print("5 - Retornar")
        print("\n")

        opcao = self.ler_num_inteiro("Opção: ", [1,2,3,4,5])
        return opcao

    def pegar_pessoa(self):
        nome = input("Nome: ")
        print("\n")
        if isinstance(nome, str) and nome is not None:
            return {"nome": nome}

    def mostrar_pessoa(self, dados_pessoa):
        print("Nome: ", dados_pessoa["nome"])

    def selecionar_pessoa(self):
        nome = input("Digite a pessoa que deseja selecionar: ")
        print("\n")
        if isinstance(nome, str) and nome is not None:
            return nome












