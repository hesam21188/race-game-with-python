# Amir Hesam Harati
import pygame
import os
pygame.init()
question = str(input("do you want to set display size [y/n] : "))
if question == "y": 
    display_width,display_height = int(input("display_width : ")),int(input("display_height : "))
elif question == "n":
    display_width,display_height = 1280,720
black,white,red = (0,0,0),(255,255,255),(250,0,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A Game From Hesam21188')
clock = pygame.time.Clock()
carimg = pygame.image.load('car.png')
x = (display_width * 0.45)
y = (display_height * 0.8)
def car(x,y):
    gameDisplay.blit(carimg,(x,y))
crashed = False
file_name = "game.log"
event = pygame.event
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        file = open(file_name,"a",)
        log_exist = True
        file.write(str(event))
    file.close()
    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)
