# -*- coding: utf-8 -*-
from forca import Forca
from os import system


jogo = Forca()
if jogo.le_arquivo():
    jogo.define_palavra()
    jogo.define_qtd_erros()
    jogo.monta_palavra_escondida()
    system('clear')
    while jogo.qtd_de_erros > 0:
        print '###########       JOGO DA FORCA        ###############'
        print
        print
        jogo.mostra_palavra_escondida()
        print
        print
        jogo.exibe_alfabeto()
        print
        print
        print 'Tamanho da palavra: %s' % jogo.tamanho_palavra
        print 'Voce tem %s erros restantes ' % jogo.qtd_de_erros
        jogo.coleta_escolha()
        system('clear')
        continue
        if jogo.qtd_de_erros == 0:
            break
    print 'GAME OVER !!!!!!!!!!!!!!!!!!!!!!!!!!11'