class Estatistica:

    @staticmethod
    def media(dados):
        return sum(dados) / len(dados)

    @staticmethod
    def mediana(dados):
        dados_ordenados = sorted(dados)
        quantidade = len(dados_ordenados)

        meio = quantidade // 2

        if quantidade % 2 == 0:
            return (dados_ordenados[meio - 1] + dados_ordenados[meio]) / 2
        else:
            return dados_ordenados[meio]

    @staticmethod
    def moda(dados):
        frequencias = {}

        for valor in dados:
            if valor in frequencias:
                frequencias[valor] += 1
            else:
                frequencias[valor] = 1

        maior_frequencia = max(frequencias.values())

        for valor in frequencias:
            if frequencias[valor] == maior_frequencia:
                return valor

    @staticmethod
    def porcentagem(parte, total):
        return (parte / total) * 100