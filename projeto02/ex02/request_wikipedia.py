import requests
import dewiki

def requisicao(termo_busca):
    url = f"https://pt.wikipedia.org/w/api.php?action=query&list=search&srsearch={termo_busca}&format=json"
    response = requests.get(url)
    data = response.json()
    if 'query' in data and 'search' in data['query'] and data['query']['search']:
        page_title = data['query']['search'][0]['title']
        return data
    else:
        print("Nenhum resultado encontrado.")

def processar_resposta_wiki(data, nome_arquivo):
    snippet = data['query']['search'][0]['snippet']
    texto_puro = dewiki.from_wiki(snippet)
    with open(f"{nome_arquivo}.wiki", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"== {nome_arquivo} ==\n{texto_puro}")
    print(f"Resultado salvo em {nome_arquivo}.wiki")

param_pesq = input('Inserir palavra para busca:')
resultado = requisicao(param_pesq)
valida = processar_resposta_wiki(resultado, param_pesq)

# criar funcao processar a resposta da request na API do Wikipedia utilizando a biblioteca json, remover a formatação wiki utilizando o dewiki

# criar uma função que salve o resultado do processamento da resposta em um arquivo nome_da_busca.wiki