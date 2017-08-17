import pygame
from gpiozero import Button

pygame.init()

btn_drum = Button(2)
btn_splash = Button(3)
btn_cowbell = Button(4)
btn_cymbal = Button(5)

drum = pygame.mixer.Sound('samples/drum_tom_mid_hard.wav')
splash = pygame.mixer.Sound('samples/drum_splash_hard.wav')
cowbell = pygame.mixer.Sound('samples/drum_cowbell.wav')
cymbal = pygame.mixer.Sound('samples/drum_cymbal_closed.wav')
                          
btn_drum.when_pressed = drum.play
btn_splash.when_pressed = splash.play
btn_cowbell.when_pressed = cowbell.play
btn_cymbal.when_pressed = cymbal.play

