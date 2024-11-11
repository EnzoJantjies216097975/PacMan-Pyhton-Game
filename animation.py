# Class responsible for accessing the sprites of the game

from os import walk
import pygame

def import_sprite(path): 
    surface_list = []
    for _, __, img_file in walk(path):
            for image in img_file:
                full_path = f"{path}/{image}"
                img_surface = pygame.image.load(full_path).convert_alpha()
                surface_list.append(img_surface)
            return surface_list

'''
 The import_sprite() function takes one argument, path, which is the directory path where the sprite images are located. 
 The surface_list is an empty list that will hold the loaded image surfaces.

 The os.walk(path) is used to traverse the directory specified by the path and returns a generator that yields a tuple for each directory it visits. 
 We use _ and __ as throwaway variables to denote the current directory path and its subdirectories. img_file is a list of filenames in the current directory.

 For each image filename in img_file, the full path to the image file is constructed by combining the path with an image. 
 The pygame.image.load() function is then used to load the image from this full path into an image surface (img_surface). 
 The .convert_alpha() method converts the image to a format that is optimized for display on the screen with per-pixel transparency, 
 then the loaded image surface (img_surface) is then appended to the surface_list.
 '''