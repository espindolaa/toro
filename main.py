import matplotlib.pyplot as plt
import numpy as np
import json

from box import Coordinate
from box import Box

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

def draw_rectangle(ax, rectangle, color, style):
  ax.plot([rectangle.first.x, rectangle.second.x], [rectangle.first.y,rectangle.second.y], [rectangle.first.z, rectangle.second.z], color = color, linestyle=style)
  ax.plot([rectangle.second.x, rectangle.second.x], [rectangle.second.y,rectangle.third.y], [rectangle.second.z, rectangle.second.z], color = color, linestyle=style)
  ax.plot([rectangle.second.x, rectangle.third.x], [rectangle.third.y,rectangle.third.y], [rectangle.second.z, rectangle.third.z], color = color, linestyle=style)
  ax.plot([rectangle.third.x, rectangle.third.x], [rectangle.fourth.y,rectangle.first.y], [rectangle.fourth.z, rectangle.fourth.z], color = color, linestyle=style)

def draw_columns(ax, bottom, top, color, style):
  ax.plot([bottom.first.x, top.first.x], [bottom.first.y, top.first.y], [bottom.first.z, top.first.z], color = color, linestyle=style)
  ax.plot([bottom.second.x, top.second.x], [bottom.second.y, top.second.y], [bottom.second.z, top.second.z], color = color, linestyle=style)
  ax.plot([bottom.third.x, top.third.x], [bottom.third.y, top.third.y], [bottom.third.z, top.third.z], color = color, linestyle=style)
  ax.plot([bottom.fourth.x, top.fourth.x], [bottom.fourth.y, top.fourth.y], [bottom.fourth.z, top.fourth.z], color = color, linestyle=style)

def draw_box(ax, box, color, style):
  draw_rectangle(ax, box.bottom, color, style)
  draw_rectangle(ax, box.top, color, style)
  draw_columns(ax, box.bottom, box.top, color, style)

def draw_boxes(ax, boxes, color, style):
  for b in boxes:
    draw_box(ax, b, color, style)

def read_boxes(data): 
  boxes = []
  for entry in data['boxes']:
    boxes.append(read_box(entry))
  return boxes

def read_areas(data): 
  areas = []
  for entry in data['areas']:
    areas.append(read_box(entry))
  return areas

def read_box(entry):
    starting = entry['bottom_left_corner']
    point = Coordinate(starting['x'], starting['y'], starting['z'])
    return Box(point, entry['width'], entry['length'], entry['height'])

def read_file():
  f = open('test.json')
  data = json.load(f)

  boxes = read_boxes(data)
  areas = read_areas(data)

  f.close()
  return boxes, areas

fig = plt.figure(figsize=(10,10),)

ax = fig.add_subplot(111, projection='3d')

boxes, areas = read_file()
draw_boxes(ax, boxes, 'b', 'solid')
draw_boxes(ax, areas, 'r', 'dashed')

set_axes_equal(ax)
plt.show()
