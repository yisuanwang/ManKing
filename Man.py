import threading
import os
import time
import pygame
from pygame.locals import *
# player 对象
# (960,540)
from Bullet import Bullet


class Man:
    # 方向默认向右为True
    __direction=True
    _s_stand,_s_run,_s_jump,_s_short,_s_long=1,2,3,4,5
    _is_stand, _is_run, _is_jump, _is_short, _is_long = True,False,False,False,False
    __status=_s_stand # 默认状态 为stand
    # 设置当前状态
    def set_run(self):
        self.__status = Man._s_run
        pass
    def set_stand(self):
        self.__status = Man._s_stand
        pass

    __p_stand  = os.listdir('./res/man/stand')#站立时的图片资源路径
    __p_run    = os.listdir('./res/man/run')#跑动图片资源
    __p_jump   = os.listdir('./res/man/jump')#跳跃图片资源
    __p_short_a= os.listdir('./res/man/short_a')#近战资源图片
    __p_long_a = os.listdir('./res/man/long_a') # 远攻图片资源

    __p_stand_ = os.listdir('./res/man/stand_')  # 站立时的图片资源路径
    __p_run_ = os.listdir('./res/man/run_')  # 跑动图片资源
    __p_jump_ = os.listdir('./res/man/jump_')  # 跳跃图片资源
    __p_short_a_ = os.listdir('./res/man/short_a_')  # 近战资源图片
    __p_long_a_ = os.listdir('./res/man/long_a_')  # 远攻图片资源

    __show_status=pygame.image.load('./res/man/stand/'+__p_stand[0]) #当前展示的图片帧
    # 根据状态实时设置人物的动画帧
    @staticmethod
    def _set_show_status(self):
        index_stand,index_run,index_jump,index_short,index_long=0,0,0,0,0
        while True:
            if self.__status==Man._s_stand:
                if self.__direction :
                    self.__show_status=pygame.image.load('./res/man/stand/'+self.__p_stand[index_stand])
                    pass
                else:
                    self.__show_status = pygame.image.load('./res/man/stand_/' + self.__p_stand_[index_stand])
                    pass
                index_stand+=1
                index_stand%=len(self.__p_stand)
                pass
            elif self.__status==Man._s_run:
                if self.__direction:
                    self.__show_status = pygame.image.load('./res/man/run/' + self.__p_run[index_run])
                    pass
                else:
                    self.__show_status = pygame.image.load('./res/man/run_/' + self.__p_run_[index_run])
                    pass
                index_run += 1
                index_run %= len(self.__p_run)
                pass
            elif self.__status==Man._s_jump:
                if self.__direction:
                    self.__show_status = pygame.image.load('./res/man/jump/' + self.__p_jump[index_jump])
                    pass
                else:
                    self.__show_status = pygame.image.load('./res/man/jump_/' + self.__p_jump_[index_jump])
                    pass
                index_jump += 1
                index_jump %= len(self.__p_jump)
                pass
            # elif self.__status==Man._s_short:
            #     self.__show_status = pygame.image.load('./res/man/short_a/' + self.__p_short_a[index_short])
            #     index_short += 1
            #     index_short %= len(self.__p_short_a)
            #     pass
            time.sleep(0.15)
        pass
    def get_show_status(self):
        return self.__show_status
    __color=''#玩家颜色
    def __init__(self,x,y,color,d,screen):
        self.__x=x
        self.__y=y
        self.__color=color
        self.__direction = d
        self.__screen=screen
        thread = threading.Thread(target=Man._set_show_status, args=(self,))
        thread.start()
        pass
    # 玩家初始位置
    __x,__y=100,360
    __hp=100
    __mp=100
    __base_y=360 # 底部位置
    def get_x(self):
        return self.__x
    def set_x(self,x):
        self.__x=x
        pass
    def get_y(self):
        return self.__y
    def set_y(self,y):
        self.__y=y
        pass
    def get_hp(self):
        return self.__hp
    def set_hp(self,hp):
        self.__hp=hp
        pass
    def get_mp(self):
        return self.__mp
    def set_mp(self,mp):
        self.__mp=mp
        pass
    # 每次移动的步长
    _step=7
    def move_left(self):
        self.__x-=self._step
        self.__x=max(0,self.__x)
        self.__direction=False
        pass
    def move_right(self):
        self.__x += self._step
        self.__x = min(800, self.__x)
        self.__direction = True
        pass
    def move_down(self):
        self.__y += self._step *2
        self.__y = min(self.__base_y, self.__y)
        pass
    # 跳跃初速度 & 加速度
    _jump_v0=-500
    _jump_a=10
    _jump_a2=20
    # 时间微元
    _div_time=0.02
    @staticmethod
    def _jump(self):
        # 通过新线程实现加速度上下的动画效果
        # 初始速度
        v0=self._jump_v0
        a=self._jump_a # 向上
        while True:
            v0+=self._div_time * a
            a+=self._jump_a2
            self.__y+=self._div_time * v0
            print('v={} y={}'.format(v0,self.__y))
            if self.__y > self.__base_y :
                self.__y = self.__base_y
                print('y>base')
                # 此处表示已经落地了
                self.__status = Man._s_stand
                self._is_jump =False
                break
                pass
            time.sleep(self._div_time)
            pass
        pass
    def jump(self):
        if self.__status==Man._s_jump or self._is_jump:
            return
        self.__status = Man._s_jump
        self._is_jump=True
        thread = threading.Thread(target=Man._jump,args=(self,))
        thread.start()
        pass

    # 玩家1技能
    @staticmethod
    def _short(self):
        # 播放一遍动画就可以结束
        if self.__direction:
            for i in self.__p_short_a:
                self.__show_status = pygame.image.load('./res/man/short_a/' + i)
                time.sleep(0.07)
                pass
            pass
        else:
            for i in self.__p_short_a_:
                self.__show_status = pygame.image.load('./res/man/short_a_/' + i)
                time.sleep(0.07)
                pass
            pass
        # 这里只要等待动画播放结束把状态调回去就可以了
        self.set_stand()
        pass
    def doability_1(self):
        if self.__status == Man._s_short:
            return
        self.__status = Man._s_short
        thread = threading.Thread(target=Man._short,args=(self,))
        thread.start()
        pass

    # 玩家2技能
    @staticmethod
    def _long(self):
        if self.__direction:
            for i in self.__p_long_a:
                self.__show_status = pygame.image.load('./res/man/long_a/' + i)
                time.sleep(0.02)
                pass
            pass
        else:
            for i in self.__p_long_a_:
                self.__show_status = pygame.image.load('./res/man/long_a_/' + i)
                time.sleep(0.02)
                pass
            pass
        bullet=Bullet(self.get_x(),self.get_y()+28,self.__direction,100,10,'./res/bullet/RPG_move/r','./res/bullet/RPG_move/l','./res/bullet/RPG_boom',self.__screen)
        bullet.Fire()
        self.set_stand()
        pass
    def doability_2(self):
        if self.__status == Man._s_long:
            return
        self.__status = Man._s_long
        thread = threading.Thread(target=Man._long, args=(self,))
        thread.start()
        pass

    pass
