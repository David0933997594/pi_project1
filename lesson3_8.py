#https://gpiozero.readthedocs.io/en/stable/installing.html
#按下蜂鳴器響,放掉停止聲響

import private
import requests



from gpiozero import Button
from signal import pause
from gpiozero import RGBLED,Buzzer


state = False
counter = 0

def user_press():
    global state,counter
    state = not state
    buzzer.on()
    
    if state == True:
        print("開燈")
        counter += 1
        if counter % 3 == 1:
            led.color=(0,1,0)
        elif counter % 3 == 2:
            led.color=(0,0,1)
        elif counter % 3 == 0:
            led.color=(1,0,0)
            url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttKey}?value1=danger&value2=100'

            r = requests.get(url)
            if r.status_code == 200:
                print("發送成功")

    else:
        print("關燈")
        led.color=(0,0,0)
#停止響
def user_release():
    buzzer.off()

button = Button(18)
led = RGBLED(red=17, green=27, blue=22)
#接25PIN
buzzer = Buzzer(25)

button.when_pressed = user_press
button.when_released = user_release

pause()
