import json
import os


class GerenciadorFavoritos:

    def __init__(self, nome_pasta):
        self.nome_pasta = nome_pasta

    def abrir_favoritos(self):
        imdb_ids = []
        index = 0

        if os.path.exists(self.nome_pasta):
            for arquivo in os.listdir(nome_pasta):
                if arquivo.endswith(".json"):
                    path = f"{nome_pasta}/{arquivo}"

                    with open(path, "r") as arquivo_json:
                        dados = json.load(arquivo_json)

                    if "Title" in dados and "imdbID" in dados:
                        titulos = filme.get("Title")
                        imdb_id = filme.get("imdbID")
                        imdb_ids[index] = imdb_id
                        print(f"{index}: {titulo}")
                        index += 1
            if index == 0:
                print("Não existe mais nada nos favoritos, adicione mais para acessar a lista.")
        else:
            print("Nao existem favoritos, use a função de pesquisa para adicionar midia como favorito.")

