# This is a sample Python script.

import json
from gerenciador_omdb import GerenciadorOMDB
import favoritos
import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    apikey = "7eade183"
    titulo = ""
    nome_pasta = "favoritos"
    pagina = 1

    titulo = input("Qual titulo deseja buscar? ")
    pesquisador = GerenciadorOMDB(apikey)

    while(1):
        dados_json = pesquisador.pesquisa_filmes(titulo, pagina)
        if dados_json:
            imdb_ids = pesquisador.exibir_titulos(dados_json)
            print("Escolha 'n' ou 'p' para ir para a proxima pagina ou anterior, ou 'q' para sair. Ou:")
            escolha = input("Escolha um número para ver os detalhes: ")
            if escolha == 'q':
                print("Saindo da pesquisa.")
                break
            elif escolha == 'n':
                pagina+=1
            elif escolha == 'p':
                pagina -=1
            else:
                try:
                    index = int(escolha)
                    imdb_id_escolhido = imdb_ids[index]
                    dados_json = pesquisador.exibir_detalhes(imdb_id_escolhido)
                    escolha = input("Escolha 'f' para salvar como favoritos ou 'l' para voltar para a lista: ")
                    if escolha == 'l':
                        print("Voltando a lista.")
                    elif escolha == 'f':
                        pesquisador.salvar_favoritos(nome_pasta, dados_json)
                        escolha = input("Escolha 'l' para voltar a lista ou 'q' para sair: ")
                        if escolha == 'l':
                            print("Voltando a lista.")
                        elif escolha == 'q':
                            print("Saindo da pesquisa.")
                            break
                except ValueError:
                    print("Escolha inválida. Insira um número válido.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
