from colorama import init
from estatistica import Estatistica
from lerdados import Lerdados
from testes import Testes
from mostrardados import Mostrardados
from interface import Interface

init(autoreset=True)

Lerdados.transformar_coluna_duracao()

Interface.mostrarcabecalho()

op = -1

while op != "0":

    op = Interface.menuprincipal()

    if op == "1":
        Mostrardados.mostrartudomusica()

    elif op == "2":
        Mostrardados.mostrartudoartista()
        nome = input("\nquer ver a duração média de um artista especifico? (nome ou enter pra pular): ")
        if nome.strip() != "":
            Mostrardados.mostrarmediaduracaoartista(nome)

    elif op == "3":
        Mostrardados.mostrartudogeral()

    elif op == "0":
        Interface.saida()

    else:
        Interface.opcaoerrada()