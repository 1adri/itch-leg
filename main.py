 # Import Modules for the Game
import pygame
import asyncio

'''
        # Changes what the score says depending on the player(if alive then shows score, if got eaten then says final score)
        if player_alive:
            score_text = score_font.render("Score: " + str(score), 1, (0, 0, 0))

        else:
            score_text = score_font.render("Final Score: " + str(score), 1, (0, 0, 0))

'''


# Start the game
pygame.init()
game_width = 960
game_height = 540
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
color = (255,255,255)
  
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)
  
# stores the width of the
# screen into a variable
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
  
# rendering a text written in
# this font
text = smallfont.render('PLAY' , True , color)

class Basketball:
    def __init__(self, screen, running, basketball, player_x, player_y, player_facing_left):
        self.screen = screen
        self.running = running
        self.basketball = basketball
        self.player_x = player_x
        self.player_y = player_y
        self.player_facing_left = player_facing_left
    def main(self):

        if self.player_facing_left:
            self.screen.blit(self.basketball, (self.player_x-7, self.player_y+75))

        else:
            self.screen.blit(self.basketball, (self.player_x+80, self.player_y+75))

class Player:
    def __init__(self, screen, running, background, player, player_x, player_y, player_speed, player_size, player_facing_left, player_hitbox, player_alive, isjump, jumping,  Y_GRAVITY, JUMP_HEIGHT, Y_VELOCITY):
        self.screen = screen
        self.running = running
        self.background = background
        self.player = player
        self.player_x = player_x
        self.player_y = player_y
        self.player_speed = player_speed
        self.player_size = player_size
        self.player_facing_left = player_facing_left
        self.player_hitbox = player_hitbox
        self.player_alive = player_alive
        self.isjump = isjump
        self.jumping = jumping
        self.Y_GRAVITY = Y_GRAVITY
        self.JUMP_HEIGHT = JUMP_HEIGHT
        self.Y_VELOCITY = Y_VELOCITY

    def main(self):
    # Everything under 'while running' will be repeated over and over again
        while self.running:
            keys = pygame.key.get_pressed()

            # Makes the game stop if the player clicks the X or presses esc
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        self.jumping = True
                
            if keys[pygame.K_a]:
                self.player_x -= self.player_speed
                self.player_facing_left = True

                #player_y += player_speed
            if keys[pygame.K_LSHIFT]:
                if keys[pygame.K_d]:
                    self.player_x += 3.5
                    #player_facing_left = False
                if keys[pygame.K_a]:
                    self.player_x -= 3.5
                    #player_facing_left = True
            if keys[pygame.K_d]:
                self.player_x += self.player_speed
                self.player_facing_left = False

            self.screen.blit(self.background, (0, 0))

            if self.jumping:
                self.player_y -= self.Y_VELOCITY
                self.Y_VELOCITY -= self.Y_GRAVITY
                if self.Y_VELOCITY < -self.JUMP_HEIGHT:
                    self.jumping = False
                    self.Y_VELOCITY = self.JUMP_HEIGHT

                
            # Spawn a new Enemy whenever enemy_timer hits 0


            # Draw Player
            player_small = pygame.transform.scale(self.player, (int(self.player_size*.7), int(self.player_size*.7)))
            if self.player_facing_left:
                player_small = pygame.transform.flip(player_small, True, False)
            screen.blit(player_small, (self.player_x, self.player_y))

            basketball = Basketball(self.screen, self.running, pygame.image.load('basketball.png').convert_alpha(), self.player_x, self.player_y, self.player_facing_left)
            basketball.main()


            #merged = self.player.copy()

            #screen.blit(score_text, (1600, 30))

            # Update Screen
            pygame.display.update()
            clock.tick(50)
            #pygame.display.set_caption("FPS: " + str(clock.get_fps()))

'''
def main_menu(running):
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((0,0,255))

main_menu(True)
'''
global jordan
jordan = Player(pygame.display.set_mode((game_width, game_height)), True, pygame.image.load('background.png').convert_alpha(), pygame.image.load('bird.png').convert_alpha(), 200, 370, 3, 160, False, pygame.Rect(0, 0, int(160*1.25), 160), True, False, False, 1, 16, 16)                     
async def main(running):
    while running:
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()
                
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                
                #if the mouse is clicked on the
                # button the game is terminated
                if width/2.5 <= mouse[0] <= width/2+45 and height/2.3 <= mouse[1] <= height/2+10:
                    while running:
                        jordan.main()

                    
        # fills the screen with a color
        screen.fill((190,0,50))
        
        # stores the (x,y) coordinates into
        # the variable as a tuple
        
        # if mouse is hovered on a button it
        # changes to lighter shade 
        if width/2.5 <= mouse[0] <= width/2+45 and height/2.3 <= mouse[1] <= height/2+10:
            pygame.draw.rect(screen,color_light,[width/2.5,height/2.3,140,40])
            
        else:
            pygame.draw.rect(screen,color_dark,[width/2.5,height/2.3,140,40])
        
        # superimposing the text onto our button
        screen.blit(text , (width/2.325,height/2.27))

        # updates the frames of the game
        pygame.display.update()
        await asyncio.sleep(0)  # Very important, and keep it 0


asyncio.run(main(True))


#jordan = Player(pygame.display.set_mode((game_width, game_height)), True, pygame.image.load('background.png').convert_alpha(), pygame.image.load('bird.png').convert_alpha(), 200, 370, 3, 160, False, pygame.Rect(0, 0, int(160*1.25), 160), True, False, False, 1, 16, 16)                     
#asyncio.run(jordan.main())


