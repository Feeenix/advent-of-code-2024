import numpy as np
with open("input","r") as f:
	text = f.read().strip()
	width = 101
	height = 103
	future = 100
modv = np.array([width,height])
qs = [0]*4
for line in text.split("\n"):
	p = np.array([int(x) for x in line.split(" ")[0][2:].split(",")])
	v = np.array([int(x) for x in line.split(" ")[1][2:].split(",")])
	
	outpos = np.mod(p+v*future,modv)
	
	q = None
	if outpos[0]<width//2 and outpos[1]<height//2:
		q=0
	if outpos[0]<width//2 and outpos[1]>height//2:
		q=1
		
	if outpos[0]>width//2 and outpos[1]<height//2:
		q=2
		
	if outpos[0]>width//2 and outpos[1]>height//2:
		q=3
		
	if not q is None:
		qs[q]+=1
		
print(np.prod(qs))
		
	
