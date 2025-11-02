class Setting:
    def __init__(self):
        # 屏幕相关配置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船相关配置
        self.ship_speed = 1.5

        # 子弹相关配置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allow = 3
