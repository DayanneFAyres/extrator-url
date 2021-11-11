import re

class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        """Valida se a url está vazia e segue o padrao"""
        padrao_url = re.compile("(http(s)?://)?(www\.)?bytebank\.com(\.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é valida")

    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogação = self.url.find("?")
        url_base = self.url[:indice_interrogação]
        return url_base

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        indice_interrogação = self.url.find("?")
        url_parametros = self.url[indice_interrogação + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        url_parametros = self.get_url_parametros()
        indice_parametro = url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = url_parametros.find("&", indice_valor)
        # Se for o ultimo parametro, nao tem e comercial.
        if indice_e_comercial == -1:
            valor = url_parametros[indice_valor:]
        else:
            valor = url_parametros[indice_valor:indice_e_comercial]
        return valor

    def converte_valores(self):
        moeda_destino = self.get_valor_parametro("moedaDestino")
        #moeda_origem = self.get_valor_parametro("moedaOrigem")
        valor_dolar_real = 5.5
        quantidade = float(self.get_valor_parametro("quantidade"))

        if moeda_destino == "real":
            return round(quantidade*valor_dolar_real,2)
        else:
            return round(quantidade/valor_dolar_real,2)


    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + self.get_url_base() + "\n" + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
print("O tamanho da URL: ", len(extrator_url))
print(extrator_url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
conversao = extrator_url.converte_valores()
print("Valor convertido: ", conversao)