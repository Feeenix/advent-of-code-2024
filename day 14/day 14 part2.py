import numpy as np
with open("input","r") as f:
	text = f.read().strip()
	width = 101
	height = 103
	future = 200
modv = np.array([width,height])
ps =[]
vs = []
for line in text.split("\n"):
	p = np.array([int(x) for x in line.split(" ")[0][2:].split(",")])
	v = np.array([int(x) for x in line.split(" ")[1][2:].split(",")])
	ps.append(p)
	vs.append(v)
t=0
while True:

	canvas = [[" "]*width for _ in range(height)]
	for p,v in zip(ps,vs):
		outpos = np.mod(p+v*t,modv)		

		canvas[outpos[1]][outpos[0]] = "#"
	for line in canvas :
		if "#"*15 in "".join(line):
			break
	else: t+=1;continue


	print("\n".join(["".join(line) for line in canvas]))
	
	input(t)

	t+=1
	
