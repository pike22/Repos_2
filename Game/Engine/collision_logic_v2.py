import re

class Collision_Logic_v2():
	def __init__(self):
		#--Collision Dictionary--#
		self.dict = {}
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


	#--Collision's Engine--#
	def Create_Grid(self, ):
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

	def Add_Collision(self, pos, obj, tag):
		x, y = pos
		for key, value in self.__gridMap.items():
			val_x, val_y = value
			if x >= val_x and x < val_x+self._boxSize:
				if y >= val_y and y < val_y+self._boxSize:
					# print('Box Number', key)
					self.__collisionMap[tag] = key
					self.__collisionObj[tag] = obj
					# print('New Collision Obj', self.__collisionObj[tag])
					# print('New Collision Pos', self.__collisionMap[tag])


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
		print('Collision Obj:\n', self.__collisionObj)
		print('Collision Map:\n', self.__collisionMap)
		print()
		if tag != None:
			print('Target Saved In CollisionObj?\n\t', self.__collisionObj[tag])
			print('Target Saved In CollisionMap?\n\t', self.__collisionMap[tag])
			if tag in self.__collisionMap and tag in self.__collisionObj:
				return True


	#Currently set up for a one-to-one collision.
	def Is_Collision(self, tag):
		objMain 	= self.__collisionObj[tag] #Focused object
		mapMain		= self.__collisionMap[tag] #objects map location
		# collResult	= [objMain]
		# sideResult	= {} #For Side Calc


		x, y = self.__gridMap[mapMain]
		for key, value in self.__gridMap.items():
			if (x+self._boxSize, y) == value:
				print('1 right')
				print('Box Numb:', key)
				self.dict['right'] = self.__collisionObj[key]

			if (x-self._boxSize, y) == value:
				print('1 left')
				print('Box Numb:', key)
				self.dict['left'] = self.__collisionObj[key]

			if (x, y+self._boxSize) == value:
				print('1 down')
				print('Box Numb:', key)
				self.dict['down'] = self.__collisionObj[key]

			if (x, y-self._boxSize) == value:
				print('1 up')
				print('Box Numb:', key)
				self.dict['up'] = self.__collisionObj[key]

			if (x+self._boxSize, y+self._boxSize) == value:
				print('1 right and down')
				print('Box Numb:', key)
				self.dict['rightDown'] = self.__collisionObj[key]

			if (x+self._boxSize, y-self._boxSize) == value:
				print('1 right and up')
				print('Box Numb:', key)
				self.dict['rightUp'] = self.__collisionObj[key]

			if (x-self._boxSize, y+self._boxSize) == value:
				print('1 left and down')
				print('Box Numb:', key)
				self.dict['leftDown'] = self.__collisionObj[key]

			if (x-self._boxSize, y-self._boxSize) == value:
				print('1 left and up')
				print('Box Numb:', key)
				self.dict['leftUp'] = self.__collisionObj[key]


		return self.dict

	"""#|-----------Ext_Functions-----------|#"""
		#this is home of extra functions...
	# def xxx(self, ):


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...
