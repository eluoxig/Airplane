import pygame

pygame.init()
#创建游戏窗口
screen = pygame.display.set_mode((480,700))

#绘制背景图像
# 加载图像数据 blit 绘制图像  update  更新屏幕

bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))


hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(170,500))
pygame.display.update()

clock = pygame.time.Clock()
#游戏循环，意味游戏的开始
hero_rect=pygame.Rect(170,300,102,206)
while True:
    clock.tick(60)
    # 修改飞机位置
    hero_rect.y -= 1
    #判断飞机的位置
    if hero_rect.y <= 0:
        hero_rect.y=700
    # 重新绘制背景图片
    screen.blit(bg, (0, 0))
    # 调用blit 方法绘制图像
    screen.blit(hero, hero_rect)
    pygame.display.update()
    pass


pygame.quit()