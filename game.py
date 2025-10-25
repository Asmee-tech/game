import pygame
pygame.init()
width=600
height=600
screen=pygame.display.set_mode((width,height))
img1=pygame.image.load("amongus.png")
img2=pygame.image.load("clash.jpeg")
img3=pygame.image.load("mario.png")
img4=pygame.image.load("minecraft.png")

img1=pygame.transform.scale(img1,(120,120))
img2=pygame.transform.scale(img2,(120,120))
img3=pygame.transform.scale(img3,(120,120))
img4=pygame.transform.scale(img4,(120,120))






run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.blit(img1,(20,10))
    screen.blit(img2,(20,150))
    screen.blit(img3,(20,290))
    screen.blit(img4,(20,460))

    #text1=font.render("Trust me, I’m not the Impostor.",True,"white")
    #screen.blit(text1,(30,100))
            

            
    pygame.display.update()
pygame.quit()