import pygame


def main():
    pygame.init()

    # Initializes the game window
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Sudoku")

    # Fonts
    welcome_font = pygame.font.SysFont("Arial", 40, bold=True)
    selection_font = pygame.font.SysFont("Arial", 35, bold=True)
    difficulty_font = pygame.font.SysFont("Arial", 23, bold=True)
    button_font = pygame.font.SysFont("Arial", 20, bold=True)

    # Colors
    white = (255, 255, 255)
    lighter_blue = (156, 188, 247)
    light_blue = (60, 123, 239)
    # dark_blue = (15, 74, 184)
    darker_blue = (11, 30, 65)
    # black = (0, 0, 0)

    # Variables
    running = True
    easy_pressed, medium_pressed, hard_pressed = False, False, False
    # win = None

    while running:
        # Variables
        x, y = pygame.mouse.get_pos()  # Cursor position

        # Background color
        screen.fill(white)

        # Checks if any of the buttons have been clicked, if not, it displays the main menu
        if (easy_pressed is False) and (medium_pressed is False) and (hard_pressed is False):
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
            # Checks if mouse is hovering over button
            if (x >= 50) and (x <= 160) and (y >= 345) and (y <= 405):
                pygame.draw.rect(screen, light_blue, pygame.Rect(55, 350, 100, 50))
            else:
                pygame.draw.rect(screen, lighter_blue, pygame.Rect(55, 350, 100, 50))
            easy = difficulty_font.render("EASY", True, darker_blue)
            screen.blit(easy, (74, 363))

            # Medium difficulty button
            pygame.draw.rect(screen, light_blue, pygame.Rect(190, 345, 110, 60))
            # Checks if mouse is hovering over button
            if (x >= 190) and (x <= 300) and (y >= 345) and (y <= 405):
                pygame.draw.rect(screen, light_blue, pygame.Rect(195, 350, 100, 50))
            else:
                pygame.draw.rect(screen, lighter_blue, pygame.Rect(195, 350, 100, 50))
            medium = difficulty_font.render("MEDIUM", True, darker_blue)
            screen.blit(medium, (198, 363))

            # Hard difficulty button
            pygame.draw.rect(screen, light_blue, pygame.Rect(330, 345, 110, 60))
            # Checks if mouse is hovering over button
            if (x >= 330) and (x <= 440) and (y >= 345) and (y <= 405):
                pygame.draw.rect(screen, light_blue, pygame.Rect(335, 350, 100, 50))
            else:
                pygame.draw.rect(screen, lighter_blue, pygame.Rect(335, 350, 100, 50))
            hard = difficulty_font.render("HARD", True, darker_blue)
            screen.blit(hard, (351, 363))
        else:
            # Reset button
            pygame.draw.rect(screen, light_blue, pygame.Rect(50, 520, 110, 60))
            # Checks if mouse is hovering over button
            if (x >= 50) and (x <= 160) and (y >= 520) and (y <= 630):
                pygame.draw.rect(screen, light_blue, pygame.Rect(55, 525, 100, 50))
            else:
                pygame.draw.rect(screen, lighter_blue, pygame.Rect(55, 525, 100, 50))
            easy = button_font.render("RESET", True, darker_blue)
            screen.blit(easy, (73, 538))

            # Restart button
            pygame.draw.rect(screen, light_blue, pygame.Rect(190, 520, 110, 60))
            # Checks if mouse is hovering over button
            if (x >= 190) and (x <= 300) and (y >= 520) and (y <= 630):
                pygame.draw.rect(screen, light_blue, pygame.Rect(195, 525, 100, 50))
            else:
                pygame.draw.rect(screen, lighter_blue, pygame.Rect(195, 525, 100, 50))
            easy = button_font.render("RESTART", True, darker_blue)
            screen.blit(easy, (200, 538))

            # Exit button
            pygame.draw.rect(screen, light_blue, pygame.Rect(330, 520, 110, 60))
            # Checks if mouse is hovering over button
            if (x >= 330) and (x <= 440) and (y >= 520) and (y <= 630):
                pygame.draw.rect(screen, light_blue, pygame.Rect(335, 525, 100, 50))
            else:
                pygame.draw.rect(screen, lighter_blue, pygame.Rect(335, 525, 100, 50))
            easy = button_font.render("EXIT", True, darker_blue)
            screen.blit(easy, (363, 538))

        for event in pygame.event.get():
            # Checks if X at the corner of the window has been clicked
            if event.type == pygame.QUIT:
                running = False

            # Checks if a button has been clicked
            if event.type == pygame.MOUSEBUTTONUP:
                # Checks if the easy button was clicked
                if (x >= 50) and (x <= 160) and (y >= 345) and (y <= 405):
                    if (medium_pressed is False) and (hard_pressed is False):
                        easy_pressed = True

                # Checks if the medium button was clicked
                elif (x >= 190) and (x <= 300) and (y >= 345) and (y <= 405):
                    if (easy_pressed is False) and (hard_pressed is False):
                        medium_pressed = True

                # Checks if the hard button was clicked
                elif (x >= 330) and (x <= 440) and (y >= 345) and (y <= 405):
                    if (easy_pressed is False) and (medium_pressed is False):
                        hard_pressed = True

                # Checks if the reset button was clicked
                elif (x >= 50) and (x <= 160) and (y >= 520) and (y <= 630):
                    pass

                # Checks if the restart button was clicked
                elif (x >= 190) and (x <= 300) and (y >= 520) and (y <= 630):
                    easy_pressed, medium_pressed, hard_pressed = False, False, False

                # Checks if the exit button was clicked
                elif (x >= 330) and (x <= 440) and (y >= 520) and (y <= 630):
                    if (easy_pressed is True) or (medium_pressed is True) or (hard_pressed is True):
                        running = False

        pygame.display.update()


if __name__ == '__main__':
    main()
