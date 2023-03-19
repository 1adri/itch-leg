#Done slight changes to code and works for me:

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
smallfont = pygame.font.Font('aachen.ttf',35)
  
# rendering a text written in
# this font
text = smallfont.render('PLAY' , True , color)
def_count = 0
#motion1 = False
motion2 = False
# Load the basketball image
basketball_image = pygame.image.load('basketball.png')

# Set the starting position of the basketball
basketball_x1 = 315
basketball_y1 = 400

# Set the initial velocity of the basketball
basketball_velocity_x = 0
basketball_velocity_y = 0

# Set the gravity constant
GRAVITY = 0.5
class Basketball:
    def __init__(self, screen, running, basketball, player_x, player_y, player_facing_left, motion, background, Y_VELOCITY, Y_GRAVITY, JUMP_HEIGHT, basketball_x, basketball_y, vx, vy, def_count, shooted):
        self.screen = screen
        self.running = running
        self.basketball = basketball
        self.player_x = player_x
        self.player_y = player_y
        self.player_facing_left = player_facing_left
        self.motion = motion
        self.background = background
        self.Y_VELOCITY = Y_VELOCITY
        self.Y_GRAVITY = Y_GRAVITY
        self.JUMP_HEIGHT = JUMP_HEIGHT
        self.basketball_x = basketball_x
        self.basketball_y = basketball_y
        self.vx = vx
        self.vy = vy
        self.def_count = def_count
        self.shooted = shooted
    def main(self):
        if not shooted:
            if self.player_facing_left:

                self.basketball_x = self.player_x+26
                self.basketball_y = self.player_y+70
                self.screen.blit(self.basketball, (self.basketball_x, self.basketball_y))


            else:

                self.basketball_x = self.player_x+115
                self.basketball_y = self.player_y+70
                self.screen.blit(self.basketball, (self.basketball_x, self.basketball_y))
        else:

            tup = (self.player_x, self.player_y)
            print(tup[0], "tupp")
            global basketball_x1, basketball_y1
            global basketball_velocity_x, basketball_velocity_y
            basketball_x1 = tup[0]
            basketball_y1=  tup[1]
            basketball_x1 += basketball_velocity_x
            basketball_y1 += basketball_velocity_y
            # Apply gravity to the basketball
            basketball_velocity_y += GRAVITY

            # Draw the screen
            screen.blit(self.basketball, (basketball_x1, basketball_y1))  # Draw the basketball
            print(basketball_x1, basketball_y1)
    def shoot(self):

        vx = 15
        vy = -15
        basketball_x = self.basketball_x
        basketball_y = self.basketball_y
        while self.motion:
            #print(vy, vx)
            #print(basketball_x)
            # Update the ball's position
            basketball_x += vx
            basketball_y += vy
            #print(vx, vy, "self1")

            #print(vx, vy, "self")

            #print(basketball_x)
            # Check if the ball is out of bounds and reverse its velocity if necessary
            if basketball_x  < 0 or basketball_x  > 850:
                global motion2
                motion2 = False
                self.motion = False

                #print("hello")
                return
            if basketball_y - 20 < 0 or basketball_y + 20 > 540:
                motion2 = False
                self.motion = False

                #print(motion2)


            # Draw the ball and update the display
            #self.screen.blit(self.background, (0, 0))
            #pygame.draw.circle(screen, (255, 255, 255), (x, y), 20)
            #print(x, y)
            #pygame.draw.rect(self.screen,  (255, 255, 255), (0, 0), 15)
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.basketball, (basketball_x, basketball_y))
            pygame.display.update()
            clock.tick(50)
            #pygame.time.delay(1000)
            #self.screen.blit(self.background, (0,0))
            #self.screen.blit(self.background, (0,0))
        #pygame.display.update()
        #clock.tick(50)


        #print("shoooted"
        '''
        if self.player_facing_left:
            pass
        else:
            for i in range(40):
                print(i)
                self.screen.blit(self.basketball, (self.basketball_x+i, self.basketball_y-i))
                self.screen.blit(self.background, (0,0))
                if i == 39:
                    self.motion = False
                    self.main()
                #pygame.time.delay(1)
        '''
        '''
            pygame.time.delay(100)

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.basketball, (basketball_pos[0]+58, basketball_pos[1]-49))
        '''
    def shoot_basketball(self):
        # Set the velocity of the basketball
        global basketball_velocity_x, basketball_velocity_y
        basketball_velocity_x = 10
        basketball_velocity_y = -10
