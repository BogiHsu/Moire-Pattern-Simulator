import matplotlib.pyplot as plt
import numpy as np

def line(shift, plt):
	return
	

plt.figure(figsize=(8, 8))
plt.ion()

step = 45
index = -1*step
while True:
	shift = step-abs(index)
	
	plt.cla()
	plt.title('A')
	plt.grid(True)

	plt.xlabel('X')
	plt.xlim(-12, 12)
	plt.xticks([])
	plt.ylabel('Y')
	plt.ylim(-12, 12)
	plt.yticks([])

	line(shift, plt)

	plt.pause(1e-20)
	index = -1*step if index == step-1 else index+1

plt.ioff()
plt.show()
