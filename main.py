from analisador import *
from listaensaio import *
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class Home(FloatLayout):
    texto = ObjectProperty(None)

    def botao_analisar(self):
        lista_ensaio = self.texto.text
        self.texto.text = ''
        lista = ListaEnsaio(lista=lista_ensaio, apelidos=False)
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


if __name__ == '__main__':
    Aplicativo().run()
