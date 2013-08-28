# -*- coding: utf-8 -*-
import random
import re


class Forca():

    def __init__(self):
        self.lista_de_palavras = []
        self.tamanho_palavra = 0
        self.palavra_escolhida = ''
        self.qtd_de_erros = 0
        self.palavra_escondida = []
        self.alfabeto = []

    def le_arquivo(self):
        for palavra in open('dictionary.txt'):
            self.lista_de_palavras.append(palavra[:-2])
        if len(self.lista_de_palavras) > 0:
            return True
        else:
            return False

    def define_palavra(self):
        self.tamanho_palavra = raw_input('Qual será o tamanho da palavra? ')
        palavras_possiveis = []
        for palavra in self.lista_de_palavras:
            if len(palavra) == int(self.tamanho_palavra):
                palavras_possiveis.append(palavra)
        if len(palavras_possiveis) != 0:
            self.palavra_escolhida = random.choice(palavras_possiveis)

    def define_qtd_erros(self):
        qtd = raw_input('Qual quantidade de erros disponiveis? ')
        self.qtd_de_erros = int(qtd)

    def monta_palavra_escondida(self):
        for l in self.palavra_escolhida:
            self.palavra_escondida.append('-')

    def mostra_palavra_escondida(self):
        print '             ' + ' '.join(self.palavra_escondida)

    def exibe_alfabeto(self):
        self.alfabeto = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        print ' '.join(self.alfabeto)

    def coleta_escolha(self):
        tentativa = raw_input('Escreva uma letra: ')
        tentativa = tentativa.upper()
        if tentativa in self.palavra_escolhida:
            for i in re.finditer(tentativa, self.palavra_escolhida):
                self.palavra_escondida.remove('-')
                self.palavra_escondida.insert(i.start(), tentativa)
        else:
            self.qtd_de_erros -= 1
            print 'Você errou!'
        self.alfabeto.remove(tentativa)