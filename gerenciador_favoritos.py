import json
import os


class GerenciadorFavoritos:

    def __init__(self, nome_pasta):
        self.nome_pasta = nome_pasta

    def abrir_favoritos(self):
        imdb_ids = {}
        index = 0

        if os.path.exists(self.nome_pasta):
            for arquivo in os.listdir(self.nome_pasta):
                if arquivo.endswith(".json"):
                    path = f"{self.nome_pasta}/{arquivo}"

                    try:
                        with open(path, "r") as arquivo_json:
                            dados = json.load(arquivo_json)

                    except IOError:
                        print("Nao foi possivel acessar o arquivo.")
                        return None

                    if "Title" in dados and "imdbID" in dados:
                        titulo = dados.get("Title")
                        imdb_id = dados.get("imdbID")
                        imdb_ids[index] = imdb_id
                        print(f"{index}: {titulo}")
                        index += 1
                    arquivo_json.close()
            if index == 0:
                print("Não existe mais nada nos favoritos, adicione mais para acessar a lista.")
                return None
            return imdb_ids
        else:
            print("Nao existem favoritos, use a função de pesquisa para adicionar midia como favorito.")
            return None

    def exibir_detalhes(self, id_escolhido):
        path = f"{self.nome_pasta}/{id_escolhido}.json"
        try:
            with open(path, "r") as arquivo_json:
                dados = json.load(arquivo_json)
                print("Detalhes da midia selecionada:")
                print(f"Titulo: {dados.get('Title')}")
                print(f"Ano de Lancamento: ", dados.get('Year'))
                print(f"Classificacao: ", dados.get('Rated'))
                print(f"Sinopse: ", dados.get('Plot'))
                print(f"Diretor: ", dados.get('Director'))

        except IOError:
            print("Nao foi possivel acessar o arquivo.")
            return
        arquivo_json.close()

    def deletar_favoritos(self, id_escolhido):
        path = f"{self.nome_pasta}/{id_escolhido}.json"
        try:
            with open(path, "r") as arquivo_json:
                dados = json.load(arquivo_json)
                while True:
                    print(f"Tem certeza que deseja deletar {dados.get('Title')}?")
                    escolha = input("Escolha 's' para confirmar ou 'n' para manter na lista de favoritos: ")
                    if escolha == 's':
                        arquivo_json.close()
                        os.remove(path)
                        print("A midia foi deletado da sua lista de favoritos com sucesso.")
                        break
                    elif escolha == 'n':
                        print("A midia foi mantida na sua lista de favoritos.")
                        break
                    else:
                        print("Escolha uma opcao valida.")
                arquivo_json.close()
        except IOError:
            print("Nao foi possivel acessar o arquivo.")
            return

    def deletar_todos_favoritos(self):
        for arquivo in os.listdir(self.nome_pasta):
            if arquivo.endswith(".json"):
                path = f"{self.nome_pasta}/{arquivo}"
                try:
                    os.remove(path)
                except IOError:
                    print("Nao foi possivel acessar o arquivo.")
                    return None