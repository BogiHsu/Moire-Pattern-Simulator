import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import math

window_length = 8
def line(angle, plt):
	wave_length = 0.5
	x_distance_mm = wave_length / math.cos(angle * math.pi / 180)
	per_cm_x_mm = 10 / x_distance_mm
	wave_length = x_distance_mm * math.cos(angle * math.pi / 180)
	delta_y = wave_length / 2 / math.sin(angle * math.pi / 180)
	wave_num = int(window_length * 10 / x_distance_mm)
	line_length = 10

	k = math.sin(angle * math.pi / 180) * line_length / 2
	for i in range(wave_num):
		line1 = [(i / per_cm_x_mm  - k, window_length / 2 - line_length / 2), (i / per_cm_x_mm + k, window_length / 2 + line_length / 2)]
		(line1_xs, line1_ys) = zip(*line1)
		plt.plot(line1_xs, line1_ys, 'k-', linewidth=1)

	for i in range(wave_num):
		line1 = [(i / per_cm_x_mm + k, window_length / 2 - line_length / 2), (i / per_cm_x_mm - k, window_length / 2 + line_length / 2)]
		(line1_xs, line1_ys) = zip(*line1)
		plt.plot(line1_xs, line1_ys, 'k-', linewidth=1)

	return wave_length, delta_y
	

plt.figure(figsize=(6, 6))
plt.ion()

step = 44
index = -1*step
while True:
	angle = step-abs(index)+1
	plt.cla()
	plt.title('A')
	plt.grid(True)

	plt.xlabel('X')
	plt.xlim(0, window_length)
	plt.xticks([])
	plt.ylabel('Y')
	plt.ylim(0, window_length)
	plt.yticks([])

	wave_length, delta_y = line(angle, plt)
	print('angle:%02d,'%angle, 'lambda:%4.1f,'%wave_length, 'delta y:%6.3f'%delta_y)

	plt.pause(1e-20)
	index = -1*step if index >= step-1 else index+2

plt.ioff()
plt.show()
