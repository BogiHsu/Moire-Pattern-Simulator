import matplotlib.pyplot as plt
import numpy as np

def circle(shift, plt):
	theta = np.arange(0, 2*np.pi, 2*np.pi/100)
	theta = np.append(theta, [2*np.pi])
	x = np.cos(theta)
	y = np.sin(theta)
	v = np.linspace(0, 8, 46)
	for r in v:
		plt.plot(r*x-0.2*shift, r*y, '0.0')
	
	for r in v:
		plt.plot(r*x+0.2*shift, r*y, '0.0')

plt.figure(figsize=(10, 5))
plt.ion()

step = 40
index = -1*step
while True:
	shift = step-abs(index)
	
	plt.cla()
	plt.title('B1')
	plt.grid(True)

	plt.xlabel('X')
	plt.xlim(-18, 18)
	plt.xticks([])
	plt.ylabel('Y')
	plt.ylim(-9, 9)
	plt.yticks([])

	circle(shift, plt)

	plt.pause(1e-50)
	index = -1*step if index == step-1 else index+1

plt.ioff()
plt.show()