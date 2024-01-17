import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):#初始化游戏并创建游戏资源
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#显示窗口大小,注意是元组
        pygame.display.set_caption("Alien Invasion")#窗口标题

        self.ship = Ship(self)
        
    def run_game(self):
        #开始游戏的主循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)#帧率控制
            
    def _check_events(self):
            #监听鼠标与键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit() 

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False       
  
         

    def _update_screen(self):
            #每次循环重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #最近绘制的屏幕可见
            pygame.display.flip()
    

if __name__ == "__main__":
    #创建实例并运行
    ai = AlienInvasion()
    ai.run_game()











































































































































# 全屏模式(待更新)
# self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
# self.settings.screen_width = self.screen.get_rect().width
# self.settings.screen_height = self.screen.get_rect().height