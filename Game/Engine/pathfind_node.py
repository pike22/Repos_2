from .image_node import Image_Node
from .node import Node

#Parent: Node
#Children:
	#None

class PathFind_Node(Node):
	def __init__(self, cLogic, cNode, iNode, tNode=None):
		Node.__init__(self, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)

		#--Breadth Search--#
		self.__frontier = {}
		self.__reached	= {}
		self._lastBox	= None
		self._numb		= 0

		#--Grid Paramaters--#
		self.__pathGRID = {}
		self.__boxSize  = 32
		self._xPos = 0
		self._yPos = 0

	def Path_Grid(self, ):
		boxCountX = int(1280/self.__boxSize)
		boxCountY = int(800/self.__boxSize)

		boxNumb = 0
		for x in range(boxCountX+1):
			if x == 0:
				self._xPos = 0
			else:
				self._xPos += self.__boxSize
			for y in range(boxCountY+1):
				self._yPos += self.__boxSize
				if y == (boxCountY):
					self._yPos = 0
				boxNumb+=1
				self.__pathGRID[boxNumb] = (self._xPos, self._yPos)
				self.__frontier[boxNumb] = (self._xPos, self._yPos)
			# 	print((self._xPos, self._yPos), 'box coords\t', y)
			# print('-----------------------------------------------')
		# print(self.__pathGRID)

	#basic path finding.
	#startOBJ == Target object to be moved
	#endOBJ == Target object that startOBJ is moving to.
	def Breadth_Search(self, startOBJ, endOBJ):
		self._lastBox = None
		print("#--Initial Prints--#")
		my_x, my_y = startOBJ[0]
		endCoords = endOBJ
		# print((my_x, my_y), 'obj coords')

		startBox = self.Find_mySquare((my_x, my_y)) #startOBJ's original box
		# print(startBox, startOBJ[1],"'s box number")

		self.__reached['Box0'] = startBox
		print(self.__reached)
		if startBox in self.__frontier:
			del self.__frontier[startBox]
		print('\n<------------------------>\n')

		# print(self.__pathGRID[self.__reached['Box0']], "Box0's coords")
		while self.__frontier != {}:
			curBox = 'Box'+str(self._numb)
			if self._lastBox == None:
				self._lastBox = 'Box0'
			else:
				self._lastBox = curBox
			if curBox in self.__reached:
				self._lastBox = None
				self.Find_Neighbors(self._numb, self._lastBox)
			self._numb += 1


			# startBox = self.Find_mySquare((my_x, my_y))
			if self._numb in self.__frontier:
				del self.__frontier[self._numb]
				print(len(self.__frontier), "Box's left")
				return

		# for key in self.__reached:
		# 	x, y = self.__pathGRID[self.__reached[key]]
		# 	Image_Node.Render.create_oval(x+15, y+15, x+25, y+25, fill='Blue')


	"""#|----------Extra Functions----------|#"""
	def Find_Neighbors(self, numb, lastBox): #this is used to find if neighboring boxes are used.
		curBox = 'Box'+str(numb)
		print(curBox, '\t\t:Current')
		print(self._lastBox, '\t\t:Last')
		if curBox in self.__reached:
			print(self.__reached[curBox], '\t\t:Reached')
		print(curCoords, '\t:Coords')
		if curBox in self.__reached:
			if self.__reached[curBox] in self.__pathGRID:
				print(self.__pathGRID[self.__reached[curBox]], '\t:Box Coords')
		curBoxNumb = self.Find_mySquare(curCoords)
		self.__reached[curBox] = curBoxNumb
		x, y = curCoords
		if curBox not in self.__reached:
			#next 4 squares, clockwise order starting at 6 o'clock and the current box
			self.__reached['Box'+str(numb+0)] = (self.Find_mySquare((x, y))) #Current Box
			self.__reached['Box'+str(numb+1)] = (self.Find_mySquare((x+self.__boxSize, y))) #North Side of curBox
			self.__reached['Box'+str(numb+2)] = (self.Find_mySquare((x, y-self.__boxSize))) #West Side of curBox
			self.__reached['Box'+str(numb+3)] = (self.Find_mySquare((x-self.__boxSize, y))) #East Side of curBox
			self.__reached['Box'+str(numb+4)] = (self.Find_mySquare((x, y+self.__boxSize))) #South Side of curBox
			print(self.__reached, 'not in reached')
			print('\n<----------------------------->\n')
			return
		else:
			print('Current Box has already ben reached.')
			#the four surrounding the current
			# self.__reached['Box'+str(numb+1)] = (self.Find_mySquare((x+self.__boxSize, y))) #North Side of curBox
			# self.__reached['Box'+str(numb+2)] = (self.Find_mySquare((x, y-self.__boxSize))) #West Side of curBox
			# self.__reached['Box'+str(numb+3)] = (self.Find_mySquare((x-self.__boxSize, y))) #East Side of curBox
			# self.__reached['Box'+str(numb+4)] = (self.Find_mySquare((x, y+self.__boxSize))) #South Side of curBox
			print(self.__reached, 'in reached')
			print('\n<----------------------------->\n')
			return


	def Find_mySquare(self, objCoords):
		x, y = objCoords
		for key in self.__pathGRID:
			xBox, yBox = self.__pathGRID[key]
			xBox32, yBox32 = xBox+32, yBox+32
			# print('\nTLC', (xBox, yBox), '\nBRC', (xBox32, yBox32), '\nOBJ', (x, y))
			if x >= xBox and y >= yBox:
				if x < xBox32 and y < yBox32:
					print(key, 'Box number')
					return key


	'''#|--------------Getters--------------|#'''
		#this is where a list of getters will go...
	def get_pathGRID(self):
		return self.__pathGRID


	'''#|--------------Setters--------------|#'''
		#this is where a list of setters will go...
	# def set_...
