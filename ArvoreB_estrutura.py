import struct
from operator import attrgetter

CAPACIDADE_MAXIMA_CHAVES = 10

class Arvore(object):
   
    def __init__(self, _quantidade_chaves_no = CAPACIDADE_MAXIMA_CHAVES):
        self._quantidade_chaves_no = int(_quantidade_chaves_no)
        self._No_raiz = int(0)

    @property
    def _quantidade_chaves_no(self):
        return self._quantidade_chaves_no

    @property
    def No_raiz(self):
        return self._No_raiz

    def adicionar_No_raiz(self, No_raiz):
        self._No_raiz = int(No_raiz)

    def escreve_arvore(self, file):
        binaria_arvore = struct.pack('qq', self._quantidade_chaves_no, self._No_raiz)
        file.write(binaria_arvore)

    def analisa_arvore(self, file):
        linha = file.read(struct.calcsize('qq'))
        auxiliar = struct.unpack('qq', linha)
        arvore = Arvore(auxiliar[0])
        arvore.adicionar_No_raiz(auxiliar[1])
        return arvore

class No(object):
   
    def __init__(self):
        self._quantidade_chaves = int(0)
        self._chaves = []
        self._No_maior_chave = int(0)
        self._endereco_pai = int(0)

    @property
    def quantidade_chaves(self):
        return self._quantidade_chaves

    def adicionar_quantidade_chaves(self, quantidade):
        self._quantidade_chaves = quantidade

    @property
    def chaves(self):
        return self._chaves

    def inclui_chave(self, chave):
        self._chaves.append(chave)
        self._quantidade_chaves += 1
        self._chaves.sort(key=attrgetter("chave"))

    @property
    def No_maior_chave(self):
        return self._No_maior_chave

    def set_No_maior_chave(self, posicao):
        self._No_maior_chave = int(posicao)

    @property
    def endereco_pai(self):
        return self._endereco_pai

    def adicionar_endereco_pai(self, ponteiro):
        self._endereco_pai = ponteiro

    def escreve_No(self, file):
        quantidade_chaves_binario = struct.pack('q', self._quantidade_chaves)
        file.write(quantidade_chaves_binario)
        for j in range(0, CAPACIDADE_MAXIMA_CHAVES):
            if (j + 1) <= self._quantidade_chaves:
                chave_binaria = struct.pack('qqq', self._chaves[j].chave, self._chaves[j].endereco_arquivo,
                                self._chaves[j].pos_No_menor_chave)
                file.write(chave_binaria)
            else:
                zero = struct.pack('qqq', 0, 0, 0)
                file.write(zero)
        maior_binario = struct.pack('q', self._No_maior_chave)
        file.write(maior_binario)
        endereco_pai_binario = struct.pack('q', self._endereco_pai)
        file.write(endereco_pai_binario)

    def le_No(self, file):
        No = No()
        quantidade_chaves_binario = file.read(struct.calcsize('q'))
        quantidade_chaves = struct.unpack('q', quantidade_chaves_binario)
        No.adicionar_quantidade_chaves(quantidade_chaves[0])
        for j in range(0, No.quantidade_chaves):
            chave_binaria = file.read(struct.calcsize('qqq'))
            chave_auxiliar = struct.unpack('qqq', chave_binaria)
            chave = Chave(chave_auxiliar[0], chave_auxiliar[1], chave_auxiliar[2])
            No.chaves.append(chave)
            No.chaves.sort(key=attrgetter("chave"))
        for i in range(No.quantidade_chaves, CAPACIDADE_MAXIMA_CHAVES):
            zero = file.read(struct.calcsize('qqq'))
        maior_binario = file.read(struct.calcsize('q'))
        pos_maior = struct.unpack('q', maior_binario)
        No.set_No_maior_chave(pos_maior[0])
        endereco_pai_binario = file.read(struct.calcsize('q'))
        endereco_pai = struct.unpack('q', endereco_pai_binario)
        No.adicionar_endereco_pai(endereco_pai[0])
        return No

class Chave(object):


    def __init__(self, chave, ponteiro, pos_No_menor_chave = 0):
        self._chave = int(chave)
        self._endereco_arquivo = int(ponteiro)
        self._No_menor_chave = int(pos_No_menor_chave)

    @property
    def chave(self):
        return self._chave

    @property
    def endereco_arquivo(self):
        return self._endereco_arquivo

    @property
    def pos_No_menor_chave(self):
        return self._No_menor_chave

    def set_No_menor_chave(self, posicao):
        self._No_menor_chave = int(posicao)