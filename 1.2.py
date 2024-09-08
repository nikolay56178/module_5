class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y  

	def distance(self):
		print((self.x**2+self.y**2)**(1/2))

	def __add__(self,other):
		print(self.x + other.x, self.y + other.y)
p1 = 3
p2 = 5
o = Point(p1,p2)
o.distance()

b1 = Point(1,1)
b2 = Point(2,2)

b3 = b1 + b2 
