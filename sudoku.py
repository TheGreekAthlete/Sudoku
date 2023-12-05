import pygame
import sys


def main():
    pygame.init()

    # Initializes the game window
    width, height = 500, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")

    # Fonts
    welcome_font = pygame.font.SysFont("Arial", 40, bold=True)
    selection_font = pygame.font.SysFont("Arial", 35, bold=True)
    difficulty_font = pygame.font.SysFont("Arial", 23, bold=True)

    # Colors
    white = (255, 255, 255)
    lighter_blue = (156, 188, 247)
    light_blue = (60, 123, 239)
    dark_blue = (15, 74, 184)
    darker_blue = (11, 30, 65)
    black = (0, 0, 0)

    running = True

    while running:
        # Background color
        screen.fill(white)

        # Gator image
        img = pygame.image.load("UFGATOR.png").convert()
        img = pygame.transform.scale(img, (100, 99))
        screen.blit(img, (200, 60))

        # Welcome message
        welcome = welcome_font.render("Welcome to Sudoku!", True, darker_blue)
        screen.blit(welcome, (50, 175))

        # Menu selection prompt
        selection_text = selection_font.render("Select Game Mode:", True, darker_blue)
        screen.blit(selection_text, (85, 265))

        # Easy difficulty button
        pygame.draw.rect(screen, light_blue, pygame.Rect(50, 345, 110, 60))
        pygame.draw.rect(screen, lighter_blue, pygame.Rect(55, 350, 100, 50))
        easy = difficulty_font.render("EASY", True, darker_blue)
        screen.blit(easy, (74, 363))

        # Medium difficulty button
        pygame.draw.rect(screen, light_blue, pygame.Rect(190, 345, 110, 60))
        pygame.draw.rect(screen, lighter_blue, pygame.Rect(195, 350, 100, 50))
        medium = difficulty_font.render("MEDIUM", True, darker_blue)
        screen.blit(medium, (198, 363))

        # Hard difficulty button
        pygame.draw.rect(screen, light_blue, pygame.Rect(330, 345, 110, 60))
        pygame.draw.rect(screen, lighter_blue, pygame.Rect(335, 350, 100, 50))
        hard = difficulty_font.render("HARD", True, darker_blue)
        screen.blit(hard, (352, 363))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == '__main__':
    main()
