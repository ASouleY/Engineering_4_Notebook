import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

lsm303 = Adafruit_LSM303.LSM303()

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

padding = 2
shape_width = 20
top = padding
bottom = height-padding

x = padding

font = ImageFont.load_default()


while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

    draw.text((x, top),    'Accel (m/s^2) X={0}'.format((accel_x/100), accel_y, accel_z, mag_x, mag_y, mag_z),  font=font, fill=255)
    draw.text((x, top+8),    'Accel (m/s^2) Y={1}'.format(accel_x, accel_y/100, accel_z, mag_x, mag_y, mag_z),  font=font, fill=255)
    draw.text((x, top+16),    'Accel (m/s^2) z={2}'.format(accel_x, accel_y, accel_z/100, mag_x, mag_y, mag_z),  font=font, fill=255)
    disp.image(image)
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    time.sleep(.5)
    
