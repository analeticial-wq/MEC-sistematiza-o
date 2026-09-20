import pandas as pd
from pathlib import Path


class Lerdados:

    _pasta_do_arquivo = Path(__file__).resolve().parent
    bancodados = pd.read_csv(_pasta_do_arquivo / ".." / "dataset" / "top-10k-spotify-songs-2025-07.csv")

    @staticmethod
    def ler_linha(linha):
        return Lerdados.bancodados.iloc[linha]

    @staticmethod
    def ler_coluna(coluna):
        return Lerdados.bancodados[coluna]

    @staticmethod
    def ler_celula(linha, coluna):
        return Lerdados.bancodados.iloc[linha][coluna]

# fazendo isso pq na tabelaa a duração é uma string e eu quero um int :)
    @staticmethod
    def transformar_duracao(duracao):
        minutos, segundos = duracao.split(":")
        return int(minutos) * 60 + int(segundos)

    @staticmethod
    def lerduracao(linha):
        duracao = Lerdados.bancodados.iloc[linha]["duration"]
        return Lerdados.transformar_duracao(duracao)

# Transformando a coluna inteira em int para possiveis calculos futuros, esse comentario é só para eu nn precisar ficar procurando onde eu apliquei essa idea
    @staticmethod
    def transformar_coluna_duracao():
        Lerdados.bancodados["duration"] = Lerdados.bancodados["duration"].apply(
        Lerdados.transformar_duracao
    )