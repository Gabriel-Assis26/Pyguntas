import pygame
from deep_translator import GoogleTranslator
from src.funcoes import (
    buscar_perguntas,
)

def executar_jogo():
    pygame.init()
    
    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Pyguntas")
    tela.fill((0,0,0))
    clock = pygame.time.Clock()

    perguntas = buscar_perguntas()
    pAtual = 0
    rodando = True
    while rodando:
        tela.fill((0,0,0))
        fonte = pygame.font.SysFont("Arial", 24)
        tradPergunta = GoogleTranslator(
            source='en',
            target='pt'
        ).translate(perguntas[pAtual]['question'])
        texto = fonte.render(
            tradPergunta,
            True,
            (255,255,255)
        )
        tela.blit(texto, (100,100))
        botao_correta = pygame.Rect(100, 300, 300, 60)
        pygame.draw.rect(tela, (0, 100, 255), botao_correta)
        tradCerta = GoogleTranslator(
            source='en',
            target='pt'
        ).translate(perguntas[pAtual]['correct_answer'])
        texto = fonte.render(tradCerta, True, (255, 255, 255))
        tela.blit(texto, texto.get_rect(center=botao_correta.center))
        
        botoes_erradas = []
        for i,text in enumerate(perguntas[pAtual]['incorrect_answers']):
            botao = pygame.Rect(
                100,
                380 + i * 80,
                300,
                60
            )
            tradErrada = GoogleTranslator(
                source='en',
                target='pt'
            ).translate(text)
            botoes_erradas.append(botao)
            pygame.draw.rect(tela,(0,100,255),botao)
            texto = fonte.render(tradErrada, True, (255, 255, 255))
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
                for i, botao_errado in enumerate(botoes_erradas):
                    if botao_errado.collidepoint(pos):
                        print("Errou!")
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()