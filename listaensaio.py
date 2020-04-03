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
        self.log = list()

    def trata_lista(self):
        self.log.append('INICIALIZANDO A LISTA...')
        if self.apelidos:
            # converte apelidos para nomes se 'apelidos' for True
            self.log.append('Apelidos serão convertidos em nomes...')
            lista_apelidos = TrataApelidos.tratar_apelidos()
        else:
            self.log.append('Apelidos não serão convertidos em nomes...')

        lista = self.lista.split('\n')

        self.log.append('Extraindo a data do ensaio...')
        self.data = lista[0].split()[::-1][0]  # extrai a data do ensaio
        self.log.append(f'Data extraída com sucesso! Data do ensaio: {self.data}')

        lista = lista[3:]  # remove as duas primeiras linhas da lista (ENSAIO dd/mm \n tema: cores)

        self.log.append('Extraindo número de pessoas na lista...')
        self.presentes = len(lista)
        self.log.append(f'Número de pessoas na lista extraído com sucesso! {self.presentes} pessoas no ensaio')

        self.log.append('Montando o cabeçalho principal...')
        self.cabecalho = self.lista.split("\n")[0] + '\n' + f'{self.presentes} pessoas na lista'
        self.log.append(f'Cabeçalho montado com sucesso!\n{self.cabecalho}')

        self.log.append('-' * 30)
        self.log.append('INICIALIZANDO ANÁLISE DE RITMISTAS...')

        for pos, pessoa in enumerate(lista):
            if len(pessoa.split()) == 3:
                # se está formatado corretamente (nome, emoji, instrumento), str nome recebe nome
                nome = pessoa.split()[0]
                self.nome_no_log(nome, pessoa)

            elif len(pessoa.split()) == 4:
                # se possui 4 valores (nome, nome2, emoji, instrumento) ou (nome, emoji, emoji, instrumento)
                if ('h' or 'H' or 'atras') in pessoa.split()[3]:
                    lista[pos] = lista[pos].split()[:3]  # remove o último valor da pessoa
                    lista[pos] = ' '.join(lista[pos])  # junta a lista novamente
                    nome = pessoa.split()[0]
                else:
                    nome = pessoa.split()[0] + ' ' + pessoa.split()[1]  # junta o primeiro com o segundo nome
                self.nome_no_log(nome, pessoa)

            elif len(pessoa.split()) == 5:
                # se possui 5 valores (nome, nome2, emoji, emoji, instrumento)
                if ('h' or 'H' or 'atras') in pessoa.split()[4]:
                    lista[pos] = lista[pos].split()[:4]
                    lista[pos] = ' '.join(lista[pos])
                nome = pessoa.split()[0] + ' ' + pessoa.split()[1]
                self.nome_no_log(nome, pessoa)

            else:
                self.lista_log.append(f'Erro em "{pessoa}"')  # adiciona erro ao log do popup
                nome = 'Erro'

            if self.apelidos:
                # funciona se 'apelidos' for True
                self.log.append('Convertendo o apelido em nome...')

                for apelido in lista_apelidos:
                    if nome == 'Erro':
                        self.log.append('Erro ao converter apelido...')
                        break

                    self.log.append(f'{nome.title()} -> {apelido.apelidos}')

                    if nome.title() in apelido.apelidos:
                        # se o apelido estiver na lista de apelidos, substitui esse apelido pelo nome
                        lista[pos] = lista[pos].title().replace(nome.title(), apelido.nome)
                        break

                self.log.append('Apelido convertido com sucesso!')

        self.lista = lista

        if len(self.lista_log) == 0:
            # se não houve erro
            self.lista_log.append('Lista analisada com sucesso')

        self.log.append('-' * 30)

        for line in self.log:  # REMOVER
            print(line)

    def nome_no_log(self, nome, pessoa):
        self.log.append(f'Encontrei o nome {nome} em [{pessoa}]')


'''
ENSAIO 17/02
tema cores

joao - caixa
didi - chocalho
ju s - primeira
davi-- tamborim
gui - agogo (18h)
'''