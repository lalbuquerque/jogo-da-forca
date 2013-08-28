# -*- coding: utf-8 -*-                                                        
import random
                        
class Forca():

    def __init__(self):
        self.lista_de_palavras = []
        self.palavra_escolhida = ''
                                                                              
    def le_arquivo(self):                               
        for palavra in open('dictionary.txt'):                                     
            self.lista_de_palavras.append(palavra[:-2])
        return True    

    def define_palavra(self):
        tamanho_palavra = raw_input('Qual o tamanho de palavra você deseja? ')
        palavras_possiveis = [palavra for palavra in self.lista_de_palavras if len(palavra) == int(tamanho_palavra)]
        if len(palavras_possiveis) != 0:
            self.palavra_escolhida = random.choice(palavras_possiveis)

forca = Forca()
forca.le_arquivo()
forca.define_palavra()
