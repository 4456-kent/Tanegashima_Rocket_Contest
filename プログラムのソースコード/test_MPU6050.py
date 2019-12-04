import wiringpi as pi
import time
import mpu6050

SAMPLING_RATE=10    #[Hz]

mpu6050_addr=0x68

pi.wiringPiSetupGpio()

i2c=pi.I2C()
acceleration=mpu6050.mpu6050(i2c,mpu6050_addr)
acceleration.setup()

while True:
    (acc_x,acc_y,acc_z,temp,gyro_x,gyro_y,gyro_z)=acceleration.get_value()

    print(acc_x,acc_y,acc_z,temp,gyro_x,gyro_y,gyro_z)
    time.sleep(1/SAMPLING_RATE)

