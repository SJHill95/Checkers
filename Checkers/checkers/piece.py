import pygame
from .constants import CROWN_RED, CROWN_WHITE, WHITE, RED, SQUARE_SIZE, RED_OUTLINE, WHITE_OUTLINE, CROWN_RED, CROWN_WHITE

class Piece:
    PADDING = 15
    OUTLINE = 5

    # Initilize variables
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False  
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    # Calculates the position of the piece
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y =  SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    #Function to make the piece a king
    def make_king(self):
        if self.king != True:
            self.king = True  

    # Function to draw the pieces
    def draw(self, window):
        radius = SQUARE_SIZE//2 - self.PADDING
        # Sets the color of the outline of the piece
        if self.color == RED:
            pygame.draw.circle(window, RED_OUTLINE, (self.x, self.y), radius + self.OUTLINE)
        elif self.color == WHITE:
            pygame.draw.circle(window, WHITE_OUTLINE, (self.x, self.y), radius + self.OUTLINE)
        
        # Draws the piece 
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)

        # Draws crown on the piece if it is a king
        if self.king:
            if self.color == RED:
                window.blit(CROWN_RED, (self.x - CROWN_RED.get_width()//2, self.y - CROWN_RED.get_height()//2))
            elif self.color == WHITE:
                window.blit(CROWN_WHITE, (self.x - CROWN_WHITE.get_width()//2, self.y - CROWN_WHITE.get_height()//2))

    # Function to move the piece
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        
    def __repr__(self):
        return str(self.color)