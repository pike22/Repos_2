import re

class Collision_Logic_v2():
	def __init__(self):

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
				print((self._xPos, self._yPos), 'box coords\t', y)
				self._yPos += self._boxSize
			print('<----------------------------------------->')

	def Add_Collision(self, pos, obj, tag):
		x, y = pos
		for key, value in self.__gridMap.items():
			val_x, val_y = value
			if x >= val_x and x < val_x+self._boxSize:
				if y >= val_y and y < val_y+self._boxSize:
					print('Box Number', key)
					self.__collisionMap[tag] = key
					self.__collisionObj[tag] = obj
					print('New Collision Obj', self.__collisionObj[tag])
					print('New Collision Pos', self.__collisionMap[tag])


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


	def Check_ifUsed(self, ):
		pass


	#Currently set up for a one-to-one collision.
	def Is_Collision(self, tag):
		objMain 	= self.__collisionObj[tag] #Focused object
		collResult	= [objMain]
		sideResult	= {} #For Side Calc
		for key in self.__collisionMap.keys():
			print('Target:', tag)
			print('Looking at:', key)
			if key != tag:
				if self.__collisionMap[key] == self.__collisionMap[tag]:
					print('Two Objects in One Square')
					objNext = self.__collisionObj[key] #Colliding with their obj
					collResult.append(objNext)

					"""look at the sorrounding 8 squares rather than coordinate position. !!!!!!!!!!!!!
					#<--Side Calculation-->#
					#<-------------------->#
					# Coord/Heights #
					Main_x, Main_y = objMain.get_myCoords()
					Main_w, main_h = objMain.get_size()
					Next_x, Next_y = objNext.get_myCoords()
					Main_w, main_h = objNext.get_size()
					#<-------------------------------------------->#
					if (Main_y+Main_h) <= Next_y+int(Next_h*0.2):
						sideResult[objNext.get_ID()] = 'up'
					elif (Next_y+Next_h) <= Main_y+int(Main_h*0.2):
						sideResult[objNext.get_ID()] = 'down'
					else:
						if Main_x > Next_x:
							sideResult[objNext.get_ID()] = 'right'
						elif Main_x < Next_x:
							sideResult[objNext.get_ID()] = 'left'
					"""

		#<--Using Collision-->#
		return (collResult, sideResult)


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_...


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...
