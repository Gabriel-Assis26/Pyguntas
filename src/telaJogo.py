import pygame
from src.funcoes import (
    buscar_perguntas,
    traduz,
    embaralha_respostas,
)

def renderJogo(tela,tempo_limite,questoes,fonte,tradPergunta,inicio,respostas):
    tempo_passado = (pygame.time.get_ticks() - inicio) // 1000
    tempo_restante = tempo_limite - tempo_passado
    if tempo_restante <= 0:
        print("Tempo esgotado!")
        inicio = pygame.time.get_ticks()
        pAtual += 1
        respostas = embaralha_respostas(questoes[pAtual])
    timer = fonte.render(
        f"Tempo: {tempo_restante}",
        True,
        (255, 255, 255)
    )
    tela.blit(timer, (50, 50))

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
    return botao_correta, botoes_erradas