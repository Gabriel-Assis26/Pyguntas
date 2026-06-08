import pygame
from deep_translator import GoogleTranslator
from src.funcoes import (
    buscar_perguntas,
    traduz,
    embaralha_respostas,
)

def executar_jogo():
    pygame.init()
    
    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Pyguntas")
    tela.fill((0,0,0))
    clock = pygame.time.Clock()

    questoes = buscar_perguntas()
    pAtual = 0
    rodando = True
    respostas = embaralha_respostas(questoes[pAtual])
    while rodando:
        tela.fill((0,0,0))
        fonte = pygame.font.SysFont("Arial", 24)
        tradPergunta = traduz(questoes[pAtual]['question'])
        texto = fonte.render(
            tradPergunta,
            True,
            (255,255,255)
        )
        tela.blit(texto, (100,100))
        botao_correta = 'pygame.Rect(100, 300, 300, 60)'
        botoes_erradas = []
        for i,resp in enumerate(respostas):
            botao = pygame.Rect(
                100,
                300 + i * 80,
                300,
                60
            )
            if resp[1] == 0:
                botao_correta = botao
                pygame.draw.rect(tela, (0, 100, 255), botao)
                texto = fonte.render(resp[0], True, (255, 255, 255))
                tela.blit(texto, texto.get_rect(center=botao.center))
            else:
                botoes_erradas.append(botao)
                pygame.draw.rect(tela,(0,100,255),botao)
                texto = fonte.render(resp[0], True, (255, 255, 255))
                texto_rect = texto.get_rect(center=botao.center)
                tela.blit(texto, texto.get_rect(center=botao.center))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if botao_correta.collidepoint(pos):
                    print("Acertou!")
                    pAtual += 1
                    respostas = embaralha_respostas(questoes[pAtual])
                for i, botao_errado in enumerate(botoes_erradas):
                    if botao_errado.collidepoint(pos):
                        print("Errou!")
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()