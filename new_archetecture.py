import rpyc
print(rpyc.__version__)
ev3_host_1 = "192.168.43.83"
ev3_host_2 = "192.168.43.238"
ev3_host_3 = "192.168.43.126"

ev3_connection_1 = rpyc.classic.connect(ev3_host_1)
ev3_connection_2 = rpyc.classic.connect(ev3_host_2)
ev3_connection_3 = rpyc.classic.connect(ev3_host_3)


ev3dev2_motor_1 = ev3_connection_1.modules['ev3dev2.motor']
ev3dev2_motor_2 = ev3_connection_2.modules['ev3dev2.motor']
ev3dev2_motor_3 = ev3_connection_3.modules['ev3dev2.motor']

ev3dev2_sensor_1 = ev3_connection_1.modules['ev3dev2.sensor']
ev3dev2_sensor_2 = ev3_connection_2.modules['ev3dev2.sensor']
ev3dev2_sensor_3 = ev3_connection_3.modules['ev3dev2.sensor']


ev3dev2_sensor_lego_1 = ev3_connection_1.modules['ev3dev2.sensor.lego']
ev3dev2_sensor_lego_2 = ev3_connection_2.modules['ev3dev2.sensor.lego']
ev3dev2_sensor_lego_3 = ev3_connection_3.modules['ev3dev2.sensor.lego']



# mWind = MediumMotor('outD')  
# motor_b = LargeMotor('outB')  
# motor_c = LargeMotor('outC')
# cl = ColorSensor('in4')
# ts =  TouchSensor('in3')
# gy = GyroSensor('in2')

#Установщик
mWind = ev3dev2_motor_1.MediumMotor(ev3dev2_motor_1.OUTPUT_D)  
mb_1 = ev3dev2_motor_1.LargeMotor(ev3dev2_motor_1.OUTPUT_B)  
mc_1 = ev3dev2_motor_1.LargeMotor(ev3dev2_motor_1.OUTPUT_C)  
cl = ev3dev2_sensor_lego_1.ColorSensor(ev3dev2_sensor_1.INPUT_2)
ts =  ev3dev2_sensor_lego_1.TouchSensor(ev3dev2_sensor_1.INPUT_3)
gy = ev3dev2_sensor_lego_1.GyroSensor(ev3dev2_sensor_1.INPUT_2)

#Установщик движение 
ma_2 = ev3dev2_motor_2.LargeMotor(ev3dev2_motor_2.OUTPUT_A)
mb_2 = ev3dev2_motor_2.LargeMotor(ev3dev2_motor_2.OUTPUT_B)  
mc_2 = ev3dev2_motor_2.LargeMotor(ev3dev2_motor_2.OUTPUT_C)
md_2 = ev3dev2_motor_2.LargeMotor(ev3dev2_motor_2.OUTPUT_D)  

GY = ev3dev2_sensor_lego_2.GyroSensor(ev3dev2_sensor_2.INPUT_1)
T = ev3dev2_sensor_lego_2.TouchSensor(ev3dev2_sensor_2.INPUT_3)
Sony1 = ev3dev2_sensor_lego_2.UltrasonicSensor(ev3dev2_sensor_2.INPUT_2)





while True:
    #mc_1.run_direct(duty_cycle_sp = 100)
    mb_1.run_direct(duty_cycle_sp = -100)













