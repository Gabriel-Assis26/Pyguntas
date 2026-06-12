import pygame
from deep_translator import GoogleTranslator
from src.funcoes import (
    buscar_perguntas,
    traduz,
    embaralha_respostas,
)
from src.telaJogo import (
    renderJogo
)
from src.telaMenu import (
    renderMenu
)

def executar_jogo():
    pygame.init()
    estado = 'menu'

    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Pyguntas")
    tela.fill((0,0,0))
    clock = pygame.time.Clock()

    questoes = buscar_perguntas()
    pAtual = 0
    rodando = True
    respostas = embaralha_respostas(questoes[pAtual])
    tradPergunta = traduz(questoes[pAtual]['question'])

    tempo_limite = 45
    inicio = pygame.time.get_ticks()

    while rodando:
        
        tela.fill((0,0,0))
        fonte = pygame.font.SysFont("Arial", 24)
        if estado == "menu":
            iniciar,config,rank=renderMenu(tela,fonte)
        elif estado == "jogo":
            botao_correta, botoes_erradas = renderJogo(
                tela,
                tempo_limite,
                questoes,
                fonte,
                tradPergunta,
                inicio,
                respostas
            )
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if estado == "menu":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if iniciar.collidepoint(pos):
                        estado = 'jogo'
            
            elif estado == "jogo":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if botao_correta.collidepoint(pos):
                        print("Acertou!")
                        if pAtual >= len(questoes)-1:
                            rodando = False
                            continue
                        pAtual += 1
                        respostas = embaralha_respostas(questoes[pAtual])
                    for i, botao_errado in enumerate(botoes_erradas):
                        if botao_errado.collidepoint(pos):
                            print("Errou!")
                    tradPergunta = traduz(questoes[pAtual]['question'])
                    inicio = pygame.time.get_ticks()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()