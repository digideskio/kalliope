# -*- coding: utf-8 -*-
import logging

import playsound
import pygame

logging.basicConfig()
logger = logging.getLogger("kalliope")

import vlc


class PlaySoundPlayer(object):
    """
    This Class is representing the Player Object used to play the all sound of the system.
    """

    @classmethod
    def play(cls, file_path):
        # pygame.init()
        freq = 44100  # audio CD quality
        bitsize = -16  # unsigned 16 bit
        channels = 2  # 1 is mono, 2 is stereo
        buffer = 4096  # number of samples (experiment to get right sound)
        # pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.init()
        clock = pygame.time.Clock()
        sounda = pygame.mixer.Sound(file_path)
        print("Music file {} loaded!".format(file_path))
        sounda.play()
        while pygame.mixer.get_busy():
            # print "Playing..."
            clock.tick(1000)
