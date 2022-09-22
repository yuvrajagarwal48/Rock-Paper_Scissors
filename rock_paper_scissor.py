import random
import pygame

options=["Rock","Paper",'Scissor']

rock=pygame.image.load("fist.png")
paper=pygame.image.load("palm.png")
scissors=pygame.image.load("scissors.png")

pygame.font.init()
f=pygame.font.Font('freesansbold.ttf',25)
over=pygame.font.Font('freesansbold.ttf',40)

def user_choose():
    choice=" "
    while True:
        choice=input("Rock Paper or Scissor:")
        if choice not in options:
            print("Choice not an option")
            continue
        else:
            break
    return choice

def computer_choose():
    choice=random.choice(options)
    return choice

def rules(user_choice,comp_choice):
    rule_win={
        "Rock":"Scissor",
        "Paper":"Rock",
        "Scissor":"Paper"
    }
    rule_lose={
        "Rock":"Paper",
        "Paper":"Scissor",
        "Scissor":"Rock"        
    }
    if rule_win[user_choice]==comp_choice:
        return "win"
    elif rule_lose[user_choice]==comp_choice:
        return "lose"
    else:
        return "draw"
    
# user=user_choose()
# computer=computer_choose()
# print(f"You chose {user}")
# print(f"Computer chose {computer}")
# result=rules(user,computer)
# if result=="win":
#     print("You Win!")
# elif result=="lose":
#     print("You Lose")
# else:
#     print("Draw")
    

def draw(screen):    
    screen.blit(rock,(64,200))
    screen.blit(paper,(192,200))
    screen.blit(scissors,(320,200))
    pygame.display.update()
    
def read_choice():
    x,y=pygame.mouse.get_pos()
    choice=" "
    if x-64<64 and x+64>128:
        choice="Rock"
    elif x-64<192 and x+64>256:
        choice="Paper"
    elif x-64<320 and x+64>384:
        choice="Scissor"
    return choice


screen=pygame.display.set_mode((448,400))
icon=pygame.image.load("rock-paper-scissors.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Rock Paper Scissors")
running=True
draw(screen)
while running:
    try:
        #draw(screen)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                user=read_choice()
                computer=computer_choose()
                screen.blit(screen,(0,0))
                pygame.display.update()   
                pygame.time.delay(500)
                comp_text=f.render("Computer",True,(255,255,255))
                screen.blit(comp_text,(100,200))
                if computer=="Rock":
                    screen.blit(rock,(150,250))
                elif computer=="Paper":
                    screen.blit(paper,(150,250))
                elif computer=="Scissor":
                    screen.blit(scissors,(150,250))
                
                user_text=f.render("Player",True,(255,255,255))
                screen.blit(user_text,(250,200))
                if user=="Rock":
                    screen.blit(rock,(250,250))
                elif user=="Paper":
                    screen.blit(paper,(250,250))
                elif user=="Scissor":
                    screen.blit(scissors,(250,250))
                        
                pygame.display.update()   
                #print(f"You chose {user}")
                #print(f"Computer chose {computer}")
                result=rules(user,computer)
                if result=="win":
                    #print("You Win!")
                    win_text=over.render("You Win!!!",True,(255,255,255))
                    screen.blit(win_text,(130,100))
                    
                    
                elif result=="lose":
                    print("You Lose")
                    lose_text=over.render("You Lose!!!",True,(255,255,255))
                    screen.blit(lose_text,(130,100))
                    
                else:
                    #print("Draw")
                    draw_text=over.render("Draw",True,(255,255,255))
                    screen.blit(draw_text,(170,100))
                pygame.display.update()
    except:
        running=False
                    
                        
                    
        
            

