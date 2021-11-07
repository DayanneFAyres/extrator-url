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
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError("URL nao pode ser vazia.")

    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogação = self.url.find("?")
        url_base = self.url[:indice_interrogação]
        return url_base

    def valida_url_base(self):
        """Valida se a url apresenta o padroa https e termina com /cambio."""
        url_base = self.get_url_base()
        if not url_base.startswith("https") and not url_base.endswith("/cambio"):
            raise ValueError("URL invalida")

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

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#url = ""
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)