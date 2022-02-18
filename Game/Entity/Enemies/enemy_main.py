from ..entity_main import Entity_Main
from Engine import *

#Parenet: Entity_Main
#Children:
	#Stalfos_Main
	#CPU_Stalfos_Main

class Enemy_Main(Entity_Main):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None, pfNode=None):
		Entity_Main.__init__(self, info=info, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode, pfNode=pfNode)
		self.Var = 1

	#Brain Power Level [BPL]
	def CPU_MoveControll(self, BPL='BPL=0', L1Pack=None, L2Pack=None):
		#level packs is a tuple of the required info of the BPL
		#BPL options
			# 'BPL=0' Random movement
			# 'BPL=1' Simple follow player
			# 'BPL=2' Advanced follow player.

		#General Info
		my_w, my_h = self._info.get_size()
		my_x, my_y = self._info.get_myCoords()
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
			#tuples of the starting object and ending objects params.
			# arg1 = (self._info.get_myCoords(), self._info.get_ID())
			# arg2 = (pl_x, pl_y)
			# self._pfNode.Breadth_Search(startOBJ=arg1, endOBJ=arg2)
			pass
		elif BPL == 'BPL=4': #Dijkstra's Algorithm
			pass
		elif BPL == 'BPL=A*': #A* method for ai mapping.
			pass



	"""#|----------Extra Functions----------|#"""
	def Personal_Move(self, dir):
		newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), dir, speed=self._info.get_speed())
		self.Move_Sets(newCoords)
