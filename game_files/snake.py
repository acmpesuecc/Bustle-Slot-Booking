gamscore=0
def main():
    import pygame #pygame is the python module used to create games
    import os #os is the python module used to interact with the operating system
    clear = lambda: os.system('cls') #lambda function to clear screen
    clear()
    import random
    from enum import Enum #used to create enumerations
    from collections import namedtuple #the collections module is used to create containers

    pygame.init() #initialises all imported pygame modules
    font = pygame.font.SysFont('arial', 25) #sets the font for the pygame window

#constants to be used throughout the file are defined here. constants are defined by using capital letters and their values cannot be altered in the file
    class Direction(Enum):
        RIGHT = 1
        LEFT = 2
        UP = 3
        DOWN = 4
        
    Point = namedtuple('Point', 'x, y')

    # rgb colors
    WHITE = (255, 255, 255)
    RED = (200,0,0)
    BLUE1 = (0, 0, 255)
    BLUE2 = (0, 100, 255)
    BLACK = (0,0,0)

    BLOCK_SIZE = 20
    SPEED = 15

    class SnakeGame:
        
        def __init__(self, w=640, h=480):
            self.w = w
            self.h = h
            # init display
            self.display = pygame.display.set_mode((self.w, self.h)) #creates a pygame surface class instance
            pygame.display.set_caption('Snake') #sets the title of the window
            self.clock = pygame.time.Clock()
            
            # init game state
            self.direction = Direction.RIGHT #defines the initial direction of the snake
            
            self.head = Point(self.w/2, self.h/2)
            self.snake = [self.head, 
                        Point(self.head.x-BLOCK_SIZE, self.head.y),
                        Point(self.head.x-(2*BLOCK_SIZE), self.head.y)] #defines the initial position of the snake
            
            self.score = 0
            self.food = None
            self._place_food() #spawns food at random spots on the screen
            
        def _place_food(self):
            #defines coordinates of the food
            x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
            y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
            self.food = Point(x, y)
            if self.food in self.snake: #if the snake coordinates encompass the good coordinates, the food is considered eaten and food is spawned again
                self._place_food()
            
        def play_step(self):
            # 1. collect user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT:
                        self.direction = Direction.RIGHT
                    elif event.key == pygame.K_UP:
                        self.direction = Direction.UP
                    elif event.key == pygame.K_DOWN:
                        self.direction = Direction.DOWN #changes snake direction based on arrow key inputs from the user
            
            # 2. move
            self._move(self.direction) # update the head
            self.snake.insert(0, self.head)
            
            # 3. check if game over
            game_over = False
            if self._is_collision(): #if the snake collides with the walls, the game is ended and score is returned
                game_over = True
                return game_over, self.score
                
            # 4. place new food or just move
            if self.head == self.food:
                self.score += 1
                self._place_food() #appends score and spawns food if the snake eats food
            else:
                self.snake.pop()
            
            # 5. update ui and clock
            self._update_ui()
            self.clock.tick(SPEED) #updates the speed of the game
            # 6. return game over and score
            return game_over, self.score
        
        def _is_collision(self): #function to handle collisions with walls
            # hits boundary
            if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
                return True
            # hits itself
            if (self.head in self.snake[1:]) and (self.head != self.snake[0]):
                return True
            
            return False
            
        def _update_ui(self):
            self.display.fill(BLACK)
            
            for pt in self.snake:
                pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
                
            pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
            
            text = font.render("Score: " + str(self.score), True, WHITE) #renders the score on the screen
            self.display.blit(text, [0, 0])
            pygame.display.flip()
            
        def _move(self, direction):
            x = self.head.x
            y = self.head.y
            #updates the position of head
            if direction == Direction.RIGHT:
                x += BLOCK_SIZE
            elif direction == Direction.LEFT:
                x -= BLOCK_SIZE
            elif direction == Direction.DOWN:
                y += BLOCK_SIZE
            elif direction == Direction.UP:
                y -= BLOCK_SIZE
                
            self.head = Point(x, y)

    if __name__ == '__main__': #__main__ is the top-level
            game = SnakeGame()
        
            # game loop
            while True:
                game_over, score = game.play_step()
            
                if game_over == True:
                    break
            
            print('Final Score is:', score) #prints final score when the game ends
            pygame.quit()
            return score           
gamscore=str(main())
with open("tempscore","w") as file:
    file.write(str(gamscore)) #adds the game's score to the tempscore file
