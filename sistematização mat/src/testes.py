import random


class Testes:

    @staticmethod
    def simulacao(dados, quantidade_testes=100):
        resultados = []

        for i in range(quantidade_testes):
            resultado = random.choice(dados)
            resultados.append(resultado)

        return resultados

    @staticmethod
    def frequencia(resultados):
        contagem = {}

        for resultado in resultados:
            if resultado in contagem:
                contagem[resultado] += 1
            else:
                contagem[resultado] = 1

        return contagem

    @staticmethod
    def porcentagens(resultados):
        contagem = Testes.frequencia(resultados)
        total = len(resultados)

        porcentagens = {}

        for resultado in contagem:
            porcentagens[resultado] = (contagem[resultado] / total) * 100

        return porcentagens