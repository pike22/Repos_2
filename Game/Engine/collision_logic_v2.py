import re
from .image_node import Image_Node

class Collision_Logic_v2():
	def __init__(self):
		#--Collision Dictionaries--#
		self.__entityRoster = None
		#--Grid Dictionaries--#
		self.__collisionMap	= {} #Used map spaces.
		self.__collisionObj = {} #Object Stored in that map square.
		self.__gridMap		= {} #The Grid, key=BoxNumb & value=(x, y)POS
		#--Grid Parameters--#
		self._heightSC	= 800
		self._widthSC	= 1280
		self._boxSize	= 32
		self._xPos		= 0
		self._yPos		= 0
		self._lineX		= 0
		self._lineY		= 0


	#--Collision's Engine--#
	def Create_Grid(self, lines=False):
		boxCountX = int(self._widthSC/self._boxSize)
		boxCountY = int(self._heightSC/self._boxSize)

		boxNumb = 0
		for x in range(boxCountX+1):
			if x == 0:
				self._xPos = 0
			else:
				self._xPos += self._boxSize
			for y in range(boxCountY+1):
				if y == (boxCountY):
					self._yPos = 0
				boxNumb+=1
				self.__gridMap[boxNumb] = (self._xPos, self._yPos)
				# print((self._xPos, self._yPos), 'box coords\t', y)
				self._yPos += self._boxSize
			# print('<----------------------------------------->')

		if lines == True:
			for item in range(boxCountX+1):
				Image_Node.Render.create_line(self._lineX, 0, self._lineX, 800)
				self._lineX += self._boxSize
			for item in range(boxCountY+1):
				Image_Node.Render.create_line(0, self._lineY, 1280, self._lineY)
				self._lineY += self._boxSize

	def Update_Collision(self, pos, obj):
		self.Add_Collision(pos, obj)


	def Add_Collision(self, pos, obj):
		# print(tag, 'added to collision')
		keyList = []
		if obj.get_groupID() == self.__entityRoster:
			print("entity Pass")
			#Four Points
			for count in range(4):
				x, y = pos
				w, h = obj.get_size() #this may be changed.
				if count == 0:		#Top Left
					pass
				elif count == 1:	#Top Right
					x += w
				elif count == 2:	#Bottom Left
					y += h
				elif count == 3:	#Bottom Right
					x += w
					y += h
				Image_Node.Render.create_oval(x-1, y-1, x+1, y+1, fill='Red')
				for key, value in self.__gridMap.items():
					val_x, val_y = value
					if x >= val_x and x < val_x+self._boxSize:
						if y >= val_y and y < val_y+self._boxSize:
							# print('Box Number', key)
							keyList.append(key)
							self.__collisionObj[obj.get_ID()] = obj
							# print('New Collision Obj', self.__collisionObj[obj.get_ID()])
			self.__collisionMap[obj.get_ID()] = keyList
		else:
			print('everything else')
			x, y = pos
			for key, value in self.__gridMap.items():
				val_x, val_y = value
				if x >= val_x and x < val_x+self._boxSize:
					if y >= val_y and y < val_y+self._boxSize:
						# print('Box Number', key)
						self.__collisionMap[obj.get_ID()] = key
						self.__collisionObj[obj.get_ID()] = obj
						# print('New Collision Obj', self.__collisionObj[obj.get_ID()])
						# print('New Collision Map', self.__collisionMap[obj.get_ID()])


	def Del_Collision(self, tag):
		if tag in self.__collisionMap and tag in self.__collisionObj:
			del self.__collisionMap[tag]
			del self.__collisionObj[tag]


	def Tag_toObject(self, tag):
		for key in self.__collisionObj.keys():
			if key == tag:
				return key
			else:
				print('Key not found \n\tFunc: Tag_toObject')


	def Object_toTag(self, object):
		for value in self.__collisionObj.values():
			if value == object:
				return value
			else:
				print('Object not found \n\tFunc: Object_toTag')


	def Check_ifUsed(self, tag=None):
		print('\n<|---------Check If Used---------|>')
		# print('Collision Obj:\n', self.__collisionObj)
		# print('Collision Map:\n', self.__collisionMap)
		print()
		if tag != None:
			print('Target Saved In CollisionObj?\n\t', self.__collisionObj[tag])
			print('Target Saved In CollisionMap?\n\t', self.__collisionMap[tag])
			if tag in self.__collisionMap and tag in self.__collisionObj:
				return True


	#Currently set up for a one-to-one collision.
	def Is_Collision(self, tag):
		objMain 	= self.__collisionObj[tag] #Focused object
		# sideResult	= {} #For Side Calc


		x, y = objMain.get_myCoords()
		w, h = objMain.get_size()
		# points = self.Find_myPoints(x, y, x+w, y+h)
		# print((x, y), 'Coords')
		# print(self.__collisionMap[tag], 'box(s)')

		#everything is set up to use boxes for collision. somehow in here
		#I will need to check for boxes used vs the target box. To then determin
		#where other objects are for collision. ## NOTE: This is a reminder for the next day.
		boxList = []
		for key in self.__collisionMap.keys():
			if key != tag:
				if self.__collisionMap[tag] == self.__collisionMap[key]:
					print(key)
					boxList.append(self.__collisionMap[key])
		# print([self.__collisionMap[tag], self.__collisionMap[key]])
		if boxList != []:
			print(objMain.get_ID(), boxList)











	"""#|-----------Ext_Functions-----------|#"""
		#this is home of extra functions...
	def Find_myPoints(self, x1, y1, x2, y2):
		saved = []
		print((x2, y2), '(x2, y2)')
		for xPoint in range(int(x2-x1+1)):
			xPos = x1+xPoint
			for yPoint in range(int(y2-y1+1)):
				yPos = y1+yPoint
				# print((xPos, yPos))
				saved.append((xPos, yPos))

		# 		if xPos == x1 or xPos == x2:
		# 			# Image_Node.Render.create_oval(xPos, yPos, xPos+1, yPos+1)
		# 			saved.append((xPos, yPos))
		# 		elif yPos == y1 or yPos == y2:
		# 			# Image_Node.Render.create_oval(xPos, yPos, xPos+1, yPos+1)
		# 			saved.append((xPos, yPos))
		#
		#
		# for value in saved:
		# 	pass

		return saved #returns list of coords within the square



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_entityRoster(self, Roster):
		self.__entityRoster = Roster
