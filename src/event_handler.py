import pygame
import pygame.constants as key_constants


def get_events():
    event_dict = {}
    events = filter(lambda x: x.type == pygame.KEYDOWN or x.type == pygame.KEYUP, pygame.event.get())
    for event in events:
        event_dict[event.key] = event.type

    return event_dict
