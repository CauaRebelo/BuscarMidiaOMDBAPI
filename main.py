# This is a sample Python script.

import json

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

caminho_fav = "galaxy.json"

def abrir_favoritos():
    try:
        with open(caminho_fav, "r") as arquivo_json:
            # Carregue o conteúdo do arquivo em uma estrutura de dados Python
            favoritos = json.load(arquivo_json)

    except FileNotFoundError:
        print(f"O arquivo '{caminho_galaxy}' não foi encontrado.")
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

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    abrir_favoritos()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
