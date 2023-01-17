import pygame, sys
from variable import *

class Menu(object):
    def __init__(self, surface):
        self.font = pygame.font.SysFont("nanumgothicbold", 30)
        self.surface = surface
        self.draw_menu()

    def draw_menu(self):
        top, left = window_height - 30, window_width - 200
        self.new_rect = self.make_text(self.font, 'New Game', BLUE, None, top - 30, left)
        self.quit_rect = self.make_text(self.font, 'Quit Game', BLUE, None, top, left)
        self.show_rect = self.make_text(self.font, 'Hide Number', BLUE, None, top - 60, left)
        self.undo_rect = self.make_text(self.font, 'Undo', BLUE, None, top - 150, left)
        self.uall_rect = self.make_text(self.font, 'Undo All', BLUE, None, top - 120, left)
        self.redo_rect = self.make_text(self.font, 'Redo', BLUE, None, top - 90, left)

    def make_text(self, font, text, color, bgcolor, top, left, position = 0):
        surf = font.render(text, False, color, bgcolor)
        rect = surf.get_rect()
        if position:
            rect.center = (left, top)
        else:    
            rect.topleft = (left, top)
        self.surface.blit(surf, rect)
        return rect

    def terminate(self):
        pygame.quit()
        sys.exit()
    
    # need to remove the message after new game is started
    def winning_message(self, turn):
        print(turn)
        if turn == 1:
            winning_message = "Black Wins!"
        else:
            winning_message = "White Wins!"
        
        self.make_text(self.font, winning_message, BLUE, None, window_height -500, window_width - 200)
        #pygame.time.set_timer(self.make_text(self.font, "", BLACK, None, window_height -500, window_width - 200), 3, 1)
        
