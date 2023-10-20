import json
import os


class Favorite:

    def __int__(self, caminho_fav, arquivos_fav, fav_index):
        self.caminho_fav: caminho_fav
        self.arquivos_fav: os.listdir(caminho_fav)
        self.fav_index: len(arquivos_fav)





caminho_fav = "galaxy.json"

def abrir_favoritos():
    try:
        with open(caminho_fav, "r") as arquivo_json:
            # Carregue o conteúdo do arquivo em uma estrutura de dados Python
            favoritos = json.load(arquivo_json)

    except FileNotFoundError:
        print(f"O arquivo '{caminho_fav}' não foi encontrado.")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")

    # Agora você pode trabalhar com os dados como uma estrutura de dados Python
    print("Conteúdo do arquivo JSON:")
    for i, item in enumerate(favoritos, 1):
        print(f"{i}: {item['Title']}")

    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(dados):
            # Exiba os detalhes do item escolhido
            item_escolhido = dados[escolha - 1]
            print("Detalhes do item escolhido:")
            for chave, valor in item_escolhido.items():
                print(f"{chave}: {valor}")
        else:
            print("Escolha inválida. Por favor, escolha um número válido.")
    except ValueError:
        print("Escolha inválida. Por favor, insira um número.")
