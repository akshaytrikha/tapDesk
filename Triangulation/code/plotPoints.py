import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import minimize
import math

import serial

port = "dev/tty.usbmodem1421"
ser = serial.Serial(port, 9600, timeout = 5)

def centroid(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    _len = len(points)
    centroid_x = sum(x_coords)/_len
    centroid_y = sum(y_coords)/_len
    return [centroid_x, centroid_y]


# Mean Square Error
# locations: [ (lat1, long1), ... ]
# distances: [ distance1, ... ]
# x = [lat, long, r_0]
def mse(x, locations, deltas, material_speed):
	mse = 0.0
	distances = [x[2]] + [x[2] + deltas[0]*material_speed,
 										  x[2] + deltas[1]*material_speed]

	for location, distance in zip(locations, distances):
 		distance_calculated = (x[0]-location[0])**2 + (x[1]-location[1])**2
 		mse += math.pow(distance_calculated - distance**2, 2.0)

	return mse / 3.0


# initial_location: (lat, long, r_x)
# locations: [ (lat1, long1), ... ]
# deltas: [ d1, d2   ... ]


def triangulate(locations,deltas,material_speed):

	initial_poss_guess = centroid(locations)
	initial_guess = list(initial_poss_guess) + \
	[np.sqrt(initial_poss_guess[0]**2 + initial_poss_guess[1]**2)]
	result = minimize(
		mse,                         # The error function
 		initial_guess,            # The initial guess
 		args=(locations,
 				deltas,
 		  material_speed), # Additional parameters for mse
 		method='L-BFGS-B',           # The optimisation algorithm
 		options={
 		'ftol':1e-5,         # Tolerance
 		'maxiter': 1e+7      # Maximum iterations
 		})
	location = result.x
	return location[:2],location[2]


locations = [(0,0),(4,4),(0,5)]
material_speed = 340

xs = [a[0] for a in locations]
ys = [b[1] for b in locations]
mes_xs = []
mes_ys = []

while(1):
    times = [int(x) for x in ser.readline().strip().split(' ')]
    if len(times) > 0:
        times = [float(x)/(1000000.0) for x in times]
        delta1 = times[1] - times[0]
        deltas2 = times[2] - times[0]
        deltas = [delta1,delta2]
        pt,r = triangulate(locations,deltas,material_speed)


        mes_xs.append(pt[0])
        mes_ys.append(pt[1])

        plt.clear()
        print(pt,r)
        plt.plot(mes_xs, mes_ys, 'ro')
        plt.plot(xs,ys,'bo')
        plt.axis([0, 6, 0, 20])
        plt.show()
