from tela import Tela

class TelaTipoOrcamento(Tela):



    def tela_opcoes(self):
        print("\n")
        print("-------- CATEGORIAS DE ORÇAMENTO ----------")
        print("Escolha uma das opções abaixo:")
        print("1 - Listar categorias")
        print("2 - Adicionar categoria")
        print("3 - Alterar categoria")
        print("4 - Excluir categoria")
        print("5 - Retornar")

        opcao = self.ler_num_inteiro("Opção: ", [1,2,3,4,5])
        return opcao

    def pegar_tipo(self):
        tipo = input("Categoria: ")
        if isinstance(tipo, str) and tipo is not None:
            return {"categoria": tipo}

    def mostrar_tipo(self, dados_tipo):
        print("Categoria: ", dados_tipo["categoria"])

    def selecionar_categoria(self):
        tipo = input("Digite a categoria que deseja selecionar: ")
        if isinstance(tipo, str) and tipo is not None:
            return tipo











