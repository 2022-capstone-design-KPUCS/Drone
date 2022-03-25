import djitellopy as tello
import KeyPressModule as kp


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

