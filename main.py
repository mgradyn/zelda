import pygame, sys
from settings import *
from level import Level
from restart_state import Restart
from gameover import GameOver


class Game:
    def __init__(self):
        pygame.init()
        self.flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), self.flags, vsync=1)
        self.title = pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()
        
        self.level = Level()

        # game state
        self.running = True
        self.restart = Restart(self.stop)

        # user interface
        self.game_over = GameOver(self.restart.restart)

        # sound
        main_sound = pygame.mixer.Sound(sound_effect_data['main'])
        main_sound.set_volume(0.3)
        main_sound.play(loops=-1)

    def stop(self):
        self.running = False
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
            
            self.screen.fill(WATER_COLOR)
            if not self.running:
                pygame.quit()
                game = Game()
                game.run()
            self.level.run(self.game_over)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()


