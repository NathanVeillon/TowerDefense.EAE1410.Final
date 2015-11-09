# StartMenu.py
# 
# File Contributors
#     
# 
# Purpose:
# 
class StartMenu():

    def __init__(self):
        self.window = pygame.display.get_surface()
        self.menu_base = pygame.Surface((self.map_size, self.map_size), flags=SRCALPHA, depth=32)
    #player clicked on the start menu
    def clicked(self, mouse_pos):


