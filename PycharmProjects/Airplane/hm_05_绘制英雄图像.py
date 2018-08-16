import pygame

pygame.init()
#创建游戏窗口
screen = pygame.display.set_mode((480,700))

#绘制背景图像
# 加载图像数据 blit 绘制图像  update  更新屏幕

bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
from plane_sprites import *

hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(170,500))
pygame.display.update()

clock = pygame.time.Clock()
#游戏循环，意味游戏的开始
hero_rect=pygame.Rect(170,300,102,206)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",3)
#创建精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)


while True:
    clock.tick(60)
    #捕获事件
    #监听事件
    event_list =  pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            print("end game!")
            #卸载所有模块
            pygame.quit()
            exit() # 直接终止当前正在执行的程序
    # 修改飞机位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= 0-hero_rect.height:
        hero_rect.y = 700
    # 重新绘制背景图片
    screen.blit(bg, (0, 0))
    # 调用blit 方法绘制图像
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法，update  draw
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()
    pass


pygame.quit()