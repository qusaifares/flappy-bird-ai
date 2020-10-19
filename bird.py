import pygame
import os


bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird" + str(x) + ".png"))) for x in range(1,4)]

class Bird:
    IMGS = bird_images
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

        def jump(self):
            """
            make the bird jump
            :return: None
            """
            self.vel = -10.5
            self.tick_count = 0
            self.height = self.y