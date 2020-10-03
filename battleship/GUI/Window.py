from .const import pygame, width, height, fill_color, text_color, text_bkg_color


class TextRectException:
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message


def create_multi_line_surface(string, font, big_font, rect, font_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
        to fit within the given rect, word-wrapping as necessary. The text
        will be anti-aliased.

        Parameters
        ----------
        string - the text you wish to render. \n begins a new line.
        font - a Font object
        rect - a rect style giving the size of the surface requested.
        font_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
        background_color - a three-byte tuple of the rgb value of the surface.
        justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

        Returns
        -------
        Success - a surface object with the text rendered onto it.
        Failure - raises a TextRectException if the text won't fit onto the surface.

        This was modified from code given here:
            https://stackoverflow.com/questions/32590131/pygame-blitting-text-with-an-escape-character-or-newline
    """

    first = True
    real_font = font
    final_lines = []
    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.
    for requested_line in requested_lines:
        if first:
            font = big_font

        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulated_line = ""
            for word in words:
                testLine = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(testLine)[0] < rect.width:
                    accumulated_line = testLine
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

        if first:
            font = real_font
            first = False

    first_3 = True
    full_height = 0
    for line in final_lines:
        if first_3:
            font = big_font

        if full_height + font.size(line)[1] >= rect.height:
            raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")

        full_height += font.size(line)[1]

        if first_3:
            font = real_font
            first_3 = False

    offset_height = (rect.height - full_height) / 2

    # Let's try to write the text out on the surface.
    first_2 = True
    surface = pygame.Surface(rect.size)
    surface.fill(background_color)
    accumulated_height = 0
    for line in final_lines:
        if first_2:
            font = big_font

        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            temp_surface = font.render(line, 1, font_color)
        if justification == 0:
            surface.blit(temp_surface, (0, accumulated_height + offset_height))
        elif justification == 1:
            surface.blit(temp_surface, ((rect.width - temp_surface.get_width()) / 2, accumulated_height + offset_height))
        elif justification == 2:
            surface.blit(temp_surface, (rect.width - temp_surface.get_width(), accumulated_height + offset_height))
        else:
            raise TextRectException("Invalid justification argument: " + str(justification))
        accumulated_height += font.size(line)[1]

        if first_2:
            font = real_font
            first_2 = False
    return surface


class Window:
    """
    A basic wrapper class for a GUI window written in PyGame.
    """

    def __init__(self):
        self._screen = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Battleship - EECS 448')

    def render_board_for_player(self, player):
        # TODO implement
        return

    def clear(self, update=True):
        """Clear the screen and fill it with the default color."""
        self._screen.fill(fill_color)
        if update:
            self.update()
        return

    def show_message(self, message):
        """Show a pop-up message at the bottom of the screen."""
        font = pygame.font.Font(None, 24)
        text = font.render(message, 1, text_color)
        rectangle = text.get_rect(center=(width / 2, height - 50))

        surf = pygame.Surface((rectangle.width + 30, rectangle.height + 30))
        surf.fill(text_bkg_color)
        surf.blit(text, rectangle.inflate(30, 30))

        self._screen.blit(surf, rectangle)
        self._screen.blit(text, rectangle.move(15, 15))
        self.update()

    def full_screen_text(self, text, title=None, continue_text='Click anywhere to continue...'):
        """Show a full-screen message with a title and some unicode body-text."""
        self.clear(update=False)
        title_font = pygame.font.Font(None, 48)
        font = pygame.font.Font(None, 24)

        rect_width = width * (2/3)
        rect_height = height * (2/3)
        offset_width = (width - rect_width) / 2
        offset_height = (height - rect_height) / 2

        rect = pygame.Rect(offset_width, offset_height, rect_width, rect_height)
        if title:
            surface = create_multi_line_surface(title + '\n \n \n' + text + '\n \n \n \n \n' + continue_text, font, title_font, rect, text_color, text_bkg_color, 1)
        else:
            surface = create_multi_line_surface(text + '\n \n \n \n \n' + continue_text, font, title_font, rect, text_color, text_bkg_color, 1)

        self._screen.blit(surface, rect)
        self.update()
        self.get_click_event()

    def get_input(self, prompt):
        """Prompt the user for input using the prompt text.

        Args:
            prompt: the message to be shown to the user as a prompt
        """
        font = pygame.font.Font(None, 50)
        text = ''
        while True:
            for evt in pygame.event.get():
                if evt.type == pygame.KEYDOWN:
                    if evt.unicode.isalnum():
                        text += evt.unicode
                    elif evt.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif evt.key == pygame.K_RETURN:
                        return text
                elif evt.type == pygame.QUIT:
                    quit()

            self.clear(update=False)

            # Render the prompt text
            header_font = pygame.font.Font(None, 30)
            header_text = header_font.render(prompt, 1, text_color)
            header_rectangle = header_text.get_rect(center=(width / 2, 150))

            header_surf = pygame.Surface((header_rectangle.width + 30, header_rectangle.height + 30))
            header_surf.fill(text_bkg_color)
            header_surf.blit(header_text, header_rectangle.inflate(30, 30))

            self._screen.blit(header_surf, header_rectangle)
            self._screen.blit(header_text, header_rectangle.move(15, 15))

            # Render the input's text
            block = font.render(text, True, text_color)

            rect = block.get_rect()
            rect.center = self._screen.get_rect().center

            surf = pygame.Surface((rect.width + 30, rect.height + 30))
            surf.fill(text_bkg_color)
            surf.blit(block, rect.inflate(30, 30))

            self._screen.blit(surf, rect)
            self._screen.blit(block, rect.move(15, 15))
            pygame.display.flip()

    def get_click_event(self):
        """Wait for the user to click anywhere on the screen and return the event."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    return event

    def update(self):
        pygame.display.update()
