'''
#CREATED BY KLEMEN
# import the pygame module, so you can use it
import pygame

from src.constants import BLACK, YELLOW

current_position = [0, 0]

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240, 180))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        screen.fill(BLACK)
        pygame.draw.circle(screen, YELLOW, current_position, 10)
        pygame.display.update()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                current_position[0] -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                current_position[0] += 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                current_position[1] -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                current_position[1] += 1

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
'''

#importing pygame so we use its rulesets
import pygame

#set of rules for the canvas of the game and other
pygame.init()

pygame.display.set_caption('Snakey')

clock = pygame.time.Clock()

TOTAL_COLS = 60 #columns
TOTAL_ROWS = 40 #rows
BLOCK_SIZE = 10 #in other words 10px

SURFACE = pygame.display.set_mode([TOTAL_COLS * BLOCK_SIZE, TOTAL_ROWS * BLOCK_SIZE])

#drawing the snakes head being rectangular
def draw_single_block(BLOCK_POSITION, COLOR):
    x = BLOCK_POSITION[0] * BLOCK_SIZE
    y = BLOCK_POSITION[1] * BLOCK_SIZE
    pygame.draw.rect(SURFACE, COLOR, (x, y, BLOCK_SIZE, BLOCK_SIZE))

#which direction will the block move when the "user" presses a key
def detect_direction (direction, event):
    if(event.type == pygame.KEYDOWN):
        if event.key == pygame.K_LEFT:
            return "LEFT"
        elif event.key == pygame.K_RIGHT:
            return "RIGHT"
        elif event.key == pygame.K_UP:
            return "UP"
        elif event.key == pygame.K_DOWN:
            return "DOWN"
    return direction;

#this definition is for the head of the snake to move when pressing a directional key
def move_block(column, row, direction):
    if direction == "LEFT":
        column = column - 1
    if direction == "RIGHT":
        column = column + 1
    if direction == "UP":
        row = row - 1
    if direction == "DOWN":
        row = row + 1
    return (column, row)

#this defintion was created first to create the window and to add other created definitions into it
def snakeLoop():
    game_over = False

    x1 = 30
    y1 = 20

    #it starts by moving up
    direction = "UP"
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            direction = detect_direction(direction, event)

        x1, y1 = move_block(x1, y1, direction)

        SURFACE.fill((0, 0, 0))

        draw_single_block([x1, y1], (0, 255, 0)) #GREEN

        pygame.display.update()

        clock.tick(15)

#definition for drawing the grid (still not working)
def drawGrid():
    for x in range(0, TOTAL_COLS, BLOCK_SIZE):

        for y in range(0, TOTAL_ROWS, BLOCK_SIZE):

            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

            pygame.draw.rect(SURFACE, WHITE, rect, 1)

snakeLoop()
pygame.quit()