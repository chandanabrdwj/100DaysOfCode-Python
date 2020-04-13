import turtle

class Polygon:
    def __init__(self,sides,name,size = 100, color = "black",line_thickness = 2):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness= line_thickness
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides


    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        

class Square(Polygon):
	def __init__(self,size=100, color="black",line_thickness=2):
		super().__init__(4,"Square",size,color,line_thickness)

	def draw(self):
		turtle.begin_fill()
		super().draw()
		turtle.end_fill()


square = Square()

print(square.sides)
print(square.angle)

print(square.draw())

turtle.done()