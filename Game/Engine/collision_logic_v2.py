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

		#--Public Variables--#
		self.boxList = []
		self.returnList = []


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
				Image_Node.Render.create_text(self._xPos+16, self._yPos+16, text=str(boxNumb), fill='Blue')
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
		# print(self.__collisionMap[P#001])


	def Add_Collision(self, pos, obj):
		# print(tag, 'added to collision')
		keyList = []
		if str(obj.get_groupID()) in self.__entityRoster:
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
				# Image_Node.Render.create_oval(x-1, y-1, x+1, y+1, fill='Red')
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


	def Check_ifUsed(self, tag=None, boxNumb=None, GC=True): #GC = Game Check
		if GC == False:
			print('\n<|---------Check If Used---------|>')
			# print('Collision Obj:\n', self.__collisionObj)
			# print('Collision Map:\n', self.__collisionMap)
			print()
			if tag != None:
				print('Target Saved In CollisionObj?\n\t', self.__collisionObj[tag])
				print('Target Saved In CollisionMap?\n\t', self.__collisionMap[tag])
				if tag in self.__collisionMap and tag in self.__collisionObj:
					return True
		else:
			if tag != None and boxNumb != None:
				for key, value in self.__collisionMap.items():
					if key != tag and boxNumb == value:
						self.boxList.append(self.__collisionObj[key])


	#Currently set up for a one-to-one collision.
	def Is_Collision(self, tag):
		objMain = self.__collisionObj[tag] #Focused Obj
		mapMain = self.__collisionMap[tag] #Focused Map
		# print(mapMain)

		x, y = objMain.get_myCoords()
		w, h = objMain.get_size()

		for box in mapMain:
			# print(mapMain, objMain.get_ID(),"'s map squares.")
			self.Check_ifUsed(objMain.get_ID(), box)
			self.Update_Collision(pos=objMain.get_myCoords(), obj=objMain)

		# print(len(self.boxList))
		if self.boxList != []:
			objMain.set_isStatic(True)
			# print(self.boxList)
		else:
			objMain.set_isStatic(False)

		returnVar = self.boxList
		self.boxList = []
		return returnVar





	"""#|-----------Ext_Functions-----------|#"""
		#this is home of extra functions...
	def Side_Calculation(self, obj, target):
		objMain = self.__collisionObj[obj.get_ID()] #Focused Obj
		mapMain = self.__collisionMap[obj.get_ID()] #Focused Map
		self.returnList = set()

		w,  h  = obj.get_size()
		x1, y1 = self.__gridMap[self.__collisionMap[target.get_ID()]] #Object B
		w1, h1 = target.get_size()

		for corner in mapMain:
			x0, y0 = self.__gridMap[corner]
			if (y0+h) <= y1+(h1*0.2):
				#Up
				# print('up')
				self.returnList.add('up')
			elif (y1+h1) <= y0+(h*0.2):
				#Down
				# print('down')
				self.returnList.add('down')
			else:
				if x0 > x1:
					#Right
					# print('right')
					self.returnList.add('right')
				elif x0 < x1:
					#Left
					# print('left')
					self.returnList.add('left')
		# print(self.returnList)
		return self.returnList

		## NOTE: Use old method for directions, might fix some problems. !!!!!!!!!
		# if (y+h) <= y1+(h1*0.2):
		# 	#Up
		# 	print('up')
		# 	x0, y0 = self.__gridMap[mapMain[3]]
		# elif (y1+h1) <= y+(h*0.2):
		# 	#Down
		# 	print('down')
		# 	x0, y0 = self.__gridMap[mapMain[0]]
		# else:
		# 	if x > x1:
		# 		#Right
		# 		print('right')
		# 		x0, y0 = self.__gridMap[mapMain[0]]
		# 	elif x < x1:
		# 		#Left
		# 		print('left')
		# 		x0, y0 = self.__gridMap[mapMain[1]]


			#You should take each box that is associated with a corner of the player.
			#Then base it on that boxes coords rather than where the exact dot is. That will
			#be easier than trying to guess where the other boxes are. Corrners may prove to
			#be difficult again. DON'T FORGET.
				## NOTE: Actual Collision Works. Just need a Side_calculation to acuratly determin the
				##		 Direction to bounce to. Fix double bouncing later.

	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_entityRoster(self, Roster):
		self.__entityRoster = Roster
