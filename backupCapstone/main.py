import pygame
from pygame.locals import *
import time 
import random

SIZE = 16
BACKGROUND_COLOUR = (186,216,10)
class Apple:
    def __init__(self,parentscreen):
        self.parentscreen = parentscreen
        self.image = pygame.image.load_extended("Resources\Rabbit.png").convert_alpha()
        self.x = SIZE
        self.y = SIZE

    def draw(self):
        self.parentscreen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load_extended("Resources\Square.png").convert_alpha()
        self.x = [SIZE]*length
        self.y = [SIZE]* length
        self.direction = "down"

    def increase_length(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((BACKGROUND_COLOUR))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = "left"
    def move_right(self):
        self.direction = "right"
    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"
        
    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i]= self.x[i-1]
            self.y[i]= self.y[i-1]
        if self.direction == 'up':
            self.y[0] -= SIZE
            self.draw()
        if self.direction == "down":
            self.y[0] += SIZE
            self.draw()
        if self.direction == 'left':
            self.x[0] -= SIZE
            self.draw()
        if self.direction == "right":
            self.x[0] += SIZE
            self.draw()
        

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,600))
        self.surface.fill((BACKGROUND_COLOUR))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1< x2 + SIZE:
            if y1 >= y2 and y1< y2 + SIZE:
                return True
            
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw() 
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()


        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise "Game Over"
        
        if not(0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            raise "Hit the boundary error"
            

    def display_score(self):
        font = pygame.font.SysFont("arial",30)
        score = font.render(f"Score: {self.snake.length}", True,(255,255,255))
        self.surface.blit(score,(600,10))

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOUR)
        font = pygame.font.SysFont("arial",30)
        line1 = font.render(f"GAME OVER! Your Score is {self.snake.length}", True,(255,255,255))
        self.surface.blit(line1,(200,300))
        line2 = font.render("Replay? Press ENTER", True, (255,255,255))
        self.surface.blit(line2,(200,350))
        pygame.display.flip()


    def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple = Apple(self.surface)


    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running =  False
                    
                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if self.is_collision(self.snake.x[0],self.snake.y[0],1000,600):
                            self.show_game_over()
                        
                elif event.type == QUIT:
                    running =  False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            
            time.sleep(0.15)



if __name__ == "__main__":

    game = Game()
    game.run()
    
    
    
    