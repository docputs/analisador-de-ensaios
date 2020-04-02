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
