import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 6 # 핀 번호 GPIO6 의미, 빵판하단 16번 홀
GPIO.setup(led, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.
# 초음파제어
trig = 20       # 빵판으로는 상단19번
echo = 16       # 빵판으로는 상단18번
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
def ledOnOff(onOff):
        global led
        GPIO.output(led, onOff)
def measureDistance():
        global trig
        global echo
        time.sleep(0.5)
        GPIO.output(trig, True) # 신호 1 발생
        time.sleep(0.00001) # 짧은 시간을 나타내기 위함
        GPIO.output(trig, False) # 신호 0 발생
        while(GPIO.input(echo) == 0):
                pass
        pulse_start = time.time() # 신호 1을 받았던 시간
        while(GPIO.input(echo) == 1):
                pass
        pulse_end = time.time() # 신호 0을 받았던 시간
        pulse_duration = pulse_end - pulse_start
        return 340*100/2*pulse_duration
