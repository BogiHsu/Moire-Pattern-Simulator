import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import math


# 该行用于设置chart 的样式，可以注掉

# plt.style.use("mystyle")


window_length = 10
fig = plt.figure(figsize=(window_length/1.72, window_length/1.72))

ax = fig.add_subplot(111)
ax.spines['left'].set_color('none')

ax.spines['bottom'].set_color('none')

ax.spines['right'].set_color('none')

ax.spines['top'].set_color('none')
ax.set_xlim(0, window_length)
ax.set_xticks([])
ax.set_ylim((0, window_length))
ax.set_yticks([])



def circle(plt):
  theta = np.arange(0, 2 * np.pi, 2 * np.pi / 100)

  theta = np.append(theta, [2 * np.pi])
  x = np.cos(theta)

  y = np.sin(theta)


  v = np.linspace(0, 10, 101)
  for r in v:

      x1 = r * x

      y1 = r * y

      plt.plot(x1, y1, '0.0')

  for r in v:

      x1 = r * x

      y1 = r * y + 0.05

      plt.plot(x1, y1, '0.0')

  plt.show()

def line(plt, angle):
  wave_length = 0.5
  x_distance_mm = wave_length / math.cos(angle * math.pi / 180)
  per_cm_x_mm = 10 / x_distance_mm
  wave_length = x_distance_mm * math.cos(angle * math.pi / 180)
  delta_y = wave_length / 2 / math.sin(angle * math.pi / 180)
  print(wave_length, delta_y)
  wave_num = int(window_length * 10 / x_distance_mm)
  line_length = 10

  k = math.sin(angle * math.pi / 180) * line_length / 2
  for i in range(wave_num):
    line1 = [(i / per_cm_x_mm  - k, window_length / 2 - line_length / 2), (i / per_cm_x_mm + k, window_length / 2 + line_length / 2)]
    (line1_xs, line1_ys) = zip(*line1)

    # 创建两条线，并添加
    ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='black'))
    # 展示
    plt.plot()
  for i in range(wave_num):
    line1 = [(i / per_cm_x_mm + k, window_length / 2 - line_length / 2), (i / per_cm_x_mm - k, window_length / 2 + line_length / 2)]
    (line1_xs, line1_ys) = zip(*line1)

    # 创建两条线，并添加
    ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='black'))
    # 展示
    plt.plot()

  return wave_length, delta_y
  # x = np.linspace(0, 10, 10)
  # y = np.dot(2, np.ones(10))
  # plt.plot(x, y, '0.0')
  # plt.show()

# circle(plt)
line(plt, 45)
plt.show()
