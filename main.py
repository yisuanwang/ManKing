import pygame
import time
from pygame.locals import *
from Man import Man

is_Key_pressed={pygame.K_ESCAPE:False,pygame.K_a:False,pygame.K_d:False,pygame.K_w:False,pygame.K_s:False,pygame.K_LEFT:False,pygame.K_RIGHT:False,pygame.K_UP:False,pygame.K_DOWN:False,pygame.K_j:False,pygame.K_k:False,pygame.K_l:False,pygame.K_1:False,pygame.K_2:False,pygame.K_3:False}


def main():
    screen = pygame.display.set_mode((960, 540))  # 宽 高
    # 设定背景图片
    bkg = pygame.image.load('./res/bkg/bkg1_.png')
    # 设置窗口title
    pygame.display.set_caption('ManKing - 人类之王')
    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./res/bgm/pubg_snow.mp3')
    pygame.mixer.music.set_volume(1)  # 设置背景音乐
    pygame.mixer.music.play(-1)  # 无限循环
    # 载入玩家1图片
    player1 = Man(0, 360, '', True, screen)
    player2 = Man(800, 360, '', False, screen)
    while True:
        time.sleep(0.02)
        # 获取键盘事件
        eventlist=pygame.event.get()
        # 判断按键
        for i_event in eventlist:
            if i_event==QUIT:
                print('QUIT')
                pygame.quit()
                pass
            elif i_event.type==KEYDOWN:
                #按下按键
                if i_event.key==pygame.K_a or i_event.key==pygame.K_d :
                    player1.set_run()
                    pass
                if i_event.key==pygame.K_LEFT or i_event.key==pygame.K_RIGHT :
                    player2.set_run()
                    pass
                is_Key_pressed[i_event.key]=True
                pass
            elif i_event.type==KEYUP:
                if i_event.key==pygame.K_a or i_event.key==pygame.K_d :
                    player1.set_stand()
                    pass
                if i_event.key==pygame.K_LEFT or i_event.key==pygame.K_RIGHT :
                    player2.set_stand()
                    pass
                is_Key_pressed[i_event.key]=False
                pass
            pass
        if is_Key_pressed[pygame.K_ESCAPE] == True:
            print('esc')
            exit()
            pass
        if is_Key_pressed[pygame.K_a] == True:
            print('p1 left')
            player1.move_left()
            pass
        if is_Key_pressed[pygame.K_LEFT] == True:
            print('p2 left')
            player2.move_left()
            pass
        if is_Key_pressed[pygame.K_d] == True:
            print('p1 right')
            player1.move_right()
            pass
        if is_Key_pressed[pygame.K_RIGHT] == True:
            print('p2 right')
            player2.move_right()
            pass
        if is_Key_pressed[pygame.K_w] == True:
            print('p1 up')
            player1.jump()
            pass
        if is_Key_pressed[pygame.K_UP] == True:
            print('p2 up')
            player2.jump()
            pass
        if is_Key_pressed[pygame.K_s] == True:
            print('p1 down')
            player1.move_down()
            pass
        if is_Key_pressed[pygame.K_DOWN] == True:
            print('p2 down')
            player2.move_down()
            pass
        if is_Key_pressed[pygame.K_j] == True:
            print('p1 j')
            player1.doability_1()
            pass
        if is_Key_pressed[pygame.K_k] == True:
            print('p1 k')
            player1.doability_2()
            pass
        if is_Key_pressed[pygame.K_l] == True:
            print('p1 l')
            pass
        if is_Key_pressed[pygame.K_1] == True:
            print('p2 1')
            player2.doability_1()
            pass
        if is_Key_pressed[pygame.K_2] == True:
            player2.doability_2()
            print('p2 2')
            pass
        if is_Key_pressed[pygame.K_3] == True:
            print('p2 3')
            pass

        # 背景必须重新绘制 不然人物图片会重叠
        screen.blit(bkg, (0, 0))  # 居中显示
        # 绘制玩家1
        print('x1={}  y1={}'.format(player1.get_x(),player1.get_y()))

        screen.blit(player1.get_show_status(), (player1.get_x(),player1.get_y()))
        screen.blit(player2.get_show_status(), (player2.get_x(), player2.get_y()))
        pygame.display.update()# 更新显示

        pass
    pass

if __name__=='__main__':
    main()
    pass