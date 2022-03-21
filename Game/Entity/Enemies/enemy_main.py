from ..entity_main import Entity_Main
from Engine import *

#Parenet: Entity_Main
#Children:
	#Stalfos_Main
	#CPU_Stalfos_Main

class Enemy_Main(Entity_Main):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None, pfNode=None):
		Entity_Main.__init__(self, info=info, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode, pfNode=pfNode)
		self.__reDrawl = False
		self.loopCount = 0
		self.lastSquare= None
		self.zero	   = None
		self.Var 	   = 1

	#Brain Power Level [BPL]
	def CPU_MoveControll(self, BPL='BPL=0', L1Pack=None, L2Pack=None):
		# print('zero', self.zero)
		#level packs is a tuple of the required info of the BPL
		#BPL options
			# 'BPL=0' Random movement
			# 'BPL=1' Simple follow player
			# 'BPL=2' Advanced follow player.

		#General Info
		my_w, my_h = self._info.get_size()
		my_x, my_y = self._info.get_myCoords()
		my_x += 2
		my_y += 2
		if L1Pack != None:
			pl_x, pl_y = L1Pack

		#Level 0: sets movement in random directions, and is the defult.
		if BPL == 'BPL=0':
			if Timer_Node.GameTime == self.Var:
				self.randNumb = int(self._rand.randint(0, 3))
				self.Var += 11

			if self.randNumb == 0:
				self.Personal_Move('left')
			elif self.randNumb == 1:
				self.Personal_Move('right')
			elif self.randNumb == 2:
				self.Personal_Move('up')
			elif self.randNumb == 3:
				self.Personal_Move('down')
		#level 1: Simply follows the player, regardless of obsticles.
		elif BPL == 'BPL=1':
			if my_x > pl_x or my_x > pl_x+my_w:
				self.Personal_Move('left')
			if my_x < pl_x or my_x < pl_x+my_w:
				self.Personal_Move('right')
			if my_y > pl_y or my_y > pl_y+my_h:
				self.Personal_Move('up')
			if my_y < pl_y or my_y < pl_y+my_h:
				self.Personal_Move('down')
		#level 2: Advanced follow/ Randomly attempts to move around the wall.
		elif BPL == 'BPL=2':
			if self.get_isStatic() == True: #Move around wall.
				var1 = self._rand.randint(0, 3)
				var2 = self._rand.randint(4, 7)
				for time in range(12, -1, -1):
					if var1 == 0 or var2 == 4:
						self.Personal_Move('left')
						self.Posible_Collide()
					if var1 == 2 or var2 == 5:
						self.Personal_Move('right')
						self.Posible_Collide()
					if var1 == 1 or var2 == 6:
						self.Personal_Move('up')
						self.Posible_Collide()
					if var1 == 3 or var2 == 7:
						self.Personal_Move('down')
						self.Posible_Collide()
				pass
			else: #General Movement twoards player.
				# print('False')
				if my_x > pl_x or my_x > pl_x+my_w:
					self.Personal_Move('left')
				if my_x < pl_x or my_x < pl_x+my_w:
					self.Personal_Move('right')
				if my_y > pl_y or my_y > pl_y+my_h:
					self.Personal_Move('up')
				if my_y < pl_y or my_y < pl_y+my_h:
					self.Personal_Move('down')
		elif BPL == 'BPL=3': #Breadth_First_Search
			# Moves based on the created path.
			path = self._pfNode.get_myPath()
			if len(path) > 0:
				#draw shift
				if path[-1][0] == 'left':
					my_x += (my_w-4)
				if path[-1][0] == 'up':
					my_y += (my_h-4)

				#next direction
				if path[-1][0] == 'left':
					my_x -= my_w
				if path[-1][0] == 'right':
					my_x += my_w
				if path[-1][0] == 'down':
					my_y += my_h
				if path[-1][0] == 'up':
					my_y -= my_h
				mySquare = self._pfNode.Find_mySquare((my_x, my_y))
				curSquare = self._pfNode.Find_mySquare((path[-1][1]))
				if mySquare != curSquare:
					if self.lastSquare == None:
						self.lastSquare = mySquare
						# print(self._pfNode.Find_mySquare((path[-1][1])), 'last Square?')
						# print(self._pfNode.Find_mySquare((path[-1][1])), 'next Square?')
					elif self.lastSquare != mySquare:
						self.lastSquare = mySquare
						# print(self._pfNode.Find_mySquare((path[-1][1])), 'last Square')
						del path[-1]
						if len(path) != 0:
							# print(self._pfNode.Find_mySquare((path[-1][1])), 'next Square')
							pass
					else:
						# print(self._pfNode.Find_mySquare((path[-1][1])), 'last Square')
						del path[-1]
						if len(path) != 0:
							# print(self._pfNode.Find_mySquare((path[-1][1])), 'next Square')
							pass
						return
					# Image_Node.Render.create_rectangle(path[-1][1][0]+10, path[-1][1][1]+10, path[-1][1][0]+20, path[-1][1][1]+20, fill='Black', tag='BFS')

					# print('\n',len(path), 'Directions')
					# print(path)
					# print('<--------------------------->\n')
				else:
					self.Personal_Move(path[-1][0])
					# print('Moved...', path[-1][0])
					# if len(path) > 2:
					# 	if path[-2][0] != path[-1][0]:
					# 		self.Personal_Move(path[-1][0])
					# 		print('Moved..', path[-1][0])
			else:
				# print('no more path')
				self.__reDrawl = True

			self.loopCount += 1


		elif BPL == 'BPL=4': #Dijkstra's Algorithm
			pass
		elif BPL == 'BPL=A*': #A* method for ai mapping.
			pass



	"""#|----------Extra Functions----------|#"""
	def Personal_Move(self, dir, speed=None):
		# print(dir, 'last moved')
		if speed == None:
			speed = self._info.get_speed()
		newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), dir, speed=speed)
		self.Move_Sets(newCoords)

	def Mics_Any(self):
		self.zero = self._pfNode._boxSize / self._info.get_speed()
		# print(self.zero, 'zero')


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_reDrawl(self):
		return self.__reDrawl
