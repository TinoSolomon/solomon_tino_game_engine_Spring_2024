# This file was created by: Tino Solomon

#completed features:
#music
#start screen
#dodge/dash with shift

#need to do:
#fix enemies
#add health bar
#enemy attacks and player attacks
#sound effects
#multiple rooms or levels
#textures and images

#want to do
#big enemy with its own music and a big health bar
#deflect enemy projectiles
#xp bar to level up stats
#charge up special move
#animations


#import necessary modules
import pygame as pg
import sys
from settings import *
from sprites import *
from random import randint
from os import path
from time import sleep

#game class
class Game:
    # define window size
    def __init__(self):
        pg.init()
        #mixer for music
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.running = True

    # load save game data
    def load_data(self):
        game_folder = path.dirname (__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
    #music files
        #self.start_menu_music = pg.mixer.Sound(path.join(game_folder, 'start_menu_music.wav'))
        #self.game_music = pg.mixer.Sound(path.join(game_folder, 'game_music.wav'))

#init all variables, setup groups, instaintiate classes
    def new(self):
        #print("create new game...")
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        # self.player1 = Player(self, 1, 1)
        # for x in range(10, 20):
        #     Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
            #print(row)
            for col, tile in enumerate(tiles):
                #print(col)
                if tile == '1':
                    #print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)
    
    #load music and loop it
        pg.mixer.music.load('game_music.wav')
        pg.mixer.music.play(loops=-1)
    
    # define run method
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

#define quit
    def quit(self):
        pg.quit()
        sys.exit()

#define update
    def update(self):
        self.all_sprites.update()

#define the grid
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, TAN, (x, 0), (x, HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, TAN, (0, y), (WIDTH, y))
        
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        surface.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    # define input method
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            #if event.type == pg.KEYDOWN:
                #if event.key == pg.K_LEFT:
                    #self.player.move(dx=-1)
                #if event.key == pg.K_RIGHT:
                    #self.player.move(dx=1)
                #if event.key == pg.K_UP:
                    #self.player.move(dy=-1)
                #if event.key == pg.K_DOWN:
                    #self.player.move(dy=1)
                    
#start screen from Mr. Cozort
    def show_start_screen(self):
        self.screen.fill(DARKGREEN)
        self.draw_text(self.screen, "Press Any Key To Start", 24, WHITE, WIDTH/2 - 32, 2)
        pg.display.flip()
#load and loop music
        pg.mixer.music.load('start_menu_music.wav')
        pg.mixer.music.play(loops=-1)
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            #import  FPS from settings
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False
        pg.mixer.music.stop()

#instantiating game class (create instance of game)
g = Game()

#showing the start screen
g.show_start_screen()
while (True):
    g.new()
    g.run()
    # g.show_go_screen()

#g.run()