# This is a sample Python script.

import favoritos
from menu import Menu

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    apikey = "7eade183"
    nome_pasta = "favorito"
    menu = Menu(apikey, nome_pasta)
    while 1:
        print("Escolha uma opcao para utilizar: ")
        escolha = input("'1' para pesquisar titulo de media e '2' para ver a lista de favortios ou 'q' para sair: ")
        if escolha == '1':
            menu.pesquisa_filmes()
        elif escolha == '2':
            print("Ainda nao esta pronto!")
        elif escolha == 'q':
            break
        else:
            print("Opcao invalida, tente outra opcao.")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
