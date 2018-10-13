import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import minimize
import math
import matplotlib.animation as animation

import serial

import webbrowser
import subprocess
import os

fig = plt.figure(figsize=(10,5))


port = "/dev/tty.usbmodem1431"
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

def euclid(x,y):
    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def animate(i):
                #  A          B.       C
    locations = [(4.35,4.44),(4,4),(4.88,4)]
    material_speed = 343

    xs = [a[0] for a in locations]
    ys = [b[1] for b in locations]
    mes_xs = []
    mes_ys = []
    serString = str(ser.readline())
    serStringCrop = serString[2:-5]
    print(serString)
    print(serStringCrop)
    times_order = [ x for x in serStringCrop.strip().split(' ')]
    print(times_order)
    times = times_order[:3]
    print(times)
    order = [int(x) for x in times_order[3:]]
    print(order)
    locs = [(0,0),(0,0),(0,0)]

    for i in range(len(order)):
        locs[order[i]] = locations[i] 

    print(locs)

    # try:
    times = [float(x)/(1000000.0) for x in times]
    delta1 = times[1] - times[0]
    delta2 = times[2] - times[0]
    deltas = [delta1,delta2]
    pt,r = triangulate(locs,deltas,material_speed)

    lele = 10101919191
    minpty = locations[0]
    for pty in locations:
        locotron = euclid(pty,pt)
        if locotron < lele:
            lele = locotron
            minpty = pty


    # if minpty == locations[0]:
    #     # call Adrian on Facetime
    #     os.popen('open facetime://+19094809798')
    # elif minpty == locations[1]:
    #     # for homework
    #     # webbrowser.open('https://drive.google.com/drive/u/0/my-drive')
    #     # webbrowser.open('https://mail.google.com/mail/u/0/')
    #     # webbrowser.open('https://sakai.claremont.edu/portal')
    #     # webbrowser.open('https://www.gradescope.com/')
    #     # subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Spotify.app"])
        
    # else:
    #     # order Dominos
    #     # webbrowser.open('https://pizza.dominos.com/california/claremont/366-w-foothill-blvd/')



    mes_xs.append(pt[0])
    mes_ys.append(pt[1])

        #plt.clear()
    print(pt,r)
    plt.plot(mes_xs, mes_ys, 'ro')
    plt.plot(xs,ys,'bo')
    plt.axis([0, 20, 0,20 ])
            
    # except:
    #     break


def update():

    ani = animation.FuncAnimation(fig,animate)
    plt.show()

update()

   
