import boost
from time import sleep

bst = boost.Boost()
try:
    print('start working....')
    bst.Blink_LEDColor()
    while(1):
        dis = bst.distance
        if dis<8:
            print('blocked.....back and turn... distance = ',dis)
            bst.Stop()
            bst.External_motor_Turn(-50)
            sleep(0.05)
            bst.External_motor_Turn(50)
            # bst.Blink_LEDColor()
            bst.MoveBack()
            bst.TurnLeft()
        else:
            bst.MoveForward()


finally:
    bst.Disconnect()
