import math

t = 2*math.pi

#\draw [solid] (0,0) to (0,-1);
#\draw[fill = black] (0,0) circle [radius=0.075];

def wheel(n,r):
	print("\\begin{tikzpicture}")

	n=n-1
	for i in range(0,n):
		x1 = round(r*math.cos(i/n*t + t/4),2)
		y1 = round(r*math.sin(i/n*t + t/4),2)


		x2 = round(r*math.cos((i+1)/n*t + t/4),2)
		y2 = round(r*math.sin((i+1)/n*t + t/4),2)

		print("\draw [solid] (",x1,",",y1,") to (",x2,",",y2,");",sep='')
		print("\draw [solid] (0,0) to (",x1,",",y1,");")

	print()

	print("\draw[fill = black] (0,0) circle [radius=0.075];")
	for i in range (0,n):
		x1 = round(r*math.cos(i/n*t + t/4),2)
		y1 = round(r*math.sin(i/n*t + t/4),2)

		print("\draw[fill = black] (",x1,",",y1,") circle [radius=0.075];")
	print("\\end{tikzpicture}")

def star(n,r1,r2):
	print("\\begin{tikzpicture}")
	n = n-1
	for i in range(0,n):
		if i %2 == 0:
			R1 = r1
			R2 = r2
		else:
			R1 = r2
			R2 = r1

		x1 = round(R1*math.cos(i/n*t-t/4),2)
		y1 = round(R1*math.sin(i/n*t-t/4),2)


		x2 = round(R2*math.cos((i+1)/n*t-t/4),2)
		y2 = round(R2*math.sin((i+1)/n*t-t/4),2)

		print("\draw [solid] (",x1,",",y1,") to (",x2,",",y2,");",sep='')
		print("\draw [solid] (0,0) to (",x1,",",y1,");")

	print()

	print("\draw[fill = black] (0,0) circle [radius=0.075];")
	for i in range (0,n):

		if i %2 == 0:
			r = r1
		else:
			r=r2

		x1 = round(r*math.cos(i/n*t-t/4),2)
		y1 = round(r*math.sin(i/n*t-t/4),2)

		print("\draw[fill = black] (",x1,",",y1,") circle [radius=0.075];")
	print("\\end{tikzpicture}")

def kn_n(n,r):
	print("\\begin{tikzpicture}")
	for i in range(0,n):

		x1 = round(r*math.cos(i/n*t + t/4),2)
		y1 = round(r*math.sin(i/n*t + t/4),2)


		for j in range(int(-(n-3)/2),int((n-3)/2)):
			theta = i/n*t + j/n*t + t/4


			x2 = round(r*math.cos(theta),2)
			y2 = round(r*math.sin(theta),2)

			print("\draw [solid] (",x1,",",y1,") to (",x2,",",y2,");",sep='')


	print()

	for i in range (0,n):
		x1 = round(r*math.cos(i/n*t + t/4),2)
		y1 = round(r*math.sin(i/n*t + t/4),2)

		print("\draw[fill = black] (",x1,",",y1,") circle [radius=0.075];")
	print("\\end{tikzpicture}")



wheel(5,2)
print("\hspace{3cm}")
star(9,2,1)
print("\hspace{3cm}")
kn_n(5,2)
print("\\vspace{3cm}")
wheel(11,2)
print("\hspace{3cm}")
star(11,1,2)
print("\hspace{3cm}")
kn_n(7,2)