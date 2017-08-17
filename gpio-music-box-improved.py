import pygame
from gpiozero import Button

pygame.init()



button_sound = {
    Button(2) : pygame.mixer.Sound('samples/drum_tom_mid_hard.wav'),
    Button(3) : pygame.mixer.Sound('samples/drum_splash_hard.wav'),
    Button(4) : pygame.mixer.Sound('samples/drum_cowbell.wav'),
    Button(5) : pygame.mixer.Sound('samples/drum_cymbal_closed.wav') 
    }



for button, sound in button_sound.items():
    button.when_pressed  = sound.play


    
    

