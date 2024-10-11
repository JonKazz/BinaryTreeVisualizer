 pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT-h), NODE_SIZE, NODE_WIDTH)
    text_surface = font.render('1', True, (0,0,0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT-h))
    screen.blit(text_surface, text_rect)