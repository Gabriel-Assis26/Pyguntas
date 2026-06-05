import pygame
from src.funcoes import (
    buscar_perguntas,
)

def executar_jogo():
    pygame.init()
    
    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Pyguntas")
    tela.fill((0,0,0))
    clock = pygame.time.Clock()
    clock.tick(60)

    perguntas = buscar_perguntas()
    pAtual = 0
    rodando = True
    while rodando:
        fonte = pygame.font.SysFont("Arial", 24)
        texto = fonte.render(
            perguntas[pAtual]['question'],
            True,
            (255,255,255)
        )
        tela.blit(texto, (100,100))
        botao = pygame.Rect(100, 300, 300, 60)
        pygame.draw.rect(tela,(0,100,255),botao)
        texto = fonte.render(perguntas[pAtual]['correct_answer'], True, (255, 255, 255))
        texto_rect = texto.get_rect(center=botao.center)
        tela.blit(texto, texto_rect)
        for i,text in enumerate(perguntas[pAtual]['incorrect_answers']):
            botao = pygame.Rect(
                100,
                380 + i * 80,
                300,
                60
            )
            pygame.draw.rect(tela,(0,100,255),botao)
            texto = fonte.render(text, True, (255, 255, 255))
            texto_rect = texto.get_rect(center=botao.center)
            tela.blit(texto, texto_rect)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        pygame.display.flip()

    pygame.quit()