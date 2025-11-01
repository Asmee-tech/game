import pygame
pygame.init()
width=600
height=600
screen=pygame.display.set_mode((width,height))
screen.fill("black")
img1=pygame.image.load("amongus.png")
img2=pygame.image.load("clash.jpeg")
img3=pygame.image.load("mario.png")
img4=pygame.image.load("minecraft.png")

img1=pygame.transform.scale(img1,(120,110))
img2=pygame.transform.scale(img2,(120,120))
img3=pygame.transform.scale(img3,(120,120))
img4=pygame.transform.scale(img4,(120,120))
#Font and text
fon=pygame.font.SysFont("arial",80)
text1=fon.render("Mario",True,"white")
screen.blit(text1,(280,20))
text2=fon.render("Minecraft",True,"white")
screen.blit(text2,(220,180))
text3=fon.render("Among Us",True,"white")
screen.blit(text3,(200,330))
text4=fon.render("Clash",True,"white")
screen.blit(text4,(300,470))
screen.blit(img1,(20,10))
screen.blit(img2,(20,150))
screen.blit(img3,(20,290))
screen.blit(img4,(20,460))



run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    #event trigger
    event=pygame.event.poll()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,(100,200,155),(pos),25,25)
        pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
        pos2=pygame.mouse.get_pos()
        pygame.draw.line(screen,(100,200,155),(pos),(pos2),5)
        pygame.draw.circle(screen,(100,200,155),(pos2),25,25)
        pygame.display.update()
        
        
    
            

            
    pygame.display.update()
pygame.quit()
