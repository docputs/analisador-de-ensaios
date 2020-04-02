from csv import reader


class Ritmista:
    def __init__(self, nome, apelidos):    # cada ritmista possui um nome e um apelido
        self.nome = nome
        self.apelidos = apelidos


class TrataApelidos:

    @staticmethod
    def tratar_apelidos():
        with open('apelidos.csv', encoding='utf8') as arquivo_apelidos:
            pessoas = reader(arquivo_apelidos)
            lista_pessoas = list(pessoas)
            lista_geral = list()

            for pessoa in lista_pessoas:
                nome = pessoa[0]
                apelidos = pessoa[1::]
                for p, c in enumerate(apelidos):
                    apelidos[p] = c.title()
                lista_geral.append(Ritmista(nome, apelidos))  # adiciona à lista um objeto Ritmista
            return lista_geral
