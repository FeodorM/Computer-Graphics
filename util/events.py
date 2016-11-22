import pygame


def is_quit_event(event):
    """True if "Esc" or "Close window" pressed"""
    return event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE


def is_zoom_in_event(event):
    """True if plus pressed or wheel rolled up"""
    return (event.type == pygame.KEYDOWN and event.key == pygame.K_KP_PLUS or
            event.type == pygame.MOUSEBUTTONDOWN and event.button == 4)


def is_zoom_out_event(event):
    """True if minus pressed or wheel rolled down"""
    return (event.type == pygame.KEYDOWN and event.key == pygame.K_KP_MINUS or
            event.type == pygame.MOUSEBUTTONDOWN and event.button == 5)
