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
