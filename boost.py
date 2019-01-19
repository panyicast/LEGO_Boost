from pylgbst.movehub import *
from pylgbst.constants import COLORS
from time import sleep



def callback_tilt_sensor(pitch, roll, yaw):
    # print("Pitch: %s / Roll: %s / Yaw: %s" % (pitch, roll, yaw))
    if pitch!='':
        Boost.pitch = pitch
    if roll!='':
        Boost.roll = roll
    if yaw!='':
        Boost.yaw = yaw


def callback_motor_A(angle):
    # print("Angle: %s" % angle)
    if angle != '':
        Boost.angle_motor_A = angle

def callback_motor_B(angle):
    # print("Angle: %s" % angle)
    if angle != '':
        Boost.angle_motor_B = angle

def callback_motor_external(angle):
    # print("Angle: %s" % angle)
    if angle != '':
        Boost.angle_motor_external = angle


def callback_color_distance_sensor(clr, distance):
    # print("Color: %s / Distance: %s" % (clr, distance))
    if distance != '':
        Boost.distance = distance
    if clr != '':
        Boost.color = clr

def callback_button(is_pressed):
    # print("Btn pressed: %s" % is_pressed)
    if is_pressed != '':
        Boost.is_pressed = is_pressed

def callback_voltage(value):
    # print("Voltage: %s" % value)
    if value != '':
        Boost.voltage = value



class Boost():
    pitch = 0
    roll = 0
    yaw = 0
    angle_motor_A = 0
    angle_motor_B = 0
    angle_motor_external = 0
    distance = 100
    color = 0
    is_pressed = 0
    voltage = 0
    
    def __init__(self):
        self.hub = MoveHub()
        self.hub.tilt_sensor.subscribe(callback_tilt_sensor, mode=TiltSensor.MODE_3AXIS_FULL)
        self.hub.motor_A.subscribe(callback_motor_A, mode=EncodedMotor.SENSOR_ANGLE)
        self.hub.motor_B.subscribe(callback_motor_B, mode=EncodedMotor.SENSOR_ANGLE)
        self.hub.motor_external.subscribe(callback_motor_external, mode=EncodedMotor.SENSOR_ANGLE)
        self.hub.button.subscribe(callback_button)
        self.hub.color_distance_sensor.subscribe(callback_color_distance_sensor, mode=ColorDistanceSensor.COLOR_DISTANCE_FLOAT)
        self.hub.voltage.subscribe(callback_voltage)

    def MoveForward(self, time=1):
        self.hub.motor_AB.timed(time,0.5,0.5)
        # sleep(time/2)

    def MoveBack(self, time=0.3):
        self.hub.motor_AB.timed(time, -0.5, -0.5)
        sleep(time)

    def TurnRight(self):
        self.hub.motor_AB.angled(200, 0.8, -0.8)
        sleep(0.1)

    def TurnLeft(self):
        self.hub.motor_AB.angled(200, -0.8, 0.8)
        sleep(0.1)
    
    def External_motor_Turn(self,angle):
        self.hub.motor_external.angled(angle)

    def Set_LED_Color(self,color):
        self.hub.led.set_color(color)

    def Blink_LEDColor(self):
        for color in COLORS:
            self.Set_LED_Color(color)
            # sleep(0.05)

    def Stop(self):
        self.hub.motor_AB.stop()
        

    def Disconnet(self):
        self.hub.tilt_sensor.unsubscribe(callback_tilt_sensor)
        self.hub.motor_A.unsubscribe(callback_motor_A)
        self.hub.motor_B.unsubscribe(callback_motor_B)
        self.hub.motor_external.unsubscribe(callback_motor_external)
        self.hub.button.unsubscribe(callback_button)
        self.hub.color_distance_sensor.unsubscribe(callback_color_distance_sensor)
        self.hub.voltage.unsubscribe(callback_voltage)       
