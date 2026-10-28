import requests

url = "https://dummyjson.com/products/category/smartphones"

def buscarCelular():
    try:
        resposta = requests.get(url, verify=False)

        if resposta.status_code == 200:
            return resposta.json()['products']
        elif resposta.status_code == 404:
            print('Não foi possível encontrar o endereço')
        elif resposta.status_code == 500:
            print('Erro no servidor')
        else:
            print(f'Erro: {resposta.status_code}')
    except ConnectionError:
        print('Erro de conexão!')
    except Exception as e:
        print(f'Erro: {e}')

def filtroCelular(buscarCelular, busca):
    resultado = []

    for celular in buscarCelular:
        titulo = celular['title']
        marca = celular.get('brand', 'Não informada')
        descricao = celular['description']

        texto = f"{titulo}  {marca}  {descricao}".lower()

        if busca in texto:
            resultado.append(celular)

    return resultado

def ordemCelular(resultado):
    resultado = sorted(resultado, key=lambda c:c ['price'])

    print(f'{len(resultado)} celulares encontrados: ')

    for celular in resultado:
        titulo = celular["title"]
        marca = celular.get("brand", "Não informada")
        descricao = celular["description"]
        preco = celular["price"]
        avaliacao = celular["rating"]

        print("-" * 30)
        print(f"Título: {titulo}")
        print(f"Marca: {marca}")
        print(f"Descrição: {descricao}")
        print(f"Preço: US$ {preco}")
        print(f"Avaliação: {avaliacao}")

def main():
    listaCelulares = buscarCelular()

    if listaCelulares is None:
        return

    while True:
        busca = input("\nBuscar celular ou sair para encerrar: ").lower()

        if busca == 'sair':
            print("Programa encerrado.")
            break

        if busca == '':
            print("Digite alguma coisa para buscar.")
            continue
        
        resultado = filtroCelular(listaCelulares, busca)

        if resultado:
            ordemCelular(resultado)
        else:
            print('nenhum celular encontrado.')
main()