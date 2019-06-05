import pygame
import time
import random

pygame.init()

#Color    Red    Green    Blue
Black  =  (0,      0,      0)
White  =  (255,   255,     255)
Red    =  (255,    0,      0)
Yellow =  (255,   255,     0)
Green  =  (0,     255,     0)
Blue   =  (0,      0,     255)

screen_size = width, height = 700, 500
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 25)
bigfont = pygame.font.Font(None, 72)
onewins = pygame.image.load("1wins.png").convert()
twowins = pygame.image.load("2wins.png").convert()
begin = pygame.image.load("begin.png").convert()
cpuwins = pygame.image.load("cpuwins.png").convert()
cpudiff = pygame.image.load("cpudif.png").convert()
Clock = pygame.time.Clock()

class RedBlock:
    """Red Block"""
    def __init__(self, x, y):
        self.lives=3
        self.width=25
        self.height=100
        self.color=Red
        self.x=x
        self.y=y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        

class YellowBlock:
    """Yellow Block"""
    def __init__(self, x, y):
        self.lives=2
        self.width=25
        self.height=100
        self.color=Yellow
        self.x=x
        self.y=y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class GreenBlock:
    """Green Block"""
    def __init__(self, x ,y):
        self.lives=1
        self.width=25
        self.height=100
        self.color=Green
        self.x=x
        self.y=y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


def main():
    player1 = 0
    player2 = 0
    myrun = True
    while myrun:
        winner = run(player1, player2)
        if winner:
            player2 += 1
            if player2 < 5:
                pausescreen2(player1, player2)
        if not winner:
            player1 +=1
            if player2 < 5: 
                pausescreen1(player1, player2)
        if player1 == 5:
            endscreen()
        if player2 == 5:
            endscreen2()

