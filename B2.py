import matplotlib.pyplot as plt
import numpy as np

def circle(shift, plt):
	theta = np.arange(0, 2*np.pi, 2*np.pi/100)
	theta = np.append(theta, [2*np.pi])
	x = np.cos(theta)
	y = np.sin(theta)
	v = np.linspace(0, 8, 41)
	for r in v:
		plt.plot(r*x, r*y, '0.0')
	
	for r in v:
		r += 0.01*shift
		plt.plot(r*x, r*y, '0.0')

plt.figure(figsize=(10, 5))
plt.ion()

step = 20
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

	plt.pause(1e-20)
	index = -1*step if index == step-1 else index+1

plt.ioff()
plt.show()