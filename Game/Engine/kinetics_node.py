from .image_node import Image_Node

class Kinetics_Node():
	def __init__(self):
		pass


	def Controlled_Move(self, myCoords, ID, direction, speed):
		x, y = myCoords
		if direction == 'left':
			x -= 1 * speed
		if direction == 'right':
			x += 1 * speed
		if direction == 'up':
			y -= 1 * speed
		if direction == 'down':
			y += 1 * speed

		# print((x, y), ' :'+str(ID)+"'s Coords.")
		Image_Node.Render.coords(ID, x, y)
		return (x, y)

	def Knock_Back(self, myCoords, ID, direction):
		x, y = myCoords
		if direction == 'left':
			x -= 1
		elif direction == 'right':
			x += 1
		elif direction == 'up':
			y -= 1
		elif direction == 'down':
			y += 1
		else:
			print('NO DIRECTIONS')

		Image_Node.Render.coords(ID, x, y)
		return (x, y)

	def Static_Hit(self, myCoords, ID, direction, speed):
		# print(myCoords, 'OLD COORDS')
		x, y = myCoords
		if direction == 'left':
			x -= 1 * speed
			# print((x, y), 'coord, left')
		if direction == 'right':
			x += 1 * speed
			# print((x, y), 'coord, right')
		if direction == 'up':
			y -= 1 * speed
			# print((x, y), 'coord, up')
		if direction == 'down':
			y += 1 * speed
			# print((x, y), 'coord, down')

		Image_Node.Render.coords(ID, x, y)
		# print((x, y), 'NEW COORDS')
		return (x, y)
