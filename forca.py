# -*- coding: utf-8 -*-                                                        
import random
                        
class Forca():

    def __init__(self):
        self.lista_de_palavras = []
        self.palavra_escolhida = ''
        self.qtd_de_erros = 0
        self.palavra_escondida = ''
        self.alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                                                                              
    def le_arquivo(self):                               
        for palavra in open('dictionary.txt'):                                     
            self.lista_de_palavras.append(palavra[:-2])
        return True    

    def define_palavra(self):
        tamanho_palavra = raw_input('Qual o tamanho de palavra você deseja? ')
        palavras_possiveis = [palavra for palavra in self.lista_de_palavras if len(palavra) == int(tamanho_palavra)]
        if len(palavras_possiveis) != 0:
            self.palavra_escolhida = random.choice(palavras_possiveis)

    def define_qtd_erros(self):
        self.qtd_de_erros = raw_input('Qual a quantidade erros disponiveis? ')
        int(self.qtd_de_erros)

    def monta_interface():        
        pass

    def esconde_palavra(self, palavra):
        for l in palavra:
            self.palavra_escondida.append('-')    



forca = Forca()
forca.le_arquivo()
forca.define_palavra()
