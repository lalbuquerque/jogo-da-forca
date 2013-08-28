# -*- coding: utf-8 -*-                                                        
import random
                                                                              
def le_arquivo():                                                              
    lista_de_palavras = []                                                     
    for palavra in open('dictionary.txt'):                                     
        lista_de_palavras.append(palavra[:-2])
    print lista_de_palavras[:11]

def define_palavra():
    pass

le_arquivo()
