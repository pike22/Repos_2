

class Side_Calculate(object):
	def __init__(self):
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
		self.oldList= []
		self._var	= 0


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
