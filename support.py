from csv import reader
from os import walk, scandir
import pygame


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            fullpath = path + '/' + image
            image_surf = pygame.image.load(fullpath).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

def import_folder_asc(path):
    surface_list = []

    img_len = len([entry for entry in scandir(path) if entry.is_file()]) - 1
    for i in range(img_len):
        fullpath = path + '/' + f'{i:02d}' + '.png'
        image_surf = pygame.image.load(fullpath).convert_alpha()
        surface_list.append(image_surf)

    # alternative
    # for _,__,img_files in walk(path):
    #     surface_list = len(img_files)*[None]
    #     for image in img_files:
    #         fullpath = path + '/' + image
    #         image_surf = pygame.image.load(fullpath).convert_alpha()
    #         surface_list[int(image[0:2])] = image_surf
            
    return surface_list

def import_folder_asc_alt(path):
    surface_list = []

    img_len = len([entry for entry in scandir(path) if entry.is_file()]) - 1
    for i in range(img_len):
        fullpath = path + '/' + 'leaf1_' + f'{i:05d}' + '.png'
        image_surf = pygame.image.load(fullpath).convert_alpha()
        surface_list.append(image_surf)

    return surface_list
