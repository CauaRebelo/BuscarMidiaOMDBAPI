from gerenciador_omdb import GerenciadorOMDB
from gerenciador_favoritos import GerenciadorFavoritos
import math

class Menu:

    def __init__(self, api_key, nome_pasta):
        self.api_key = api_key
        self.nome_pasta = nome_pasta

    def pesquisa_filmes(self):
        pagina = 1
        titulo = input("Qual titulo deseja buscar? ")
        pesquisador = GerenciadorOMDB(self.api_key)
        while True:
            dados_json = pesquisador.pesquisa_filmes(titulo, pagina)
            if dados_json.get('totalResults') is not  None:
                imdb_ids = pesquisador.exibir_titulos(dados_json)
                print(f"Pagina: {pagina}/{math.ceil(int(dados_json.get('totalResults')) / 10)}.")
                print("Escolha 'p' ou 'a' para ir para a proxima pagina ou anterior, ou 'q' para sair. Ou:")
                escolha = input("Escolha um número para ver os detalhes: ")
                if escolha == 'q':
                    print("Saindo da pesquisa.")
                    break
                elif escolha == 'p':
                    if not pagina == math.ceil(int(dados_json.get('totalResults')) / 10):
                        pagina += 1
                elif escolha == 'a':
                    if not pagina == 1:
                        pagina -= 1
                else:
                    try:
                        index = int(escolha)
                        imdb_id_escolhido = imdb_ids[index]
                        dados_json = pesquisador.exibir_detalhes(imdb_id_escolhido)
                        escolha = input("Escolha 'f' para salvar como favoritos ou 'l' para voltar para a lista: ")
                        if escolha == 'l':
                            print("Voltando a lista.")
                        elif escolha == 'f':
                            pesquisador.salvar_favoritos(self.nome_pasta, dados_json)
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

    def acessar_favoritos(self):
        favoritos = GerenciadorFavoritos(self.nome_pasta)
        while True:
            imdb_ids = favoritos.abrir_favoritos()
            if not imdb_ids is None:
                escolha = input("Escolha um número para ver os detalhes, 'q' para sair ou 'd' para limpar a lista: ")
                if escolha == 'q':
                    print("Saindo da lista de favoritos.")
                    break
                elif escolha == 'd':
                    print("Voce tem certeza que deseja deletar TODOS os itens da lista? Isso nao e reversivel: ")
                    escolha = input("Escolha 's' para confirmar ou 'n' para abortar a operacao: ")
                    if escolha == 's':
                        favoritos.deletar_todos_favoritos()
                    elif escolha == 'n':
                        print("Abortando operacao. ")
                else:
                    try:
                        index = int(escolha)
                        imdb_id_escolhido = imdb_ids[index]
                        favoritos.exibir_detalhes(imdb_id_escolhido)
                        escolha = input("Escolha 'd' para remover dos favoritos ou 'l' para voltar para a lista: ")
                        if escolha == 'l':
                            print("Voltando a lista.")
                        elif escolha == 'd':
                            favoritos.deletar_favoritos(imdb_id_escolhido)
                            escolha = input("Escolha 'l' para voltar a lista ou 'q' para sair: ")
                            if escolha == 'l':
                                print("Voltando a lista.")
                            elif escolha == 'q':
                                print("Saindo da lista de favoritos.")
                                break
                    except ValueError:
                        print("Escolha inválida. Insira um número válido.")

            else:
                break