def run(player1, player2):
    Block1 = RandomBlock(305,0)
    Block2 = RandomBlock(330,0)
    Block3 = RandomBlock(355,0)
    Block4 = RandomBlock(305,100)
    Block5 = RandomBlock(330,100)
    Block6 = RandomBlock(355,100)
    Block7 = RandomBlock(280,0)
    Block8 = RandomBlock(380,0)
    Block9 = RandomBlock(280,100)
    Block10 = RandomBlock(380,100)
    Block11 = RandomBlock(280, 200)
    Block12 = RandomBlock(305,200)
    Block13 = RandomBlock(330,200)
    Block14 = RandomBlock(355,200)
    Block15 = RandomBlock(380,200)
    Block16 = RandomBlock(280, 300)
    Block17 = RandomBlock(305,300)
    Block18 = RandomBlock(330,300)
    Block19 = RandomBlock(355,300)
    Block20 = RandomBlock(380,300)
    Block21 = RandomBlock(280, 400)
    Block22 = RandomBlock(305,400)
    Block23 = RandomBlock(330,400)
    Block24 = RandomBlock(355,400)
    Block25 = RandomBlock(380,400)
    LeftPaddle = pygame.Rect(0, height//2, 10, 100)
    RightPaddle = pygame.Rect(width-10, height//2, 10, 100)
    BallRect1 = pygame.Rect(100,200,15,15)
    BallRect2 = pygame.Rect(600,200,15,15)
    LPSpeed = [0,0]
    RPSpeed = [0,0]
    BSpeed1 = [5,3]
    BSpeed2 = [-5,3]
    BallSpeed = 5
    speed = 10
    running = True
    BlockList = [Block1, Block2, Block3, Block4, Block5, Block6, Block7, Block8, Block9, Block10, Block11, Block12, Block13, Block14, Block15, Block16, Block17, Block18, Block19, Block20, Block21, Block22, Block23, Block24, Block25]

    while running:
                #Controls Paddels
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    LPSpeed[1] = -speed
                if event.key == pygame.K_s:
                    LPSpeed[1] = speed
                if event.key == pygame.K_UP:
                    RPSpeed[1] = -speed
                if event.key == pygame.K_DOWN:
                    RPSpeed[1] = speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    LPSpeed[1] = 0
                if event.key == pygame.K_s:
                    LPSpeed[1] = 0
                if event.key == pygame.K_UP:
                    RPSpeed[1] = 0
                if event.key == pygame.K_DOWN:
                    RPSpeed[1] = 0
                    
          #Paddals can't go through edge
                    
        if LeftPaddle.top <= 0:
            LeftPaddle.x = 0
            LeftPaddle.y = 0
        if LeftPaddle.bottom >= height:
            LeftPaddle.x = 0
            LeftPaddle.y = 400
        if RightPaddle.top <= 0:
            RightPaddle.x = 690
            RightPaddle.y = 0
        if RightPaddle.bottom >= height:
            RightPaddle.x = 690
            RightPaddle.y = 400
            
            #Prints everything on screen
            
        LeftPaddle=LeftPaddle.move(LPSpeed)
        RightPaddle=RightPaddle.move(RPSpeed)
        BallRect1=BallRect1.move(BSpeed1)
        BallRect2=BallRect2.move(BSpeed2)
        screen.fill(Black)
        drawblocks(BlockList)
        pygame.draw.rect(screen, White, LeftPaddle)
        pygame.draw.rect(screen, White, RightPaddle)
        pygame.draw.rect(screen, White, BallRect1)
        pygame.draw.rect(screen, White, BallRect2)
        Score(player1, player2)
        RectCollide(BlockList, BallRect1, BSpeed1)
        RectCollide(BlockList, BallRect2, BSpeed2)
        
            #Checks if ball collides with paddle
        
        if BallRect1.colliderect(LeftPaddle):
            if LPSpeed[1] > 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed1[0]
                
        if BallRect1.colliderect(RightPaddle):
            if RPSpeed[1] > 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed1[0]
                
        if BallRect2.colliderect(LeftPaddle):
            if LPSpeed[1] > 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed2[0]
                
        if BallRect2.colliderect(RightPaddle):
            if RPSpeed[1] > 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = -BallSpeed
            else:
                BSpeed2[0] = -BSpeed2[0]

            #Checks if ball hits top or bottom of screen

        if BallRect1.top < 0 or BallRect1.bottom > height:
            BSpeed1[1] = -BSpeed1[1]
        if BallRect2.top < 0 or BallRect2.bottom > height:
            BSpeed2[1] = -BSpeed2[1]

                  #Checks if someone scored
            
        if BallRect1.left < 0 or BallRect2.left < 0:
            running = False
            return True
        if BallRect1.right > width or BallRect2.right > width:
            running = False
            return False

            #Display Flip

        Clock.tick(65)
        pygame.display.flip()


def main2():
    CPU = 0
    player2 = 0
    myrun = True
    while myrun:
        winner = run2(CPU, player2)
        if winner:
            player2 += 1
            if player2 < 5:
                pausescreen2_2(CPU, player2)
        if not winner:
            CPU +=1
            if player2 < 5: 
                pausescreen1_2(CPU, player2)
        if CPU == 5:
            endscreen_2()
        if player2 == 5:
            endscreen2_2()

            
def run2(CPU, player2):
    Block1 = RandomBlock(305,0)
    Block2 = RandomBlock(330,0)
    Block3 = RandomBlock(355,0)
    Block4 = RandomBlock(305,100)
    Block5 = RandomBlock(330,100)
    Block6 = RandomBlock(355,100)
    Block7 = RandomBlock(280,0)
    Block8 = RandomBlock(380,0)
    Block9 = RandomBlock(280,100)
    Block10 = RandomBlock(380,100)
    Block11 = RandomBlock(280, 200)
    Block12 = RandomBlock(305,200)
    Block13 = RandomBlock(330,200)
    Block14 = RandomBlock(355,200)
    Block15 = RandomBlock(380,200)
    Block16 = RandomBlock(280, 300)
    Block17 = RandomBlock(305,300)
    Block18 = RandomBlock(330,300)
    Block19 = RandomBlock(355,300)
    Block20 = RandomBlock(380,300)
    Block21 = RandomBlock(280, 400)
    Block22 = RandomBlock(305,400)
    Block23 = RandomBlock(330,400)
    Block24 = RandomBlock(355,400)
    Block25 = RandomBlock(380,400)
    LeftPaddle = pygame.Rect(0, height//2, 10, 100)
    RightPaddle = pygame.Rect(width-10, height//2, 10, 100)
    BallRect1 = pygame.Rect(100,200,15,15)
    BallRect2 = pygame.Rect(600,200,15,15)
#    BallPosition = [0,200]
    LPSpeed = [0,0]
    RPSpeed = [0,0]
    BSpeed1 = [5,3]
    BSpeed2 = [-5,3]
    BallSpeed = 5
    speed = 10
    running = True
    BlockList = [Block1, Block2, Block3, Block4, Block5, Block6, Block7, Block8, Block9, Block10, Block11, Block12, Block13, Block14, Block15, Block16, Block17, Block18, Block19, Block20, Block21, Block22, Block23, Block24, Block25]

    while running:
                #Controls Paddels
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    RPSpeed[1] = -speed
                if event.key == pygame.K_DOWN:
                    RPSpeed[1] = speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    RPSpeed[1] = 0
                if event.key == pygame.K_DOWN:
                    RPSpeed[1] = 0
            if True:
                LeftPaddle.y = BallRect1.y
                LPSpeed[1] = BSpeed1[1]
#                if BSpeed1[1] > 0:
#                    LPSpeed[1] = BSpeed2[1] + 2
#                if BSpeed1[1] < 0:
#                    LPSpeed[1] = BSpeed2[1] - 2
#                LPSpeed[1] = BallPosition[1]
#
#        if BSpeed1[1] < 0:
#            BallPosition[1] -= 3
#        if BSpeed1[1] > 0:
#            BallPosition[1] += 3
        
                    
          #Paddals can't go through edge
                    
        if LeftPaddle.top <= 0:
            LeftPaddle.x = 0
            LeftPaddle.y = 0
        if LeftPaddle.bottom >= height:
            LeftPaddle.x = 0
            LeftPaddle.y = 400
        if RightPaddle.top <= 0:
            RightPaddle.x = 690
            RightPaddle.y = 0
        if RightPaddle.bottom >= height:
            RightPaddle.x = 690
            RightPaddle.y = 400
            
            #Prints everything on screen
            
        LeftPaddle=LeftPaddle.move(LPSpeed)
        RightPaddle=RightPaddle.move(RPSpeed)
        BallRect1=BallRect1.move(BSpeed1)
        BallRect2=BallRect2.move(BSpeed2)
        screen.fill(Black)
        drawblocks(BlockList)
        pygame.draw.rect(screen, White, LeftPaddle)
        pygame.draw.rect(screen, White, RightPaddle)
        pygame.draw.rect(screen, White, BallRect1)
        pygame.draw.rect(screen, White, BallRect2)
        Score_2(CPU, player2)
        RectCollide(BlockList, BallRect1, BSpeed1)
        RectCollide(BlockList, BallRect2, BSpeed2)
        
            #Checks if ball collides with paddle
        
        if BallRect1.colliderect(LeftPaddle):
            if LPSpeed[1] > 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed1[0]
                
        if BallRect1.colliderect(RightPaddle):
            if RPSpeed[1] > 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed1[0]
                
        if BallRect2.colliderect(LeftPaddle):
            if LPSpeed[1] > 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed2[0]
                
        if BallRect2.colliderect(RightPaddle):
            if RPSpeed[1] > 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = -BallSpeed
            else:
                BSpeed2[0] = -BSpeed2[0]

            #Checks if ball hits top or bottom of screen

        if BallRect1.top < 0 or BallRect1.bottom > height:
            BSpeed1[1] = -BSpeed1[1]
        if BallRect2.top < 0 or BallRect2.bottom > height:
            BSpeed2[1] = -BSpeed2[1]

                  #Checks if someone scored
            
        if BallRect1.left < 0 or BallRect2.left < 0:
            running = False
            return True
        if BallRect1.right > width or BallRect2.right > width:
            running = False
            return False

            #Display Flip

        Clock.tick(65)
        pygame.display.flip()


def pausescreen1_2(CPU, player2):
    text1 = bigfont.render("CPU Wins The Round", True, White)
    text2 = bigfont.render(str(CPU) + "  -  " + str(player2), True, White)
    text3 = font.render("Press Enter To Continue", True, White)
    screen.fill(Black)
    screen.blit(text1, [100, 80])
    screen.blit(text2, [277, 250])
    screen.blit(text3, [181, 390])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = False

def pausescreen2_2(CPU, player2):
    text1 = bigfont.render("Player 2 Wins The Round", True, White)
    text2 = bigfont.render(str(CPU) + "  -  " + str(player2), True, White)
    text3 = font.render("Press Enter To Continue", True, White)
    screen.fill(Black)
    screen.blit(text1, [45, 80])
    screen.blit(text2, [277, 250])
    screen.blit(text3, [181, 390])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = False     

def endscreen_2():
    screen.blit(cpuwins, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main2()
                if event.key == pygame.K_m:
                    BeginScreen()

def endscreen2_2():
    screen.blit(twowins, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main2()
                if event.key == pygame.K_m:
                    BeginScreen()

    

def Score_2(player1, player2):
    text1 = font.render("CPU   :   " +str(player1), True, White)
    text2 = font.render("Player 2   :   " +str(player2), True, White)
    screen.blit(text1, [50,0])
    screen.blit(text2, [465,0])


def main3():
    CPU = 0
    player2 = 0
    myrun = True
    while myrun:
        winner = run3(CPU, player2)
        if winner:
            player2 += 1
            if player2 < 5:
                pausescreen2_3(CPU, player2)
        if not winner:
            CPU +=1
            if player2 < 5: 
                pausescreen1_3(CPU, player2)
        if CPU == 5:
            endscreen_3()
        if player2 == 5:
            endscreen2_3()

            
def run3(CPU, player2):
    Block1 = RandomBlock(305,0)
    Block2 = RandomBlock(330,0)
    Block3 = RandomBlock(355,0)
    Block4 = RandomBlock(305,100)
    Block5 = RandomBlock(330,100)
    Block6 = RandomBlock(355,100)
    Block7 = RandomBlock(280,0)
    Block8 = RandomBlock(380,0)
    Block9 = RandomBlock(280,100)
    Block10 = RandomBlock(380,100)
    Block11 = RandomBlock(280, 200)
    Block12 = RandomBlock(305,200)
    Block13 = RandomBlock(330,200)
    Block14 = RandomBlock(355,200)
    Block15 = RandomBlock(380,200)
    Block16 = RandomBlock(280, 300)
    Block17 = RandomBlock(305,300)
    Block18 = RandomBlock(330,300)
    Block19 = RandomBlock(355,300)
    Block20 = RandomBlock(380,300)
    Block21 = RandomBlock(280, 400)
    Block22 = RandomBlock(305,400)
    Block23 = RandomBlock(330,400)
    Block24 = RandomBlock(355,400)
    Block25 = RandomBlock(380,400)
    LeftPaddle = pygame.Rect(0, height//2, 10, 100)
    RightPaddle = pygame.Rect(width-10, height//2, 10, 100)
    BallRect1 = pygame.Rect(100,200,15,15)
    BallRect2 = pygame.Rect(600,200,15,15)
#    BallPosition = [0,200]
    LPSpeed = [0,0]
    RPSpeed = [0,0]
    BSpeed1 = [5,3]
    BSpeed2 = [-5,3]
    BallSpeed = 5
    speed = 10
    running = True
    BlockList = [Block1, Block2, Block3, Block4, Block5, Block6, Block7, Block8, Block9, Block10, Block11, Block12, Block13, Block14, Block15, Block16, Block17, Block18, Block19, Block20, Block21, Block22, Block23, Block24, Block25]

    while running:
                #Controls Paddels
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    RPSpeed[1] = -speed
                if event.key == pygame.K_DOWN:
                    RPSpeed[1] = speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    RPSpeed[1] = 0
                if event.key == pygame.K_DOWN:
                    RPSpeed[1] = 0

            if True:
                if BallRect1[0] - LeftPaddle[0] < BallRect2[0] - LeftPaddle[0]:
                    LeftPaddle.y = BallRect1.y
                    LPSpeed[1] = BSpeed1[1]
                else:
                    LeftPaddle.y = BallRect2.y
                    LPSpeed[1] = BSpeed2[1]        
                    
          #Paddals can't go through edge
                    
        if LeftPaddle.top <= 0:
            LeftPaddle.x = 0
            LeftPaddle.y = 0
        if LeftPaddle.bottom >= height:
            LeftPaddle.x = 0
            LeftPaddle.y = 400
        if RightPaddle.top <= 0:
            RightPaddle.x = 690
            RightPaddle.y = 0
        if RightPaddle.bottom >= height:
            RightPaddle.x = 690
            RightPaddle.y = 400
            
            #Prints everything on screen
            
        LeftPaddle=LeftPaddle.move(LPSpeed)
        RightPaddle=RightPaddle.move(RPSpeed)
        BallRect1=BallRect1.move(BSpeed1)
        BallRect2=BallRect2.move(BSpeed2)
        screen.fill(Black)
        drawblocks(BlockList)
        pygame.draw.rect(screen, White, LeftPaddle)
        pygame.draw.rect(screen, White, RightPaddle)
        pygame.draw.rect(screen, White, BallRect1)
        pygame.draw.rect(screen, White, BallRect2)
        Score_2(CPU, player2)
        RectCollide(BlockList, BallRect1, BSpeed1)
        RectCollide(BlockList, BallRect2, BSpeed2)
        
            #Checks if ball collides with paddle
        
        if BallRect1.colliderect(LeftPaddle):
            if LPSpeed[1] > 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed1[0]
                
        if BallRect1.colliderect(RightPaddle):
            if RPSpeed[1] > 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed1[0] = -BSpeed1[0]
                BSpeed1[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed1[0]
                
        if BallRect2.colliderect(LeftPaddle):
            if LPSpeed[1] > 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = -BallSpeed
            else:
                BSpeed1[0] = -BSpeed2[0]
                
        if BallRect2.colliderect(RightPaddle):
            if RPSpeed[1] > 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = BallSpeed
            elif LPSpeed[1] < 0:
                BSpeed2[0] = -BSpeed2[0]
                BSpeed2[1] = -BallSpeed
            else:
                BSpeed2[0] = -BSpeed2[0]

            #Checks if ball hits top or bottom of screen

        if BallRect1.top < 0 or BallRect1.bottom > height:
            BSpeed1[1] = -BSpeed1[1]
        if BallRect2.top < 0 or BallRect2.bottom > height:
            BSpeed2[1] = -BSpeed2[1]

                  #Checks if someone scored
            
        if BallRect1.left < 0 or BallRect2.left < 0:
            running = False
            return True
        if BallRect1.right > width or BallRect2.right > width:
            running = False
            return False

            #Display Flip

        Clock.tick(65)
        pygame.display.flip()


def pausescreen1_3(player1, player2):
    text1 = bigfont.render("Player 1 Wins The Round", True, White)
    text2 = bigfont.render(str(player1) + "  -  " + str(player2), True, White)
    text3 = font.render("Press Enter To Continue", True, White)
    screen.fill(Black)
    screen.blit(text1, [45, 80])
    screen.blit(text2, [277, 250])
    screen.blit(text3, [181, 390])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = False

def pausescreen2_3(player1, player2):
    text1 = bigfont.render("Player 2 Wins The Round", True, White)
    text2 = bigfont.render(str(player1) + "  -  " + str(player2), True, White)
    text3 = font.render("Press Enter To Continue", True, White)
    screen.fill(Black)
    screen.blit(text1, [45, 80])
    screen.blit(text2, [277, 250])
    screen.blit(text3, [181, 390])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = False
        

def endscreen_3():
    screen.blit(onewins, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main3()
                if event.key == pygame.K_m:
                    BeginScreen()

def endscreen2_3():
    screen.blit(twowins, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main3()
                if event.key == pygame.K_m:
                    BeginScreen()

            
def rules():
    rule1 = bigfont.render("Rules", True, White)
    rule2 = font2.render("This game is a combination of Breakout and Pong", True, White)
    rule3 = font2.render("Player 1 will use the arrow keys, and Player two will use W and S", True, White)
    rule4 = font2.render("Red blocks have 3 lives, Yellow blocks have 2 lives, and Green blocks will have 1", True, White)
    rule5 = font2.render("You have to try to break through the blocks and hit the other players side to win", True, White)
    rule6 = font2.render("Press B to go to the Main Menu", True, White)
    rule7 = font2.render("Press 1 to play a 1 player game against the CPU", True, White)
    rule8 = font2.render("Press 2 to play a 2 player game against your friend", True, White)
    screen.fill(Black)
    screen.blit(rule1, [275, 20])
    screen.blit(rule2, [10, 150])
    screen.blit(rule3, [10, 200])
    screen.blit(rule4, [10, 250])
    screen.blit(rule5, [10, 300])
    screen.blit(rule6, [10, 350])
    screen.blit(rule7, [10, 400])
    screen.blit(rule8, [10, 450])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    BeginScreen()
                    done = False
                if event.key == pygame.K_1:
                    cpudif()
                    done = False
                if event.key == pygame.K_2:
                    main()
                    done = False

def cpudif():
    screen.blit(cpudiff, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygmae.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    main2()
                    done = False
                if event.key == pygame.K_h:
                    main3()
                    done = False


def pausescreen1(player1, player2):
    text1 = bigfont.render("Player 1 Wins The Round", True, White)
    text2 = bigfont.render(str(player1) + "  -  " + str(player2), True, White)
    text3 = font.render("Press Enter To Continue", True, White)
    screen.fill(Black)
    screen.blit(text1, [45, 80])
    screen.blit(text2, [277, 250])
    screen.blit(text3, [181, 390])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = False

def pausescreen2(player1, player2):
    text1 = bigfont.render("Player 2 Wins The Round", True, White)
    text2 = bigfont.render(str(player1) + "  -  " + str(player2), True, White)
    text3 = font.render("Press Enter To Continue", True, White)
    screen.fill(Black)
    screen.blit(text1, [45, 80])
    screen.blit(text2, [277, 250])
    screen.blit(text3, [181, 390])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = False
        

def endscreen():
    screen.blit(onewins, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                if event.key == pygame.K_m:
                    BeginScreen()

def endscreen2():
    screen.blit(twowins, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                if event.key == pygame.K_m:
                    BeginScreen()
    

def Score(player1, player2):
    text1 = font.render("Player 1   :   " +str(player1), True, White)
    text2 = font.render("Player 2   :   " +str(player2), True, White)
    screen.blit(text1, [50,0])
    screen.blit(text2, [465,0])

def RectCollide(BlockList, BallRect, BSpeed):
    a=0
    while a < len(BlockList):
        if BallRect.colliderect(BlockList[a]):
            BSpeed[0] = -BSpeed[0]
            BlockList[a].lives -= 1
            if BlockList[a].lives == 1:
                BlockList[a].color = Green
            if BlockList[a].lives == 2:
                BlockList[a].color = Yellow
            if BlockList[a].lives == 0:
                del BlockList[a]
            break
        else:
            a += 1

def drawblocks(BlockList):
    a=0
    while a < len(BlockList):
        BlockList[a].draw()
        a+=1

def RandomBlock(x,y):
    ColorList = [GreenBlock(x,y), YellowBlock(x,y), RedBlock(x,y), GreenBlock(x,y), YellowBlock(x,y), GreenBlock(x,y)]
    a = random.randint(0, len(ColorList)-1)
    return ColorList[a]

def BeginScreen():
    screen.blit(begin, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    done = False
                    main()
                if event.key == pygame.K_1:
                    done = False
                    cpudif()
                if event.key == pygame.K_r:
                    rules()
                    done = False
    
    
if __name__ == "__main__":
    if BeginScreen():
        main()
