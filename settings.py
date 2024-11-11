# Define game variables and useful external functions

MAP = [
['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
['1','B','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1','B','1'],
['1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1'],
['1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1'],
['1',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ','1'],
['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
['1',' ',' ',' ',' ',' ',' ',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ','1'],
['1','1',' ','1','1','1',' ','1','1','-','1','1',' ','1','1','1',' ','1','1'],
[' ',' ',' ',' ',' ','1',' ','1','s','p','o','1',' ','1',' ',' ',' ',' ',' '],
['1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1'],
['1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1'],
['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
['1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1'],
['1',' ',' ',' ','1',' ',' ',' ',' ','P',' ',' ',' ',' ','1',' ',' ',' ','1'],
['1','B','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1','B','1'],
['1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1'],
['1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1'],
['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
]
BOARD_RATIO = (len(MAP[0]), len(MAP))
CHAR_SIZE = 32
WIDTH, HEIGHT = (BOARD_RATIO[0] * CHAR_SIZE, BOARD_RATIO[1] * CHAR_SIZE)
NAV_HEIGHT = 64
PLAYER_SPEED = CHAR_SIZE // 4
GHOST_SPEED = 4

def update(self):
    if not self.game_over:
        # player movement
        pressed_key = pygame.key.get_pressed()
        self.player.sprite.animate(pressed_key, self.walls_collide_list)
        # teleporting to the other side of the map
        if self.player.sprite.rect.right <= 0:
            self.player.sprite.rect.x = WIDTH
        elif self.player.sprite.rect.left >= WIDTH:
            self.player.sprite.rect.x = 0
        # PacMan eating-berry effect
        for berry in self.berries.sprites():
            if self.player.sprite.rect.colliderect(berry.rect):
                if berry.power_up:
                    self.player.sprite.immune_time = 150 # Timer based from FPS count
                    self.player.sprite.pac_score += 50
                else:
                    self.player.sprite.pac_score += 10
                berry.kill()
        # PacMan bumping into ghosts
        for ghost in self.ghosts.sprites():
            if self.player.sprite.rect.colliderect(ghost.rect):
                if not self.player.sprite.immune:
                    time.sleep(2)
                    self.player.sprite.life -= 1
                    self.reset_pos = True
                    break
                else:
                    ghost.move_to_start_pos()
                    self.player.sprite.pac_score += 100
    self._check_game_state()
    # rendering
    [wall.update(self.screen) for wall in self.walls.sprites()]
    [berry.update(self.screen) for berry in self.berries.sprites()]
    [ghost.update(self.walls_collide_list) for ghost in self.ghosts.sprites()]
    self.ghosts.draw(self.screen)
    self.player.update()
    self.player.draw(self.screen)
    self.display.game_over() if self.game_over else None
    self._dashboard()
    # reset Pac and Ghosts position after PacMan get captured
    if self.reset_pos and not self.game_over:
        [ghost.move_to_start_pos() for ghost in self.ghosts.sprites()]
        self.player.sprite.move_to_start_pos()
        self.player.sprite.status = "idle"
        self.player.sprite.direction = (0,0)
        self.reset_pos = False
    # for restart button
    if self.game_over:
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_r]:
            self.game_over = False
            self.restart_level()
            