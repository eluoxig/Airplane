import pygame

pygame.init()
#创建游戏窗口
screen = pygame.display.set_mode((482,717))

#绘制背景图像
# 加载图像数据 blit 绘制图像  update  更新屏幕

bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()


while True:
    pass

pygame.quit()