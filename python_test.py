import pygame
from pygame.locals import *
 "napomena: Rendint(a, b) je funkcija za random brojeve."
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((700,700), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("ba33e6f8-5790-4f75-bed1-96a76d8e06ce.jpg").convert()
        pygame.mouse.set_visible(True)
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    def on_loop(self):
        mouse = pygame.mouse.get_pos()
        
    def on_render(self):
        self._display_surf.blit(self._image_surf,(0,0))
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running )
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
