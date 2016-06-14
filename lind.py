import random as rd
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns; sns.set()
import numpy as np

def generate_string(length):

	symbols = ('f', '-', '+')
	replacement_str = 'f'
	
	for i in range(length):

		replacement_str = replacement_str + rd.choice(symbols) + 'f'

	return replacement_str

def generate_points(string):

	pts = [(0,0)]
	counter = 0
	i = 0

	for char in string:

		if char == '+':
			counter += 1
		if char == '-':
			counter -= 1
		if char == 'f':

			mod_count = counter % 4
	
			bit_1 = (-1)**(mod_count % 2) * 2
			bit_2 = mod_count // 2 
			
			pt = (pts[i][0] + bit_1*int(not(bit_2)),  pts[i][1] + bit_1*bit_2)
			pts.append(pt)
			i += 1

	return pts


def animate(nframes):
	plt.cla()
	plt.ylim([-30, 30])
	plt.xlim([-30, 30])
	plt.xticks([])
	plt.yticks([])
	
	plt.plot(xs[:nframes], ys[:nframes])
	plt.plot(xs[nframes], ys[nframes], 'ro')



replacements = 7

string = 'f'## string initialisation


for i in range(replacements):

	string = string.replace('f',generate_string(5))

points = generate_points(string)

xs = [i[0] for i in points]
ys = [i[1] for i in points]

xs = xs - np.mean(xs[:100])
ys = ys - np.mean(ys[:100])

fig = plt.figure()


anim = animation.FuncAnimation(fig, animate, frames=200)
anim.save('animation.gif', writer='imagemagick', fps=6);

fig = plt.figure()
plt.plot(xs[:300],ys[:300])
plt.savefig('fractal.png')



