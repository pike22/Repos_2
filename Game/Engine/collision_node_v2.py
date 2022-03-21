from .collision_logic_v2 import Collision_Logic_v2

#use this for the games loop collision
class Collision_Node_v2():
	def __init__(self, cLogic):
		self.__logic = cLogic

		#<--Rosters-->#
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


	def Use_Collision(self, tag):
		#cResult is a dictionary
		self.__cResult = self.__logic.Is_Collision(tag)
		print('Dict of objects in relation to mainObj=tag\n', self.__cResult)


		for key, value in self.__cResult.items():
			print('keys=Direction', key)
			print('values=Object', value)



			#<--Player_Collision-->#
			if value.get_ID() in self.__playerRoster:
				print("Player")

			#<--Enemy_Collision-->#
			if value.get_ID() in self.__enemyRoster:
				print("Enemy")

			#<--Weapon_Collision-->#
			if value.get_ID() in self.__weaponRoster:
				print("Weapon")

			#<--Static_Collision-->#
			if value.get_ID() in self.__staticRoster:
				print("Statics")

			#<--Wall_Collision-->#
			if value.get_ID() in self.__wallRoster:
				print("Walls")




	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
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
