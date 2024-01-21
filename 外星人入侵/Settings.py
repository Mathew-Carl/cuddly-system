class Settings:
    def __init__(self):
        #初始化游戏设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


        self.ship_speed = 1.5
        self.ship_limit = 3


        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        '''无限子弹模式? 割草无双 超大子弹多种武器?'''

        '''极速模式? 更改子弹以及飞船速度, 或者开放自定义端口?'''
        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction 1为右面 -1为左面
        self.fleet_direction = 1

