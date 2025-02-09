# NOTE: Spritesheet is made of 96x96

import pygame as pg
import json
import spritesheet

pg.init()

SCREEN_WIDTH = 384
SCREEN_HEIGHT = 192

# Speed / FPS
SPEED = 60

# Setting up display and clock
pg.display.set_caption("Spritesheets")
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.Clock()

# Setting up default colours
darkGray = (50, 50, 50)
black = (0, 0, 0)

# Load sprite metadata file
with open("sprite_metadata.json", "r") as file:
    spriteMetadata = json.load(file)

# Loading spritesheet in
playerSprites = spritesheet.SpriteSheet("character_sprite.png").getSpriteImages(
    spriteSheetMetadata=spriteMetadata["SpriteSheets"]["SpriteSheetExample_Player"]
)

animations = [
    playerSprites["player_idle_right"],
    playerSprites["player_idle_left"],
    playerSprites["player_walk_right"],
    playerSprites["player_walk_left"],
    playerSprites["player_shoot_right"],
    playerSprites["player_shoot_left"],
    playerSprites["player_jump_right"],
    playerSprites["player_jump_left"],
]

animation_states = [[0, 0] for _ in animations]

FRAME_UPDATE_INTERVAL = 10

drawRow = 0
numDrawn = 0
xDrawPos = 0

# Game Loop
running = True
while running:
    clock.tick(SPEED)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(darkGray)

    xDrawPos = 0
    yDrawPos = 0
    # Render
    for index, frames in enumerate(animations):
        currentFrame, counter = animation_states[index]

        counter += 1
        if counter >= FRAME_UPDATE_INTERVAL:
            currentFrame = (currentFrame + 1) % len(animations[index])
            counter = 0

        animation_states[index] = [currentFrame, counter]

        screen.blit(frames[currentFrame], (xDrawPos, yDrawPos))

        xDrawPos += 96
        if xDrawPos >= SCREEN_WIDTH:  
            xDrawPos = 0
            yDrawPos += 96

    pg.display.update()

pg.quit()
