import pygame
from photoplugins.photoExceptions import NextClassException


class PhotoManager:
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super(PhotoManager, self).__new__(self)
            self._instance.classes = []
            pygame.init()
            # Stop double text on touch screens
            pygame.event.set_blocked([pygame.FINGERUP, pygame.FINGERDOWN])
            self._instance.display = pygame.display.set_mode((1080, 1920), pygame.FULLSCREEN)

        return self._instance

    def run(self, session):
        a_class = self.classes[0]
        #print("Running %s" % (a_class))

        try:
            a_class.run(self.display, pygame.event.get(), session)
        except NextClassException:
            a_class = self.classes.pop(0)
            self.classes.append(a_class)

    def register(self, a_class):
        #print(aClass)
        self.classes.append(a_class)
