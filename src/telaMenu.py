import pygame

def renderMenu(tela,fonte):
    texto = fonte.render(
        'Menu',
        True,
        (255,255,255)
    )
    tela.blit(texto, (100,100))

    iniciar = pygame.Rect(100,300,300,60)
    pygame.draw.rect(tela, (0, 100, 255), iniciar)
    texto = fonte.render('Iniciar', True, (255, 255, 255))
    tela.blit(texto, texto.get_rect(center=iniciar.center))

    config = pygame.Rect(100,380,300,60)
    pygame.draw.rect(tela, (0, 100, 255), config)
    texto = fonte.render('Configuração', True, (255, 255, 255))
    tela.blit(texto, texto.get_rect(center=config.center))

    rank = pygame.Rect(100,460,300,60)
    pygame.draw.rect(tela, (0, 100, 255), rank)
    texto = fonte.render('Rank', True, (255, 255, 255))
    tela.blit(texto, texto.get_rect(center=rank.center))

    return iniciar,config,rank
        