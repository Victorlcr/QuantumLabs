import pygame


class FisicaDaEntidade:
    def __init__(self, jogo, tipo:str, posicao:int, tamanho:int):
        self.jogo = jogo
        self.tipo = tipo
        self.posicao = list(posicao)
        self.tamanho = tamanho
        self.velocidade = [0,0]

    def atualizar(self, movimento=(0,0)):
        movimento_por_frame = (movimento[0] + self.velocidade[0],
                               movimento[1] + self.velocidade[1])
        
        # Soma valores no vetor da direçao pressionada
        self.posicao[0] += movimento_por_frame[0]
        self.posicao[1] += movimento_por_frame[1]

    def renderizar(self, andar):
        andar.blit(self.jogo.caracter['jogador'], self.posicao)