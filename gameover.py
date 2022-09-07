import pygame
from settings import *

class GameOver:
    def __init__(self, restart):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.attribute = ['yes', 'no']
        self.font_title = pygame.font.Font(UI_FONT, UI_FONT_TITLE_SIZE)
        self.font_sub = pygame.font.Font(UI_FONT, UI_FONT_SUBHEADING_SIZE)
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.attribute_nr = 2

        # display setup 
        self.bg = pygame.Surface(self.display_surface.get_size())
        self.height = self.display_surface.get_size()[1] * 0.7
        self.width = self.display_surface.get_size()[0] // 10
        self.full_width = self.display_surface.get_size()[0]
        self.top_rect = pygame.Rect(0,0,self.full_width,self.height)
        self.create_items()

        # selection system 
        self.selection_index = 0
        self.selection_duration_cooldown = 300
        self.selection_time = None
        self.can_move = True

        # game state
        self.restart = restart
    
    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT]:
                if not self.selection_index >= self.attribute_nr - 1:
                    self.selection_index += 1
                else:
                    self.selection_index = 0
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT]:
                if not self.selection_index <= 0:
                    self.selection_index -= 1
                else:
                    self.selection_index = self.attribute_nr - 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_RETURN]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                if self.selection_index == 0:
                    self.restart()
                else:
                    pass
                

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()

            if current_time - self.selection_time >= self.selection_duration_cooldown:
                self.can_move = True

    def display_name(self):
        top_padding = pygame.math.Vector2(0, self.display_surface.get_size()[1]*0.2)

        # title
        title_surf = self.font_title.render('GAME OVER',False,TEXT_COLOR)
        title_rect = title_surf.get_rect(midtop = self.top_rect.midtop + top_padding)

        # sub heading
        sub_surf = self.font_sub.render('RETRY?',False,TEXT_COLOR)
        sub_rect = sub_surf.get_rect(midtop = title_rect.midbottom + pygame.math.Vector2(0,20))

        # draw
        self.display_surface.blit(title_surf, title_rect)
        self.display_surface.blit(sub_surf, sub_rect)

    def create_items(self):
        self.item_list = []
        button_height = 60

        increment = self.full_width // self.attribute_nr

        for item in range(self.attribute_nr):
            left = (item * increment) + (increment - self.width) // 2
            top = self.display_surface.get_size()[1] * 0.7
            item = Item(left, top, self.width, button_height, item, self.font)
            self.item_list.append(item)

    def display(self):
        self.input()
        self.selection_cooldown()

        self.bg.set_alpha(128)               
        self.bg.fill('black')           
        self.display_surface.blit(self.bg, (0,0)) 

        self.display_name()

        for index, item in enumerate(self.item_list):
            name = self.attribute[index]
            item.display(self.display_surface, self.selection_index,name)

class Item:
    def __init__(self,l,t,w,h,index,font):
        self.rect = pygame.Rect(l,t,w,h)
        self.index = index
        self.font = font

    def display_name(self, surface, name, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        title_surf = self.font.render(name,False,color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))

        surface.blit(title_surf, title_rect)

    def display(self, surface, selection_num, name):
        selected = self.index == selection_num

        if selected :
            pygame.draw.rect(surface,UPGRADE_BG_COLOR_SELECTED,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect, 3)
        else:
            pygame.draw.rect(surface,UI_BG_COLOR,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect, 3)

        self.display_name(surface, name, selected)


