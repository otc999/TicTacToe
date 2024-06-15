import pygame
from pygame.locals import *


pygame.init()


#window resolution
screen_width=800  #must be EXACTLY 200 more than height
screen_height=600  #must divide by 3 and be at least 300


#window setup
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('TicTacToe')


#variables
line_width = 6
markers = []
clicked = False
pos = []
player=1
winner=0
game_over=False
tie=False
turns=0
run=True
sc_w=screen_width
sc_h=screen_height
sc_s=screen_height


#colors
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
bg = (255,255,240)
grid = (50,50,50)


#font
font=pygame.font.SysFont(None,40)


#rectangle for 'play again?' button
again_rect=Rect(sc_w-196,60,196,50)


#creating cells for 'X' and 'O'
for x in range(3):
    row=[0]*3
    markers.append(row)


#drawing grid function
def draw_grid():
    screen.fill(bg)
    for x in range(0,4):
        pygame.draw.line(screen, grid, (0, x*sc_h//3), (sc_w-200, x*sc_h//3), line_width)
        pygame.draw.line(screen, grid, (x*(sc_w-200)//3, 0), (x*(sc_w-200)//3, sc_h), line_width)


#drawing 'X' and 'O' function
def draw_markers():
    x_pos=0
    for x in markers:
        y_pos=0
        for y in x:
            if y==1:
                pygame.draw.line(screen,blue,(sc_s//3*x_pos+sc_s//20, sc_s//3*y_pos+sc_s//20),(sc_s//3*(x_pos+1)-sc_s//20,sc_s//3*(y_pos+1)-sc_s//20),line_width)
                pygame.draw.line(screen,blue,(sc_s//3*x_pos+sc_s//20, sc_s//3*(y_pos+1)-sc_s//20),(sc_s//3*(x_pos+1)-sc_s//20,sc_s//3*y_pos+sc_s//20),line_width)
            if y==-1:
                pygame.draw.circle(screen,red,(sc_s//3*(x_pos+1/2),sc_s//3*(y_pos+1/2)),sc_s//8,line_width)
            y_pos+=1
        x_pos+=1


#checking the game state function
def check_winner():
    global winner
    global game_over
    global tie
    y_pos=0


    for x in range(3):
        #check rows
        if sum(markers[x])==3:
            winner=1
            game_over=True
        if sum(markers[x])==-3:
            winner=2
            game_over=True

        #check columns
        if markers[0][x] + markers[1][x] + markers[2][x] == 3:
            winner=1
            game_over=True
        if markers[0][x] + markers[1][x] + markers[2][x] == -3:
            winner=2
            game_over=True

    #check diagonals
    if markers[0][0] + markers[1][1] + markers[2][2] == 3:
        winner=1
        game_over=True
    if markers[0][2] + markers[1][1] + markers[2][0] == 3:
        winner=1
        game_over=True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3:
        winner=2
        game_over=True
    if markers[0][2] + markers[1][1] + markers[2][0] == -3:
        winner=2
        game_over=True
    
    #check tie situation
    elif turns==9 and winner==0:
        tie=True
        game_over=True


#drawing results of the game function
def draw_winner(winner,tie):
    if tie==False:
        win_text= 'Player ' + str(winner) + ' wins!'
        win_img= font.render(win_text,True,blue)
        pygame.draw.rect(screen,green,(sc_w-196,0,196,50))
        screen.blit(win_img, (sc_w-196,12))
    elif tie==True:
        tie_text='Tie'
        tie_img=font.render(tie_text,True,blue)
        pygame.draw.rect(screen,green,(sc_w-196,0,196,50))
        screen.blit(tie_img, (sc_w-126,12))

    again_text='Play again?'
    again_img=font.render(again_text,True,blue)
    pygame.draw.rect(screen,green,again_rect)
    screen.blit(again_img,(sc_w-176,72))
 

#main loop
while run:
    
    draw_grid()
    draw_markers()

    #checking the events
    for event in pygame.event.get():
        

        #quitting game
        if event.type==pygame.QUIT:
            run=False

        
        #if game isn't over
        if game_over==False:


            #checking IF the mouse is clicked
            if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True


            #checking WHERE the mouse is clicked
            if event.type==pygame.MOUSEBUTTONUP and clicked==True:
                clicked=False
                pos=pygame.mouse.get_pos()
                cell_x=pos[0]//((sc_w-200)//3)
                cell_y=pos[1]//(sc_h//3)

                #filling the 'markers' array with player's value and checking game state afterwards
                if pos[0]<sc_w-200 and pos[1]<sc_h and markers[cell_x][cell_y]==0:
                        markers[cell_x][cell_y]=player
                        player*=-1
                        turns+=1
                        check_winner()


    #asking player to play again
    if game_over==True:
        draw_winner(winner,tie)

        #if so returning game state to beginning
        if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
            clicked=True
        if event.type==pygame.MOUSEBUTTONUP and clicked==True:
            clicked=False
            pos=pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers = []
                pos = []
                player=1
                winner=0
                game_over=False
                tie=False
                turns=0
                for x in range(3):
                    row=[0]*3
                    markers.append(row)


    pygame.display.update()

pygame.quit()
