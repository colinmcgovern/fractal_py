from tkinter import *

master = Tk()

w = Canvas(master, width=256, height=256)
w.pack()

# Image size (pixels)
WIDTH = 256
HEIGHT = 256

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

MAX_ITER = 20

def mandelbrot(c):
	z = 0
	n = 0
	while abs(z) <= 2 and n < MAX_ITER:
		z = z*z + c
		n += 1
	return n

def _from_rgb(rgb):
	return "#%02x%02x%02x" % rgb


points = {}

for x in range(0, WIDTH):

	points[x] = {}

	for y in range(0, HEIGHT):
		# Convert pixel coordinate to complex number
		c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
		IM_START + (y / HEIGHT) * (IM_END - IM_START))
		# Compute the number of iterations
		m = mandelbrot(c)

		sat = int(255 - int(m * 255 / MAX_ITER))

		points[x][y] = sat

for x in range(0, WIDTH):
	for y in range(0, HEIGHT):

		sat = points[x][y]
		color = _from_rgb((sat,sat,sat))

		x1, y1 = (x - 1), (y - 1)
		x2, y2 = (x + 1), (y + 1)
		w.create_line(x, y, x + 1, y, fill=color)

mainloop()