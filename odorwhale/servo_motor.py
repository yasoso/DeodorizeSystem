#!/usr/bin/env python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO4を制御パルスの出力に設定
gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)

#「GPIO4出力」でPWMインスタンスを作成する。
#GPIO.PWM( [ピン番号] , [周波数Hz] )
#SG92RはPWMサイクル:20ms(=50Hz), 制御パルス:0.5ms〜2.4ms, (=2.5%〜12%)。
servo = GPIO.PWM(gp_out, 50)

#パルス出力開始。　servo.start( [デューティサイクル 0~100%] )
#とりあえずゼロ指定だとサイクルが生まれないので特に動かないっぽい？
servo.start(0.0)
#time.sleep(1)

for i in range(1):
#while 1:
    #デューティサイクルの値を変更することでサーボが回って角度が変わる。
    #PWMサイクルが20ms
    #90度なら0.5ms / 20ms = 2.5%
    #servo.ChangeDutyCycle(2.5)
    #time.sleep(0.5)

    #servo.ChangeDutyCycle(7.25)
    #time.sleep(0.5)
    countDown = 3

    while (countDown >= 0):
        time.sleep(0.5)
        print(countDown)
        countDown = countDown - 1
        if countDown == 0:
            time.sleep(0.5)
            print("Action!")
            break
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)

    servo.ChangeDutyCycle(6.0625)
    time.sleep(0.5)

    #servo.ChangeDutyCycle(12)
    #time.sleep(0.5)

    #servo.ChangeDutyCycle(7.25)
    #time.sleep(0.5)

servo.stop()
GPIO.cleanup()
