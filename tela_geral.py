from tela import Tela


class TelaGeral(Tela):

    def tela_opcoes(self):
        print("\n")
        print("-------- SisFinanças ----------")
        print("Olá, bem-vindo ao SisFinanças!")
        print("-------------------------------")
        print("Escolha uma das opções abaixo:")
        print("1 - Cadastrar orçamentos")
        print("2 - Cadastrar pessoas")
        print("3 - Cadastrar categorias orçamentárias")
        print("4 - Registrar movimentações")
        print("5 - Encerrar sistema")
        print("-------------------------------")
        opcao = self.ler_num_inteiro("Opção: ", [1,2,3,4,5])
        return opcao