import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
  
def run():
    pygame.init()
    screen = pygame.display.set_mode((700,800))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game == True:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats, screen, sc, gun, aliens, bullets)


run()   