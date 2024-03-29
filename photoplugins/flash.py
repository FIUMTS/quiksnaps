from .photoExceptions import nextClassException
import pygame
import time
import sys
from datetime import datetime, timedelta


class flash:

    def __init__(self):
        self.time = None

    def run(self, display = None, events = None):

        if self.time == None:
            self.time = datetime.now()

        if display == None:
            print("No pygame in step 2")
            pygame.quit()

        display.fill((255,255,255))
        print("Step 2")
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        timetest = (datetime.now() - self.time)/timedelta(microseconds=1)

        if timetest > 800000:
            pygame.event.clear()
            raise nextClassException("Moving on from Step 2.")

    def __str__(self):
        return "Flash, smile!"
