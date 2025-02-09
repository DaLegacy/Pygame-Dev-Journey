import pygame as pg


class SpriteSheet:
    def __init__(self, filePath):
        self.sheet = pg.image.load(filePath)

    def getSpriteImage(
        self,
        frame: int,
        width: int,
        height: int,
        scaleFactor: int = 1,
        transparent: bool = True,
        row: int = 0,
    ) -> pg.Surface:
        # Creating a surface with giving dimensions
        image = pg.Surface((width, height)).convert_alpha()

        # Setting x coord for a selected frame
        x = frame * width

        # Setting y coord for a selected row
        y = row * height

        # Drawing the selected frame onto a surface
        image.blit(self.sheet, (0, 0), (x, y, width, height))

        # Rescaling the sprite
        image = pg.transform.scale(image, (width * scaleFactor, height * scaleFactor))

        # Removing the background of the sprite
        if transparent:
            image.set_colorkey((0, 0, 0))

        return image

    def getSpriteImages(
        self, spriteSheetMetadata: str, scaleFactor: int = 1, transparent: bool = True
    ) -> dict:
        # Returning sprite dict
        sprites = {}

        # Setting dimensions of all sprites on that spritesheet
        sprite_width = spriteSheetMetadata["spriteMetadata"]["spriteWidth"]
        sprite_height = spriteSheetMetadata["spriteMetadata"]["spriteHeight"]

        # Row index to get multiple rows if multiple rows exist in the same spritesheet
        rowIndex = 0

        # Load sprites from each row
        for spriteName, numFrames in spriteSheetMetadata["rows"].items():
            spriteFrames = []

            # Looping over each frame and getting the sprite
            for frame in range(numFrames):
                try:
                    sprite = self.getSpriteImage(
                        frame,
                        sprite_width,
                        sprite_height,
                        scaleFactor=scaleFactor,
                        transparent=transparent,
                        row=rowIndex,
                    )
                    spriteFrames.append(sprite)

                    # Debug for loaded success
                    print(f"Loaded sprite: {spriteName}, Frame {frame}")
                except Exception as e:
                    # Debug for error occurd during loading sprite
                    print(f"Error loading sprite: {spriteName}, Frame {frame} - {e}")

            # Store loaded sprites
            sprites[spriteName] = spriteFrames

            # Move the the next row
            rowIndex += 1

        return sprites
