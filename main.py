url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

# Separando url base e parâmetros.
indice_interrogação = url.find("?")
url_base = url[:indice_interrogação]
print(url_base)
url_parametros = url[indice_interrogação+1:]
print(url_parametros)

# Buscando por parametros especificos.
parametro_busca = "moedaDestino"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
# Se for o ultimo parametro, nao tem e comercial.
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)