shooted=False
class Player:
    def __init__(self, screen, running, background, player, player_x, player_y, player_speed, player_size, player_facing_left, player_hitbox, player_alive, isjump, jumping,  Y_GRAVITY, JUMP_HEIGHT, Y_VELOCITY, def_count):
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
        self.def_count = def_count
    async def main(self):
        # Everything under 'while running' will be repeated over and over again
        self.running = True


        while self.running:

            #basketball = Basketball(self.screen, self.running, pygame.image.load('basketball.png').convert_alpha(), self.player_x, self.player_y, self.player_facing_left,
                                    #motion1, pygame.image.load('background.png').convert_alpha(),1, 16, 16, self.player_x+80, self.player_y+75)

            self.screen.blit(self.background, (0, 0))

            keys = pygame.key.get_pressed()

            # Makes the game stop if the player clicks the X or presses esc
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        self.jumping = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                        pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    global shooted
                    shooted = True
                    basketball.shoot_basketball()
            basketball = Basketball(self.screen, self.running, pygame.image.load('basketball.png').convert_alpha(), self.player_x, self.player_y, self.player_facing_left,
                                    motion2, pygame.image.load('background.png').convert_alpha(), 5, 3, 2,  self.player_x+80, self.player_y+75, 5, -5,  self.def_count, shooted)
            #basketball.main()
            #print(motion2)

            basketball.main()


            # Check for out-of-bounds


            if keys[pygame.K_a]:
                #print(self.player_x, self.player_y)
                if self.player_x > 0:
                    self.player_x -= self.player_speed
                    self.player_facing_left = True

                #player_y += player_speed
            if keys[pygame.K_LSHIFT]:
                #print(self.player_x, self.player_y)

                    if keys[pygame.K_d]:
                        if self.player_x < 850:
                            self.player_x += 3.5
                        #player_facing_left = False
                    if keys[pygame.K_a]:
                        if self.player_x > 0:

                            self.player_x -= 3.5
                        #player_facing_left = True
            if keys[pygame.K_d]:
                #print(self.player_x, self.player_y)
                if self.player_x < 850:
                    self.player_x += self.player_speed
                    self.player_facing_left = False


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
                pass
            screen.blit(player_small, (self.player_x, self.player_y))




            #merged = self.player.copy()

            #screen.blit(score_text, (1600, 30))

            # Update Screen
            pygame.display.update()
            clock.tick(50)
            await asyncio.sleep(0)
            pygame.display.set_caption("FPS: " + str(clock.get_fps()))

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
jordan = Player(pygame.display.set_mode((game_width, game_height)), True, pygame.image.load('background.png').convert(), pygame.image.load('curry3.png').convert_alpha(), 200, 300, 3, 260, False, pygame.Rect(0, 0, int(160*1.25), 160), True, False, False, 1, 16, 16, def_count)                
async def main():
    running = True
    while running:
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                running = False
                
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on the
                # button the game is terminated
                if width/2.5 <= mouse[0] <= width/2+45 and height/2.3 <= mouse[1] <= height/2+10:
                    await jordan.main()

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
        screen.blit(text, (width/2.325,height/2.27))

        # updates the frames of the game
        pygame.display.update()
        await asyncio.sleep(0)  # Very important, and keep it 0
    #pygame.quit()


asyncio.run(main())

#[Diff](https://diffy.org/diff/3626b7ae7b5fc)

#What did I change?
#Game loop also needs to be asynchronous, otherwise the window wouldn't be refreshed.