from csv import reader


class Ritmista:
    def __init__(self, nome, apelidos):    # cada ritmista possui um nome e um apelido
        self.nome = nome
        self.apelidos = apelidos


class TrataApelidos:

    @staticmethod
    def tratar_apelidos():
        with open('apelidos.csv', encoding='utf8') as arquivo_apelidos:  # abre o arquivo com nomes e apelidos
            pessoas = reader(arquivo_apelidos)
            lista_pessoas = list(pessoas)  # lista de nomes e apelidos
            lista_geral = list()  # lista_geral será uma lista com vários objetos de Ritmista

            for pessoa in lista_pessoas:
                nome = pessoa[0]  # pega o nome da pessoa
                apelidos = pessoa[1::]  # pega os apelidos dessa pessoa

                for p, c in enumerate(apelidos):
                    apelidos[p] = c.title()  # muda os apelidos para maíusculo

                lista_geral.append(Ritmista(nome, apelidos))  # adiciona à lista um objeto Ritmista
            return lista_geral
