
from ArvoreB_estrutura import *
import sys

def Pesquisa_Arvore(key, endereco, pasta):
    No = No()
    pasta.seek(endereco)
    No_auxiliar = No.le_No(pasta)
    for i in range(0, No_auxiliar.quantidade_chaves):
        if key == No_auxiliar.chaves[i].chave:
            print("\nChave " + str(No_auxiliar.chaves[i].chave) + " Está na arvore.\n")
        return
    for i in range(0, No_auxiliar.quantidade_chaves):
        if key < No_auxiliar.chaves[i].chave:
            if No_auxiliar.chaves[i].No_menor_chave == 0:
                print("\nChave " + str(key) + " Não está na arvore.\n")
            else:
                Pesquisa_Arvore(key, No_auxiliar.chaves[i].No_menor_chave, pasta)
            return
    Pesquisa_Arvore(key, No_auxiliar.No_maior_chave, pasta)

def insere_arvore(chave, endereco, pasta):
    No = No()
    pasta.seek(endereco)
    No_auxiliar = No.le_No(pasta)
    for i in range(0, No_auxiliar.quantidade_chaves):
        if chave.chave == No_auxiliar.chaves[i].chave:
            print('A chave já se encontra presente na arvore.')
            return
        if chave.chave < No_auxiliar.chaves[i].chave:
            if No_auxiliar.chaves[i].No_menor_chave == 0:
                No_auxiliar.adicionar_chave(chave)
                if No_auxiliar.quantidade_chaves < CAPACIDADE_MAXIMA_CHAVES:
                    pasta.seek(endereco)
                    No_auxiliar.escreve_No(pasta)
                    print('Chave adicionada com sucesso.')
                    return
                else:
                    dividir(No_auxiliar, endereco, pasta)
                    return
            else:
                endereco = No_auxiliar.chaves[i].No_menor_chave
                insere_arvore(chave, endereco, pasta)
                return
    if chave.chave > No_auxiliar.chaves[No_auxiliar.quantidade_chaves - 1].chave:
        if No_auxiliar.No_maior_chave == 0:
            No_auxiliar.adicionar_chave(chave)
            if No_auxiliar.quantidade_chaves < CAPACIDADE_MAXIMA_CHAVES:
                    pasta.seek(endereco)
                    No_auxiliar.escreve_No(pasta)
                    print('Chave adicionada com sucesso.')
            else:
                dividir(No_auxiliar, endereco, pasta)
        else:
            endereco = No_auxiliar.No_maior_chave
            insere_arvore(chave, endereco, pasta)

def dividir(No, endereco, pasta):
    chave_aux = Chave(0, 0)
    No_auxiliar1 = No()
    No_auxiliar2 = No()
    No_auxiliar3 = No()
    for i in range(0, No.quantidade_chaves):
        if i < (CAPACIDADE_MAXIMA_CHAVES)//2:
            No_auxiliar2.adicionar_chave(No.chaves[i])
        if i == (CAPACIDADE_MAXIMA_CHAVES)//2:
            chave_aux = No.chaves[i]
        if i > (CAPACIDADE_MAXIMA_CHAVES)//2:
            No_auxiliar3.adicionar_chave(No.chaves[i])
    pos = pasta.seek(endereco)
    chave_aux.set_No_menor_chave(pos)
    No_auxiliar2.adiciona_endereco_pai(No.endereco_pai)
    No_auxiliar2.escreve_No(pasta)
    pasta.seek(0, 2)
    No_auxiliar3.adiciona_endereco_pai(No.endereco_pai)
    No_auxiliar3.escreve_No(pasta)
    pasta.seek(No.endereco_pai)
    No_auxiliar1 = No_auxiliar1.le_No(pasta)
    No_auxiliar1.adicionar_chave(chave_aux)
    if No_auxiliar1.quantidade_chaves == CAPACIDADE_MAXIMA_CHAVES:
        dividir(No_auxiliar1, No.endereco_pai, pasta)
    else:
        pasta.seek(No.endereco_pai)
        No_auxiliar1.escreve_No(pasta)
        print('Chave adicionada com sucesso.')

def delete_arvore(chave, endereco, pasta):
    pass

def imprime_arvore_ordem(pasta):
    arvore = Arvore()
    pasta.seek(0, 0)
    limite = pasta.tell()
    lista = []
    arvore_auxiliar = arvore.le_arvore(pasta)
    print('Esta arvore B esta lotada: ' + str(arvore_auxiliar.quantidade_chaves_No))
    No = No()
    tamanho_pasta = pasta.seek(0, 2)
    pasta.seek(arvore_auxiliar.No_raiz)
    while limite < tamanho_pasta:
        No_auxiliar = No.le_No(pasta)
        for i in range(0, No_auxiliar.quantidade_chaves):
            lista.append(No_auxiliar.chaves[i])
        limite = pasta.tell()
    lista.sort(key=attrgetter("chave"))
    for chave in lista:
        print(chave.chave, end=' ')

def imprime_arvore(pasta):
    pasta.seek(0, 0)
    arvore_auxiliar = Arvore()
    arvore_auxiliar = arvore_auxiliar.le_arvore(pasta)
    No = No()
    limite = pasta.seek(0, 2)
    pasta.seek(arvore_auxiliar.No_raiz)
    while No:
        aux = pasta.tell()
        if aux == limite:
            break
        No_auxiliar = No.le_No(pasta)
        print('\nposição: ' + str(aux))
        print("quantidade de chaves: " + str(No_auxiliar.quantidade_chaves))
        print("No Pai: " + str(No_auxiliar.endereco_pai))
        for i in range(0, int(No_auxiliar.quantidade_chaves)):
            print("Chave: " + str(No_auxiliar.chaves[i].chave) + str(No_auxiliar.chaves[i].No_menor_chave))