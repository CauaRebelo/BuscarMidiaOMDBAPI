from menu import Menu

if __name__ == '__main__':
    apikey = "7eade183"
    nome_pasta = "favoritos"
    menu = Menu(apikey, nome_pasta)
    while True:
        print("Escolha uma opcao para utilizar: ")
        print("'1' para pesquisar titulo de media.")
        print("'2' para ver a lista de favortios ou 'q' para sair: ")
        escolha = input()
        if escolha == '1':
            menu.pesquisa_filmes()
        elif escolha == '2':
            menu.acessar_favoritos()
        elif escolha == 'q':
            break
        else:
            print("Opcao invalida, tente outra opcao.")
