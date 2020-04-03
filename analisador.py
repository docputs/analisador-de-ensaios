class Analisador:
    def __init__(self):
        self.naipes = {'caixa': [['caixa', 'cx', 'kxa', 'kx'], 0],
                       'chocalho': [['choc', 'chocs', 'chocalho'], 0],
                       'agogo': [['agogo', 'agg'], 0],
                       'ripa': [['ripa', 'rp', 'repique', 'repinique', 'ripik'], 0],
                       'terceira': [['3', '3ª', 'terças', 'terça', 'terceira'], 0],
                       'primeira': [['primeira', '1ª', '1'], 0],
                       'segunda': [['segunda,' '2', '2ª'], 0],
                       'xequere': [['xequere', 'xqr'], 0],
                       'tamborim': [['tamborim', 'tambo'], 0]}
        self.contador = 0
        self.log = list()

    def checa_instrumento(self, instrumento):
        for naipe, instrumentos in self.naipes.items():
            self.log.append(f'Procurando {instrumento} em {instrumentos[0]}')

            if instrumento in instrumentos[0]:
                self.log.append(f'Encontrei {instrumento}!')

                # se o instrumento (primeiro item da lista invertida) estiver na lista de instrumentos, contador += 1
                self.naipes[naipe][1] += 1
                break

    def analisa_ensaio(self, lista):
        self.log.append('INICIALIZANDO ANÁLISE DE INSTRUMENTOS...')
        lista_ensaio = list()

        for c in lista:
            lista_ensaio.append(c.split())

        for linha in lista_ensaio:
            self.log.append(f'Linha: {linha}')

            try:
                self.checa_instrumento(linha[::-1][0].lower())

            except IndexError:
                self.log.append(f'Erro: {linha}')

            finally:
                self.contador += 1

    def mostra_infos(self):
        lista = set()

        for naipe, num in self.naipes.items():
            if num[1] > 0:  # se o instrumento tiver contador > 0
                lista.add(f'{naipe}: {num[1]}')

        for linha in self.log:
            print(linha)
        return lista
