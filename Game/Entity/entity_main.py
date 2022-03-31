from Engine import *
import random

#Parent: Main_Node
#Children:
	#Enemy_Main
	#Player_Main

class Entity_Main(Main_Node):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None, pfNode=None):
		Main_Node.__init__(self, info=info, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode, pfNode=pfNode)
		# print(pfNode, 'pfNode 2', self._info.get_ID())
		self.__occupied	= True
		self._rand		= random

		#---Controlls---#
		self._keyUP		= 'w'
		self._keyDOWN	= 's'
		self._keyLEFT	= 'a'
		self._keyRIGHT	= 'd'
		self._ranged	= 'l'
		self._melee		= 'k'

		#---Active Parameters---#
		self._lastDir	= None #last Directions looked
		self._myHealth	= 0

		self.__isStatic	= False
		self._isMoving	= False
		self._isAttack	= False
		self._isAlive	= True
		self._isHit		= False
		self._side		= None

		self._static = None

	def Random_Place(self, size, screenWidth, screenHeight):
		w, h = size
		while self.__occupied == True:
			x = int(self._rand.randint((48+w), screenWidth-(48+w)))
			y = int(self._rand.randint((48+h), screenHeight-(48+h)))
			if self._pfNode != None:
				# print(self._pfNode, 'pfNode RP')
				x, y = self._pfNode.Find_mySquare((x, y), RP=True)
			objects = self._cLogic.Check_forCollision(objCorners=(x, y, x+w, y+h))
			print(objects, 'LOC?')
			if objects != [] and len(objects) >= 0:
				print('someones here.')
			else:
				self.__occupied = False
		return (x, y)

	def Reset_Hit(self, Name=None):
		if Timer_Node.GameTime == self._saveTime+5:
			self._isHit = False
			print(str(Name)+' Can Get Hit')
			print(self._myHealth, ':'+str(Name)+' Health')

	def Check_Health(self):
		if self._isHit == True:
			if self._myHealth > 0:
				# print('Alive')
				return True
			elif self._myHealth <= 0:
				Image_Node.Render.delete(self._info.get_ID())
				self._cLogic.Del_CollisionDict(self._info.get_ID())
				return False
		elif self._isHit == False:
			print("Error: 'self._isHit == False' \n\t Game\Entity\entity_main.py Check_Health #63")

	#OSC == Other Side of Collision, it represents the other object that collided with player
	#OSA == Other Side's Attack, represents the other objects needed parameters.
	def My_Collision(self, OSC=None, OSA=None, side=None, staticsList=None):
		# print('My_Collision:\n\t', OSC)
		if self._isHit == False:
			if OSC == True or OSC == None: #Var Resets happen here.
				# self.__isStatic  = False
				# print(self.__isStatic)

				return
			#__Other Side Collision: Static__#
			elif OSC == 'Static':
				# if self.__isStatic == False and self._varTrack == False:
				# 	self._varTime = Timer_Node.GameTime
				# 	self._varTime += 5
				# 	self._varTrack = True
				# self.__isStatic = True
				# print(self.__isStatic)
				for newSide in side:
					# print(newSide)
					new_Coords = self._kNode.Static_Hit(self._info.get_myCoords(), self._info.get_ID(), newSide, speed=self._info.get_speed())
					self._info.set_myCoords(new_Coords)
					self._info.set_myCorners(self._info.get_ID())
				#__Other Side Collision: Enemy/Weapon/Friend__#
			elif OSC == 'Enemy' or OSC == 'Weapon' or OSC == 'Friend':
				#---------------Math---------------#
				if OSC != 'Friend':
					self._myHealth -= OSA
				for newSide in side:
					side = newSide
					for time in range(50):
						newCoords = self._kNode.Knock_Back(self._info.get_myCoords(), self._info.get_ID(), side)
						self.Move_Sets(newCoords)
						self.Posible_Collide()


				#---------------Logic---------------#
				if OSC != 'Friend':
					self._isHit		= True
					self._isAlive	= self.Check_Health()
					self._saveTime	= Timer_Node.GameTime

	"""#|----------Extra Functions----------|#"""
	def Move_Sets(self, newCoords):
		self._info.set_myCoords(newCoords)
		self._info.set_myCorners(self._info.get_ID())
		self._isMoving = True

	def Posible_Collide(self, staticsList=None):
		possibleCollide = self._cLogic.Check_forCollision(self._info.get_ID())
		if possibleCollide != None:
			#print(possibleCollide, 'MyCollision')
			for obj in possibleCollide:
				if obj != None:
					if obj.get_groupID() in self._cLogic.get_staticRoster():
						direction = self._cLogic.Side_Calc(self._cLogic.Tag_toObject(self._info.get_ID()))
						self.My_Collision(OSC='Static', side=direction)
						return


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_isAlive(self):
		return self._isAlive

	def get_isHit(self):
		return self._isHit

	def get_isMoving(self):
		return self._isMoving

	def get_isAttack(self):
		return self._isAttack

	def get_isStatic(self):
		return self.__isStatic



	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_isAlive(self, isAlive):
	# 	self._isAlive = isAlive

	def set_isStatic(self, isStatic):
		self.__isStatic = isStatic
