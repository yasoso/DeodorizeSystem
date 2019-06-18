#coding:utf-8
import csv
import datetime
import spidev
import RPi.GPIO as GPIO

#import pygame.mixer
import time

threshold = 500 #閾値を変えるときはここを変更

#pygame.mixer.init()
#pygame.mixer.music.load("/home/pi/data/kussa.mp3") #mp3データを変えるときはここを変更
f = open("data.csv","w")

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

spi = spidev.SpiDev()

spi.open(0,0)

spi.max_speed_hz=1000000

spi.bits_per_word=8

dummy = 0xff
start = 0x47
sgl = 0x20

ch0 = 0x00

msbf = 0x08

def measure(ch):
    ad = spi.xfer2( [ (start + sgl + ch + msbf), dummy ] )
    val = ((ad[0] & 0x03) << 8) + ad[1]
    return val

d = datetime.datetime.today() 
print(d, type(d))
count =0
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
        

        print(Val)
        count+=1
        th = [count,Val]
        writer = csv.writer(f,lineterminator="\n")
        writer.writerow(th)
        

        #if Val > threshold:
           # pygame.mixer.music.play(0)

except KeyboardInterrupt:
    pass

#pygame.mixer.music.stop()
f.close()
spi.close()

