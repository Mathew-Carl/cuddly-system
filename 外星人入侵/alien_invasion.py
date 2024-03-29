import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):#初始化游戏并创建游戏资源
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#显示窗口大小,注意是元组
        pygame.display.set_caption("Alien Invasion")#窗口标题

        #存储游戏统计数据
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        #self._create_fleet()

        self.game_active = False

        #play
        self.play_button = Button(self, "PLAY")
        
    def run_game(self):
        #开始游戏的主循环
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
                
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit() 

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False       
    
    def _check_fleet_edges(self):
        #外星人边缘策略
        for alien in self.aliens.sprites():
            if alien.check_edges() :
                self._change_fleet_direction()
                break

    def _check_bullet_alien_collisions(self):
        #碰撞检测
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.prep_high_score()

        
        if not self.aliens:
            #删除现有子弹并创建新舰队
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _check_aliens_bottom(self):
        #底部检测
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()#像被撞处理即可
                break

    def _check_play_button(self, mouse_pos):
        #play时开始新游戏
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()
            self.game_active = True

        #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()

        #创建新编组
            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _change_fleet_direction(self):
        #向下移动并改变方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        #每次循环重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        #显示得分
        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()#更新屏幕
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        

    def _update_aliens(self):
        #检查是否边缘并更新
        self._check_fleet_edges()
        self.aliens.update()

        #检测碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size      
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x <= (self.settings.screen_width - 2 * alien_width):#余下的空间不少于外星人的两倍
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            #添加一行后
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
            new_alien =Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _fire_bullet(self):
        #创建子弹,并加入编组
        if len(self.bullets) < self.settings.bullets_allowed:#子弹数设置
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    def _ship_hit(self):
        #响应碰撞
        if self.stats.ship_left >= 0:
            #飞船剩余数减一
            self.stats.ship_left -= 1
            self.sb.prep_ship()

            #清空外星人和子弹
            self.bullets.empty()
            self.aliens.empty()

            #新部队和飞船
            self._create_fleet()
            self.ship.center_ship()

            #暂停
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)



if __name__ == "__main__":
    #创建实例并运行
    ai = AlienInvasion()
    ai.run_game()











































































































































'''
全屏模式(待更新)
self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
self.settings.screen_width = self.screen.get_rect().width
self.settings.screen_height = self.screen.get_rect().height

#随机生成地方对象?
from random import randint
random_number = randint(-10, 10)
 '''
