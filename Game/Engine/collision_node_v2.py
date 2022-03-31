from .collision_logic_v2 import Collision_Logic_v2

#use this for the games loop collision
class Collision_Node_v2():
	def __init__(self, cLogic):
		self.__logic = cLogic

		#<--Rosters-->#
		self.__entityRoster = None #All Entities\if move then here.
		self.__staticRoster	= None #Tags that can't move, Exclude Walls
		self.__playerRoster	= None #Player Tags
		self.__weaponRoster	= None #Any Weapons Tags
		self.__enemyRoster	= None #Enemy Tags
		self.__everyRoster	= None #All Tags Roster
		self.__projRoster	= None #Any Flying Tags
		self.__wallRoster	= None #Wall Tags

		#Statics vs. Walls#
		"""Statics can't move alone, Walls can't move period."""

		#<--Collision Results-->#
		self.__cResult = None #Collision
		self.__sResult = None #Side
		self.__wallHit = None


	def Collision_Result(self, cResult, objMain):
		#cResult is a dictionary
		self.__cResult = cResult #List of objects that are colliding with given objMain.

		if self.__cResult == []:
			objMain.My_Collision()

		limit = len(self.__cResult)
		timer = 0
		print('limit:', limit)
		for obj in self.__cResult:
			timer += 1
			print('Timer:', timer)
			if obj.get_groupID() in self.__entityRoster:
				print('entity')
				#if 'friend':
				#	OSC='friend'
				#else:
				#	OSC='enemy'

			elif obj.get_groupID() in self.__wallRoster:
				print('wall', obj.get_ID())
				objMain.My_Collision(OSC='Static', side=['down'])

			elif obj.get_groupID() in self.__weaponRoster:
				print('weapon')

			elif obj.get_groupID() in self.__projRoster:
				print('arrow')

			elif obj.get_groupID() in self.__staticRoster:
				print('statics')

			if timer == limit:
				print('End')
				break






	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_entityRoster(self, Roster):
		self.__entityRoster = Roster
		self.__logic.set_entityRoster(Roster)

	def set_playerRoster(self, Roster):
		self.__playerRoster = Roster

	def set_staticRoster(self, Roster):
		self.__staticRoster = Roster

	def set_weaponRoster(self, Roster):
		self.__weaponRoster = Roster

	def set_enemyRoster(self, Roster):
		self.__enemyRoster = Roster

	def set_everyRoster(self, Roster):
		self.__everyRoster = Roster

	def set_projRoster(self, Roster):
		self.__projRoster = Roster

	def set_wallRoster(self, Roster):
		self.__wallRoster = Roster
