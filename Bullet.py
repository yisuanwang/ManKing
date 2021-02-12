import threading
import os
import time
import pygame
from pygame.locals import *
import Man

class Bullet:
    # 这是子弹类

    # 初始化数据是 子弹对象的坐标 方向和速度 伤害 运动时的动画目录 boom时的动画目录
    def __init__(self,x,y,direction,speed,injure,p_move,p_move_,p_boom,sc):
        self.__x=x
        self.__y=y
        self.__direction=direction
        self.__speed=speed
        self.__injure=injure
        self.__p_move=p_move
        self.__p_move_= p_move_
        self.__p_boom=p_boom
        self.__list_move = os.listdir(p_move)
        self.__list_boom = os.listdir(p_boom)
        self.__list_move_ = os.listdir(p_move_)
        self.__screen=sc
        pass


    # move
    @staticmethod
    def _move_run(self):
        v = self.__speed if self.__direction else -1 * self.__speed
        show_pic=1
        while True:
            if self.__direction:
                show_pic = pygame.image.load(self.__p_move + '/' + self.__list_move[0])
                self.__x+=v
                pass
            else:
                show_pic = pygame.image.load(self.__p_move_ + '/' + self.__list_move_[0])
                self.__x += v
                pass
            if self.__x >= 800 or self.__x <= 0:
                break
            self.__screen.blit(show_pic, (self.__x, self.__y))
            pygame.display.update()  # 更新显示
            time.sleep(0.02)
            pass
        self._boom_run(self)
        pass
    def Fire(self):
        print('in bullet Fire()')
        thread = threading.Thread(target=Bullet._move_run, args=(self,))
        thread.start()
        pass

    # move
    @staticmethod
    def _boom_run(self):
        for show_pic in self.__list_boom:
            self.__screen.blit(pygame.image.load(self.__p_boom+'/'+show_pic) , (self.__x-30, self.__y-30))
            pygame.display.update()  # 更新显示
            time.sleep(0.02)
        pass

    def Boom(self):
        thread = threading.Thread(target=Bullet._move_run, args=(self,))
        thread.start()
        pass

    pass
