import pygame

class Ship:
    #管理飞船的类
    def __init__(self, ai_game):
        #初始化飞船及其位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() 

        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()

        #飞船放入屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        #指定位置放置飞船
        self.screen.blit(self.image, self.rect)