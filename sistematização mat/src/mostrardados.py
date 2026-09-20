import matplotlib.pyplot as plt
from lerdados import Lerdados
from estatistica import Estatistica
from testes import Testes


class Mostrardados:

    # dados sobre musica

    @staticmethod
    def mostrarporcentagemduracao():
        duracoes = Lerdados.bancodados["duration"]
        total = len(duracoes)

        menos_2min = [d for d in duracoes if d < 120]
        entre_2_3min = [d for d in duracoes if 120 <= d < 180]
        entre_3_4min = [d for d in duracoes if 180 <= d < 240]
        mais_4min = [d for d in duracoes if d >= 240]

        print(f"< 2 min: {Estatistica.porcentagem(len(menos_2min), total):.2f}%")
        print(f"2–3 min: {Estatistica.porcentagem(len(entre_2_3min), total):.2f}%")
        print(f"3–4 min: {Estatistica.porcentagem(len(entre_3_4min), total):.2f}%")
        print(f"> 4 min: {Estatistica.porcentagem(len(mais_4min), total):.2f}%")

    @staticmethod
    def mostrarmediaduracaomusica():
        duracoes = Lerdados.bancodados["duration"]
        print(f"Duração média: {Estatistica.media(duracoes):.2f} segundos")
        print(f"Mediana: {Estatistica.mediana(duracoes):.2f} segundos")
        print(f"Moda: {Estatistica.moda(duracoes)} segundos")

    @staticmethod
    def mostrarmusicamaistocada():
        linha = Lerdados.bancodados["popularity"].idxmax()
        musica = Lerdados.bancodados.loc[linha]
        print(f"Música mais tocada: {musica['track_name']} ({musica['artist_names']}) - popularidade {musica['popularity']}")

    @staticmethod
    def mostrarmusicamenostocada():
        linha = Lerdados.bancodados["popularity"].idxmin()
        musica = Lerdados.bancodados.loc[linha]
        print(f"Música menos tocada: {musica['track_name']} ({musica['artist_names']}) - popularidade {musica['popularity']}")

    @staticmethod
    def mostrarmusicamaislonga():
        linha = Lerdados.bancodados["duration"].idxmax()
        musica = Lerdados.bancodados.loc[linha]
        print(f"Música mais longa: {musica['track_name']} - {musica['duration']} segundos")

    @staticmethod
    def mostrarmusicamaiscurta():
        linha = Lerdados.bancodados["duration"].idxmin()
        musica = Lerdados.bancodados.loc[linha]
        print(f"Música mais curta: {musica['track_name']} - {musica['duration']} segundos")

    @staticmethod
    def mostrarrelacaotempopopularidade():
        duracoes = Lerdados.bancodados["duration"]
        popularidades = Lerdados.bancodados["popularity"]
        correlacao = duracoes.corr(popularidades)
        print(f"Correlação entre duração e popularidade: {correlacao:.3f}")

    @staticmethod
    def mostrarsorteioduracao():
        duracoes = list(Lerdados.bancodados["duration"])
        resultados = Testes.simulacao(duracoes, 1000)
        print(f"Duração média em 1000 sorteios: {Estatistica.media(resultados):.2f} segundos")

    # dados sobre artistas

    @staticmethod
    def listaartistas():
        artistas = []
        for nomes in Lerdados.bancodados["artist_names"]:
            for artista in nomes.split("|"):
                artistas.append(artista)
        return artistas

    @staticmethod
    def mostrarartistamaistocado():
        artistas = Mostrardados.listaartistas()
        contagem = Testes.frequencia(artistas)
        maior = max(contagem.values())
        for artista in contagem:
            if contagem[artista] == maior:
                print(f"Artista com mais músicas no top 10k: {artista} ({maior} músicas)")
                break

    @staticmethod
    def mostrarartistamenostocado():
        artistas = Mostrardados.listaartistas()
        contagem = Testes.frequencia(artistas)
        menor = min(contagem.values())
        for artista in contagem:
            if contagem[artista] == menor:
                print(f"Artista com menos músicas no top 10k: {artista} ({menor} música(s))")
                break

    @staticmethod
    def mostrarmediaduracaoartista(nome_artista):
        duracoes = []
        for i in range(len(Lerdados.bancodados)):
            nomes = Lerdados.bancodados.iloc[i]["artist_names"]
            if nome_artista in nomes.split("|"):
                duracoes.append(Lerdados.bancodados.iloc[i]["duration"])
        if duracoes:
            print(f"Duração média de {nome_artista}: {Estatistica.media(duracoes):.2f} segundos")
        else:
            print(f"Artista {nome_artista} não encontrado")

    @staticmethod
    def mostrarsorteioartista():
        artistas = Mostrardados.listaartistas()
        resultados = Testes.simulacao(artistas, 100)
        porcentagens = Testes.porcentagens(resultados)
        for artista in porcentagens:
            print(f"{artista}: {porcentagens[artista]:.2f}%")

    # dados gerais

    @staticmethod
    def mostrarestatisticasgerais():
        print("=== Estatísticas gerais ===")
        Mostrardados.mostrarmediaduracaomusica()
        Mostrardados.mostrarmusicamaistocada()
        Mostrardados.mostrarmusicamenostocada()
        Mostrardados.mostrarartistamaistocado()
        Mostrardados.mostrarartistamenostocado()
        Mostrardados.mostrarrelacaotempopopularidade()

    @staticmethod
    def mostrarporcentagemsorteioacimade3min():
        duracoes = list(Lerdados.bancodados["duration"])
        resultados = Testes.simulacao(duracoes, 1000)
        acima_3min_sorteio = [d for d in resultados if d > 180]
        acima_3min_geral = [d for d in duracoes if d > 180]

        porcentagem_sorteio = Estatistica.porcentagem(len(acima_3min_sorteio), len(resultados))
        porcentagem_geral = Estatistica.porcentagem(len(acima_3min_geral), len(duracoes))

        print(f"Sorteio (1000x) acima de 3 min: {porcentagem_sorteio:.2f}%")
        print(f"Geral do dataset acima de 3 min: {porcentagem_geral:.2f}%")

    # graficos

    @staticmethod
    def mostrargraficoduracao():
        duracoes = Lerdados.bancodados["duration"]

        menos_2min = len([d for d in duracoes if d < 120])
        entre_2_3min = len([d for d in duracoes if 120 <= d < 180])
        entre_3_4min = len([d for d in duracoes if 180 <= d < 240])
        mais_4min = len([d for d in duracoes if d >= 240])

        faixas = ["< 2 min", "2-3 min", "3-4 min", "> 4 min"]
        valores = [menos_2min, entre_2_3min, entre_3_4min, mais_4min]

        plt.bar(faixas, valores, color="hotpink")
        plt.title("Músicas por faixa de duração")
        plt.ylabel("quantidade de músicas")
        plt.show()

    @staticmethod
    def mostrargraficocorrelacao():
        duracoes = Lerdados.bancodados["duration"]
        popularidades = Lerdados.bancodados["popularity"]

        plt.scatter(duracoes, popularidades, color="hotpink", alpha=0.4)
        plt.title("Duração x Popularidade")
        plt.xlabel("duração (segundos)")
        plt.ylabel("popularidade")
        plt.show()

    @staticmethod
    def mostrargraficoartistas():
        artistas = Mostrardados.listaartistas()
        contagem = Testes.frequencia(artistas)

        top10 = sorted(contagem.items(), key=lambda item: item[1], reverse=True)[:10]
        nomes = [item[0] for item in top10]
        quantidades = [item[1] for item in top10]

        plt.barh(nomes, quantidades, color="hotpink")
        plt.title("Top 10 artistas com mais músicas no top 10k")
        plt.xlabel("quantidade de músicas")
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()

    # mostra tudo de uma vez por topico

    @staticmethod
    def mostrartudomusica():
        print("\n=== MUSICA ===")
        Mostrardados.mostrarmediaduracaomusica()
        Mostrardados.mostrarmusicamaistocada()
        Mostrardados.mostrarmusicamenostocada()
        Mostrardados.mostrarmusicamaislonga()
        Mostrardados.mostrarmusicamaiscurta()
        Mostrardados.mostrarrelacaotempopopularidade()
        Mostrardados.mostrarsorteioduracao()
        Mostrardados.mostrarporcentagemsorteioacimade3min()
        Mostrardados.mostrargraficoduracao()
        Mostrardados.mostrargraficocorrelacao()

    @staticmethod
    def mostrartudoartista():
        print("\n=== ARTISTA ===")
        Mostrardados.mostrarartistamaistocado()
        Mostrardados.mostrarartistamenostocado()
        Mostrardados.mostrarsorteioartista()
        Mostrardados.mostrargraficoartistas()

    @staticmethod
    def mostrartudogeral():
        Mostrardados.mostrarestatisticasgerais()
        Mostrardados.mostrarporcentagemsorteioacimade3min()
        Mostrardados.mostrargraficoduracao()
        Mostrardados.mostrargraficoartistas()