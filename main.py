# This is a sample Python script.

from gerenciador_omdb import GerenciadorOMDB
import favoritos
import requests
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    apikey = "7eade183"
    titulo = ""
    nome_pasta = "favorito"
    pagina = 1

    titulo = input("Qual titulo deseja buscar? ")
    pesquisador = GerenciadorOMDB(apikey)
    while(1):
        dados_json = pesquisador.pesquisa_filmes(titulo, pagina)
        if dados_json.get('totalResults') != None:
            imdb_ids = pesquisador.exibir_titulos(dados_json)
            print(f"Pagina: {pagina}/{math.ceil(int(dados_json.get('totalResults'))/10)}.")
            print("Escolha 'p' ou 'a' para ir para a proxima pagina ou anterior, ou 'q' para sair. Ou:")
            escolha = input("Escolha um número para ver os detalhes: ")
            if escolha == 'q':
                print("Saindo da pesquisa.")
                break
            elif escolha == 'p':
                if not pagina == math.ceil(int(dados_json.get('totalResults'))/10):
                    pagina+=1
            elif escolha == 'a':
                if not pagina == 1:
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
        else:
            print("Não há nenhuma midia com esse titulo, deseja fazer outra pesquisa?")
            escolha = input("Escolha 's' para fazer outra pesquisa ou 'q' para sair da pesquisa: ")
            if escolha == 's':
                titulo = input("Qual titulo deseja buscar? ")
            elif escolha == 'q':
                break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
