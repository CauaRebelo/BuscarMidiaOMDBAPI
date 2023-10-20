import json
import requests
import os


class GerenciadorOMDB:

    def __init__(self, api_key):
        self.api_key = api_key

    def pesquisa_filmes(self, titulo, pagina):
        try:
            url = f"https://www.omdbapi.com/?apikey={self.api_key}&s={titulo}&page={pagina}"
            resposta = requests.get(url)
            if resposta.status_code == 200:
                return resposta.json()
            else:
                print(f"Erro ao buscar dados JSON. Status code: {resposta.status_code}")
                return None
        except Exception as e:
            print(f"Erro na solicitação: {e}")
            return None

    def exibir_titulos(self, data):
        if not data:
            return
        filmes = data.get("Search", [])
        imdb_ids = {}
        for i, filme in enumerate(filmes):
            titulo = filme.get("Title")
            imdb_id = filme.get("imdbID")
            imdb_ids[i] = imdb_id
            print(f"{i}: {titulo}")

        return imdb_ids

    def exibir_detalhes(self, id_escolhido):
        try:
            url = f"https://www.omdbapi.com/?apikey={self.api_key}&i={id_escolhido}"
            resposta = requests.get(url)

            if resposta.status_code == 200:
                midia_escolhida = resposta.json()
                print("Detalhes da midia selecionada:")
                print(f"Titulo: {midia_escolhida.get('Title')}")
                print(f"Ano de Lancamento: ", midia_escolhida.get('Year'))
                print(f"Classificacao: ", midia_escolhida.get('Rated'))
                print(f"Sinopse: ", midia_escolhida.get('Plot'))
                print(f"Diretor: ", midia_escolhida.get('Director'))
                return resposta.json()
        except Exception as e:
            print(f"Erro na solicitação: {e}")
            return None

    def salvar_favoritos(self, nome_pasta, data):
        if not data:
            return
        os.makedirs(nome_pasta, exist_ok=True)
        path = f"{nome_pasta}/{data.get('imdbID')}.json"
        if not os.path.exists(path):
            try:
                with open(path, 'w') as arquivo_filme:
                    json.dump(data, arquivo_filme)
                arquivo_filme.close()
                print("Salvo como favoritos com sucesso!")
                return
            except IOError:
                print("Nao foi possivel criar o arquivo.")
                return
        print("O arquivo ja esta salvo como favoritos.")
        return