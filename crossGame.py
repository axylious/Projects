# Pygame Development

import pygame

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'

# Colors
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)

# Clock to update events and FPS
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    # FPS
    TICK_RATE = 60

    # Initializer for game class to set up title, width, and height
    def __init__(self, imgPath, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        
        # Create game window to specified size
        self.gameScreen = pygame.display.set_mode((width, height))

        # Set game window to white
        self.gameScreen.fill(WHITE_COLOR)

        # Set game window title
        pygame.display.set_caption(title)

        bgImg = pygame.image.load(imgPath)
        self.image = pygame.transform.scale(bgImg,(width, height))

    def runGameLoop(self, lvlSpd):
        # Initialize gameOver variable
        gameOver = False
        win = False
        direction = 0

        p1 = PlayerCharacter('player.png', 375, 700, 50, 50)
        e0 = EnemyCharacter('enemy.png', 20, 600, 50, 50)
        e0.SPEED *= lvlSpd
        
        e1 = EnemyCharacter('enemy.png', self.width - 40, 400, 50, 50)
        e1.SPEED *= lvlSpd

        e2 = EnemyCharacter('enemy.png', 20, 200, 50, 50)
        e2.SPEED *= lvlSpd
        
        treasure = GameObj('treasure.png', 375, 50, 50, 50)
        
        # Main game loop runs until gameOver = True
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                # Detects when key is pressed
                elif event.type == pygame.KEYDOWN:
                    # Move up when up key is pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down when down key is pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Detect when key is released
                elif event.type == pygame.KEYUP:
                    # Stop movement when key is released
                    if event.key == pygame.K_UP or pygame.K_DOWN:
                        direction = 0
                print(event)

            # Redraw screen to be blank window
            self.gameScreen.fill(WHITE_COLOR)
            self.gameScreen.blit(self.image,(0,0))

            treasure.draw(self.gameScreen)
            
            # Update player position
            p1.move(direction, self.height)
            p1.draw(self.gameScreen)

            e0.move(self.width)
            e0.draw(self.gameScreen)

            if lvlSpd > 1.5:
                e1.move(self.width)
                e1.draw(self.gameScreen)
            if lvlSpd > 3:
                e2.move(self.width)
                e2.draw(self.gameScreen)
            
            # End game on collision with enemy or treasure
            if p1.detectCollision(e0):
                gameOver = True
                win = False
                text = font.render('Git Gud Scrub', True, BLACK_COLOR)
                self.gameScreen.blit(text,(225,350))
                pygame.display.update()
                clock.tick(1)
                break
            elif p1.detectCollision(treasure):
                gameOver = True
                win = True
                text = font.render('Well Done Guardian!', True, BLACK_COLOR)
                self.gameScreen.blit(text,(175,350))
                pygame.display.update()
                clock.tick(1)
                break
            
            # Updates display and runs clock
            pygame.display.update()
            clock.tick(self.TICK_RATE)

        if win:
            self.runGameLoop(lvlSpd + 0.5)
        else:
            return

class GameObj:
    def __init__(self, imgPath, x, y, width, height):   
        # Load and scale player image
        objImg = pygame.image.load(imgPath)
        self.img = pygame.transform.scale(objImg, (width, height))

        self.x = x
        self.y = y
        self.width = width
        self.height = height
            
    def draw(self, background):
            background.blit(self.img, (self.x, self.y))


class PlayerCharacter(GameObj):
    SPEED = 5
    
    def __init__(self, imgPath, x, y, width, height):
        super().__init__(imgPath, x, y, width, height)

    # Moves character up if direction > 0 and down if < 0
    def move(self, direction, maxHeight):
        if direction > 0:
            self.y -= self.SPEED
        elif direction < 0:
            self.y += self.SPEED

        if self.y >= maxHeight - 50:
            self.y = maxHeight - 50
    # Detects collision between pc and npc
    def detectCollision(self, otherBody):
        # Checks if pc is below npc
        if self.y > otherBody.y + otherBody.height:
            return False
        # Checks if pc is above npc
        elif self.y + self.height < otherBody.y:
            return False

        # Checks if pc is right of npc
        if self.x > otherBody.x + otherBody.width:
            return False
        # Checks if pc is left of npc
        elif self.x + self.width < otherBody.x:
            return False

        return True
    
class EnemyCharacter(GameObj):
    SPEED = 5
    
    def __init__(self, imgPath, x, y, width, height):
        super().__init__(imgPath, x, y, width, height)

    def move(self, maxWidth):
        if self.x <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x >= maxWidth - 70:
            self.SPEED = -abs(self.SPEED)
        self.x += self.SPEED            
            
pygame.init()

newGame = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
newGame.runGameLoop(1)


# Quit pygame and program
pygame.quit()
quit()
