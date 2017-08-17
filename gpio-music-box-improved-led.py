import pygame
from gpiozero import Button, LEDBoard
from signal import pause

pygame.init()

button_1 = Button(2)
button_2 = Button(3)
button_3 = Button(4)
button_4 = Button(5)

led = LEDBoard(6,7,8,9)


drum = pygame.mixer.Sound('samples/drum_tom_mid_hard.wav')
splash = pygame.mixer.Sound('samples/drum_splash_hard.wav')
cowbell = pygame.mixer.Sound('samples/drum_cowbell.wav')
cymbal = pygame.mixer.Sound('samples/drum_cymbal_closed.wav')

def button_1_on() :
    drum.play()
    led.value = (1,0,0,0)
     
def button_2_on() :
     splash.play()
     led.value = (0,1,0,0)
     
def button_3_on() :
     cowbell.play()
     led.value = (0,0,1,0)
     
def button_4_on() :
     cymbal.play()
     led.value = (0,0,0,1)
     

while True:
    if button_1.is_pressed:
          button_1_on()
          
    if button_2.is_pressed:
      button_2_on() 
          
    if button_3.is_pressed:
      button_3_on()

    if button_4.is_pressed:
      button_4_on()
          
