from kivy.app import App
from csv import reader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class Home(FloatLayout):
    texto = ObjectProperty(None)

    def botao_analisar(self):
        lista_ensaio = self.texto.text
        self.texto.text = ''
        lista = ListaEnsaio(lista_ensaio)
        try:
            lista.trata_lista()
        except IndexError:
            self.janela_popup(lista.lista_log)
        else:
            Analisador.analisa_ensaio(lista.lista)
            quantidade = Analisador.mostra_infos()
            lista_quantidade = '\n'.join(quantidade)
            self.texto.text = f'{lista.presentes} pessoas na lista\n\n{lista_quantidade}'
            self.janela_popup(lista.lista_log)

    def botao_colar(self):
        self.texto.paste()

    def botao_copiar(self):
        self.texto.copy(data=self.texto.text)
        self.texto.text = ''

    def janela_popup(self, msg):
        janela = Janela()
        janela.imprimir(msg)
        janela.open()


class Janela(Popup):
    label = ObjectProperty(None)

    def imprimir(self, msg):
        self.label.text = str(msg)


class Aplicativo(App):
    def build(self):
        return Home()


class Analisador:
    naipes = {'caixa': [['caixa', 'cx', 'kxa', 'kx'], 0],
              'chocalho': [['choc', 'chocs', 'chocalho'], 0],
              'agogo': [['agogo', 'agg'], 0],
              'ripa': [['ripa', 'rp', 'repique', 'repinique', 'ripik'], 0],
              'terceira': [['3', '3ª', 'terças', 'terça', 'terceira'], 0],
              'primeira': [['primeira', '1ª', '1'], 0],
              'segunda': [['segunda,' '2', '2ª'], 0],
              'xequere': [['xequere', 'xqr'], 0],
              'tamborim': [['tamborim', 'tambo'], 0]}
    contador = 0

    @classmethod
    def checa_instrumento(cls, naipe):
        for np, nomes in cls.naipes.items():
            if naipe in nomes[0]:
                cls.naipes[np][1] += 1
                break

    @classmethod
    def analisa_ensaio(cls, lista):
        lista_ensaio = list()
        for c in lista:
            lista_ensaio.append(c.split())
        for linha in lista_ensaio:
            try:
                for instrumento in cls.naipes.values():
                    if linha[::-1][0].lower() in instrumento[0]:
                        cls.checa_instrumento(linha[::-1][0].lower())
                        break
            except IndexError:
                print(f'\033[31mErro na linha {linha}\033[m')
            finally:
                cls.contador += 1

    @classmethod
    def mostra_infos(cls):
        lista = set()
        for naipe, num in cls.naipes.items():
            lista.add(f'{naipe}: {num[1]}')
        return lista


class Ritmista:
    def __init__(self, nome, apelidos):
        self.__nome = nome
        self.__apelidos = apelidos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def apelidos(self):
        return self.__apelidos


class ListaEnsaio:
    def __init__(self, lista):
        self.lista = lista
        self.lista_apelidos = self.tratar_apelidos()
        self.data = None
        self.presentes = None
        self.cabecalho = None
        self.lista_log = set()

    def lista_apelidos(self):
        return self.lista_apelidos

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
                lista_geral.append(Ritmista(nome, apelidos))
            return lista_geral

    def trata_lista(self):
        lista = self.lista.split('\n')
        self.data = lista[0].split()[::-1][0]
        lista = lista[3:]
        self.presentes = len(lista)
        self.cabecalho = self.lista.split("\n")[0] + '\n' + f'{self.presentes} pessoas na lista'
        for pos, pessoa in enumerate(lista):
            if len(pessoa.split()) == 3:
                name = pessoa.split()[0].title()
            elif len(pessoa.split()) == 4:
                if ('h' or 'H' or 'atras') in pessoa.split()[3]:
                    lista[pos] = lista[pos].split()[:3]
                    lista[pos] = ' '.join(lista[pos]).title()
                name = (pessoa.split()[0] + ' ' + pessoa.split()[1]).title()
            elif len(pessoa.split()) == 5:
                if ('h' or 'H' or 'atras') in pessoa.split()[4]:
                    lista[pos] = lista[pos].split()[:3]
                    lista[pos] = ' '.join(lista[pos]).title()
                name = (pessoa.split()[0] + ' ' + pessoa.split()[1]).title()
            else:
                self.lista_log.add(f'Linha {pos+1} -> "{pessoa}"')
                name = ''
            for apelido in self.lista_apelidos:
                if name in apelido.apelidos:
                    lista[pos] = lista[pos].title().replace(name, apelido.nome)
                    break
        self.lista = lista
        if len(self.lista_log) == 0:
            self.lista_log.add('Lista analisada com sucesso')


if __name__ == '__main__':
    Aplicativo().run()
