from colorama import Fore, Style


class Interface:

    @staticmethod
    def mostrarcabecalho():
        print(Fore.MAGENTA + "╔════════════════════════════╗\n"
              "║  ♫ estatisticas spotify    ║\n"
              "╚════════════════════════════╝")

    @staticmethod
    def menuprincipal():
        print(Fore.MAGENTA + "\n· · · menu · · ·")
        print(Fore.MAGENTA + "* digite:\n"
              "°[1] estatisticas de musica\n"
              "  °[2] estatisticas de artista\n"
              "    °[3] estatisticas gerais\n"
              "*   [0] sair")
        return input("> ")

    @staticmethod
    def opcaoerrada():
        print(Fore.RED + "opção errada, tenta de novo")

    @staticmethod
    def saida():
        print(Fore.GREEN + "flw ( °w° )/")