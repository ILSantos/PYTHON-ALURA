from extrator_argumentos_url import ExtratorArgumentoURL

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"

cambio = ExtratorArgumentoURL(url)
moeda_origem, moeda_destino = cambio.retorna_moedas()
valor = cambio.retorna_valor()

print("Teste 1: ", moeda_origem, moeda_destino, valor)
""" 
url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"

cambio = ExtratorArgumentoURL(url)
moeda_origem, moeda_destino = cambio.retorna_moedas()
valor = cambio.retorna_valor()

print("Teste 2: ", moeda_origem, moeda_destino, valor)
 """