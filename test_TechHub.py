from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait
from pybricks.pupdevices import ForceSensor

# Initialize the hub.
hub = TechnicHub()
'''
button = ForceSensor(Port.D)

while True:
    # Read all the information we can get from this sensor.
    force = button.force()
    dist = button.distance()
    press = button.pressed()
    touch = button.touched()

    # Print the values
    print("Force", force, "Dist:", dist, "Pressed:", press, "Touched:", touch)

    # Push the sensor button see what happens to the values.

    # Wait some time so we can read what is printed.
    wait(200)

'''
left_motor = Motor(Port.A)
#right_motor = Motor(Port.C)

left_motor.run_angle(500, 400)
print("finished")
#right_motor.run_angle(400, 300)

'''
while True:
    # Read the tilt values.
    pitch, roll = hub.imu.tilt()

    # Print the result.
    print(pitch, roll)
    wait(200)


# Turn the light on and off 5 times.
for i in range(5):

    hub.light.on(Color.RED)
    wait(1000)

    hub.light.on(Color.GREEN)
    wait(1000)

    hub.light.off()
    wait(500)
'''