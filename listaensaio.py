from tratar_apelidos import *


class ListaEnsaio:
    """
    Recebe uma lista de ensaio e converte para um objeto do tipo ListaEnsaio, com atributos:
    - lista: lista não tratada
    - data: data do ensaio
    - presentes: número de pessoas presentes na lista
    - cabecalho: primeira linha da lista e número de presentes (ex: ENSAIO 17/02 TABU \n 12 pessoas na lista)
    - lista_log: log das operações executadas

    OBS: Se 'apelidos' for verdadeiro, então os apelidos na lista serão convertidos para nomes.
    """

    def __init__(self, lista, apelidos=False):
        self.lista = lista
        self.apelidos = apelidos
        self.data = None
        self.presentes = None
        self.cabecalho = None
        self.lista_log = list()

    def lista_apelidos(self):
        return self.lista_apelidos

    def trata_lista(self):
        lista = self.lista.split('\n')
        self.data = lista[0].split()[::-1][0]  # extrai a data do ensaio
        lista = lista[3:]  # remove as duas primeiras linhas da lista (ENSAIO dd/mm \n tema: cores)
        self.presentes = len(lista)
        self.cabecalho = self.lista.split("\n")[0] + '\n' + f'{self.presentes} pessoas na lista'

        for pos, pessoa in enumerate(lista):
            if len(pessoa.split()) == 3:
                # se está formatado corretamente (nome, emoji, instrumento), str nome recebe nome
                nome = pessoa.split()[0]
            elif len(pessoa.split()) == 4:
                # se possui 4 valores (nome, nome2, emoji, instrumento) ou (nome, emoji, emoji, instrumento)
                if ('h' or 'H' or 'atras') in pessoa.split()[3]:
                    lista[pos] = lista[pos].split()[:3]  # remove o último valor da pessoa
                    lista[pos] = ' '.join(lista[pos])  # junta a lista novamente
                nome = pessoa.split()[0] + ' ' + pessoa.split()[1]  # junta o primeiro com o segundo nome
            elif len(pessoa.split()) == 5:
                # se possui 5 valores (nome, nome2, emoji, emoji, instrumento)
                if ('h' or 'H' or 'atras') in pessoa.split()[4]:
                    lista[pos] = lista[pos].split()[:4]
                    lista[pos] = ' '.join(lista[pos])
                nome = pessoa.split()[0] + ' ' + pessoa.split()[1]
            else:
                self.lista_log.append(f'Erro em "{pessoa}"')  # adiciona erro ao log
                nome = ''

            if self.apelidos:
                lista_apelidos = TrataApelidos.tratar_apelidos()
                for apelido in lista_apelidos:
                    if nome in apelido.apelidos:
                        lista[pos] = lista[pos].title().replace(nome, apelido.nome)
                        break

        self.lista = lista

        if len(self.lista_log) == 0:
            self.lista_log.append('Lista analisada com sucesso')
