from .const import pygame, width, height, fill_color, text_color, text_bkg_color, button_bkg_color
from ..enum import board_cell_state_to_render_color, BoardCellState


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

    def _render_board(self, board, block_size, pixel_gap, offset_left, offset_top, override_statuses=None, masks=None):
        """Render the given board to the screen using the offset and gap info.

            Args:
                board: a Board object
                block_size: number of pixels square for each cell
                pixel_gap: how many pixels between cells
                offset_left: left-most position of the grid
                offset_top: top-most position of the grid
                override_statuses: array of ((row, col), BoardCellState) to override from the board
        """
        if override_statuses is None:
            override_statuses = []

        if masks is None:
            masks = []

        rect_coords = []
        for row in range(9):
            for col in range(9):
                rect = pygame.Rect(
                    offset_left + (col * (block_size + pixel_gap)),
                    offset_top + (row * (block_size + pixel_gap)),
                    block_size,
                    block_size
                )

                surf = pygame.Surface((rect.width, rect.height))

                status = board.board[row][col]

                if status in masks:
                    status = BoardCellState.Empty

                for status_group in override_statuses:
                    coord = status_group[0]
                    override = status_group[1]
                    if coord[0] == row and coord[1] == col:
                        status = override

                surf.fill(board_cell_state_to_render_color(status))

                rect_coords.append((rect, (row, col)))
                self._screen.blit(surf, rect)

        return rect_coords

    def render_board_for_player(self, player, override_statuses=None, mask_opponent=True, victor=False):
        """Given a player, render the play screen for them, showing their grid and their opponent's.

        Args:
            player: the Player instance
            override_statuses: array of ((row, col), BoardCellState) to override from the player's Board

        Returns:
            player_rects: array of rectangle, coordinate pairs placed
            opponent_rects: array of rectangle, coordinate pairs placed
        """
        if override_statuses is None:
            override_statuses = []

        self.clear(update=False)
        font = pygame.font.Font(None, 24)

        block_size = 40
        pixel_gap = 2
        offset_left = 50
        offset_top = 70

        # Render the left board (the opponent)
        masks = []
        if mask_opponent:
            masks = [BoardCellState.Ship]

        opponent_rects = self._render_board(player.other_player.board, block_size, pixel_gap, offset_left, offset_top, masks=masks)

        # Render the label for the grid
        opponent_text = font.render(str(player.other_player.name) + '\'s Fleet', 1, text_color)
        opponent_text_offset_left = (offset_left + (block_size * 4.5)) - (opponent_text.get_rect().width / 2)
        opponent_text_rect = opponent_text.get_rect(left=opponent_text_offset_left, top=offset_top - 30)
        self._screen.blit(opponent_text, opponent_text_rect)

        # Render the right board (the player)
        offset_left = width - (offset_left + (9 * (block_size + pixel_gap)))  # Recalculate how far from the left
        player_rects = self._render_board(player.board, block_size, pixel_gap, offset_left, offset_top, override_statuses)

        # Render the label for the grid
        player_text = font.render(player.name + '\'s Fleet'+(' (winner)' if victor else ''), 1, text_color)
        player_text_offset_left = (offset_left + (block_size * 4.5)) - (player_text.get_rect().width / 2)
        player_text_rect = player_text.get_rect(left=player_text_offset_left, top=offset_top - 30)
        self._screen.blit(player_text, player_text_rect)

        self.update()
        return player_rects, opponent_rects

    def get_grid_click_event(self, rect_coords):
        """Wait for a click event, then return the coordinates of the cell that was clicked.

        Args:
            rect_coords: array of (pygame.Rect, (row, col)) "A1" or "D5"
        Returns:
            (row, col)
        """
        while True:
            event = self.get_click_event()
            for rect_coord in rect_coords:
                rect = rect_coord[0]
                coords = rect_coord[1]
                if rect.collidepoint(event.pos):
                    return coords

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
        rectangle = text.get_rect(center=(width / 2, height - 75))

        surf = pygame.Surface((rectangle.width + 30, rectangle.height + 30))
        surf.fill(text_bkg_color)
        surf.blit(text, rectangle.inflate(30, 30))

        self._screen.blit(surf, rectangle.move(-15, -15))
        self._screen.blit(text, rectangle)
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

    def two_button_prompt(self, text, yes='Yes', no='No'):
        """Draw a full-screen message as a prompt with two buttons.

        Args:
            text: the text to show the user
            yes: the text of the "Yes" action
            no: the text of the "No" action

        Returns:
            True: if the user clicked the "Yes" action
            False: if the user clicked the "No" action
        """
        self.clear(update=False)

        # Draw the full-screen text
        title_font = pygame.font.Font(None, 48)
        font = pygame.font.Font(None, 24)

        rect_width = width * (2 / 3)
        rect_height = height * (2 / 3)
        offset_width = (width - rect_width) / 2
        offset_height = (height - rect_height) / 2

        rect = pygame.Rect(offset_width, offset_height, rect_width, rect_height)
        surface = create_multi_line_surface(' \n' + text + '\n \n \n ', font, title_font, rect, text_color, text_bkg_color, 1)

        self._screen.blit(surface, rect)

        # Draw the buttons
        yes_text = font.render(yes, 1, text_color)
        yes_rect = yes_text.get_rect(center=(width / 2, height - 150))

        yes_surf = pygame.Surface((yes_rect.width + 30, yes_rect.height + 30))
        yes_surf.fill(button_bkg_color)
        yes_surf.blit(yes_text, yes_rect.inflate(30, 30))

        no_text = font.render(no, 1, text_color)
        no_rect = no_text.get_rect(center=(width / 2, height - 150))

        no_surf = pygame.Surface((no_rect.width + 30, no_rect.height + 30))
        no_surf.fill(button_bkg_color)
        no_surf.blit(no_text, no_rect.inflate(30, 30))

        # Move the buttons to their appropriate places
        yes_half_width = (yes_rect.width / 2) + 30
        no_half_width = (no_rect.width / 2) + 30

        yes_rect.move_ip(-yes_half_width, 0)
        no_rect.move_ip(no_half_width, 0)

        self._screen.blit(yes_surf, yes_rect)

        yes_rect.move_ip(15, 15)
        self._screen.blit(yes_text, yes_rect)

        self._screen.blit(no_surf, no_rect)

        no_rect.move_ip(15, 15)
        self._screen.blit(no_text, no_rect)
        self.update()

        # Wait for a valid click event
        while True:
            event = self.get_click_event()
            if yes_rect.inflate(30, 30).collidepoint(event.pos):
                return True
            elif no_rect.inflate(30, 30).collidepoint(event.pos):
                return False

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
