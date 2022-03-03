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
		self.__reached	= {} # Box(#) : numbValue
		self.__cameFrom = {} #BoxNumb : direction
		self.__path		= [] #Path the entity will take.
		self._lastBox	= None
		self._next		= 0

		#--Grid Paramaters--#
		self.__pathGRID = {} # NumValue : (x, y)
		self._boxSize  = 32
		self._xPos = 0
		self._yPos = 0
		self.end_x = 0
		self.end_y = 0

	def Map_Grid(self, colDict): #changes
		for value in colDict.values():
			# print(value.get_myCoords(), value.get_ID())
			if value.get_myCoords() != None:
				if len(value.get_ID()) >= 9:
					# print('this is Wall')
					# print(value.get_ID())
					x, y = value.get_myCoords()
					for key in self.__pathGRID.keys():
						if (x, y) == self.__pathGRID[key][0]:
							# print(self.__pathGRID[key][0], 'pathGRID coord')
							# print((x, y), 'colDict coord')
							self.__pathGRID[key] = [(x, y), 'wall*']
							self.__frontier[key] = [(x, y), 'wall*']
				else:
					print(value.get_ID())
					x, y = value.get_myCoords()
					for key in self.__pathGRID.keys():
						if (x, y) == self.__pathGRID[key][0]:
							# print(self.__pathGRID[key][0], 'pathGRID coord')
							# print((x, y), 'colDict coord')
							self.__pathGRID[key] = [(x, y), 'other*']
							self.__frontier[key] = [(x, y), 'other*']
			# print('<------------------->\n')
		# print('pathGRID', self.__pathGRID, '\n')



	def System_Grid(self): #sets up the grid for all spaces centered around a target.
		boxCountX = int(1280/self._boxSize)
		boxCountY = int(800/self._boxSize)

		boxNumb = 0
		for x in range(boxCountX+1):
			if x == 0:
				self._xPos = 0
			else:
				self._xPos += self._boxSize
			for y in range(boxCountY+1):
				self._yPos += self._boxSize
				if y == (boxCountY):
					self._yPos = 0
				boxNumb+=1
				self.__pathGRID[boxNumb] = [(self._xPos, self._yPos)]
				self.__frontier[boxNumb] = [(self._xPos, self._yPos)]
			# 	print((self._xPos, self._yPos), 'box coords\t', y)
			# print('-----------------------------------------------')
		# print(self.__pathGRID)

	#basic path finding.
	#startOBJ == Target object to be moved
	#endOBJ == Target object that startOBJ is moving to.
	def Breadth_Search(self, startOBJ=None, endOBJ=None):
		# print("\n\n#--Initial Prints--#")
		my_x, my_y = startOBJ.get_myCoords()
		my_w, my_h = startOBJ.get_size()
		# x, y = endOBJ.get_myCoords()
		self.end_x, self.end_y = self.__pathGRID[self.Find_mySquare(endOBJ.get_myCoords())][0]
		# print((my_x, my_y), 'obj coords')

		startBox = self.Find_mySquare((my_x, my_y)) #startOBJ's original box
		# print(startBox, startOBJ.get_ID(),"'s box number")

		self.__reached['Box0'] = startBox
		self.__cameFrom[startBox] = None
		if startBox in self.__frontier:
			del self.__frontier[startBox]
		# print('<------------------------>\n')

		# print(self.__pathGRID[self.__reached['Box0']], "Box0's coords")
		count = 0
		while self.__frontier != {}:
			curBox = 'Box'+str(count)

			#Current Box Prints
			# print(count, '\tCurrent Box')
			# if curBox in self.__reached.keys():
			# 	print(self.__pathGRID[self.__reached[curBox]], '\t curBox')
			# print(self._next, '\tNext Empty Box')
			# print('<---------->\n')

			if curBox == 'Box1066':
				print("END OF THE ROAD")
				break
			if self.__pathGRID[self.__reached[curBox]][0] == (self.end_x, self.end_y):
				print("FOUND EM")
				break

			#---Finds Neighbors and puts the square into self.__reached---#
			newNumb = self.Find_Neighbors(curBox, self._next)
			count += 1
			self._next = newNumb


			if self._next in self.__frontier:
				del self.__frontier[self._next]
				# print(len(self.__frontier), "Box's left")

		#actually finding a path to the target.
		# print(self.Find_mySquare((self.end_x, self.end_y)), 'Key')

		current = self.Find_mySquare((self.end_x, self.end_y))
		# print(self.__cameFrom, 'Wut?')
		# print(current, 'current before while loop')
		# if current in self.__reached.values():
		# 	print(self.Find_boxName(current), 'should be the box name')
		while current != self.__reached['Box0']:
			x, y = self.__pathGRID[current][0]
			if current not in self.__cameFrom.keys():
				break
			if self.__cameFrom[current] == 'right':
				self.__path.append(['left', (x, y)])
				current = self.Find_mySquare((x+self._boxSize, y))
				# print(current, 'Next Box')
			elif self.__cameFrom[current] == 'left':
				self.__path.append(['right', (x, y)])
				current = self.Find_mySquare((x-self._boxSize, y))
				# print(current, 'Next Box')
			elif self.__cameFrom[current] == 'down':
				self.__path.append(['up', (x, y)])
				current = self.Find_mySquare((x, y+self._boxSize))
				# print(current, 'Next Box')
			elif self.__cameFrom[current] == 'up':
				self.__path.append(['down', (x, y)])
				current = self.Find_mySquare((x, y-self._boxSize))
				# print(current, 'Next Box')
			# print(current, self.__reached['Box0'])
		print('<-------------->')
		print(len(self.__path))
		print(self.__path)


	"""#|----------Extra Functions----------|#"""
	def Find_Neighbors(self, curBox, next): #this is used to find if neighboring boxes are used.
		# print('<---Find Neighbors--->')
		# print(curBox, '\t\t:Current Box')
		# print(self.__reached[curBox], '\t\t:Reached Box')
		# print(self.__pathGRID[self.__reached[curBox]][0], '\t:Box Coords')
		#----------------------------------------------------------------------#

		if curBox in self.__reached:
			x, y = self.__pathGRID[self.__reached[curBox]][0]
			# print('Current Box has already ben reached.')
			#the four surrounding the current
			if self.Find_mySquare((x+self._boxSize, y)) not in self.__reached.values():
				if len(self.__pathGRID[self.Find_mySquare((x+self._boxSize, y))]) >= 2:
					pass
				else:
					# print('no Wall')
					next+=1
					self.__reached['Box'+str(next)] = (self.Find_mySquare((x+self._boxSize, y)))
					self.__cameFrom[self.Find_mySquare((x+self._boxSize, y))] = 'left'
					# print(self.__reached['Box'+str(next)], 'Box'+str(next), )

			if self.Find_mySquare((x, y-self._boxSize)) not in self.__reached.values():
				if len(self.__pathGRID[self.Find_mySquare((x, y-self._boxSize))]) >= 2:
					pass
				else:
					# print('no Wall')
					next+=1
					self.__reached['Box'+str(next)] = (self.Find_mySquare((x, y-self._boxSize)))
					self.__cameFrom[self.Find_mySquare((x, y-self._boxSize))] = 'down'
					# print(self.__reached['Box'+str(next)], 'Box'+str(next), )

			if self.Find_mySquare((x-self._boxSize, y)) not in self.__reached.values():
				if len(self.__pathGRID[self.Find_mySquare((x-self._boxSize, y))]) >= 2:
					pass
				else:
					# print('no Wall')
					next+=1
					self.__reached['Box'+str(next)] = (self.Find_mySquare((x-self._boxSize, y)))
					self.__cameFrom[self.Find_mySquare((x-self._boxSize, y))] = 'right'
					# print(self.__reached['Box'+str(next)], 'Box'+str(next), )

			if self.Find_mySquare((x, y+self._boxSize)) not in self.__reached.values():
				if len(self.__pathGRID[self.Find_mySquare((x, y+self._boxSize))]) >= 2:
					pass
				else:
					# print('no Wall')
					next+=1
					self.__reached['Box'+str(next)] = (self.Find_mySquare((x, y+self._boxSize)))
					self.__cameFrom[self.Find_mySquare((x, y+self._boxSize))] = 'up'
					# print(self.__reached['Box'+str(next)], 'Box'+str(next), )

			# print(self.__reached, 'in reached')
			# print('\n<----------------------------->\n')
			return next
		else:
			# print('curBox not in reached', curBox)
			return next


	def Find_mySquare(self, objCoords, RP=False): #RP== Random Place
		x, y = objCoords
		for key in self.__pathGRID.keys():
			xBox, yBox = self.__pathGRID[key][0]
			xBox32, yBox32 = xBox+32, yBox+32
			if x >= xBox and y >= yBox:
				if x < xBox32 and y < yBox32:
					# print('\nTLC', (xBox, yBox), '\nBRC', (xBox32, yBox32), '\nOBJ', (x, y))
					# print(key, 'Box number', '\n<------------->\n')
					if RP == False:
						return key
					else:
						return self.__pathGRID[key][0]


	def Clear_Path(self):
		self.__path = []


	def Show_Breadth(self, var):
		box = 'Box'+str(var)
		if box in self.__reached.keys():
			x, y = self.__pathGRID[self.__reached[box]][0]
			Image_Node.Render.create_text(x+16, y+16, text=str(var), fill='Blue')

			if self.__cameFrom[self.__reached[box]] == 'right':
				Image_Node.Render.create_oval(x+20, y+4, x+24, y+24, fill='Yellow')
			if self.__cameFrom[self.__reached[box]] == 'left':
				Image_Node.Render.create_oval(x+4, y+4, x+8, y+24, fill='Orange')
			if self.__cameFrom[self.__reached[box]] == 'up':
				Image_Node.Render.create_oval(x+4, y+4, x+24, y+8, fill='Green')
			if self.__cameFrom[self.__reached[box]] == 'down':
				Image_Node.Render.create_oval(x+4, y+20, x+24, y+24, fill='Pink')

			Image_Node.Render.create_rectangle(x+4, y+4, x+28, y+28)
			self.Show_Ends()

	def Show_Ends(self, var=None):
		end_x, end_y = self.__pathGRID[self.Find_mySquare((self.end_x, self.end_y))][0]
		if var != None:
			Image_Node.Render.create_oval(end_x+8-var, end_y+8-var, end_x+16-var, end_y+16-var, fill='Red')
		else:
			Image_Node.Render.create_oval(end_x+8, end_y +8, end_x+16, end_y +16, fill='Red')


	'''#|--------------Getters--------------|#'''
		#this is where a list of getters will go...
	def get_pathGRID(self):
		return self.__pathGRID

	def get_myPath(self, ):
		return self.__path


	'''#|--------------Setters--------------|#'''
		#this is where a list of setters will go...
	# def set_...
