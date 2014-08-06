import spidev

led_count = 32
color_count = 3

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 12000000

gamma = bytearray(256)
for i in range(256):
	gamma[i] = 0x80 | int(pow(float(i) / 255.0, 2.5) * 127.0 + .5)

leds = [[0] * color_count] * led_count

def main():
	set(5, red)

def set(index, color):
	leds[index] = color
	update()

def update():
	for x in range(led_count):
		spi.xfer2([gamma[i] for i in leds[x]])
	spi.xfer2([0x00,0x00,0x00])
	spi.xfer2([0x00])

green = [255, 0, 0]
yellow = [255, 255, 0]
red = [0, 255, 0]
purple = [0, 255, 255]
blue = [0, 0, 255]
cyan = [0, 255, 255]
		
if __name__ == '__main__':
	main()