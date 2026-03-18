from svgpathtools import svg2paths
import csv
from svgpathtools import svg2paths
import matplotlib.pyplot as plt
import numpy as np

# 1. Load paths and attributes
paths, attributes = svg2paths('projects/assettocorsa/trackgen/spa.svg')

plt.figure(figsize=(10, 10))

traces = []

for path in paths:
    # 2. Sample points along the path (e.g., 500 points for smoothness)
    # This handles the Bezier curves correctly
    points = [path.point(t) for t in np.linspace(0, 0.508, 3000)]
    
    x = [p.real for p in points]
    y = [p.imag for p in points]
    
    traces.append(points)

    


def get_centerline_points():
        
    # points = [path.point(t) for t in np.linspace(0, 1, 1920)]
    centerline_points = [(p.real, p.imag) for p in traces[3]]
        
    xs = [p[0] for p in centerline_points]
    ys = [p[1] for p in centerline_points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    scale_x = 1920 / (max_x - min_x)
    scale_y = 1080 / (max_y - min_y)
    scale = 0.5
    translated_points = [[int((x - min_x) * scale + (1920 - (max_x - min_x) * scale) / 2),
                          int((y - min_y) * scale + (1080 - (max_y - min_y) * scale) / 2)]
                         for x, y in centerline_points]
    
    centerline_points = translated_points
    
    centerline_points = [(x, 1080 - y + 110) for x, y in centerline_points]
    
    return centerline_points

# paths, _ = svg2paths("projects/assettocorsa/trackgen/spa.svg")
# path = paths[0]

# def get_centerline_points():
#     points = []
#     for i in range(1500):
#         t = i / 1499 
#         p = path.point(t)
#         points.append((p.real, p.imag))
        
#     xs = [p[0] for p in points]
#     ys = [p[1] for p in points]
#     min_x, max_x = min(xs), max(xs)
#     min_y, max_y = min(ys), max(ys)
#     scale_x = 900 / (max_x - min_x)
#     scale_y = 520 / (max_y - min_y)
#     scale = min(scale_x, scale_y) * 0.9
#     translated_points = [[int((x - min_x) * scale + (900 - (max_x - min_x) * scale) / 2),
#                         int((y - min_y) * scale + (520 - (max_y - min_y) * scale) / 2)]
#                         for x, y in points]
    
    
#     print(translated_points[0:20])
#     return translated_points

with open('projects/assettocorsa/trackgen/spa.csv', 'w', newline='') as f:
    writer = csv.writer(f, )
    writer.writerows(get_centerline_points())
    

