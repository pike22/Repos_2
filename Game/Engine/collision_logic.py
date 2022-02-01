import re
from .image_node import Image_Node

class Collision_Logic():
	def __init__(self):
		self.__collisionDict = {}
		self.__collisionList = []
		self.__collideList	 = []
		self.__cornersLVD	 = []
		self.__cornersALL	 = []
		self.__isCollision   = False

		#vars for statics
		self.__wallRoster = []
		self.__keyA = None
		self.__keyB = None

		#Roster Vars
		self.__stalfosRoster = None
		self.__playerRoster  = None
		self.__staticRoster	 = None
		self.__weaponRoster	 = None
		self.__slimeRoster	 = None
		self.__enemyRoster	 = None
		self.__wallRoster	 = None
		self.__projRoster	 = None

		#obj Parameters
		self.__sideResult = []
		self.__mainOBJ 	  = None
		self.__objA		  = None
		self.__objB		  = None
		self.__objC		  = None
		self.__objD		  = None
		"""OBJECT COORDS"""
		self.__xM, self.__yM = None, None
		self.__xA, self.__yA = None, None
		self.__xB, self.__yB = None, None
		self.__xC, self.__yC = None, None
		"""OBJECT  SIZE"""
		self.__hM, self.__wM = None, None
		self.__hA, self.__wA = None, None
		self.__hB, self.__wB = None, None
		self.__hC, self.__wC = None, None

		#rand var
		self.__CurrentSquare = None
		self.__GRID = None
		self.tempL  = []

	'''#_COLLISION DICTIONARY FUNCTIONS_#'''
	#tagOrId == dictionary key
	#object == The keys related class object
	def Add_CollisionDict(self, tagOrId, obj):
		self.__collisionDict[tagOrId] = obj

	def Del_CollisionDict(self, tagOrId):
		del self.__collisionDict[tagOrId]

	def Tag_toObject(self, tagOrId):
		#output == tag's object
		output = self.__collisionDict[tagOrId]
		return output

	def Object_toTag(self, obj):
		for key, object in self.__collisionDict.items():
			if obj == object:
				return key

	def CollisionDict_Keys(self):
		newList = []
		for key in self.__collisionDict.keys():
			newList.append(key)
		return newList

	'''#_COLLISON CALCULATION FUNCTIONS_#'''
	def Add_Collision(self, listofCorners=None, LVD_Corner=None):
		if listofCorners != None:
			self.tempL = []
			for item in range(len(listofCorners)):
				self.tempL.append(listofCorners[item])

		if LVD_Corner != None:
			self.__cornersLVD.append(LVD_Corner)

		self.__cornersALL = self.tempL + self.__cornersLVD


	def Check_forCollision(self, targOBJ=None, objectID=None):
		if targOBJ != None:
			x1, y1, x2, y2 = targOBJ.get_Corners()
		if objectID != None:
			print(objectID)
			print(Image_Node.Render.bbox(objectID))
			x1, y1, x2, y2 = Image_Node.Render.bbox(objectID)
		collision = Image_Node.Render.find_overlapping(x1, y1, x2, y2)
		# print(collision, 'ForT Collision')
		if len(collision) > 1:
			self.__collideList = []
			self.__collisionList   = []
			for count in range(len(collision)):
				# print('item:', item, 'CL#113')
				tag = Image_Node.Render.gettags(collision[count])
				# print(tag, 'tag CL#100')
				self.__collisionList.append(tag[0])
			# print(self.__collisionList, 'Colliding') #print Tags of Entity Colliding

			self.oldList = self.__collisionList
			self.__collisionList = []
			for count in range(len(self.oldList)-1, -1, -1):
				tagOrId = self.oldList[count]
				if tagOrId not in self.__wallRoster:
					self.__collisionList.append(tagOrId)
				elif tagOrId in self.__wallRoster and self.__collisionList != []:
					self.__collisionList.append(tagOrId)
			# print(self.__collisionList, 'new Colliding') #print Tags of Entity Colliding


			for count in range(len(self.__collisionList)):
				tagOrId = self.__collisionList[count]
				obj = self.__collisionDict[tagOrId]
				# print(obj.get_myCoords(), tagOrId, 'objCoords')
				self.__collideList.append(obj)

			self.__isCollision = True
			# print(self.__collideList, 'objList')
			return self.__collideList

	#use this: .find_overlapping
	# only outputs the last assigned var.
	def Is_Collision(self, item):
		# print(item)
		if item == 0:
			self.__collideList = []
			self.__collisionList   = []


		x1, y1, x2, y2 = self.__cornersALL[item]
		print(self.__cornersALL[item])
		collision = Image_Node.Render.find_overlapping(x1, y1, x2, y2)


		#this only shows what is colliding.
		if len(collision) > 1:
			self.__collideList = []
			self.__collisionList   = []
			for count in range(len(collision)):
				# print('item:', item, 'CL#113')
				tag = Image_Node.Render.gettags(collision[count])
				# print(tag, 'tag CL#115')
				self.__collisionList.append(tag[0])
			# print(self.__collisionList, 'Colliding') #print Tags of Entity Colliding

			self.oldList = self.__collisionList
			self.__collisionList = []
			for count in range(len(self.oldList)-1, -1, -1):
				tagOrId = self.oldList[count]
				if tagOrId not in self.__wallRoster:
					self.__collisionList.append(tagOrId)
				elif tagOrId in self.__wallRoster and self.__collisionList != []:
					self.__collisionList.append(tagOrId)
			# print(self.__collisionList, 'new Colliding') #print Tags of Entity Colliding


			for count in range(len(self.__collisionList)):
				tagOrId = self.__collisionList[count]
				obj = self.__collisionDict[tagOrId]
				# print(obj.get_myCoords(), tagOrId, 'objCoords')
				self.__collideList.append(obj)



			self.__isCollision = True
			# print(self.__collideList, 'objList')
			return self.__collideList
		else:
			self.__isCollision = False
			return []

	#I want to use this to purly find where objects are in relation to others and push
	#the opposite direction through so that I can do proper knockback/wall collision
	def Side_Calc(self, mainOBJ):
		self.__mainOBJ = mainOBJ
		self.__xM, self.__yM = mainOBJ.get_myCoords()
		self.__hM, self.__wM = mainOBJ.get_size()


		self.__mainSQ = self.Find_Square(self.__xM+(self.__wM/2), self.__yM+(self.__hM/2))
		self.tempL = []
		self.tempL.append(self.__mainOBJ)
		if len(self.__collideList) >= 3:
			for obj in self.__collideList:
				if obj != self.__mainOBJ:
					if self.__mainSQ != None:
						if obj.get_myCoords()[0] == self.__GRID[self.__mainSQ][0]:
							if obj.get_myCoords()[1] == (self.__GRID[self.__mainSQ][1]-32):
								# print(obj.get_ID(), 'bottom side')
								self.tempL.append(obj)
						if obj.get_myCoords()[0] == self.__GRID[self.__mainSQ+1][0]:
							if obj.get_myCoords()[1] == self.__GRID[self.__mainSQ+1][1]:
								# print(obj.get_ID(), 'top side')
								self.tempL.append(obj)
						if obj.get_myCoords()[0] == (self.__GRID[self.__mainSQ][0]-32):
							if obj.get_myCoords()[1] == self.__GRID[self.__mainSQ][1]:
								# print(obj.get_ID(), 'right side')
								self.tempL.append(obj)
						if obj.get_myCoords()[0] == (self.__GRID[self.__mainSQ][0]+32):
							if obj.get_myCoords()[1] == self.__GRID[self.__mainSQ][1]:
								# print(obj.get_ID(), 'left side')
								self.tempL.append(obj)
					else:
						self.__mainSQ = self.Find_Square((self.__xM+(self.__wM/2)+1), (self.__yM+(self.__hM/2)+1))
						if self.__mainSQ != None:
							if obj.get_myCoords()[0] == self.__GRID[self.__mainSQ][0]:
								if obj.get_myCoords()[1] == (self.__GRID[self.__mainSQ][1]-32):
									# print(obj.get_ID(), 'bottom side2')
									self.tempL.append(obj)
							if obj.get_myCoords()[0] == self.__GRID[self.__mainSQ+1][0]:
								if obj.get_myCoords()[1] == self.__GRID[self.__mainSQ+1][1]:
									# print(obj.get_ID(), 'top side2')
									self.tempL.append(obj)
							if obj.get_myCoords()[0] == (self.__GRID[self.__mainSQ][0]-32):
								if obj.get_myCoords()[1] == self.__GRID[self.__mainSQ][1]:
									# print(obj.get_ID(), 'right side2')
									self.tempL.append(obj)
							if obj.get_myCoords()[0] == (self.__GRID[self.__mainSQ][0]+32):
								if obj.get_myCoords()[1] == self.__GRID[self.__mainSQ][1]:
									# print(obj.get_ID(), 'left side2')
									self.tempL.append(obj)


			# print(self.__collideList, 'list 1')
			self.__collideList = []
			self.__collideList = self.tempL
			# print(self.__collideList, 'list 2')


		#Clears the object variables
		self.__objA = None
		self.__objB = None
		self.__objC = None
		self.__objD = None
		for item in range(len(self.__collideList)):
			#this is object A
			if item == 0:
				if self.__collideList[0] != self.__mainOBJ:
					self.__objA = self.__collideList[0]
					self.__xA, self.__yA = self.__collideList[0].get_myCoords()
					self.__hA, self.__wA = self.__collideList[0].get_size()
				else:
					self.__objA = None
			#this is object B
			elif item == 1:
				if self.__collideList[1] != self.__mainOBJ:
					self.__objB = self.__collideList[1]
					self.__xB, self.__yB = self.__collideList[1].get_myCoords()
					self.__hB, self.__wB = self.__collideList[1].get_size()
				else:
					self.__objB = None
			#this is object C
			elif item == 2:
				if self.__collideList[2] != self.__mainOBJ:
					self.__objC = self.__collideList[2]
					self.__xC, self.__yC = self.__collideList[2].get_myCoords()
					self.__hC, self.__wC = self.__collideList[2].get_size()
				else:
					self.__objC = None
			#this is object D
			elif item == 3:
				if self.__collideList[3] != self.__mainOBJ:
					self.__objD = self.__collideList[3]
					self.__xD, self.__yD = self.__collideList[3].get_myCoords()
					self.__hD, self.__wD = self.__collideList[3].get_size()
				else:
					self.__objD = None

		# self.objPRINTOUT()
		#checks which collision objects are used and "returns" the individual squares collision direction
		self.__sideResult = []
		self.__resultTAG  = []
		"""mainOBJ vs. objA"""
		if self.__objA != None:
			# print(self.__objA, ':objA', self.__objA.get_ID(), ':tagA')
			if (self.__yM+self.__hM) <= self.__yA+(self.__hA*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objA.get_ID())
			elif (self.__yA+self.__hA) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objA.get_ID())
			else:
				if self.__xM > self.__xA:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objA.get_ID())
				elif self.__xM < self.__xA:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objA.get_ID())

		"""mainOBJ vs. objB"""
		if self.__objB != None:
			# print(self.__objB, ':objB', self.__objB.get_ID(), ':tagB')
			if (self.__yM+self.__hM) <= self.__yB+(self.__hB*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objB.get_ID())
			elif (self.__yB+self.__hB) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objB.get_ID())
			else:
				if self.__xM > self.__xB:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objB.get_ID())
				elif self.__xM < self.__xB:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objB.get_ID())

		"""mainOBJ vs. objC"""
		if self.__objC != None:
			# print(self.__objC, ':objC', self.__objC.get_ID(), ':tagC')
			if (self.__yM+self.__hM) <= self.__yC+(self.__hC*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objB.get_ID())
			elif (self.__yC+self.__hC) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objB.get_ID())
			else:
				if self.__xM > self.__xC:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objB.get_ID())
				elif self.__xM < self.__xC:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objB.get_ID())

		"""mainOBJ vs. objD"""
		if self.__objD != None:
			# print(self.__objD, ':objD', self.__objD.get_ID(), ':tagD')
			if (self.__yM+self.__hM) <= self.__yD+(self.__hD*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objD.get_ID())
			elif (self.__yD+self.__hD) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objD.get_ID())
			else:
				if self.__xM > self.__xD:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objD.get_ID())
				elif self.__xM < self.__xD:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objD.get_ID())

		# print(
		# 	'---------------Direction off of Wall---------------\n',
		# 	self.__sideResult, '\t:Given To', self.__mainOBJ.get_ID(), '\n',
		# 	self.__resultTAG,  '\t:Given By', '\n',
		# 	'---------------------------------------------------\n'
		# 	 )
		return self.__sideResult


	def Side_Calc_Print(self):
		print(self.__mainOBJ.get_ID(), 'ID')
		print(self.__xM, 'coordx mainOBJ')
		print(self.__yM, 'coordy mainOBJ')
		print(self.__hM, 'height mainOBJ')
		print('--------------------------------------------')
		if self.__objA != None:
			print(self.__objA.get_ID(), 'ID')
			print(self.__xA, 'coordx objA')
			print(self.__yA, 'coordy objA')
			print(self.__hA, 'height objA')
			print('--------------------------------------------')
		if self.__objB != None:
			print(self.__objB.get_ID(), 'ID')
			print(self.__xB, 'coordx objB')
			print(self.__yB, 'coordy objB')
			print(self.__hB, 'height objB')
			print('--------------------------------------------')
		if self.__objC != None:
			print(self.__objC.get_ID(), 'ID')
			print(self.__xC, 'coordx objC')
			print(self.__yC, 'coordy objC')
			print(self.__hC, 'height objC')
			print('--------------------------------------------')
		if self.__objD != None:
			print(self.__objD.get_ID(), 'ID')
			print(self.__xD, 'coordx objD')
			print(self.__yD, 'coordy objD')
			print(self.__hD, 'height objD')
			print('--------------------------------------------')


	def Find_Square(self, x, y):
		#this is staple for when I need to know what square my mouse is in.
		for item in range(len(self.__GRID)):
			if x > self.__GRID[item][0] and y > self.__GRID[item][1]:
				if x < self.__GRID[item][2] and y < self.__GRID[item][3]:
					self.__CurrentSquare = item
					return self.__CurrentSquare



	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_collisionDict(self):
		return self.__collisionDict

	def get_isCollision(self):
		return self.__isCollision

	def get_collideList(self):
		return self.__collideList

	def reset_collideList(self):
		self.__collideList = []


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_playerRoster(self, Roster):
		self.__playerRoster = Roster

	def set_enemyRoster(self, Roster):
		self.__enemyRoster = Roster

	def set_slimeRoster(self, Roster):
		self.__cpstalfosRost = Roster

	def set_stalfosRoster(self, Roster):
		self.__stalfosRoster = Roster

	def set_weaponRoster(self, Roster):
		self.__weaponRoster = Roster

	def set_projRoster(self, Roster):
		self.__projRoster = Roster

	def set_staticRoster(self, Roster):
		self.__staticRoster = Roster

	def set_wallRoster(self, Roster):
		self.__wallRoster = Roster

	def set_grid(self, grid):
		self.__GRID = grid
