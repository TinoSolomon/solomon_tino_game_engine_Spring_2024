#loop through a list
import pygame as pg

clock = pg.time.Clock

FPS = 30

frames = ["frame1", "frame2", "frame3", "frame4"]

current_frame = 0

#print(len(frames))

frames_length = len(frames)

then = 0

while True:
    #print("forever.......")
    clock.tick(FPS)
    if now - then > 1000:
        print(now)
        then = now
        now = pg.time.get_ticks
    #print(pg.time.get_ticks())
    current_frame += 1
    print(frames[current_frame%frames_length])