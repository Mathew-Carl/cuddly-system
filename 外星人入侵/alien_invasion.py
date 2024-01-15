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
            #监听鼠标与键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #每次循环重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60)#帧率控制
            
if __name__ == "__main__":
    #创建实例并运行
    ai = AlienInvasion()
    ai.run_game()