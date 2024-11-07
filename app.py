import sys
import pygame

from entidade import FisicaDaEntidade
from utils import load_image

class Jogo:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('M00RS')  # Nome da janela 
        self.tela = pygame.display.set_mode((720,480))  # Largura x altura
        self.tempo = pygame.time.Clock()  # Permanencia da janela

        self.movimento = [False, False]  # Força nao espelhar os controles
        self.caracter = {'jogador': load_image('jogador.png', (40,40))}
        self.jogador = FisicaDaEntidade(self, 'jogador', (300,300), (20,32))

    def executar(self):
        while True:
            self.tela.fill('slategrey')  # Preenche o fundo
            
            self.jogador.atualizar((self.movimento[1] - self.movimento[0], 0))
            self.jogador.renderizar(self.tela)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    raise SystemExit  # Em caso de erro retorna uma exceçao
                
                # Ao pressionar as setas do teclado
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.movimento[0] = True
                    if evento.key == pygame.K_RIGHT:
                        self.movimento[1] = True
                    if evento.key == pygame.K_UP:
                        self.jogador.velocidade[1] = -3
                
                # Ao parar de pressionar
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT:
                        self.movimento[0] = False
                    if evento.key == pygame.K_RIGHT:
                        self.movimento[1] = False


            pygame.display.flip()  # att a exibiçao na tela
            pygame.display.update()

            self.tempo.tick(60)  # taxa de de quadros: 60FPS

Jogo().executar()