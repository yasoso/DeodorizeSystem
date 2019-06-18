#coding:utf-8

import spidev
import RPi.GPIO as GPIO
#import pygame.mixer
import time

import sys, json, numpy as np


threshold = 500 #匂いの閾値

#pygame.mixer.init()
#pygame.mixer.music.load("/home/pi/data/kussa.mp3") #mp3データを変えるときはここを変更

GPIO.setmode(GPIO.BCM)
gp_servo = 4
GPIO.setup(gp_servo, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


#servomotorの設定
servo = GPIO.PWM(gp_servo, 50)
servo.start(0.0)


spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
spi.bits_per_word=8

dummy = 0xff
start = 0x47
sgl = 0x20

ch0 = 0x00

msbf = 0x08

flag = 0        #閾値を超えたかどうか
startflag = 0   #起動時の匂い検知の値が閾値を超えている場合の誤爆防止

tmp = 1

#匂い計測
def measure(ch):
    ad = spi.xfer2( [ (start + sgl + ch + msbf), dummy ] )
    val = ((ad[0] & 0x03) << 8) + ad[1]
    return val

#node.jsから値を受ける
def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

try:
    while 1:
        time.sleep(0.237)

        GPIO.output(22,True)
        time.sleep(0.003)

        ch0_val = measure(ch0)
        Val = 1023 - ch0_val
        time.sleep(0.002)
        GPIO.output(22,False)
        
        GPIO.output(17,True)
        time.sleep(0.008)
        GPIO.output(17,False)

        print(Val, flag, startflag)

        #node.jsから引数を受ける
        #if tmp == 0:
        #   lines = read_in()       #get flag as array from read_in()
        #   np.lines = np.array(lines)
        #   print(np.lines)


        if Val < threshold:
             startflag += 1
        if Val > threshold and startflag > 0 and flag == 0:
             flag = 1
             servo.ChangeDutyCycle(2.5) #右に30度
             time.sleep(0.5)
             servo.ChangeDutyCycle(6.0625)#元に戻る
             time.sleep(0.5)
             servo.start(0.0)

        
        if Val < threshold and flag == 1:
             flag = 0


except KeyboardInterrupt:
    pass

#pygame.mixer.music.stop()
spi.close()
GPIO.cleanup()

